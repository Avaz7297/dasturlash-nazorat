# -*- coding: utf-8 -*-
import os
import sys
import time
import re
import subprocess
import threading

base_dir = r"C:\Users\Asus\.gemini\antigravity\scratch\python_exam_system"
desktop_dir = r"C:\Users\Asus\Desktop"

# 1. Start Flask app in background thread/process
print("[1/2] Flask server ishga tushirilmoqda (http://127.0.0.1:5000)...")
flask_proc = subprocess.Popen(
    [sys.executable, "app.py"],
    cwd=base_dir,
    stdout=subprocess.PIPE,
    stderr=subprocess.STDOUT,
    text=True,
    encoding="utf-8"
)

# 2. Start cloudflared tunnel
cloudflared_bin = os.path.join(base_dir, "cloudflared.exe")
if not os.path.exists(cloudflared_bin):
    print("Xatolik: cloudflared.exe topilmadi!")
    sys.exit(1)

print("[2/2] Cloudflare xavfsiz onlayn tuneli ochilmoqda...")
tunnel_proc = subprocess.Popen(
    [cloudflared_bin, "tunnel", "--url", "http://127.0.0.1:5000"],
    cwd=base_dir,
    stdout=subprocess.PIPE,
    stderr=subprocess.STDOUT,
    text=True,
    encoding="utf-8"
)

public_url = None
url_pattern = re.compile(r"https://[a-zA-Z0-9\-]+\.trycloudflare\.com")

start_time = time.time()
while time.time() - start_time < 30:
    line = tunnel_proc.stdout.readline()
    if not line:
        continue
    # print(line.strip())
    match = url_pattern.search(line)
    if match:
        public_url = match.group(0)
        break

if public_url:
    print("=" * 70)
    print("YAKUNIY JONLI IMTIHON LINKI (ONLAYN HAVOLA):")
    print(f"👉 {public_url}")
    print("=" * 70)

    # Save to desktop
    desktop_file = os.path.join(desktop_dir, "IMTIHON_LINKI.txt")
    with open(desktop_file, "w", encoding="utf-8") as f:
        f.write("=" * 60 + "\n")
        f.write("PYTHON FANIDAN JORIY NAZORAT IMTIHONI ONLAYN HAVOLASI\n")
        f.write("=" * 60 + "\n\n")
        f.write(f"Talabalar uchun yagona havola:\n👉 {public_url}\n\n")
        f.write("O'qituvchi boshqaruv paneli:\n")
        f.write(f"👉 {public_url}\n")
        f.write("   (O'qituvchi Kabineti tugmasini bosib kiriladi)\n")
        f.write("   Login: admin\n")
        f.write("   Parol: admin 123 (yoki admin123)\n\n")
        f.write("Eslatma:\n")
        f.write("- Barcha viloyatlardagi talabalar telefonidan yoki kompyuteridan shu havolaga kiradi.\n")
        f.write("- Testni yakunlagan talabalar natijasi avtomatik sizning o'qituvchi panelingizga tushadi.\n")
        f.write("- Talabalar testni faqat 1 marta topshira oladi.\n")
        f.write("=" * 60 + "\n")
    print(f"Ish stoliga saqlandi: {desktop_file}")
    sys.stdout.flush()

    # Keep alive and pipe logs
    while True:
        time.sleep(1)
else:
    print("Xatolik: 30 soniya ichida havola olinmadi!")
    sys.exit(1)
