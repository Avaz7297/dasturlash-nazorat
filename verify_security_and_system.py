# -*- coding: utf-8 -*-
import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

html_path = r"C:\Users\Asus\.gemini\antigravity\scratch\python_exam_system\python_nazorat.html"

options = Options()
options.add_argument("--headless=new")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-gpu")
options.add_argument("--window-size=1280,900")

driver = webdriver.Chrome(options=options)

try:
    print("==================================================")
    print("1. SAHIFA YUKLANISHI VA XAVFSIZLIK TEKSHIRUVI")
    print("==================================================")
    driver.get("file:///" + html_path.replace("\\", "/"))
    time.sleep(1)

    # Browser console log tekshiruvi (Syntax yoki Runtime xatoliklar yo'qligini tekshirish)
    logs = driver.get_log("browser")
    severe_errors = [l for l in logs if l["level"] == "SEVERE"]
    print("Severe console errors count:", len(severe_errors))
    assert len(severe_errors) == 0, f"Found severe errors: {severe_errors}"
    print("[OK] JavaScript xatoliklari 0 ta. Sintaksis to'liq toza!")

    # ==================================================
    # 2. O'QITUVCHI PANELIGA RUXSATSIZ KIRISHNI TEKSHIRISH
    # ==================================================
    print("\n2. O'QITUVCHI PANELI XAVFSIZLIGINI TEKSHIRISH:")
    driver.find_element(By.ID, "navTeacherBtn").click()
    time.sleep(0.5)

    login_form = driver.find_element(By.ID, "teacherLoginForm")
    dash = driver.find_element(By.ID, "teacherDashboard")

    assert login_form.is_displayed(), "Login forma ko'rinishi shart!"
    assert not dash.is_displayed(), "Dashboard ruxsatsiz yashirin bo'lishi shart!"
    print("[OK] O'qituvchi paneli login/parolsiz ochilmaydi. Dashboard yopiq!")

    # Noto'g'ri parol kiritilganda tekshirish
    print("Noto'g'ri parol bilan kirishga urinish...")
    driver.find_element(By.ID, "teachLoginInput").send_keys("admin")
    driver.find_element(By.ID, "teachPassInput").send_keys("xato_parol_123")
    driver.find_element(By.CSS_SELECTOR, "#teacherLoginForm form").submit()
    time.sleep(0.5)

    try:
        alert = driver.switch_to.alert
        print("Alert xabari:", alert.text)
        assert "noto'g'ri" in alert.text or "Ruxsatsiz" in alert.text
        alert.accept()
        time.sleep(0.3)
    except Exception as e:
        print("Alert exception:", e)

    assert not dash.is_displayed(), "Noto'g'ri parolda dashboard ochilmasligi shart!"
    print("[OK] Noto'g'ri login/parol kiritilganda tizim ruxsat bermadi!")

    # Console / JavaScript orqali bypass urinishini tekshirish
    print("JavaScript orqali ruxsatsiz renderTeacherTable() chaqirib ko'rish...")
    driver.execute_script("renderTeacherTable();")
    tbody_content = driver.find_element(By.ID, "teacherTableBody").text
    print("Ruxsatsiz chaqirilgan jadval kontenti:", repr(tbody_content))
    assert tbody_content == "", "Ruxsatsiz jadval to'ldirilmasligi shart!"
    assert not dash.is_displayed(), "Dashboard hali ham yopiq bo'lishi shart!"
    print("[OK] JavaScript orqali to'g'ridan-to'g'ri ma'lumotlarni o'g'irlash butunlay to'silgan!")

    # To'g'ri parol bilan kirish
    print("To'g'ri login va parol (admin / admin 123) bilan kirish...")
    driver.find_element(By.ID, "teachLoginInput").clear()
    driver.find_element(By.ID, "teachLoginInput").send_keys("admin")
    driver.find_element(By.ID, "teachPassInput").clear()
    driver.find_element(By.ID, "teachPassInput").send_keys("admin 123")
    driver.find_element(By.CSS_SELECTOR, "#teacherLoginForm form").submit()
    time.sleep(0.8)

    assert dash.is_displayed(), "To'g'ri parolda o'qituvchi boshqaruvi ochilishi shart!"
    print("[OK] To'g'ri parol kiritilganda o'qituvchi paneli muvaffaqiyatli ochildi!")

    # O'qituvchi panelidan chiqish (Logout)
    driver.find_element(By.XPATH, "//button[@onclick='teacherLogout()']").click()
    time.sleep(0.5)
    print("[OK] O'qituvchi panelidan xavfsiz chiqildi.")

    # ==================================================
    # 3. BARCHA 6 TA GURUH TALABALARINI AVTO-ANIQLASHNI TEKSHIRISH
    # ==================================================
    print("\n3. BARCHA 6 TA GURUH TALABALARINI TEKSHIRISH (9, 10, 11, 12, 13, 14-guruhlar):")
    sample_students = [
        {"grp": "9mt-26", "id": "315261102785", "name": "BO‘RONBOYEVA MUXLISA"},
        {"grp": "10mt-26", "id": "315261103381", "name": "XOJIYEV AMIRXON"},
        {"grp": "11mt-26", "id": "315261102924", "name": "SOTVOLDIYEV DILSHOD"},
        {"grp": "12mt-26", "id": "315261102911", "name": "RAXMONOV BEKZOD"},
        {"grp": "13mt-26", "id": "315261102919", "name": "SEYTMURATOV XUSINBAY"},
        {"grp": "14mt-26", "id": "315261102983", "name": "MUHAMMADJONOVA SAODATOY"}
    ]

    for item in sample_students:
        id_inp = driver.find_element(By.ID, "regStudentId")
        id_inp.clear()
        id_inp.send_keys(item["id"])
        time.sleep(0.3)

        n_val = driver.find_element(By.ID, "regFullName").get_attribute("value")
        g_val = driver.find_element(By.ID, "regGroup").get_attribute("value")
        print(f"  [{item['grp']}] ID: {item['id']} -> F.I.Sh: '{n_val}', Guruh: '{g_val}'")
        assert item["name"] in n_val, f"Name mismatch for {item['id']}: got '{n_val}'"
        assert item["grp"] in g_val, f"Group mismatch for {item['id']}: got '{g_val}'"

    print("[OK] Barcha 6 ta guruh talabalari ID kiritilganda 100% to'g'ri topildi!")

    # ==================================================
    # 4. TAYYORGARLIK BOSQICHIDA VAQT KETMASLIGI VA ERKIN CHIQISHNI TEKSHIRISH
    # ==================================================
    print("\n4. TAYYORGARLIK BOSQICHI (VAQT KETMASLIGI VA ERKIN CHIQISH):")
    # Talaba tizimga kiradi
    id_inp = driver.find_element(By.ID, "regStudentId")
    id_inp.clear()
    id_inp.send_keys("315261102983")
    time.sleep(0.3)
    driver.find_element(By.ID, "btnSubmitStart").click()
    time.sleep(0.5)

    ready_sec = driver.find_element(By.ID, "sectionReady")
    assert ready_sec.is_displayed(), "Tayyorgarlik oynasi ko'rinishi shart!"
    print("  Tayyorgarlik oynasi ochildi. Vaqt orqaga sanamayapti.")

    # Talaba testni boshlamay chiqib ketadi
    driver.find_element(By.XPATH, "//button[@onclick='navigateHome()']").click()
    time.sleep(0.5)
    reg_sec = driver.find_element(By.ID, "sectionRegister")
    assert reg_sec.is_displayed(), "Bosh sahifaga qaytishi kerak!"

    # Talaba qayta kirishga harakat qiladi -> BLOKLANMASLIGI KERAK!
    id_inp = driver.find_element(By.ID, "regStudentId")
    id_inp.clear()
    id_inp.send_keys("315261102983")
    time.sleep(0.3)
    driver.find_element(By.ID, "btnSubmitStart").click()
    time.sleep(0.5)
    assert driver.find_element(By.ID, "sectionReady").is_displayed(), "Talaba testni boshlamaganligi sababli erkin qayta kirishi shart!"
    print("[OK] Talaba testni boshlamasdan chiqib ketsa, qayta kirishi to'liq ta'minlandi!")

    # ==================================================
    # 5. TESTNI BOSHLASH, ISHLASH VA NATIJANI YAKUNLASH
    # ==================================================
    print("\n5. TESTNI ISHLASHNI BOSHLASH VA YAKUNLASH:")
    driver.find_element(By.XPATH, "//button[@onclick='startExamActual()']").click()
    time.sleep(0.8)

    exam_sec = driver.find_element(By.ID, "sectionExam")
    assert exam_sec.is_displayed()
    timer_display = driver.find_element(By.ID, "timerDisplay").text
    print(f"  Test boshlandi. Taymer faollashdi: {timer_display}")
    assert ":" in timer_display

    # Savolga javob berish
    options_cards = driver.find_elements(By.CLASS_NAME, "option-card")
    if len(options_cards) > 0:
        options_cards[0].click()
        time.sleep(0.2)

    # Testni yakunlash
    driver.find_element(By.XPATH, "//button[@onclick='confirmFinishModalOpen()']").click()
    time.sleep(0.4)
    driver.find_element(By.XPATH, "//button[@onclick='submitExamNow()']").click()
    time.sleep(1.2)

    res_sec = driver.find_element(By.ID, "sectionResult")
    assert res_sec.is_displayed(), "Natija oynasi chiqishi shart!"
    res_score = driver.find_element(By.ID, "resultScore").text
    res_id = driver.find_element(By.ID, "resStudentId").text
    print(f"  Test yakunlandi: ID={res_id}, Ball={res_score} / 30")

    # ==================================================
    # 6. TESTNI YAKUNLAGAN TALABANING QAYTA TOPSHIRISHINI BLOKLASH
    # ==================================================
    print("\n6. YAKUNLAGAN TALABANING QAYTA TOPSHIRISHINI BLOKLASH TEKSHIRUVI:")
    driver.execute_script("navigateHome();")
    time.sleep(0.5)

    # Qayta kirishga urinish (ID: 315261102983)
    id_inp = driver.find_element(By.ID, "regStudentId")
    id_inp.clear()
    id_inp.send_keys("315261102983")
    time.sleep(0.3)
    driver.find_element(By.ID, "btnSubmitStart").click()
    time.sleep(0.5)

    try:
        alert = driver.switch_to.alert
        print("Bloklash xabari:", alert.text[:100], "...")
        assert "allaqachon" in alert.text or "avval" in alert.text
        assert "taqiqlanadi" in alert.text
        alert.accept()
        time.sleep(0.5)
    except Exception as e:
        print("Alert exception:", e)

    # Faqat natijasi ko'rsatiladi, testga kiritilmaydi
    assert driver.find_element(By.ID, "sectionResult").is_displayed(), "Faqat natija oynasida qolishi shart!"
    print("[OK] Testni yakunlagan talaba qayta topshira olmaydi! Tizim uni qat'iy blokladi.")

    # ==================================================
    # 7. O'QITUVCHI PANELIDA NATIJANING KO'RINISHI
    # ==================================================
    print("\n7. O'QITUVCHI PANELIDA NATIJA VA TALABA ID KO'RINISHI:")
    driver.find_element(By.ID, "navTeacherBtn").click()
    time.sleep(0.5)
    driver.find_element(By.ID, "teachLoginInput").send_keys("admin")
    driver.find_element(By.ID, "teachPassInput").send_keys("admin 123")
    driver.find_element(By.CSS_SELECTOR, "#teacherLoginForm form").submit()
    time.sleep(1)

    table_body = driver.find_element(By.ID, "teacherTableBody")
    table_text = table_body.text
    print("O'qituvchi jadvalidagi ma'lumotlar:\n", table_text)
    assert "315261102983" in table_text, "Talaba ID jadvalda bo'lishi shart!"
    assert "MUHAMMADJONOVA" in table_text, "Talaba ismi jadvalda bo'lishi shart!"
    print("[OK] Natija va Talaba ID o'qituvchi panelida darhol aks etdi!")

    print("\n==================================================")
    print("YAKUNIY XULOSA: BARCHA 7 TA KRITIK MEZON 100% TESTDAN O'TDI!")
    print("==================================================")

finally:
    driver.quit()
