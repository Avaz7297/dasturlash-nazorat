# -*- coding: utf-8 -*-
import os
import random
import json
from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, session, jsonify, flash, send_file, Response
from werkzeug.security import check_password_hash

from database import (
    init_db,
    get_db_connection,
    check_student_already_tested,
    register_student_and_session,
    get_session_by_id,
    update_session_answers_and_violations,
    finalize_exam_session,
    get_all_results_for_teacher,
    get_all_groups,
    update_student_score_with_audit,
    delete_exam_session_with_audit,
    get_audit_logs,
    get_student_exam_detail
)
from questions_data import QUESTIONS, SAMPLE_DISTRIBUTION
from export_utils import generate_excel_report, generate_pdf_report, generate_vedomost_excel, generate_vedomost_pdf

app = Flask(__name__)
app.secret_key = 'super_secret_python_exam_key_2026_secured'

# Bazani ishga tushirish
init_db()

def sample_exam_questions():
    """
    7 ta mavzudan talab etilgan miqdorda savollarni tanlash
    va variantlarini tasodifiy aralashtirish
    """
    selected_questions = []

    # Mavzular bo'yicha savollarni guruhlash
    topics_pool = {}
    for q in QUESTIONS:
        t = q['topic']
        if t not in topics_pool:
            topics_pool[t] = []
        topics_pool[t].append(q)

    # Har bir mavzudan belgilangan miqdorda tanlash
    for topic, count in SAMPLE_DISTRIBUTION.items():
        pool = topics_pool.get(topic, [])
        sampled = random.sample(pool, min(count, len(pool)))
        for item in sampled:
            # Variantlarni aralashtirish
            original_options = list(item['options'])
            correct_val = original_options[item['correct']]
            
            # Yangi aralashtirilgan ro'yxat
            shuffled_options = list(original_options)
            random.shuffle(shuffled_options)
            new_correct_idx = shuffled_options.index(correct_val)

            selected_questions.append({
                "id": item['id'],
                "topic": item['topic'],
                "difficulty": item['difficulty'],
                "question": item['question'],
                "code": item.get('code', ''),
                "options": shuffled_options,
                "correct": new_correct_idx
            })

    # 30 ta savol ketma-ketligini ham aralashtirish
    random.shuffle(selected_questions)
    return selected_questions

# =========================================================================
# TALABA MARSHRUTLARI (STUDENT ROUTES)
# =========================================================================

@app.route('/')
def index():
    return send_file(os.path.join(os.path.dirname(__file__), 'python_nazorat.html'))

@app.route('/start_exam', methods=['POST'])
def start_exam():
    student_id_number = request.form.get('student_id_number', '').strip()
    full_name = request.form.get('full_name', '').strip()
    direction = request.form.get('direction', '').strip() or "Axborot-kommunikatsiya texnologiyalari"
    course = request.form.get('course', '1').strip()
    group_name = request.form.get('group_name', '').strip()

    # Majburiy maydonlar tekshiruvi
    if not student_id_number or not full_name or not group_name:
        flash("Talaba ID, F.I.Sh. va Guruh maydonlarini to'ldirish majburiy!", "danger")
        return redirect(url_for('index'))

    # Talaba avval topshirganmi tekshirish (1 marta topshirish talabi)
    existing = check_student_already_tested(student_id_number, full_name, group_name)
    if existing:
        flash(f"Hurmatli {full_name}, siz ushbu Talaba ID ({student_id_number}) bo'yicha avval test topshirgansiz! Qayta topshirish taqiqlanadi.", "warning")
        return redirect(url_for('exam_result', session_id=existing['session_id']))

    # 30 ta savolni tanlash
    sampled_questions = sample_exam_questions()

    # Bazada ro'yxatdan o'tkazish
    session_id = register_student_and_session(
        student_id_number=student_id_number,
        full_name=full_name,
        direction=direction,
        course=int(course),
        group_name=group_name,
        sampled_questions=sampled_questions
    )

    session['student_session_id'] = session_id
    return redirect(url_for('exam_room'))

@app.route('/exam')
def exam_room():
    session_id = session.get('student_session_id')
    if not session_id:
        flash("Iltimos, avval ro'yxatdan o'ting!", "danger")
        return redirect(url_for('index'))

    sess_data = get_session_by_id(session_id)
    if not sess_data:
        flash("Sessiya topilmadi!", "danger")
        return redirect(url_for('index'))

    if sess_data['is_completed'] == 1:
        return redirect(url_for('exam_result', session_id=session_id))

    # Vaqtni hisoblash (60 daqiqa = 3600 soniya)
    started_at = datetime.strptime(sess_data['started_at'], '%Y-%m-%d %H:%M:%S')
    elapsed_seconds = (datetime.now() - started_at).total_seconds()
    remaining_seconds = max(0, 3600 - int(elapsed_seconds))

    if remaining_seconds <= 0:
        # Vaqt tugagan bo'lsa avtomatik yakunlash
        saved_answers = json.loads(sess_data['student_answers_json']) if sess_data['student_answers_json'] else {}
        finalize_exam_session(session_id, saved_answers, sess_data['tab_switch_count'])
        return redirect(url_for('exam_result', session_id=session_id))

    # Xavfsizlik: Talabaga savollar yuborilganda 'correct' indeksi OLIB TASHLANADI!
    raw_questions = json.loads(sess_data['session_questions_json'])
    client_questions = []
    for idx, q in enumerate(raw_questions):
        client_questions.append({
            "index": idx,
            "id": q['id'],
            "topic": q['topic'],
            "difficulty": q['difficulty'],
            "question": q['question'],
            "code": q.get('code', ''),
            "options": q['options']
        })

    saved_answers = json.loads(sess_data['student_answers_json']) if sess_data['student_answers_json'] else {}

    return render_template(
        'exam.html',
        session_id=session_id,
        student=sess_data,
        questions=client_questions,
        remaining_seconds=remaining_seconds,
        saved_answers=saved_answers,
        tab_switch_count=sess_data['tab_switch_count']
    )

@app.route('/api/save_progress', methods=['POST'])
def save_progress():
    """Talaba test ishlayotganda oraliq javoblarni va qoidabuzarliklarni avtomatik saqlash"""
    data = request.get_json() or {}
    session_id = data.get('session_id')
    answers = data.get('answers', {})
    tab_switch_count = data.get('tab_switch_count')

    if not session_id:
        return jsonify({"success": False, "error": "session_id required"}), 400

    update_session_answers_and_violations(session_id, answers, tab_switch_count)
    return jsonify({"success": True})

@app.route('/api/submit_exam', methods=['POST'])
def submit_exam():
    """Testni serverda to'liq tekshirish va baholash"""
    data = request.get_json() or {}
    session_id = data.get('session_id')
    answers = data.get('answers', {})
    tab_switch_count = data.get('tab_switch_count', 0)

    if not session_id:
        return jsonify({"success": False, "error": "session_id required"}), 400

    result = finalize_exam_session(session_id, answers, tab_switch_count)
    if not result:
        return jsonify({"success": True, "already_completed": True, "redirect": url_for('exam_result', session_id=session_id)})

    return jsonify({
        "success": True,
        "redirect": url_for('exam_result', session_id=session_id),
        "result": result
    })

@app.route('/result/<int:session_id>')
def exam_result(session_id):
    sess_data = get_session_by_id(session_id)
    if not sess_data:
        flash("Natija topilmadi!", "danger")
        return redirect(url_for('index'))

    return render_template('result.html', exam=sess_data)

# =========================================================================
# O'QITUVCHI MARSHRUTLARI (TEACHER ROUTES)
# =========================================================================

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        password = request.form.get('password', '').strip()

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM teachers WHERE username = ?', (username,))
        teacher = cursor.fetchone()
        conn.close()

        clean_pass = password.replace(' ', '')
        if teacher and (check_password_hash(teacher['password_hash'], password) or check_password_hash(teacher['password_hash'], clean_pass)):
            session['teacher_logged_in'] = True
            session['teacher_username'] = teacher['username']
            session['teacher_name'] = teacher['full_name']
            flash(f"Xush kelibsiz, {teacher['full_name']}!", "success")
            return redirect(url_for('teacher_dashboard'))
        else:
            flash("Login yoki parol noto'g'ri!", "danger")

    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('teacher_logged_in', None)
    session.pop('teacher_username', None)
    session.pop('teacher_name', None)
    flash("Tizimdan chiqildi.", "info")
    return redirect(url_for('login'))

def teacher_required(f):
    from functools import wraps
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not session.get('teacher_logged_in'):
            flash("Ushbu sahifaga kirish uchun avval tizimga kiring!", "warning")
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/teacher')
@teacher_required
def teacher_dashboard():
    search_query = request.args.get('search', '').strip()
    group_filter = request.args.get('group', '').strip()

    results = get_all_results_for_teacher(search_query, group_filter)
    all_groups = get_all_groups()

    # Statistika hisoblash
    total_students = len(results)
    passed_count = sum(1 for r in results if 'o‘tdi' in r['status_text'].lower())
    failed_count = sum(1 for r in results if 'o‘tmadi' in r['status_text'].lower())
    avg_score = round(sum(r['total_score'] for r in results) / total_students, 1) if total_students > 0 else 0
    pass_rate = round((passed_count / total_students) * 100, 1) if total_students > 0 else 0

    return render_template(
        'teacher.html',
        results=results,
        all_groups=all_groups,
        search_query=search_query,
        group_filter=group_filter,
        total_students=total_students,
        passed_count=passed_count,
        failed_count=failed_count,
        avg_score=avg_score,
        pass_rate=pass_rate
    )

@app.route('/teacher/export/excel')
@teacher_required
def export_excel():
    search_query = request.args.get('search', '').strip()
    group_filter = request.args.get('group', '').strip()
    results = get_all_results_for_teacher(search_query, group_filter)

    excel_data = generate_excel_report(results)
    filename = f"Joriy_nazorat_natijalari_{datetime.now().strftime('%Y%m%d_%H%M')}.xlsx"
    return Response(
        excel_data,
        mimetype="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        headers={"Content-Disposition": f"attachment;filename={filename}"}
    )

@app.route('/teacher/export/pdf')
@teacher_required
def export_pdf():
    search_query = request.args.get('search', '').strip()
    group_filter = request.args.get('group', '').strip()
    results = get_all_results_for_teacher(search_query, group_filter)

    pdf_data = generate_pdf_report(results)
    filename = f"Joriy_nazorat_natijalari_{datetime.now().strftime('%Y%m%d_%H%M')}.pdf"
    return Response(
        pdf_data,
        mimetype="application/pdf",
        headers={"Content-Disposition": f"attachment;filename={filename}"}
    )


@app.route('/teacher/export/vedomost/excel')
@teacher_required
def export_vedomost_excel():
    search_query = request.args.get('search', '').strip()
    group_filter = request.args.get('group', '').strip()
    results = get_all_results_for_teacher(search_query, group_filter)
    grp_title = group_filter if group_filter else "Barcha guruhlar"
    
    excel_data = generate_vedomost_excel(results, grp_title)
    clean_grp = grp_title.replace(' ', '_').replace('/', '_').replace("'", "")
    filename = f"Vedomost_Dasturlash_{clean_grp}_{datetime.now().strftime('%Y%m%d_%H%M')}.xlsx"
    return Response(
        excel_data,
        mimetype="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        headers={"Content-Disposition": f"attachment;filename={filename}"}
    )

@app.route('/teacher/export/vedomost/pdf')
@teacher_required
def export_vedomost_pdf():
    search_query = request.args.get('search', '').strip()
    group_filter = request.args.get('group', '').strip()
    results = get_all_results_for_teacher(search_query, group_filter)
    grp_title = group_filter if group_filter else "Barcha guruhlar"

    pdf_data = generate_vedomost_pdf(results, grp_title)
    clean_grp = grp_title.replace(' ', '_').replace('/', '_').replace("'", "")
    filename = f"Vedomost_Dasturlash_{clean_grp}_{datetime.now().strftime('%Y%m%d_%H%M')}.pdf"
    return Response(
        pdf_data,
        mimetype="application/pdf",
        headers={"Content-Disposition": f"attachment;filename={filename}"}
    )

@app.route('/api/teacher/student/<int:session_id>')
@teacher_required
def student_detail_api(session_id):
    detail = get_student_exam_detail(session_id)
    if not detail:
        return jsonify({"success": False, "error": "Topilmadi"}), 404
    return jsonify({"success": True, "data": detail})

@app.route('/api/teacher/update_score', methods=['POST'])
@teacher_required
def update_score_api():
    data = request.get_json() or {}
    session_id = data.get('session_id')
    new_score = data.get('new_score')
    reason = data.get('reason', '').strip()
    teacher_username = session.get('teacher_username', 'admin')

    if session_id is None or new_score is None or not reason:
        return jsonify({"success": False, "error": "Barcha maydonlar (sessiya, yangi ball, sabab) to'ldirilishi shart!"}), 400

    try:
        new_score = int(new_score)
        if not (0 <= new_score <= 30):
            return jsonify({"success": False, "error": "Ball 0 dan 30 gacha bo'lishi kerak!"}), 400
    except ValueError:
        return jsonify({"success": False, "error": "Ball butun son bo'lishi kerak!"}), 400

    success, msg = update_student_score_with_audit(session_id, new_score, reason, teacher_username)
    return jsonify({"success": success, "message": msg})

@app.route('/api/direct_submit', methods=['POST'])
def direct_submit():
    """Tashqi standalone HTML dan yoki boshqa qurilmadan kelgan natijani to'g'ridan-to'g'ri qabul qilish"""
    data = request.get_json() or {}
    student_id_number = str(data.get('studentId', '')).strip()
    full_name = data.get('fullName', '').strip()
    direction = data.get('direction', '').strip()
    course = data.get('course', 1)
    group_name = str(data.get('groupName', '')).strip()
    total_score = data.get('totalScore', 0)
    correct_count = data.get('correctCount', 0)
    incorrect_count = data.get('incorrectCount', 0)
    status_text = data.get('statusText', '')
    tab_switch_count = data.get('tabSwitchCount', 0)
    questions = data.get('questions', [])
    answers = data.get('answers', {})
    started_at = data.get('startedAt', datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    finished_at = data.get('finishedAt', datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

    if not full_name or not group_name:
        return jsonify({"success": False, "error": "F.I.Sh. va Guruh kiritilmagan"}), 400

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        SELECT id FROM students WHERE (student_id_number = ? AND student_id_number != '' AND student_id_number != '000000000000') OR (LOWER(TRIM(full_name)) = LOWER(TRIM(?)) AND group_name = ?)
    ''', (student_id_number, full_name, group_name))
    row = cursor.fetchone()
    if row:
        student_id = row['id']
    else:
        cursor.execute('''
            INSERT INTO students (student_id_number, full_name, direction, course, group_name, created_at)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (student_id_number, full_name, direction, int(course), group_name, started_at))
        student_id = cursor.lastrowid

    cursor.execute('''
        INSERT INTO exam_sessions (
            student_id, subject, started_at, finished_at, time_limit_minutes,
            is_completed, total_score, max_score, correct_count, incorrect_count,
            status_text, tab_switch_count, session_questions_json, student_answers_json
        )
        VALUES (?, 'Dasturlash', ?, ?, 60, 1, ?, 30, ?, ?, ?, ?, ?, ?)
    ''', (
        student_id, started_at, finished_at, total_score, correct_count,
        incorrect_count, status_text, tab_switch_count,
        json.dumps(questions, ensure_ascii=False),
        json.dumps(answers, ensure_ascii=False)
    ))
    conn.commit()
    conn.close()
    return jsonify({"success": True, "message": "Natija qabul qilindi"})

@app.route('/api/teacher_results')
def teacher_results_api():
    """O'qituvchi jadvalini real vaqtda yangilash uchun API"""
    search_query = request.args.get('search', '').strip()
    group_filter = request.args.get('group', '').strip()
    results = get_all_results_for_teacher(search_query, group_filter)
    return jsonify({"success": True, "results": results})

@app.route('/teacher/audit')
@teacher_required
def audit_view():
    logs = get_audit_logs()
    return render_template('audit.html', logs=logs)

if __name__ == '__main__':
    import socket
    local_ip = "127.0.0.1"
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        local_ip = s.getsockname()[0]
        s.close()
    except Exception:
        pass

    print("=" * 60)
    print("PYTHON MASOFAVIY JORIY NAZORAT SERVERI ISHGA TUSHDI!")
    print(f"Kompyuter brauzeri uchun:    http://localhost:5000")
    print(f"Telefonlar uchun (Wi-Fi):    http://{local_ip}:5000")
    print(f"O'qituvchi boshqaruv paneli:  http://localhost:5000/login")
    print(f"Login: admin | Parol: admin 123")
    print("=" * 60)

    app.run(host='0.0.0.0', port=5000, debug=False)


@app.route('/api/teacher/delete_student', methods=['POST'])
def api_teacher_delete_student():
    """O'qituvchi talabani o'chirganda uni bazadan to'liq tozalash (talaba qayta topshira olishi uchun)"""
    data = request.get_json() or {}
    session_id = data.get('sessionId')
    student_id_number = str(data.get('studentId', '')).strip()
    full_name = data.get('fullName', '').strip()
    group_name = data.get('groupName', '').strip()
    teacher_username = data.get('teacher', 'admin')
    reason = data.get('reason', 'O‘qituvchi tomonidan natija o‘chirildi (qayta topshirishga ruxsat)')

    conn = get_db_connection()
    cursor = conn.cursor()

    if session_id:
        delete_exam_session_with_audit(session_id, teacher_username, reason)
    
    if student_id_number:
        # Ushbu student_id_number ga tegishli barcha sessiyalar va student yozuvlarini o'chirish
        cursor.execute('''
            SELECT e.id FROM exam_sessions e
            JOIN students s ON e.student_id = s.id
            WHERE s.student_id_number = ?
        ''', (student_id_number,))
        rows = cursor.fetchall()
        for r in rows:
            delete_exam_session_with_audit(r['id'], teacher_username, reason)

        cursor.execute('DELETE FROM students WHERE student_id_number = ?', (student_id_number,))
        conn.commit()

    if full_name and group_name:
        cursor.execute('''
            SELECT e.id FROM exam_sessions e
            JOIN students s ON e.student_id = s.id
            WHERE LOWER(TRIM(s.full_name)) = LOWER(TRIM(?)) AND s.group_name = ?
        ''', (full_name, group_name))
        rows = cursor.fetchall()
        for r in rows:
            delete_exam_session_with_audit(r['id'], teacher_username, reason)

        cursor.execute('DELETE FROM students WHERE LOWER(TRIM(full_name)) = LOWER(TRIM(?)) AND group_name = ?', (full_name, group_name))
        conn.commit()

    conn.close()
    return jsonify({"success": True, "message": "Talaba muvaffaqiyatli o'chirildi va qayta topshirish imkoni berildi."})

@app.route('/api/check_student_status')
def api_check_student_status():
    """Talaba ID sini kiritganda u bazada topshirgan holatda turibdimi yoki o'qituvchi o'chirganmi tekshirish"""
    sid = request.args.get('id', '').strip()
    if not sid:
        return jsonify({"tested": False})
    
    # 000000000000 sinov ID si hech qachon bloklanmaydi
    if sid == '000000000000':
        return jsonify({"tested": False})

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        SELECT e.id, e.total_score, e.status_text, e.finished_at, s.full_name, s.group_name
        FROM exam_sessions e
        JOIN students s ON e.student_id = s.id
        WHERE s.student_id_number = ? AND e.is_completed = 1
        ORDER BY e.id DESC LIMIT 1
    ''', (sid,))
    row = cursor.fetchone()
    conn.close()

    if row:
        return jsonify({
            "tested": True,
            "session": {
                "sessionId": row['id'],
                "totalScore": row['total_score'],
                "statusText": row['status_text'],
                "finishedAt": row['finished_at'],
                "fullName": row['full_name'],
                "groupName": row['group_name']
            }
        })
    else:
        return jsonify({"tested": False})
