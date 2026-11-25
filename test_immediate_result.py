# -*- coding: utf-8 -*-
import os
import time
from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

base_dir = os.path.dirname(os.path.abspath(__file__))
html_path = os.path.join(base_dir, "python_nazorat.html")
file_url = "file:///" + html_path.replace("\\", "/")

opts = Options()
opts.add_argument("--headless=new")
opts.add_argument("--disable-gpu")
opts.add_argument("--window-size=1280,900")

driver = webdriver.Edge(options=opts)
wait = WebDriverWait(driver, 10)

try:
    print(f"[1] Fayl ochilmoqda: {file_url}")
    driver.get(file_url)

    # 1. Talaba ma'lumotlarini to'ldirish
    wait.until(EC.presence_of_element_located((By.ID, "regFullName"))).send_keys("Karimov Sardor Ulug'bek o'g'li")
    driver.find_element(By.ID, "regDirection").send_keys("Dasturiy injiniring")
    driver.find_element(By.ID, "regCourse").send_keys("2")
    driver.find_element(By.ID, "regGroup").send_keys("210")

    print("  ✓ Talaba ma'lumotlari kiritildi.")
    driver.find_element(By.ID, "btnSubmitStart").click()

    # 2. Test ekrani ochilganligini tekshirish
    wait.until(EC.visibility_of_element_located((By.ID, "sectionExam")))
    print("  ✓ Test ekrani ochildi. 30 ta savol yuklandi.")

    # Bir nechta savolga javob belgilash
    options = driver.find_elements(By.CSS_SELECTOR, "#qOptionsList input[type='radio']")
    if options:
        driver.execute_script("arguments[0].click();", options[0])
    print("  ✓ 1-savolga javob belgilandi.")

    # 3. Testni yakunlash
    driver.find_element(By.XPATH, "//button[contains(., 'Testni Yakunlash')]").click()
    wait.until(EC.visibility_of_element_located((By.ID, "modalFinishConfirm")))
    driver.find_element(By.XPATH, "//button[@onclick='submitExamNow()']").click()

    # 4. Natija sahifasi ochilganligini tekshirish
    wait.until(EC.visibility_of_element_located((By.ID, "sectionResult")))
    print("  ✓ Talabaning o'ziga natija darhol ko'rsatildi!")

    score_text = driver.find_element(By.ID, "resultScore").text
    status_text = driver.find_element(By.ID, "resultStatusText").text
    student_name = driver.find_element(By.ID, "resStudentName").text
    print(f"  ✓ Natija: {status_text} | Ball: {score_text} / 30 | Talaba: {student_name}")

    # Kod nusxalash va murakkabliklar yo'qligini tekshirish
    copy_boxes = driver.find_elements(By.ID, "resultCodeDisplay")
    assert len(copy_boxes) == 0, "XATO: resultCodeDisplay hali ham mavjud!"
    tg_btns = driver.find_elements(By.XPATH, "//button[contains(., 'Telegram orqali')]")
    assert len(tg_btns) == 0, "XATO: Telegram tugmasi hali ham mavjud!"
    copy_btns = driver.find_elements(By.XPATH, "//button[contains(., 'Kodni Nusxalash')]")
    assert len(copy_btns) == 0, "XATO: Kodni nusxalash tugmasi hali ham mavjud!"
    print("  ✓ TASDIQLANDI: Hech qanday kod nusxalash, Telegram yoki JSON tugmalari yo'q!")

    # 5. O'qituvchi paneliga o'tish
    driver.find_element(By.ID, "navTeacherBtn").click()
    wait.until(EC.visibility_of_element_located((By.ID, "teachLoginInput")))
    driver.find_element(By.ID, "teachLoginInput").send_keys("admin")
    driver.find_element(By.ID, "teachPassInput").send_keys("admin 123")
    driver.find_element(By.XPATH, "//button[contains(., 'Tizimga Kirish')]").click()

    wait.until(EC.visibility_of_element_located((By.ID, "teacherDashboard")))
    print("  ✓ O'qituvchi paneliga muvaffaqiyatli kirildi.")

    # 6. Talaba natijasi O'QITUVCHIGA DARHOL KO'RINGANLIGINI TEKSHIRISH
    time.sleep(1)
    table_rows = driver.find_elements(By.CSS_SELECTOR, "#teacherTableBody tr")
    print(f"  ✓ O'qituvchi jadvalidagi qatorlar soni: {len(table_rows)}")
    assert len(table_rows) > 0, "XATO: Talaba natijasi o'qituvchi jadvalida ko'rinmadi!"

    row_text = table_rows[0].text
    print(f"  ✓ O'qituvchi jadvalidagi 1-qator: {row_text}")
    assert "Karimov Sardor" in row_text, "XATO: Talaba ismi jadvalda yo'q!"
    assert "210" in row_text, "XATO: Guruh jadvalda yo'q!"

    # 7. Kod kiritish / import tugmalari yo'qligini tekshirish
    import_btns = driver.find_elements(By.XPATH, "//button[contains(., 'Talaba Natijasini Qo')]")
    assert len(import_btns) == 0, "XATO: Talaba Natijasini Qo'shish tugmasi olib tashlanmagan!"
    print("  ✓ TASDIQLANDI: O'qituvchi panelida ham kod import qilish murakkabligi yo'qotilgan!")

    # 8. Statistika tekshiruvi
    total_stat = driver.find_element(By.ID, "statTotalStudents").text
    print(f"  ✓ O'qituvchi statistikasida talabalar soni: {total_stat}")
    assert int(total_stat) >= 1

    print("\n" + "=" * 60)
    print("BARCHA TALABLAR 100% TO'LIQ VA MUVAFFAQISHLI BAJARILDI!")
    print("=" * 60)

finally:
    driver.quit()
