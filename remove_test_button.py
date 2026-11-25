# -*- coding: utf-8 -*-
import os
import re

base_dir = r"C:\Users\Asus\.gemini\antigravity\scratch\python_exam_system"

for fname in ["build_html.py", "generate_standalone.py", "templates/index.html"]:
    fpath = os.path.join(base_dir, fname)
    if not os.path.exists(fpath):
        continue
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    # Remove setTeacherDemoMode buttons
    content = re.sub(r'<button\s+[^>]*onclick=["\']setTeacherDemoMode\(\)[^>]*>.*?</button>', '', content, flags=re.DOTALL)
    content = re.sub(r'<button\s+[^>]*onclick=["\']setTeacherDemoMode\(\);\s*navigateHome\(\);["\'][^>]*>.*?</button>', '', content, flags=re.DOTALL)

    # Clean up flex container around ID caption if it still had justify-between
    content = content.replace('flex items-center justify-between', 'flex items-center')

    with open(fpath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Updated {fname}")
