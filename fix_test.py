# -*- coding: utf-8 -*-
with open("test_full_workflow.py", "r", encoding="utf-8") as f:
    text = f.read()

text = text.replace("driver.find_element(By.XPATH, \"//button[@onclick='navigateHome()']\").click()", "driver.execute_script('navigateHome()')")

with open("test_full_workflow.py", "w", encoding="utf-8") as f:
    f.write(text)
print("Updated test_full_workflow.py")
