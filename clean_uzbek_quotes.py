# -*- coding: utf-8 -*-
import re

for fname in ["build_html.py", "app_standalone.js"]:
    with open(fname, "r", encoding="utf-8") as f:
        code = f.read()

    # Replace (To'g'ri) with (To‘g‘ri)
    code = code.replace("(To\\'g\\'ri)", "(To‘g‘ri)")
    code = code.replace("(To\'g\'ri)", "(To‘g‘ri)")
    code = code.replace("To'g'ri", "To‘g‘ri")
    code = code.replace("Noto'g'ri", "Noto‘g‘ri")
    code = code.replace("to'g'ri", "to‘g‘ri")
    code = code.replace("noto'g'ri", "noto‘g‘ri")
    code = code.replace("o'tdi", "o‘tdi")
    code = code.replace("o'tmadi", "o‘tmadi")
    code = code.replace("O'tdi", "O‘tdi")
    code = code.replace("O'tmadi", "O‘tmadi")
    code = code.replace("o'chirish", "o‘chirish")
    code = code.replace("o'chiril", "o‘chiril")
    code = code.replace("O'chirish", "O‘chirish")
    code = code.replace("ko'rish", "ko‘rish")
    code = code.replace("Ko'rish", "Ko‘rish")
    code = code.replace("bo'sh", "bo‘sh")

    with open(fname, "w", encoding="utf-8") as f:
        f.write(code)
    print(f"Cleaned {fname}")
