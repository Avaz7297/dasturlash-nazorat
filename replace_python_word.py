# -*- coding: utf-8 -*-
import os

base_dir = r"C:\Users\Asus\.gemini\antigravity\scratch\python_exam_system"

replacements = [
    ("Python Dasturlash | Masofaviy Joriy Nazorat Platformasi", "Dasturlash Fani | Masofaviy Joriy Nazorat Platformasi"),
    ("Python Dasturlash Fanidan Joriy Nazorat", "Dasturlash Fanidan Joriy Nazorat"),
    ("Python dasturlash fanidan masofaviy joriy nazorat sinovi yakunlandi.", "Dasturlash fanidan masofaviy joriy nazorat sinovi yakunlandi."),
    ("Dasturlash (Python)", "Dasturlash fani"),
    ("PythonTest", "Dasturlash"),
    ('<i class="fa-brands fa-python text-amber-400"></i> Python', '<i class="fa-solid fa-code text-blue-500"></i> Dasturlash'),
    ("Python dasturlash tili va dastur kodini yozish", "Dasturlash tili va dastur kodini yozish"),
]

target_files = [
    "build_html.py",
    "generate_standalone.py",
    "app_standalone.js",
    "questions_data.py",
    "templates/index.html",
    "templates/exam.html",
    "templates/result.html",
    "templates/teacher.html"
]

for fn in target_files:
    fpath = os.path.join(base_dir, fn)
    if not os.path.exists(fpath):
        continue
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    changed = False
    for old, new in replacements:
        if old in content:
            content = content.replace(old, new)
            changed = True

    if changed:
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Updated {fn}")

print("Replacement complete.")
