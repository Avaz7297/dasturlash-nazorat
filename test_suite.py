# -*- coding: utf-8 -*-
"""
Tizimni to'liq avtomatlashtirilgan test sinovi
"""
import sys
import os
import json
import io

# Loyiha papkasini yo'lga qo'shish
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app import app, sample_exam_questions
from database import (
    init_db,
    check_student_already_tested,
    register_student_and_session,
    get_session_by_id,
    finalize_exam_session,
    get_all_results_for_teacher,
    update_student_score_with_audit,
    get_audit_logs,
    get_student_exam_detail
)
from export_utils import generate_excel_report, generate_pdf_report

def run_tests():
    print("=" * 60)
    print("PYTHON TEST PLATFORMASI SINOV DASTURI BOSHLANDI")
    print("=" * 60)

    # 1. DB yaratilishi
    init_db()
    print("[TEST 1] Ma'lumotlar bazasi muvaffaqiyatli ishga tushirildi.")

    # 2. Savollar tanlanishi testi
    sampled = sample_exam_questions()
    assert len(sampled) == 30, f"Savollar soni 30 bo'lishi kerak, {len(sampled)} olindi!"
    for q in sampled:
        assert len(q['options']) == 4, "Variantlar 4 ta bo'lishi kerak!"
        assert 0 <= q['correct'] < 4, "To'g'ri variant indeksi 0..3 oralig'ida bo'lishi kerak!"
    print("[TEST 2] 30 ta savolni tanlash va aralashtirish testi: O'TDI.")

    # 3. Talaba ro'yxatdan o'tishi va test topshirishi (Yuqori ball: 25 ball)
    s1_id = register_student_and_session(
        full_name="Aliyev Jasur Bekzod o'g'li",
        direction="Dasturiy injiniring",
        course=2,
        group_name="941-22",
        sampled_questions=sampled
    )
    assert s1_id > 0, "Sessiya yaratilmadi!"

    # 25 ta to'g'ri, 5 ta noto'g'ri javob beramiz
    answers1 = {}
    for i in range(25):
        answers1[str(i)] = sampled[i]['correct']
    for i in range(25, 30):
        answers1[str(i)] = (sampled[i]['correct'] + 1) % 4 # Noto'g'ri javob

    res1 = finalize_exam_session(s1_id, answers1, tab_switch_count=1)
    assert res1['total_score'] == 25, f"Ball 25 bo'lishi kerak, {res1['total_score']} chiqdi!"
    assert res1['correct_count'] == 25
    assert res1['incorrect_count'] == 5
    assert res1['status_text'] == "Joriy nazoratdan o‘tdi"
    print(f"[TEST 3] Talaba 1 (25 ball): '{res1['status_text']}' natijasi: O'TDI.")

    # 4. Ikkinchi talaba (Past ball: 14 ball -> Yiqilgan)
    sampled2 = sample_exam_questions()
    s2_id = register_student_and_session(
        full_name="Sobirova Malika Anvar qizi",
        direction="Axborot xavfsizligi",
        course=3,
        group_name="932-21",
        sampled_questions=sampled2
    )
    answers2 = {}
    for i in range(14):
        answers2[str(i)] = sampled2[i]['correct']
    for i in range(14, 30):
        answers2[str(i)] = (sampled2[i]['correct'] + 1) % 4

    res2 = finalize_exam_session(s2_id, answers2, tab_switch_count=3)
    assert res2['total_score'] == 14
    assert res2['status_text'] == "Joriy nazoratdan o‘tmadi"
    print(f"[TEST 4] Talaba 2 (14 ball): '{res2['status_text']}' natijasi: O'TDI.")

    # 5. Qayta topshirishni cheklash testi
    existing = check_student_already_tested("Aliyev Jasur Bekzod o'g'li", "941-22")
    assert existing is not None, "Talaba qayta topshirish tekshiruvida topilmadi!"
    print("[TEST 5] Bir talabaning qayta topshirishini cheklash testi: O'TDI.")

    # 6. O'qituvchi paneli ma'lumotlarini olish
    all_results = get_all_results_for_teacher()
    assert len(all_results) >= 2, "Kamida 2 ta natija bo'lishi kerak!"
    print(f"[TEST 6] O'qituvchi jadvali uchun {len(all_results)} ta natija olindi: O'TDI.")

    # 7. Ballni o'zgartirish va audit jurnaliga yozish
    success, msg = update_student_score_with_audit(
        session_id=s2_id,
        new_score=19,
        reason="Apellyatsiya arizasi ko'rib chiqilib, hisoblash xatosi to'g'rilandi",
        teacher_username="admin"
    )
    assert success is True, "Ball o'zgartirish muvaffaqiyatsiz bo'ldi!"
    updated_session = get_session_by_id(s2_id)
    assert updated_session['total_score'] == 19
    assert updated_session['status_text'] == "Joriy nazoratdan o‘tdi"
    assert updated_session['is_modified_by_teacher'] == 1

    logs = get_audit_logs()
    assert len(logs) >= 1, "Audit jurnali bo'sh!"
    assert logs[0]['old_score'] == 14
    assert logs[0]['new_score'] == 19
    print(f"[TEST 7] Ballni tahrirlash va Audit jurnali ({logs[0]['reason']}): O'TDI.")

    # 8. Excel hisoboti generatsiyasi testi
    excel_bytes = generate_excel_report(all_results)
    assert len(excel_bytes) > 1000, "Excel fayli hajmi juda kichik!"
    print(f"[TEST 8] Excel hisoboti (.xlsx) muvaffaqiyatli generatsiya qilindi ({len(excel_bytes)} bayt): O'TDI.")

    # 9. PDF hisoboti generatsiyasi testi
    pdf_bytes = generate_pdf_report(all_results)
    assert len(pdf_bytes) > 1000, "PDF fayli hajmi juda kichik!"
    print(f"[TEST 9] PDF hisoboti (.pdf) muvaffaqiyatli generatsiya qilindi ({len(pdf_bytes)} bayt): O'TDI.")

    # 10. Flask Test Client orqali HTTP marshrutlar testi
    print("\n[TEST 10] Flask HTTP endpointlar testi boshlandi:")
    with app.test_client() as client:
        # Bosh sahifa
        r = client.get('/')
        assert r.status_code == 200
        assert "Python Dasturlash Fanidan Joriy Nazorat" in r.data.decode('utf-8')
        print("  - GET /: 200 OK")

        # Login sahifasi
        r = client.get('/login')
        assert r.status_code == 200
        print("  - GET /login: 200 OK")

        # O'qituvchi login qilish
        r = client.post('/login', data={'username': 'admin', 'password': 'admin123'}, follow_redirects=True)
        assert r.status_code == 200
        assert "O'qituvchi Paneli" in r.data.decode('utf-8')
        print("  - POST /login (muvaffaqiyatli kirish): 200 OK")

        # O'qituvchi paneli
        r = client.get('/teacher')
        assert r.status_code == 200
        print("  - GET /teacher: 200 OK")

        # Excel export marshruti
        r = client.get('/teacher/export/excel')
        assert r.status_code == 200
        assert r.headers['Content-Type'] == "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        print("  - GET /teacher/export/excel: 200 OK")

        # PDF export marshruti
        r = client.get('/teacher/export/pdf')
        assert r.status_code == 200
        assert r.headers['Content-Type'] == "application/pdf"
        print("  - GET /teacher/export/pdf: 200 OK")

        # Audit jurnali sahifasi
        r = client.get('/teacher/audit')
        assert r.status_code == 200
        assert "Audit jurnali" in r.data.decode('utf-8')
        print("  - GET /teacher/audit: 200 OK")

        # Talaba batafsil javoblari API
        r = client.get(f'/api/teacher/student/{s1_id}')
        assert r.status_code == 200
        data = json.loads(r.data.decode('utf-8'))
        assert data['success'] is True
        assert len(data['data']['questions']) == 30
        print("  - GET /api/teacher/student/<id>: 200 OK")

    print("\n" + "=" * 60)
    print("BARCHA TESTLAR (10 TA) 100% MUVAFFAQIYATLI O'TDI!")
    print("=" * 60)

if __name__ == '__main__':
    run_tests()
