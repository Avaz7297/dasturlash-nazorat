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
    print("1. Opening HTML file...")
    driver.get("file:///" + html_path.replace("\\", "/"))
    time.sleep(1)

    # 1. Check title
    print("Title:", driver.title)
    assert "Python Dasturlash" in driver.title

    # 2. Enter 9mt-26 student: 315261102785 (BO‘RONBOYEVA MUXLISA KOMILJON QIZI)
    id_input = driver.find_element(By.ID, "regStudentId")
    id_input.clear()
    id_input.send_keys("315261102785")
    time.sleep(0.5)

    name_val = driver.find_element(By.ID, "regFullName").get_attribute("value")
    group_val = driver.find_element(By.ID, "regGroup").get_attribute("value")
    print(f"Auto-filled: Name='{name_val}', Group='{group_val}'")
    assert "BO‘RONBOYEVA MUXLISA" in name_val
    assert "9mt-26" in group_val

    # 3. Submit register form -> should go to Ready screen (NOT exam, timer NOT running yet!)
    print("Submitting login form to enter Ready screen...")
    driver.find_element(By.ID, "btnSubmitStart").click()
    time.sleep(1)

    ready_sec = driver.find_element(By.ID, "sectionReady")
    assert ready_sec.is_displayed(), "sectionReady should be visible!"
    ready_id = driver.find_element(By.ID, "readyStudentId").text
    ready_name = driver.find_element(By.ID, "readyStudentName").text
    print(f"Ready screen shows: ID={ready_id}, Name={ready_name}")
    assert ready_id == "315261102785"

    # Check that exam has NOT started in storage
    has_active_exam = driver.execute_script("return SafeStorage.getItem('py_exam_active_session_v1') !== null;")
    print("Active exam started in storage?", has_active_exam)
    assert not has_active_exam, "Exam should NOT be active yet!"

    # 4. Student leaves before starting (clicks Chiqish / Orqaga)
    print("Testing leaving before exam starts...")
    driver.execute_script('navigateHome()')
    time.sleep(0.5)
    reg_sec = driver.find_element(By.ID, "sectionRegister")
    assert reg_sec.is_displayed(), "Should be back on register screen!"

    # Verify student is NOT blocked from entering again
    stored_students = driver.execute_script("return getStoredStudents();")
    print("Stored students after leaving:", len(stored_students))
    assert len(stored_students) == 0, "No student should be saved as tested!"

    # 5. Now student enters again and actually starts test
    print("Student logs in again...")
    id_input = driver.find_element(By.ID, "regStudentId")
    id_input.clear()
    id_input.send_keys("315261102785")
    time.sleep(0.5)
    driver.find_element(By.ID, "btnSubmitStart").click()
    time.sleep(1)

    print("Now clicking 'Testni Ishlashni Boshlash'...")
    driver.find_element(By.XPATH, "//button[@onclick='startExamActual()']").click()
    time.sleep(1)

    exam_sec = driver.find_element(By.ID, "sectionExam")
    assert exam_sec.is_displayed(), "sectionExam should be visible now!"

    timer_text = driver.find_element(By.ID, "timerDisplay").text
    print("Timer display on start:", timer_text)
    assert ":" in timer_text

    # 6. Answer a couple questions
    print("Answering question 1...")
    options_cards = driver.find_elements(By.CLASS_NAME, "option-card")
    if len(options_cards) > 0:
        options_cards[0].click()
        time.sleep(0.3)

    # Click Next
    driver.find_element(By.ID, "btnNextQ").click()
    time.sleep(0.5)
    q_num = driver.find_element(By.ID, "qCurrentNumber").text
    print("Current question after Next:", q_num)
    assert q_num == "2"

    # 7. Finish Exam
    print("Finishing exam...")
    driver.find_element(By.XPATH, "//button[@onclick='confirmFinishModalOpen()']").click()
    time.sleep(0.5)
    modal_finish = driver.find_element(By.ID, "modalFinishConfirm")
    assert modal_finish.is_displayed()

    # Click Yakunlash in modal
    driver.find_element(By.XPATH, "//button[@onclick='submitExamNow()']").click()
    time.sleep(1.5)

    res_sec = driver.find_element(By.ID, "sectionResult")
    assert res_sec.is_displayed(), "sectionResult should be visible now!"

    res_id = driver.find_element(By.ID, "resStudentId").text
    res_score = driver.find_element(By.ID, "resultScore").text
    res_status = driver.find_element(By.ID, "resultStatusText").text
    print(f"Result Page: ID={res_id}, Score={res_score}/30, Status='{res_status}'")
    assert res_id == "315261102785"

    # 8. Test Retake Blocking!
    print("Testing retake blocking for completed student...")
    driver.execute_script('navigateHome()')
    time.sleep(0.5)

    # Try entering again with 315261102785
    id_input = driver.find_element(By.ID, "regStudentId")
    id_input.clear()
    id_input.send_keys("315261102785")
    time.sleep(0.5)

    # Click submit
    driver.find_element(By.ID, "btnSubmitStart").click()
    time.sleep(0.5)

    # Alert should appear blocking entry
    try:
        alert = driver.switch_to.alert
        alert_text = alert.text
        print("Alert text when trying to retake:", alert_text[:120], "...")
        assert "allaqachon" in alert_text or "avval" in alert_text
        assert "taqiqlanadi" in alert_text
        alert.accept()
        time.sleep(0.5)
    except Exception as e:
        print("Alert handle exception:", e)

    # Verify that view was directed to result page
    res_sec = driver.find_element(By.ID, "sectionResult")
    assert res_sec.is_displayed(), "Student should be shown their result page, not allowed to take test!"
    print("SUCCESS: Student was blocked from retaking and shown their result!")

    # 9. Test Teacher Sinov (Test) Mode (000000000000)
    print("Testing Teacher Test Mode...")
    driver.execute_script('navigateHome()')
    time.sleep(0.5)

    driver.find_element(By.XPATH, "//button[@onclick='setTeacherDemoMode()']").click()
    time.sleep(0.5)
    test_id_val = driver.find_element(By.ID, "regStudentId").get_attribute("value")
    print("Demo mode ID:", test_id_val)
    assert test_id_val == "000000000000"

    driver.find_element(By.ID, "btnSubmitStart").click()
    time.sleep(0.5)
    driver.find_element(By.XPATH, "//button[@onclick='startExamActual()']").click()
    time.sleep(0.5)
    driver.find_element(By.XPATH, "//button[@onclick='confirmFinishModalOpen()']").click()
    time.sleep(0.3)
    driver.find_element(By.XPATH, "//button[@onclick='submitExamNow()']").click()
    time.sleep(1)

    print("Teacher test completed. Now testing repeat run for teacher ID...")
    driver.execute_script('navigateHome()')
    time.sleep(0.5)
    driver.find_element(By.XPATH, "//button[@onclick='setTeacherDemoMode()']").click()
    time.sleep(0.5)
    driver.find_element(By.ID, "btnSubmitStart").click()
    time.sleep(0.5)
    assert driver.find_element(By.ID, "sectionReady").is_displayed(), "Teacher should be able to run test repeatedly without block!"
    print("SUCCESS: Teacher test mode has unlimited re-takes!")

    # 10. Test Teacher Panel
    print("Testing Teacher Panel...")
    driver.find_element(By.ID, "navTeacherBtn").click()
    time.sleep(0.5)

    driver.find_element(By.ID, "teachLoginInput").send_keys("admin")
    driver.find_element(By.ID, "teachPassInput").send_keys("admin 123")
    driver.find_element(By.CSS_SELECTOR, "#teacherLoginForm form").submit()
    time.sleep(1)

    dash = driver.find_element(By.ID, "teacherDashboard")
    assert dash.is_displayed(), "Teacher dashboard should be visible!"

    # Verify table has results with Talaba ID
    tbody = driver.find_element(By.ID, "teacherTableBody")
    rows = tbody.find_elements(By.TAG_NAME, "tr")
    print("Teacher table rows count:", len(rows))
    assert len(rows) >= 1

    first_row_text = rows[0].text
    print("First row text:", first_row_text)
    assert "315261102785" in first_row_text or "000000000000" in first_row_text
    print("SUCCESS: Teacher table contains Talaba ID!")

    # Check stats
    stat_total = driver.find_element(By.ID, "statTotalStudents").text
    print("Stat total students:", stat_total)
    assert "/ 130" in stat_total

    print("\n==========================================")
    print("ALL TESTS PASSED WITH 100% SUCCESS!")
    print("==========================================")

finally:
    driver.quit()
