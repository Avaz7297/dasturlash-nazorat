# Python Dasturlash Fanidan Masofaviy Joriy Nazorat Platformasi

Zamonaviy, mobil qurilmalarga to'liq moslashuvchan (responsive), shaffof va xavfsiz masofaviy test tizimi.

## 📌 Tizimning Asosiy Imkoniyatlari

### 1. Talaba Paneli
- **Avtomatik Fan:** Fan nomi o'zgartirib bo'lmaydigan qilib «Dasturlash» deb belgilangan.
- **Majburiy Maydonlar:** Talaba F.I.Sh., Ta'lim yo'nalishi, Kurs (1–4) va Guruh maydonlarini kiritgandan so'ngгина test boshlanadi.
- **Faqat 1 Marta Topshirish:** Baza darajasida tekshiriladi; bir xil talaba qayta topshira olmaydi.
- **30 ta Tasodifiy Savol:** 100 ta savoldan iborat bazadan 7 ta mavzu bo'yicha mutanosib tanlanadi. Variantlar har bir talaba uchun tasodifiy aralashtiriladi.
- **30 Daqiqa Vaqt Chegarasi:** Jonli teskari sanovchi taymer. Oxirgi 5 daqiqada ogohlantiruvchi qizil rangga o'tadi va vaqt tugaganda avtomatik topshiriladi.
- **Baholash:**
  * Maksimal: 30 ball (har bir to'g'ri javob uchun 1 ball).
  * 18–30 ball: **«Joriy nazoratdan o‘tdi»** (yashil ko'rsatkich).
  * 0–17 ball: **«Joriy nazoratdan o‘tmadi»** (qizil ko'rsatkich).

### 2. Shaffoflik va Xavfsizlik (Anti-Cheat)
- **Nusxalashni cheklash:** Matnni belgilash (`selectstart`), nusxalash (`copy`, `cut`) va sichqonchaning o'ng tugmasi (`contextmenu`) cheklangan.
- **Boshqa sahifaga o'tishni nazorat qilish:** Test vaqtida boshqa tabga yoki ilovaga o'tish (`visibilitychange`, `blur`) aniqlanadi, talabaga qat'iy ogohlantirish beriladi va o'tishlar soni serverdagi audit hisobotiga yoziladi.
- **Server tomonida tekshirish:** To'g'ri javoblar kaliti frontendga umuman berilmaydi; barcha hisob-kitob faqat serverda amalga oshiriladi.
- **Oraliq avtosave:** Har bir belgilangan javob oraliq saqlanib boriladi.

### 3. O'qituvchi Paneli (Himoyalangan Boshqaruv)
- **Xavfsiz Kirish:** Login va parol bilan himoyalangan (`admin` / `admin123`).
- **Natijalar Jadvali:**
  * №, F.I.Sh., Yo‘nalish, Kurs, Guruh, To‘g‘ri, Noto‘g‘ri, To‘plangan ball, Natija, Topshirilgan sana va vaqt.
- **Filtr va Qidiruv:** Talaba F.I.Sh., yo'nalish va akademik guruh bo'yicha tezkor saralash.
- **Batafsil Ko'rish:** Har bir talabaning 30 ta savoli, qaysi javobni tanlagani, qaysi to'g'ri bo'lgani va tab almashtirishlar sonini modal oynada ko'rish.
- **Ballni Tahrirlash & Audit Jurnali:** O'qituvchi ballni o'zgartirsa, eski va yangi ball, sababi, vaqti va o'qituvchi logini audit jurnalida saqlanadi.
- **Eksport:**
  * **Excel (.xlsx)** formatida yuklab olish.
  * **PDF (Vedomost)** formatida yuklab olish.

### 4. 100 ta Savolning 7 ta Mavzu Bo'yicha Taqsimoti:
1. Python dasturlash tili va dastur kodini yozish – 15 ta (har bir talabaga 4 ta)
2. String va sonlar bilan ishlash – 15 ta (har bir talabaga 4 ta)
3. While sikli – 14 ta (har bir talabaga 4 ta)
4. Lug‘atlar bilan ishlash – 14 ta (har bir talabaga 4 ta)
5. Klasslar bilan ishlash – 14 ta (har bir talabaga 4 ta)
6. O‘zgaruvchilar va ma’lumot toifalari – 14 ta (har bir talabaga 5 ta)
7. Shartli ifodalar – 14 ta (har bir talabaga 5 ta)
**Jami: 100 ta savol; Har bir talabaga 30 ta savol.**

---

## 🚀 Ishga Tushirish Yo'riqnomasi

### 1. Bog'liqliklarni o'rnatish
```bash
pip install -r requirements.txt
```

### 2. Tizimni ishga tushirish
```bash
python app.py
```

Brauzerda oching:
- **Talaba paneli (Test topshirish):** [http://localhost:5000](http://localhost:5000)
- **O'qituvchi paneli:** [http://localhost:5000/login](http://localhost:5000/login)
  - **Login:** `admin`
  - **Parol:** `admin123`

### 3. Test sinovini yurgizish
```bash
python test_suite.py
```
