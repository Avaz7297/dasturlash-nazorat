# -*- coding: utf-8 -*-
with open("python_nazorat.html", "r", encoding="utf-8") as f:
    lines = f.readlines()

for i in range(max(0, 1880), min(len(lines), 1895)):
    print(f"{i+1}: {repr(lines[i])}")
