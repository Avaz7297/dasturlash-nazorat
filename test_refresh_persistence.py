import os
import sys
import time
from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def run_test():
    html_file = os.path.abspath("C:/Users/Asus/.gemini/antigravity/scratch/python_exam_system/python_nazorat.html")
    file_url = f"file:///{html_file.replace(os.sep, '/')}"

    edge_options = Options()
    edge_options.add_argument("--headless=new")
    edge_options.add_argument("--disable-gpu")
    edge_options.add_argument("--no-sandbox")
    edge_options.add_argument("--window-size=1280,800")

    driver = webdriver.Edge(options=edge_options)
    wait = WebDriverWait(driver, 10)

    try:
        print("[1] Ochilmoqda:", file_url)
        driver.get(file_url)
        time.sleep(1)

        # Clear localStorage for clean test run
        driver.execute_script("localStorage.clear(); sessionStorage.clear(); location.reload();")
        time.sleep(1)

        # 1. Tekshirish: 7 ta mavzu qutisi olib tashlanganligini tekshirish
        page_source = driver.page_source
        assert "7 ta nazorat mavzusi" not in page_source, "XATO: '7 ta nazorat mavzusi' qutisi sahifada mavjud!"
        print("  ✓ '7 ta nazorat mavzusi' qutisi muvaffaqiyatli olib tashlangan.")

        # 2. Ro'yxatdan o'tish
        name_input = driver.find_element(By.ID, "regFullName")
        dir_input = driver.find_element(By.ID, "regDirection")
        course_select = driver.find_element(By.ID, "regCourse")
        group_input = driver.find_element(By.ID, "regGroup")

        name_input.send_keys("Testchi Alisher Botirovich")
        dir_input.send_keys("Axborot xavfsizligi")
        
        for option in course_select.find_elements(By.TAG_NAME, "option"):
            if option.get_attribute("value") == "2":
                option.click()
                break

        group_input.send_keys("314")
        print("  ✓ Talaba ma'lumotlari kiritildi (Guruh: 314).")

        # Boshlash tugmasini bosish
        start_btn = driver.find_element(By.ID, "btnSubmitStart")
        driver.execute_script("arguments[0].click();", start_btn)
        time.sleep(1)

        # 3. Test oynasi ochilganligini tekshirish
        exam_section = driver.find_element(By.ID, "sectionExam")
        assert "hidden" not in exam_section.get_attribute("class"), "XATO: Test oynasi ochilmadi!"
        
        timer_text = driver.find_element(By.ID, "timerDisplay").text
        print(f"  ✓ Test boshlandi. Boshlang'ich taymer ko'rsatkichi: {timer_text}")
        assert "59:" in timer_text or "60:00" in timer_text, f"XATO: Taymer 60 daqiqadan boshlanmadi ({timer_text})"

        # 4. 1-savolga javob berish (1-variantni tanlash)
        labels = driver.find_elements(By.CSS_SELECTOR, "#qOptionsList label")
        assert len(labels) == 4, "XATO: Variantlar 4 ta emas!"
        labels[1].click() # B variant
        time.sleep(0.5)

        # 2-savolga o'tish
        btn_next = driver.find_element(By.ID, "btnNextQ")
        btn_next.click()
        time.sleep(0.5)

        q_curr = driver.find_element(By.ID, "qCurrentNumber").text
        assert q_curr == "2", f"XATO: 2-savolga o'tilmadi (qCurrentNumber: {q_curr})"
        print("  ✓ 2-savolga o'tildi.")

        # 2-savolga ham javob berish (C variant)
        labels = driver.find_elements(By.CSS_SELECTOR, "#qOptionsList label")
        labels[2].click()
        time.sleep(0.5)

        answered_badge = driver.find_element(By.ID, "mapAnsweredCount").text
        assert answered_badge == "2", f"XATO: Javob berilganlar soni 2 emas ({answered_badge})"
        print("  ✓ 2 ta savolga javob belgilandi.")

        # =========================================================================
        # 5. ENG MUHIM QADAM: SAHIFANI YANGILASH (F5 / RELOAD) SINAVI
        # =========================================================================
        print("\n[5] Sahifa yangilanmoqda (F5 / reload)...")
        driver.refresh()
        time.sleep(2)

        # Tekshirish: Ro'yxatdan o'tish oynasiga chiqib ketmadimi?
        reg_section = driver.find_element(By.ID, "sectionRegister")
        assert "hidden" in reg_section.get_attribute("class"), "XATO: Yangilanishdan so'ng ro'yxatdan o'tish oynasiga chiqib ketdi!"

        exam_section = driver.find_element(By.ID, "sectionExam")
        assert "hidden" not in exam_section.get_attribute("class"), "XATO: Yangilanishdan so'ng test oynasida qolmadi!"
        print("  ✓ Yangilangandan so'ng TEST OYNASIDA QOLDI (asosiy sahifaga chiqib ketmadi)!")

        # Tekshirish: Talaba ma'lumotlari saqlanganmi?
        student_name = driver.find_element(By.ID, "examStudentName").text
        assert "Testchi Alisher Botirovich" in student_name, f"XATO: Talaba ismi tiklanmadi ({student_name})"
        print(f"  ✓ Talaba ismi to'liq saqlanib qoldi: {student_name}")

        # Tekshirish: 2-savolda qolganmi?
        q_curr_after = driver.find_element(By.ID, "qCurrentNumber").text
        assert q_curr_after == "2", f"XATO: 2-savolda qolmadi, hozir {q_curr_after}"
        print(f"  ✓ Aynan 2-savolda turibdi: {q_curr_after}-savol.")

        # Tekshirish: Oldingi javoblar saqlanganmi?
        answered_badge_after = driver.find_element(By.ID, "mapAnsweredCount").text
        assert answered_badge_after == "2", f"XATO: Belgilangan javoblar soni tiklanmadi ({answered_badge_after})"
        print(f"  ✓ Belgilangan javoblar xaritasi tiklandi: {answered_badge_after} ta belgilangan.")

        # Tekshirish: Taymer davom etyaptimi?
        timer_after = driver.find_element(By.ID, "timerDisplay").text
        print(f"  ✓ Taymer yangilanishdan keyin davom etmoqda: {timer_after}")
        assert "59:" in timer_after or "58:" in timer_after, f"XATO: Taymer noto'g'ri ({timer_after})"

        # 6. Testni yakunlash
        print("\n[6] Test yakunlanmoqda...")
        driver.execute_script("submitExamNow();")
        time.sleep(1)

        result_section = driver.find_element(By.ID, "sectionResult")
        assert "hidden" not in result_section.get_attribute("class"), "XATO: Natija oynasi ochilmadi!"
        score_text = driver.find_element(By.ID, "resultScore").text
        print(f"  ✓ Natija oynasi ko'rsatildi. To'plangan ball: {score_text} / 30")

        # 7. Natija oynasida sahifani yangilash sinovi
        print("\n[7] Natija oynasida sahifa yangilanmoqda (F5 / reload)...")
        driver.refresh()
        time.sleep(2)

        result_section_after = driver.find_element(By.ID, "sectionResult")
        assert "hidden" not in result_section_after.get_attribute("class"), "XATO: Natija oynasidan chiqib ketdi!"
        score_after = driver.find_element(By.ID, "resultScore").text
        assert score_after == score_text, "XATO: Natija bali yangilanishdan so'ng o'zgardi!"
        print(f"  ✓ Natija sahifasida yangilangandan keyin ham natija oynasida qoldi (Ball: {score_after})!")

        # 8. O'qituvchi paneli sinovi
        print("\n[8] O'qituvchi bo'limiga kirish sinovi...")
        driver.execute_script("toggleTeacherSection();")
        time.sleep(0.5)

        teacher_section = driver.find_element(By.ID, "sectionTeacher")
        assert "hidden" not in teacher_section.get_attribute("class")

        # Login: admin, Parol: admin 123
        driver.find_element(By.ID, "teachLoginInput").send_keys("admin")
        driver.find_element(By.ID, "teachPassInput").send_keys("admin 123")
        driver.find_element(By.CSS_SELECTOR, "#teacherLoginForm button[type='submit']").click()
        time.sleep(1)

        dashboard = driver.find_element(By.ID, "teacherDashboard")
        assert "hidden" not in dashboard.get_attribute("class"), "XATO: O'qituvchi dashboardi ochilmadi!"
        print("  ✓ O'qituvchi paneliga kirildi (Login: admin, Parol: admin 123).")

        # 9. O'qituvchi panelida sahifani yangilash sinovi
        print("\n[9] O'qituvchi panelida sahifa yangilanmoqda (F5 / reload)...")
        driver.refresh()
        time.sleep(2)

        teacher_section_after = driver.find_element(By.ID, "sectionTeacher")
        assert "hidden" not in teacher_section_after.get_attribute("class"), "XATO: O'qituvchi bo'limidan chiqib ketdi!"
        dashboard_after = driver.find_element(By.ID, "teacherDashboard")
        assert "hidden" not in dashboard_after.get_attribute("class"), "XATO: O'qituvchi dashboardidan chiqib ketdi!"
        print("  ✓ O'qituvchi panelida yangilangandan keyin ham dashboardda qoldi!")

        print("\n============================================================")
        print("BARCHA TEKSHIRUVLAR 100% MUVAFFAQISHLI O'TDI!")
        print("============================================================")

    finally:
        driver.quit()

if __name__ == "__main__":
    run_test()
