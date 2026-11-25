# -*- coding: utf-8 -*-
with open("test_full_workflow.py", "r", encoding="utf-8") as f:
    text = f.read()

text = text.replace("driver.find_element(By.XPATH, \"//form//button[@type='submit']\").click()", "driver.find_element(By.CSS_SELECTOR, \"#teacherLoginForm form\").submit()")

with open("test_full_workflow.py", "w", encoding="utf-8") as f:
    f.write(text)
print("Updated teacher login click in test_full_workflow.py")
