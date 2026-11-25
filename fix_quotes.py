# -*- coding: utf-8 -*-
for fname in ["build_html.py", "app_standalone.js"]:
    with open(fname, "r", encoding="utf-8") as f:
        text = f.read()
    
    text = text.replace("title=\"Batafsil ko'rish\"", 'title="Batafsil ko‘rish"')
    text = text.replace("title=\"Talaba natijasini o'chirish (qayta topshirishga ruxsat)\"", 'title="Talaba natijasini o‘chirish (qayta topshirishga ruxsat)"')
    text = text.replace("bo'sh", 'bo‘sh')
    text = text.replace("o'chirish", 'o‘chirish')
    text = text.replace("o'chiril", 'o‘chiril')
    text = text.replace("O'qituvchi", 'O‘qituvchi')
    text = text.replace("o'tdi", 'o‘tdi')
    text = text.replace("o'tmadi", 'o‘tmadi')

    with open(fname, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"Sanitized {fname}")

