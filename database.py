# -*- coding: utf-8 -*-
import sqlite3
import os
import json
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'exam_system.db')

def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()

    # O'qituvchilar jadvali
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS teachers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password_hash TEXT NOT NULL,
        full_name TEXT NOT NULL,
        created_at TEXT NOT NULL
    )
    ''')

    # Talabalar jadvali
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_id_number TEXT DEFAULT '',
        full_name TEXT NOT NULL,
        direction TEXT NOT NULL,
        course INTEGER NOT NULL,
        group_name TEXT NOT NULL,
        created_at TEXT NOT NULL
    )
    ''')

    # Agar jadvalda student_id_number bo'lmasa qo'shish
    try:
        cursor.execute("ALTER TABLE students ADD COLUMN student_id_number TEXT DEFAULT ''")
    except Exception:
        pass

    # Test sessiyalari jadvali
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS exam_sessions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_id INTEGER NOT NULL,
        subject TEXT NOT NULL DEFAULT 'Dasturlash',
        started_at TEXT NOT NULL,
        finished_at TEXT,
        time_limit_minutes INTEGER NOT NULL DEFAULT 60,
        is_completed INTEGER NOT NULL DEFAULT 0,
        total_score INTEGER DEFAULT 0,
        max_score INTEGER NOT NULL DEFAULT 30,
        correct_count INTEGER DEFAULT 0,
        incorrect_count INTEGER DEFAULT 0,
        status_text TEXT DEFAULT '',
        tab_switch_count INTEGER DEFAULT 0,
        session_questions_json TEXT NOT NULL,
        student_answers_json TEXT DEFAULT '{}',
        is_modified_by_teacher INTEGER DEFAULT 0,
        FOREIGN KEY (student_id) REFERENCES students (id)
    )
    ''')

    # Audit jurnali (o'qituvchi o'zgartirishlari tarixi)
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS audit_logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        session_id INTEGER NOT NULL,
        student_name TEXT NOT NULL,
        old_score INTEGER NOT NULL,
        new_score INTEGER NOT NULL,
        old_status TEXT NOT NULL,
        new_status TEXT NOT NULL,
        reason TEXT NOT NULL,
        teacher_username TEXT NOT NULL,
        changed_at TEXT NOT NULL,
        FOREIGN KEY (session_id) REFERENCES exam_sessions (id)
    )
    ''')

    # Standart o'qituvchi akkauntini qo'shish (agar bo'lmasa)
    cursor.execute('SELECT * FROM teachers WHERE username = ?', ('admin',))
    if not cursor.fetchone():
        cursor.execute('''
        INSERT INTO teachers (username, password_hash, full_name, created_at)
        VALUES (?, ?, ?, ?)
        ''', (
            'admin',
            generate_password_hash('admin123'),
            'Bosh O\'qituvchi',
            datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        ))

    conn.commit()
    conn.close()

def check_student_already_tested(student_id_number, full_name='', group_name=''):
    """Talaba ID raqami bo'yicha talaba avval test topshirganmi tekshirish"""
    # Sinov talabasi (000000000000) o'qituvchi tomonidan qayta-qayta topshirilishi mumkin
    if str(student_id_number).strip() == '000000000000':
        return None

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        SELECT s.id, s.student_id_number, s.full_name, e.id as session_id, e.is_completed, e.started_at, e.finished_at, e.total_score, e.status_text
        FROM students s
        JOIN exam_sessions e ON s.id = e.student_id
        WHERE s.student_id_number = ? OR (LOWER(TRIM(s.full_name)) = LOWER(TRIM(?)) AND LOWER(TRIM(s.group_name)) = LOWER(TRIM(?)))
    ''', (str(student_id_number).strip(), full_name, group_name))
    row = cursor.fetchone()
    conn.close()
    return row

def register_student_and_session(student_id_number, full_name, direction, course, group_name, sampled_questions):
    """Yangi talaba va test sessiyasini yaratish"""
    conn = get_db_connection()
    cursor = conn.cursor()
    now_str = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    cursor.execute('''
    INSERT INTO students (student_id_number, full_name, direction, course, group_name, created_at)
    VALUES (?, ?, ?, ?, ?, ?)
    ''', (str(student_id_number).strip(), full_name.strip(), direction.strip(), int(course), group_name.strip(), now_str))
    student_id = cursor.lastrowid

    # Savollarni json formatida saqlash
    # (har bir savolda id, topic, difficulty, question, code, options, correct_index bor)
    questions_json = json.dumps(sampled_questions, ensure_ascii=False)

    cursor.execute('''
    INSERT INTO exam_sessions (
        student_id, subject, started_at, time_limit_minutes, is_completed,
        max_score, session_questions_json, student_answers_json
    )
    VALUES (?, 'Dasturlash', ?, 60, 0, 30, ?, '{}')
    ''', (student_id, now_str, questions_json))
    session_id = cursor.lastrowid

    conn.commit()
    conn.close()
    return session_id

def get_session_by_id(session_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        SELECT e.*, s.student_id_number, s.full_name, s.direction, s.course, s.group_name
        FROM exam_sessions e
        JOIN students s ON e.student_id = s.id
        WHERE e.id = ?
    ''', (session_id,))
    row = cursor.fetchone()
    conn.close()
    return row

def update_session_answers_and_violations(session_id, answers_dict, tab_switch_count=None):
    """Talabaning oraliq javoblarini va tab almashtirishlarini saqlash"""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    if tab_switch_count is not None:
        cursor.execute('''
        UPDATE exam_sessions
        SET student_answers_json = ?, tab_switch_count = ?
        WHERE id = ? AND is_completed = 0
        ''', (json.dumps(answers_dict, ensure_ascii=False), tab_switch_count, session_id))
    else:
        cursor.execute('''
        UPDATE exam_sessions
        SET student_answers_json = ?
        WHERE id = ? AND is_completed = 0
        ''', (json.dumps(answers_dict, ensure_ascii=False), session_id))
        
    conn.commit()
    conn.close()

def finalize_exam_session(session_id, answers_dict, tab_switch_count=0):
    """Testni yakunlash va serverda ballni hisoblash"""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM exam_sessions WHERE id = ?', (session_id,))
    session = cursor.fetchone()
    if not session or session['is_completed'] == 1:
        conn.close()
        return None

    questions = json.loads(session['session_questions_json'])
    correct_count = 0
    total_questions = len(questions)

    # Server tomonida javoblarni tekshirish
    for idx, q in enumerate(questions):
        q_idx_str = str(idx)
        chosen_opt_index = answers_dict.get(q_idx_str)
        if chosen_opt_index is not None and int(chosen_opt_index) == q['correct']:
            correct_count += 1

    incorrect_count = total_questions - correct_count
    total_score = correct_count  # Har bir to'g'ri javob - 1 ball

    # 18-30 ball: "Joriy nazoratdan o‘tdi"
    # 0-17 ball: "Joriy nazoratdan o‘tmadi"
    if total_score >= 18:
        status_text = "Joriy nazoratdan o‘tdi"
    else:
        status_text = "Joriy nazoratdan o‘tmadi"

    finished_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    cursor.execute('''
    UPDATE exam_sessions
    SET is_completed = 1,
        finished_at = ?,
        total_score = ?,
        correct_count = ?,
        incorrect_count = ?,
        status_text = ?,
        tab_switch_count = ?,
        student_answers_json = ?
    WHERE id = ?
    ''', (
        finished_at,
        total_score,
        correct_count,
        incorrect_count,
        status_text,
        tab_switch_count,
        json.dumps(answers_dict, ensure_ascii=False),
        session_id
    ))

    conn.commit()
    conn.close()
    return {
        "session_id": session_id,
        "total_score": total_score,
        "max_score": 30,
        "correct_count": correct_count,
        "incorrect_count": incorrect_count,
        "status_text": status_text,
        "finished_at": finished_at
    }

def get_all_results_for_teacher(search_query="", group_filter=""):
    """O'qituvchi uchun barcha talabalar natijalarini olish"""
    conn = get_db_connection()
    cursor = conn.cursor()

    query = '''
    SELECT 
        e.id as session_id,
        s.id as student_id,
        s.student_id_number,
        s.full_name,
        s.direction,
        s.course,
        s.group_name,
        e.subject,
        e.started_at,
        e.finished_at,
        e.is_completed,
        e.total_score,
        e.max_score,
        e.correct_count,
        e.incorrect_count,
        e.status_text,
        e.tab_switch_count,
        e.is_modified_by_teacher
    FROM exam_sessions e
    JOIN students s ON e.student_id = s.id
    WHERE 1=1
    '''
    params = []

    if search_query:
        query += " AND (LOWER(s.full_name) LIKE ? OR s.student_id_number LIKE ? OR LOWER(s.group_name) LIKE ? OR LOWER(s.direction) LIKE ?)"
        term = f"%{search_query.lower().strip()}%"
        params.extend([term, term, term, term])

    if group_filter:
        query += " AND s.group_name = ?"
        params.append(group_filter)

    query += " ORDER BY e.id DESC"

    cursor.execute(query, params)
    rows = cursor.fetchall()
    conn.close()
    return [dict(row) for row in rows]

def get_all_groups():
    """Mavjud barcha guruhlar ro'yxatini olish"""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT DISTINCT group_name FROM students ORDER BY group_name ASC')
    rows = cursor.fetchall()
    conn.close()
    return [row['group_name'] for row in rows]

def update_student_score_with_audit(session_id, new_score, reason, teacher_username):
    """O'qituvchi tomonidan ballni o'zgartirish va audit jurnaliga yozish"""
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute('''
    SELECT e.*, s.full_name 
    FROM exam_sessions e
    JOIN students s ON e.student_id = s.id
    WHERE e.id = ?
    ''', (session_id,))
    session = cursor.fetchone()
    if not session:
        conn.close()
        return False, "Sessiya topilmadi"

    old_score = session['total_score']
    old_status = session['status_text']

    new_score = int(new_score)
    if new_score < 0:
        new_score = 0
    if new_score > 30:
        new_score = 30

    new_status = "Joriy nazoratdan o‘tdi" if new_score >= 18 else "Joriy nazoratdan o‘tmadi"
    changed_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Audit jurnaliga yozish
    cursor.execute('''
    INSERT INTO audit_logs (
        session_id, student_name, old_score, new_score,
        old_status, new_status, reason, teacher_username, changed_at
    )
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        session_id,
        session['full_name'],
        old_score,
        new_score,
        old_status,
        new_status,
        reason.strip(),
        teacher_username,
        changed_at
    ))

    # Sessiyani yangilash
    cursor.execute('''
    UPDATE exam_sessions
    SET total_score = ?,
        correct_count = ?,
        incorrect_count = ?,
        status_text = ?,
        is_modified_by_teacher = 1
    WHERE id = ?
    ''', (new_score, new_score, 30 - new_score, new_status, session_id))

    conn.commit()
    conn.close()
    return True, "Ball muvaffaqiyatli o'zgartirildi va audit qayd qilindi"

def get_audit_logs():
    """Audit jurnalini olish"""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM audit_logs ORDER BY id DESC')
    rows = cursor.fetchall()
    conn.close()
    return [dict(row) for row in rows]

def delete_exam_session_with_audit(session_id, teacher_username, reason="O'qituvchi tomonidan natija o'chirildi"):
    """Talaba sessiyasini o'chirish va audit jurnalida saqlash"""
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute('''
    SELECT e.*, s.full_name, s.group_name
    FROM exam_sessions e
    JOIN students s ON e.student_id = s.id
    WHERE e.id = ?
    ''', (session_id,))
    session = cursor.fetchone()
    if not session:
        conn.close()
        return False, "Sessiya topilmadi"

    student_name = f"{session['full_name']} ({session['group_name']})"
    old_score = session['total_score']
    old_status = session['status_text']
    changed_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Auditga yozish
    cursor.execute('''
    INSERT INTO audit_logs (
        session_id, student_name, old_score, new_score,
        old_status, new_status, reason, teacher_username, changed_at
    )
    VALUES (?, ?, ?, 0, ?, 'NATIJA O\'CHIRILDI', ?, ?, ?)
    ''', (
        session_id,
        student_name,
        old_score,
        old_status,
        reason.strip(),
        teacher_username,
        changed_at
    ))

    # Sessiya va studentni o'chirish (talaba qayta topshira olishi uchun)
    student_id = session['student_id']
    cursor.execute('DELETE FROM exam_sessions WHERE id = ?', (session_id,))
    cursor.execute('DELETE FROM students WHERE id = ?', (student_id,))

    conn.commit()
    conn.close()
    return True, "Natija muvaffaqiyatli o'chirildi! Endi talaba testni qaytadan topshira oladi."

def get_student_exam_detail(session_id):
    """Talabaning batafsil javoblarini ko'rish"""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
    SELECT e.*, s.student_id_number, s.full_name, s.direction, s.course, s.group_name
    FROM exam_sessions e
    JOIN students s ON e.student_id = s.id
    WHERE e.id = ?
    ''', (session_id,))
    row = cursor.fetchone()
    conn.close()
    if not row:
        return None

    data = dict(row)
    data['questions'] = json.loads(data['session_questions_json'])
    data['answers'] = json.loads(data['student_answers_json']) if data['student_answers_json'] else {}
    return data


