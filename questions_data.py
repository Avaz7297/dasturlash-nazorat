# -*- coding: utf-8 -*-
"""
Python dasturlash fanidan joriy nazorat savollar bazasi.
Jami 100 ta savol 7 ta mavzu bo'yicha:
1. Dasturlash tili va dastur kodini yozish - 15 ta
2. String va sonlar bilan ishlash - 15 ta
3. While sikli - 14 ta
4. Lug'atlar bilan ishlash - 14 ta
5. Klasslar bilan ishlash - 14 ta
6. O'zgaruvchilar va ma'lumot toifalari - 14 ta
7. Shartli ifodalar - 14 ta
"""

QUESTIONS = [
    # =========================================================================
    # 1. PYTHON DASTURLASH TILI VA DASTUR KODINI YOZISH (15 ta)
    # =========================================================================
    {
        "id": 1,
        "topic": "Dasturlash tili va dastur kodini yozish",
        "difficulty": "oson",
        "question": "Python dasturlash tilining yaratuvchisi kim?",
        "code": "",
        "options": ["Gvido van Rossum", "Dennis Ritchie", "Bjarne Stroustrup", "Jeyms Gosling"],
        "correct": 0
    },
    {
        "id": 2,
        "topic": "Dasturlash tili va dastur kodini yozish",
        "difficulty": "oson",
        "question": "Python fayllarining standart kengaytmasi qanday bo'ladi?",
        "code": "",
        "options": [".py", ".python", ".pt", ".pyd"],
        "correct": 0
    },
    {
        "id": 3,
        "topic": "Dasturlash tili va dastur kodini yozish",
        "difficulty": "oson",
        "question": "Python-da bir qatorli izoh (kommentariy) qaysi belgi bilan yoziladi?",
        "code": "",
        "options": ["#", "//", "/*", "--"],
        "correct": 0
    },
    {
        "id": 4,
        "topic": "Dasturlash tili va dastur kodini yozish",
        "difficulty": "oson",
        "question": "Konsolga ma'lumot chiqarish uchun qaysi standart funksiya ishlatiladi?",
        "code": "",
        "options": ["print()", "echo()", "console.log()", "write()"],
        "correct": 0
    },
    {
        "id": 5,
        "topic": "Dasturlash tili va dastur kodini yozish",
        "difficulty": "o'rta",
        "question": "Python dasturlash tilida kod bloklari qanday ajratiladi?",
        "code": "",
        "options": [
            "Bo'shliqlar (indentatsiya/surish) orqali",
            "Faqat jingalak qavslar { } orqali",
            "Faqat begin va end kalit so'zlari orqali",
            "Nuqta-vergul (;) belgisi orqali"
        ],
        "correct": 0
    },
    {
        "id": 6,
        "topic": "Dasturlash tili va dastur kodini yozish",
        "difficulty": "o'rta",
        "question": "PEP 8 uslubiy qo'llanmasiga ko'ra, har bir chekinish (indentation) darajasi nechta bo'shliqdan iborat bo'lishi tavsiya etiladi?",
        "code": "",
        "options": ["4 ta bo'shliq", "2 ta bo'shliq", "8 ta bo'shliq", "1 ta tabulyatsiya belgisi"],
        "correct": 0
    },
    {
        "id": 7,
        "topic": "Dasturlash tili va dastur kodini yozish",
        "difficulty": "o'rta",
        "question": "Quyidagi kod bajarilganda konsolga nima chiqadi?",
        "code": "print('Salom', 'Dunyo', sep='-', end='!')",
        "options": ["Salom-Dunyo!", "Salom Dunyo-!", "Salom-Dunyo\n!", "Salom Dunyo!"],
        "correct": 0
    },
    {
        "id": 8,
        "topic": "Dasturlash tili va dastur kodini yozish",
        "difficulty": "o'rta",
        "question": "Foydalanuvchidan klaviatura orqali ma'lumot kiritish uchun qaysi funksiya qo'llaniladi va u qaysi toifada qaytaradi?",
        "code": "",
        "options": [
            "input(), har doim satr (str) toifasida qaytaradi",
            "input(), faqat son (int) toifasida qaytaradi",
            "scan(), kiritilgan qiymat turiga mos holda qaytaradi",
            "read(), bayt (bytes) toifasida qaytaradi"
        ],
        "correct": 0
    },
    {
        "id": 9,
        "topic": "Dasturlash tili va dastur kodini yozish",
        "difficulty": "o'rta",
        "question": "Python qanday turdagi dasturlash tili hisoblanadi?",
        "code": "",
        "options": [
            "Interpretatsiya qilinadigan, yuqori darajali va dinamik tiplangan",
            "Faqat quyi darajali va statik tiplangan",
            "Faqat mashina kodiga kompilyatsiya qilinuvchi til",
            "Faqat veb brauzerda ishlovchi skript tili"
        ],
        "correct": 0
    },
    {
        "id": 10,
        "topic": "Dasturlash tili va dastur kodini yozish",
        "difficulty": "murakkab",
        "question": "Quyidagi kodda qanday xatolik yuz beradi?",
        "code": "def hisobla():\nprint(\"Natija\")\nhisobla()",
        "options": [
            "IndentationError (chekinish xatoligi)",
            "SyntaxError: invalid function",
            "TypeError: missing argument",
            "NameError: hisobla not defined"
        ],
        "correct": 0
    },
    {
        "id": 11,
        "topic": "Dasturlash tili va dastur kodini yozish",
        "difficulty": "murakkab",
        "question": "Python-da `import math` va `from math import sqrt` yozuvlari orasidagi asosiy farq nima?",
        "code": "",
        "options": [
            "Birinchisida funksiya math.sqrt() deb chaqiriladi, ikkinchisida to'g'ridan-to'g'ri sqrt() deb chaqiriladi",
            "Ikkinchisi math modulidagi barcha funksiyalarni xotiraga to'liq yuklaydi",
            "Birinchisi faqat C tilida yozilgan modullar uchun amal qiladi",
            "Hech qanday farqi yo'q, ikkalasi ham bir xil ishlaydi"
        ],
        "correct": 0
    },
    {
        "id": 12,
        "topic": "Dasturlash tili va dastur kodini yozish",
        "difficulty": "o'rta",
        "question": "Ko'p qatorli satr yoki docstring yaratish uchun qaysi belgilardan foydalaniladi?",
        "code": "",
        "options": [
            "''' yoki \"\"\" (uchta bittalik yoki qo'shtirnoq)",
            "/* va */ belgilari",
            "<!-- va --> belgilari",
            "faqat qavslar ( )"
        ],
        "correct": 0
    },
    {
        "id": 13,
        "topic": "Dasturlash tili va dastur kodini yozish",
        "difficulty": "murakkab",
        "question": "Quyidagi buyruq terminalda nima vazifani bajaradi: `python -m venv myenv`?",
        "code": "",
        "options": [
            "Yangi virtual muhit (virtual environment) yaratadi",
            "Python-ni yangi versiyaga yangilaydi",
            "Barcha o'rnatilgan paketlarni o'chiradi",
            "Python skriptini fon rejimida ishga tushiradi"
        ],
        "correct": 0
    },
    {
        "id": 14,
        "topic": "Dasturlash tili va dastur kodini yozish",
        "difficulty": "murakkab",
        "question": "Quyidagi kod natijasi nima bo'ladi?",
        "code": "a = [1, 2, 3]\nb = a\nb.append(4)\nprint(len(a))",
        "options": ["4", "3", "Error", "None"],
        "correct": 0
    },
    {
        "id": 15,
        "topic": "Dasturlash tili va dastur kodini yozish",
        "difficulty": "oson",
        "question": "Python interaktiv qobig'idan (REPL) chiqish uchun qaysi buyruq qo'llaniladi?",
        "code": "",
        "options": ["exit() yoki quit()", "stop()", "close()", "break"],
        "correct": 0
    },

    # =========================================================================
    # 2. STRING VA SONLAR BILAN ISHLASH (15 ta)
    # =========================================================================
    {
        "id": 16,
        "topic": "String va sonlar bilan ishlash",
        "difficulty": "oson",
        "question": "Quyidagi kod natijasi nima bo'ladi?",
        "code": "s = 'python'\nprint(s[1:4])",
        "options": ["yth", "ytho", "pyt", "th"],
        "correct": 0
    },
    {
        "id": 17,
        "topic": "String va sonlar bilan ishlash",
        "difficulty": "oson",
        "question": "Satrdagi barcha harflarni katta harfga o'tkazish uchun qaysi metod ishlatiladi?",
        "code": "",
        "options": ["upper()", "capitalize()", "title()", "toUpper()"],
        "correct": 0
    },
    {
        "id": 18,
        "topic": "String va sonlar bilan ishlash",
        "difficulty": "oson",
        "question": "Python-da butun sonli bo'lish (qoldiqsiz bo'lish) operatori qaysi?",
        "code": "",
        "options": ["//", "/", "%", "div"],
        "correct": 0
    },
    {
        "id": 19,
        "topic": "String va sonlar bilan ishlash",
        "difficulty": "oson",
        "question": "Python-da darajaga ko'tarish operatori qaysi?",
        "code": "",
        "options": ["**", "^", "pow", "^^"],
        "correct": 0
    },
    {
        "id": 20,
        "topic": "String va sonlar bilan ishlash",
        "difficulty": "o'rta",
        "question": "Quyidagi ifoda natijasi nima bo'ladi?",
        "code": "print(17 % 5 + 2 ** 3)",
        "options": ["10", "11", "9", "8"],
        "correct": 0
    },
    {
        "id": 21,
        "topic": "String va sonlar bilan ishlash",
        "difficulty": "o'rta",
        "question": "Satrning ikki chetidagi bo'shliqlarni olib tashlash uchun qaysi metod ishlatiladi?",
        "code": "",
        "options": ["strip()", "trim()", "clean()", "cut()"],
        "correct": 0
    },
    {
        "id": 22,
        "topic": "String va sonlar bilan ishlash",
        "difficulty": "o'rta",
        "question": "Quyidagi f-string kodining natijasi qanday bo'ladi?",
        "code": "x = 5\ny = 3\nprint(f'{x} * {y} = {x * y}')",
        "options": ["5 * 3 = 15", "x * y = 15", "5 * 3 = {15}", "x * y = {x * y}"],
        "correct": 0
    },
    {
        "id": 23,
        "topic": "String va sonlar bilan ishlash",
        "difficulty": "o'rta",
        "question": "Satrni berilgan belgi bo'yicha bo'lib, ro'yxat (list) ko'rinishida qaytaruvchi metod qaysi?",
        "code": "",
        "options": ["split()", "join()", "slice()", "separate()"],
        "correct": 0
    },
    {
        "id": 24,
        "topic": "String va sonlar bilan ishlash",
        "difficulty": "o'rta",
        "question": "Quyidagi kod natijasi nima bo'ladi?",
        "code": "matn = 'O\'zbekiston'\nprint(matn[-3:])",
        "options": ["ton", "ston", "sto", "on"],
        "correct": 0
    },
    {
        "id": 25,
        "topic": "String va sonlar bilan ishlash",
        "difficulty": "murakkab",
        "question": "Quyidagi kod natijasini aniqlang:",
        "code": "s = 'ab-cd-ef'\nres = '-'.join(s.split('-')[::-1])\nprint(res)",
        "options": ["ef-cd-ab", "fe-dc-ba", "ab-cd-ef", "ef-ab-cd"],
        "correct": 0
    },
    {
        "id": 26,
        "topic": "String va sonlar bilan ishlash",
        "difficulty": "o'rta",
        "question": "Quyidagi kod bajarilganda qanday natija chiqadi?",
        "code": "print(round(3.567, 2))",
        "options": ["3.57", "3.56", "3.6", "4.0"],
        "correct": 0
    },
    {
        "id": 27,
        "topic": "String va sonlar bilan ishlash",
        "difficulty": "murakkab",
        "question": "Quyidagi amallar ketma-ketligi natijasi nima bo'ladi?",
        "code": "s = 'banana'\nprint(s.count('an') + s.find('n'))",
        "options": ["4", "5", "3", "2"],
        "correct": 0
    },
    {
        "id": 28,
        "topic": "String va sonlar bilan ishlash",
        "difficulty": "murakkab",
        "question": "Quyidagi kod qanday xatolik qaytaradi?",
        "code": "soz = 'salom'\nsoz[0] = 'S'",
        "options": [
            "TypeError: 'str' object does not support item assignment",
            "ValueError: string is immutable",
            "IndexError: string index out of range",
            "SyntaxError: invalid assignment"
        ],
        "correct": 0
    },
    {
        "id": 29,
        "topic": "String va sonlar bilan ishlash",
        "difficulty": "o'rta",
        "question": "Quyidagi kod natijasi nima bo'ladi?",
        "code": "a = '5'\nb = 3\nprint(a * b)",
        "options": ["555", "15", "TypeError", "'15'"],
        "correct": 0
    },
    {
        "id": 30,
        "topic": "String va sonlar bilan ishlash",
        "difficulty": "murakkab",
        "question": "Sonning absolyut (modul) qiymatini topish uchun qaysi ichki funksiya ishlatiladi?",
        "code": "",
        "options": ["abs()", "mod()", "math.abs()", "val()"],
        "correct": 0
    },

    # =========================================================================
    # 3. WHILE SIKLI (14 ta)
    # =========================================================================
    {
        "id": 31,
        "topic": "While sikli",
        "difficulty": "oson",
        "question": "While sikli qachongacha davom etadi?",
        "code": "",
        "options": [
            "Berilgan shart rost (True) bo'lib turguniga qadar",
            "Faqat 10 marta aylanadi",
            "Shart yolg'on (False) bo'lguniga qadar har doim to'xtamaydi degani emas",
            "Faqat massiv elementlari tugaguncha"
        ],
        "correct": 0
    },
    {
        "id": 32,
        "topic": "While sikli",
        "difficulty": "oson",
        "question": "Siklni muddatidan oldin butunlay to'xtatish (chiqib ketish) uchun qaysi kalit so'z ishlatiladi?",
        "code": "",
        "options": ["break", "continue", "pass", "exit"],
        "correct": 0
    },
    {
        "id": 33,
        "topic": "While sikli",
        "difficulty": "oson",
        "question": "Siklning joriy iteratsiyasini to'xtatib, darhol keyingi iteratsiyaga o'tish uchun nima ishlatiladi?",
        "code": "",
        "options": ["continue", "break", "pass", "skip"],
        "correct": 0
    },
    {
        "id": 34,
        "topic": "While sikli",
        "difficulty": "o'rta",
        "question": "Quyidagi kod konsolga nima chiqaradi?",
        "code": "i = 1\nwhile i < 4:\n    print(i, end=' ')\n    i += 1",
        "options": ["1 2 3 ", "1 2 3 4 ", "0 1 2 3 ", "2 3 4 "],
        "correct": 0
    },
    {
        "id": 35,
        "topic": "While sikli",
        "difficulty": "o'rta",
        "question": "Quyidagi kod natijasini aniqlang:",
        "code": "x = 10\nwhile x > 5:\n    x -= 2\nprint(x)",
        "options": ["4", "5", "6", "3"],
        "correct": 0
    },
    {
        "id": 36,
        "topic": "While sikli",
        "difficulty": "o'rta",
        "question": "Quyidagi kod necha marta aylanadi (iteratsiya qiladi)?",
        "code": "son = 0\nwhile son < 5:\n    son += 2",
        "options": ["3 marta", "5 marta", "2 marta", "Cheksiz marta"],
        "correct": 0
    },
    {
        "id": 37,
        "topic": "While sikli",
        "difficulty": "murakkab",
        "question": "Quyidagi kod natijasida qanday qiymat chop etiladi?",
        "code": "s = 0\ni = 1\nwhile i <= 5:\n    if i == 3:\n        i += 1\n        continue\n    s += i\n    i += 1\nprint(s)",
        "options": ["12", "15", "10", "13"],
        "correct": 0
    },
    {
        "id": 38,
        "topic": "While sikli",
        "difficulty": "murakkab",
        "question": "Quyidagi kod bajarilganda nima yuz beradi?",
        "code": "x = 1\nwhile x > 0:\n    x += 1",
        "options": [
            "Cheksiz sikl (infinite loop) yuzaga keladi",
            "Dastur xatolik bilan to'xtaydi",
            "x = 100 bo'lganda avtomatik to'xtaydi",
            "Hech narsa bo'lmaydi"
        ],
        "correct": 0
    },
    {
        "id": 39,
        "topic": "While sikli",
        "difficulty": "o'rta",
        "question": "Python-da `while...else` blokidagi `else` qachon ishga tushadi?",
        "code": "",
        "options": [
            "Sikl `break` orqali to'xtatilmasdan, shart False bo'lib tabiiy yakunlanganda",
            "Sikl ichida `break` bajarilganda",
            "Faqat sikl hech qachon ishga tushmagan taqdirdagina",
            "Sikl ichida xatolik yuz berganda"
        ],
        "correct": 0
    },
    {
        "id": 40,
        "topic": "While sikli",
        "difficulty": "murakkab",
        "question": "Quyidagi kod natijasini toping:",
        "code": "n = 5\nwhile n > 0:\n    n -= 1\n    if n == 2:\n        break\nelse:\n    print('Tugadi')\nprint(n)",
        "options": ["2", "Tugadi 2", "Tugadi 0", "0"],
        "correct": 0
    },
    {
        "id": 41,
        "topic": "While sikli",
        "difficulty": "murakkab",
        "question": "Quyidagi kod necha marta 'salom' so'zini ekranga chiqaradi?",
        "code": "a = 8\nwhile a > 1:\n    print('salom')\n    a = a // 2",
        "options": ["3", "4", "2", "8"],
        "correct": 0
    },
    {
        "id": 42,
        "topic": "While sikli",
        "difficulty": "o'rta",
        "question": "Quyidagi sikldagi xatolik nimada?",
        "code": "k = 1\nwhile k <= 5:\n    print(k)",
        "options": [
            "k o'zgaruvchisi qiymati oshirilmagan, natijada cheksiz sikl yuzaga keladi",
            "while sharti xato yozilgan",
            "print funksiyasida sintaksis xato",
            "k tipi mos emas"
        ],
        "correct": 0
    },
    {
        "id": 43,
        "topic": "While sikli",
        "difficulty": "murakkab",
        "question": "Quyidagi kod natijasi nima bo'ladi?",
        "code": "i = 0\ns = 0\nwhile i < 10:\n    i += 1\n    if i % 2 == 0:\n        continue\n    s += i\nprint(s)",
        "options": ["25", "20", "30", "15"],
        "correct": 0
    },
    {
        "id": 44,
        "topic": "While sikli",
        "difficulty": "murakkab",
        "question": "Quyidagi kod natijasi nima bo'ladi?",
        "code": "x = 0\nwhile True:\n    x += 1\n    if x * x >= 20:\n        break\nprint(x)",
        "options": ["5", "4", "6", "20"],
        "correct": 0
    },

    # =========================================================================
    # 4. LUG'ATLAR BILAN ISHLASH (14 ta)
    # =========================================================================
    {
        "id": 45,
        "topic": "Lug‘atlar bilan ishlash",
        "difficulty": "oson",
        "question": "Python-da lug'at (dict) yaratish uchun qaysi qavslardan foydalaniladi?",
        "code": "",
        "options": ["Jingalak qavslar { }", "Kvadrat qavslar [ ]", "Oddiy qavslar ( )", "Burchakli qavslar < >"],
        "correct": 0
    },
    {
        "id": 46,
        "topic": "Lug‘atlar bilan ishlash",
        "difficulty": "oson",
        "question": "Lug'atdagi mavjud kalitning qiymatini olish yoki kalit bo'lmasa xatolik bermasdan standart qiymat qaytarish uchun qaysi metod ishlatiladi?",
        "code": "",
        "options": ["get()", "find()", "search()", "lookup()"],
        "correct": 0
    },
    {
        "id": 47,
        "topic": "Lug‘atlar bilan ishlash",
        "difficulty": "oson",
        "question": "Lug'atdagi barcha kalitlarni olish uchun qaysi metod ishlatiladi?",
        "code": "",
        "options": ["keys()", "all_keys()", "names()", "indices()"],
        "correct": 0
    },
    {
        "id": 48,
        "topic": "Lug‘atlar bilan ishlash",
        "difficulty": "oson",
        "question": "Lug'atdagi barcha qiymatlarni olish uchun qaysi metod ishlatiladi?",
        "code": "",
        "options": ["values()", "items()", "list()", "get_values()"],
        "correct": 0
    },
    {
        "id": 49,
        "topic": "Lug‘atlar bilan ishlash",
        "difficulty": "o'rta",
        "question": "Lug'atdagi (kalit, qiymat) juftliklarini kortej (tuple) ko'rinishida olish uchun qaysi metod ishlatiladi?",
        "code": "",
        "options": ["items()", "pairs()", "elements()", "tuples()"],
        "correct": 0
    },
    {
        "id": 50,
        "topic": "Lug‘atlar bilan ishlash",
        "difficulty": "o'rta",
        "question": "Quyidagi kod natijasi nima bo'ladi?",
        "code": "d = {'a': 1, 'b': 2}\nprint(d.get('c', 100))",
        "options": ["100", "None", "KeyError", "0"],
        "correct": 0
    },
    {
        "id": 51,
        "topic": "Lug‘atlar bilan ishlash",
        "difficulty": "o'rta",
        "question": "Quyidagi toifalardan qaysi biri lug'at kaliti (key) sifatida ISHLATILMAYDI?",
        "code": "",
        "options": ["Ro'yxat (list)", "Satr (str)", "Butun son (int)", "Kortej (tuple)"],
        "correct": 0
    },
    {
        "id": 52,
        "topic": "Lug‘atlar bilan ishlash",
        "difficulty": "o'rta",
        "question": "Quyidagi kod natijasini aniqlang:",
        "code": "talaba = {'ism': 'Ali', 'yosh': 20}\ntalaba['yosh'] = 21\ntalaba['kurs'] = 2\nprint(len(talaba))",
        "options": ["3", "4", "2", "Error"],
        "correct": 0
    },
    {
        "id": 53,
        "topic": "Lug‘atlar bilan ishlash",
        "difficulty": "murakkab",
        "question": "Quyidagi kod bajarilganda nima chop etiladi?",
        "code": "d = {'x': 10, 'y': 20}\nval = d.pop('x')\nprint(val, len(d))",
        "options": ["10 1", "20 1", "10 2", "KeyError"],
        "correct": 0
    },
    {
        "id": 54,
        "topic": "Lug‘atlar bilan ishlash",
        "difficulty": "murakkab",
        "question": "Quyidagi kod natijasi nima bo'ladi?",
        "code": "d1 = {'a': 1, 'b': 2}\nd2 = {'b': 99, 'c': 3}\nd1.update(d2)\nprint(d1['b'])",
        "options": ["99", "2", "101", "Error"],
        "correct": 0
    },
    {
        "id": 55,
        "topic": "Lug‘atlar bilan ishlash",
        "difficulty": "o'rta",
        "question": "Lug'atdan ma'lum bir kalit va uning qiymatini butunlay o'chirish uchun qaysi kalit so'z ishlatiladi?",
        "code": "",
        "options": ["del", "remove", "discard", "erase"],
        "correct": 0
    },
    {
        "id": 56,
        "topic": "Lug‘atlar bilan ishlash",
        "difficulty": "murakkab",
        "question": "Quyidagi dictionary comprehension natijasi nima bo'ladi?",
        "code": "kv = {x: x**2 for x in range(1, 4)}\nprint(kv[3])",
        "options": ["9", "6", "4", "3"],
        "correct": 0
    },
    {
        "id": 57,
        "topic": "Lug‘atlar bilan ishlash",
        "difficulty": "murakkab",
        "question": "Quyidagi kodda nima sodir bo'ladi?",
        "code": "d = {'a': 1}\nprint(d['b'])",
        "options": [
            "KeyError: 'b' xatoligi yuzaga keladi",
            "None qiymati qaytariladi",
            "0 qiymati qaytariladi",
            "IndexError yuzaga keladi"
        ],
        "correct": 0
    },
    {
        "id": 58,
        "topic": "Lug‘atlar bilan ishlash",
        "difficulty": "murakkab",
        "question": "Lug'atdagi barcha elementlarni birato'la tozalash uchun qaysi metod chaqiriladi?",
        "code": "",
        "options": ["clear()", "empty()", "reset()", "clean()"],
        "correct": 0
    },

    # =========================================================================
    # 5. KLASSLAR BILAN ISHLASH (14 ta)
    # =========================================================================
    {
        "id": 59,
        "topic": "Klasslar bilan ishlash",
        "difficulty": "oson",
        "question": "Python-da yangi klass e'lon qilish uchun qaysi kalit so'z ishlatiladi?",
        "code": "",
        "options": ["class", "def", "struct", "object"],
        "correct": 0
    },
    {
        "id": 60,
        "topic": "Klasslar bilan ishlash",
        "difficulty": "oson",
        "question": "Klassdan yangi obyekt olinganda avtomatik chaqiriladigan konstruktor metodi nomi nima?",
        "code": "",
        "options": ["__init__", "__new__", "__construct__", "__start__"],
        "correct": 0
    },
    {
        "id": 61,
        "topic": "Klasslar bilan ishlash",
        "difficulty": "oson",
        "question": "Klass metodlarida obyektning o'ziga havola (reference) beruvchi birinchi parametr qanday nomlanadi?",
        "code": "",
        "options": ["self", "this", "me", "cls"],
        "correct": 0
    },
    {
        "id": 62,
        "topic": "Klasslar bilan ishlash",
        "difficulty": "o'rta",
        "question": "Quyidagi kod natijasi nima bo'ladi?",
        "code": "class Avto:\n    def __init__(self, model):\n        self.model = model\n\na1 = Avto('Nexia')\nprint(a1.model)",
        "options": ["Nexia", "model", "Avto object", "None"],
        "correct": 0
    },
    {
        "id": 63,
        "topic": "Klasslar bilan ishlash",
        "difficulty": "o'rta",
        "question": "Obyektni satr ko'rinishida ifodalash uchun qaysi maxsus (dunder) metod qayta aniqlanadi?",
        "code": "",
        "options": ["__str__", "__print__", "__repr__ faqat konsol uchun", "__show__"],
        "correct": 0
    },
    {
        "id": 64,
        "topic": "Klasslar bilan ishlash",
        "difficulty": "o'rta",
        "question": "Python-da vorislik (inheritance) qanday sintaksis bilan amalga oshiriladi?",
        "code": "",
        "options": [
            "class Bola(Ota):",
            "class Bola extends Ota:",
            "class Bola implements Ota:",
            "class Bola : public Ota:"
        ],
        "correct": 0
    },
    {
        "id": 65,
        "topic": "Klasslar bilan ishlash",
        "difficulty": "murakkab",
        "question": "Voris klassdan ota (baza) klass metodini chaqirish uchun qaysi funksiyadan foydalaniladi?",
        "code": "",
        "options": ["super()", "parent()", "base()", "root()"],
        "correct": 0
    },
    {
        "id": 66,
        "topic": "Klasslar bilan ishlash",
        "difficulty": "murakkab",
        "question": "Quyidagi kod natijasini aniqlang:",
        "code": "class A:\n    x = 10\nobj1 = A()\nobj2 = A()\nobj1.x = 20\nprint(obj2.x)",
        "options": ["10", "20", "0", "AttributeError"],
        "correct": 0
    },
    {
        "id": 67,
        "topic": "Klasslar bilan ishlash",
        "difficulty": "murakkab",
        "question": "Quyidagi kod natijasi nima bo'ladi?",
        "code": "class Hisob:\n    son = 0\n    def __init__(self):\n        Hisob.son += 1\n\nh1 = Hisob()\nh2 = Hisob()\nh3 = Hisob()\nprint(Hisob.son)",
        "options": ["3", "1", "0", "None"],
        "correct": 0
    },
    {
        "id": 68,
        "topic": "Klasslar bilan ishlash",
        "difficulty": "o'rta",
        "question": "Python-da atribut nomining oldiga ikkita pastki chiziq (masalan, `__parol`) qo'yilsa, u nima ma'noni bildiradi?",
        "code": "",
        "options": [
            "Atribut xususiy (private / name mangling qo'llanadi) hisoblanadi",
            "Atribut faqat o'zgarmas (const) bo'ladi",
            "Atribut barcha klasslar uchun global bo'ladi",
            "Atribut dastur o'chguncha xotirada saqlanadi"
        ],
        "correct": 0
    },
    {
        "id": 69,
        "topic": "Klasslar bilan ishlash",
        "difficulty": "murakkab",
        "question": "Quyidagi kod natijasini toping:",
        "code": "class Hayvon:\n    def ovoz(self):\n        return 'Noma\'lum'\n\nclass Kuchuk(Hayvon):\n    def ovoz(self):\n        return 'Vov'\n\nk = Kuchuk()\nprint(k.ovoz())",
        "options": ["Vov", "Noma'lum", "None", "AttributeError"],
        "correct": 0
    },
    {
        "id": 70,
        "topic": "Klasslar bilan ishlash",
        "difficulty": "murakkab",
        "question": "Quyidagi kodda qanday xatolik yuz beradi?",
        "code": "class Talaba:\n    def salom():\n        print('Salom!')\n\nt = Talaba()\nt.salom()",
        "options": [
            "TypeError: salom() takes 0 positional arguments but 1 was given (self yo'qligi sababli)",
            "SyntaxError: self shart emas",
            "NameError: salom aniqlanmagan",
            "Kod xatosiz ishlaydi va 'Salom!' chiqadi"
        ],
        "correct": 0
    },
    {
        "id": 71,
        "topic": "Klasslar bilan ishlash",
        "difficulty": "o'rta",
        "question": "Obyekt ma'lum bir klassning nusxasi (instance) ekanligini tekshirish uchun qaysi funksiya ishlatiladi?",
        "code": "",
        "options": ["isinstance()", "issubclass()", "typecheck()", "hasattr()"],
        "correct": 0
    },
    {
        "id": 72,
        "topic": "Klasslar bilan ishlash",
        "difficulty": "murakkab",
        "question": "Quyidagi kod natijasini aniqlang:",
        "code": "class Baza:\n    def __init__(self):\n        self.a = 5\n\nclass Bola(Baza):\n    def __init__(self):\n        super().__init__()\n        self.a += 10\n\nb = Bola()\nprint(b.a)",
        "options": ["15", "10", "5", "AttributeError"],
        "correct": 0
    },

    # =========================================================================
    # 6. O'ZGARUVCHILAR VA MA'LUMOT TOIFALARI (14 ta)
    # =========================================================================
    {
        "id": 73,
        "topic": "O‘zgaruvchilar va ma’lumot toifalari",
        "difficulty": "oson",
        "question": "O'zgaruvchining ma'lumot toifasini aniqlash uchun qaysi ichki funksiya qo'llaniladi?",
        "code": "",
        "options": ["type()", "typeof()", "datatype()", "check()"],
        "correct": 0
    },
    {
        "id": 74,
        "topic": "O‘zgaruvchilar va ma’lumot toifalari",
        "difficulty": "oson",
        "question": "Quyidagi o'zgaruvchi nomlaridan qaysi biri Python qoidalariga ko'ra TO'G'RI nomlangan?",
        "code": "",
        "options": ["_talaba_yoshi", "2kurs", "talaba-ism", "class"],
        "correct": 0
    },
    {
        "id": 75,
        "topic": "O‘zgaruvchilar va ma’lumot toifalari",
        "difficulty": "oson",
        "question": "Python-da qiymatning yo'qligini (null qiymatni) ifodalovchi maxsus toifa qaysi?",
        "code": "",
        "options": ["None", "null", "nil", "undefined"],
        "correct": 0
    },
    {
        "id": 76,
        "topic": "O‘zgaruvchilar va ma’lumot toifalari",
        "difficulty": "o'rta",
        "question": "Quyidagi toifalardan qaysi biri o'zgarmas (immutable) toifa hisoblanadi?",
        "code": "",
        "options": ["Kortej (tuple)", "Ro'yxat (list)", "Lug'at (dict)", "To'plam (set)"],
        "correct": 0
    },
    {
        "id": 77,
        "topic": "O‘zgaruvchilar va ma’lumot toifalari",
        "difficulty": "o'rta",
        "question": "Quyidagi ifoda qanday toifaga (type) ega?",
        "code": "x = (42,)",
        "options": ["tuple", "int", "list", "set"],
        "correct": 0
    },
    {
        "id": 78,
        "topic": "O‘zgaruvchilar va ma’lumot toifalari",
        "difficulty": "o'rta",
        "question": "Quyidagi kod natijasi nima bo'ladi?",
        "code": "print(bool(0), bool(''), bool([]), bool(None))",
        "options": [
            "False False False False",
            "True False False False",
            "False True False True",
            "True True True True"
        ],
        "correct": 0
    },
    {
        "id": 79,
        "topic": "O‘zgaruvchilar va ma’lumot toifalari",
        "difficulty": "o'rta",
        "question": "Quyidagi kod bajarilganda `c` o'zgaruvchisining qiymati va toifasi nima bo'ladi?",
        "code": "a = 10\nb = 2.5\nc = a / 2",
        "options": ["5.0, float", "5, int", "5.0, int", "Error"],
        "correct": 0
    },
    {
        "id": 80,
        "topic": "O‘zgaruvchilar va ma’lumot toifalari",
        "difficulty": "murakkab",
        "question": "Quyidagi kod natijasi nima bo'ladi?",
        "code": "a = [1, 2]\nb = a.copy()\nprint(a is b, a == b)",
        "options": ["False True", "True True", "False False", "True False"],
        "correct": 0
    },
    {
        "id": 81,
        "topic": "O‘zgaruvchilar va ma’lumot toifalari",
        "difficulty": "murakkab",
        "question": "Quyidagi kod natijasi nima bo'ladi?",
        "code": "x = 10\ndef ozgartir():\n    global x\n    x = 20\nozgartir()\nprint(x)",
        "options": ["20", "10", "UnboundLocalError", "None"],
        "correct": 0
    },
    {
        "id": 82,
        "topic": "O‘zgaruvchilar va ma’lumot toifalari",
        "difficulty": "o'rta",
        "question": "Python-da bir vaqtning o'zida bir nechta o'zgaruvchiga qiymat berish (multiple assignment) to'g'ri ko'rsatilgan qatorni toping:",
        "code": "",
        "options": [
            "x, y, z = 1, 2, 3",
            "x & y & z = 1, 2, 3",
            "x, y, z := 1, 2, 3",
            "var x=1, y=2, z=3"
        ],
        "correct": 0
    },
    {
        "id": 83,
        "topic": "O‘zgaruvchilar va ma’lumot toifalari",
        "difficulty": "murakkab",
        "question": "Quyidagi kodda `type(a)` nima natija qaytaradi?",
        "code": "a = {1, 2, 3, 2, 1}",
        "options": ["<class 'set'>", "<class 'dict'>", "<class 'list'>", "<class 'tuple'>"],
        "correct": 0
    },
    {
        "id": 84,
        "topic": "O‘zgaruvchilar va ma’lumot toifalari",
        "difficulty": "murakkab",
        "question": "Quyidagi toifalardan qaysi biri o'zgaruvchan (mutable) hisoblanadi?",
        "code": "",
        "options": ["Ro'yxat (list)", "Satr (str)", "Butun son (int)", "Kortej (tuple)"],
        "correct": 0
    },
    {
        "id": 85,
        "topic": "O‘zgaruvchilar va ma’lumot toifalari",
        "difficulty": "murakkab",
        "question": "Quyidagi kod natijasini aniqlang:",
        "code": "x = '123'\ny = int(x) + 7\nprint(type(y).__name__, y)",
        "options": ["int 130", "str 1237", "float 130.0", "TypeError"],
        "correct": 0
    },
    {
        "id": 86,
        "topic": "O‘zgaruvchilar va ma’lumot toifalari",
        "difficulty": "oson",
        "question": "Mantiqiy (boolean) toifaning mumkin bo'lgan qiymatlari qaysilar?",
        "code": "",
        "options": ["True va False", "true va false", "1 va 0 faqat", "YES va NO"],
        "correct": 0
    },

    # =========================================================================
    # 7. SHARTLI IFODALAR (14 ta)
    # =========================================================================
    {
        "id": 87,
        "topic": "Shartli ifodalar",
        "difficulty": "oson",
        "question": "Python-da shartli tekshirish uchun qaysi kalit so'z ishlatiladi?",
        "code": "",
        "options": ["if", "when", "check", "condition"],
        "correct": 0
    },
    {
        "id": 88,
        "topic": "Shartli ifodalar",
        "difficulty": "oson",
        "question": "Python-da «aks holda, agar» shartini qo'shish uchun qaysi qisqartma kalit so'z ishlatiladi?",
        "code": "",
        "options": ["elif", "else if", "elsif", "elseif"],
        "correct": 0
    },
    {
        "id": 89,
        "topic": "Shartli ifodalar",
        "difficulty": "oson",
        "question": "Tenglikni tekshirish uchun qaysi operator ishlatiladi?",
        "code": "",
        "options": ["==", "=", "===", "equals"],
        "correct": 0
    },
    {
        "id": 90,
        "topic": "Shartli ifodalar",
        "difficulty": "oson",
        "question": "Teng emaslikni (not equal) ifodalovchi operator qaysi?",
        "code": "",
        "options": ["!=", "<>", "not ==", "!=="],
        "correct": 0
    },
    {
        "id": 91,
        "topic": "Shartli ifodalar",
        "difficulty": "o'rta",
        "question": "Quyidagi mantiqiy ifoda natijasi nima bo'ladi?",
        "code": "x = 10\nprint(x > 5 and x < 8)",
        "options": ["False", "True", "None", "Error"],
        "correct": 0
    },
    {
        "id": 92,
        "topic": "Shartli ifodalar",
        "difficulty": "o'rta",
        "question": "Quyidagi mantiqiy ifoda natijasi nima bo'ladi?",
        "code": "a = True\nb = False\nprint(not b or a and False)",
        "options": ["True", "False", "None", "SyntaxError"],
        "correct": 0
    },
    {
        "id": 93,
        "topic": "Shartli ifodalar",
        "difficulty": "o'rta",
        "question": "Quyidagi ternar ifoda (bir qatorli if-else) natijasi nima bo'ladi?",
        "code": "yosh = 19\nholat = 'Katta' if yosh >= 18 else 'Kichik'\nprint(holat)",
        "options": ["Katta", "Kichik", "True", "SyntaxError"],
        "correct": 0
    },
    {
        "id": 94,
        "topic": "Shartli ifodalar",
        "difficulty": "o'rta",
        "question": "Quyidagi kod natijasini aniqlang:",
        "code": "baho = 75\nif baho >= 86:\n    natija = 'A'\nelif baho >= 71:\n    natija = 'B'\nelif baho >= 56:\n    natija = 'C'\nelse:\n    natija = 'F'\nprint(natija)",
        "options": ["B", "A", "C", "F"],
        "correct": 0
    },
    {
        "id": 95,
        "topic": "Shartli ifodalar",
        "difficulty": "murakkab",
        "question": "Quyidagi kod natijasini toping:",
        "code": "x = [1, 2, 3]\nif 2 in x and 4 not in x:\n    print('Mos')\nelse:\n    print('Mos emas')",
        "options": ["Mos", "Mos emas", "Error", "None"],
        "correct": 0
    },
    {
        "id": 96,
        "topic": "Shartli ifodalar",
        "difficulty": "murakkab",
        "question": "Quyidagi kodda nima chop etiladi?",
        "code": "a = 0\nif a:\n    print('Birinchi')\nelif not a:\n    print('Ikkinchi')\nelse:\n    print('Uchinchi')",
        "options": ["Ikkinchi", "Birinchi", "Uchinchi", "Hech narsa"],
        "correct": 0
    },
    {
        "id": 97,
        "topic": "Shartli ifodalar",
        "difficulty": "murakkab",
        "question": "Python-da zanjirli taqqoslash (chained comparison) natijasi nima bo'ladi?",
        "code": "x = 15\nprint(10 < x < 20)",
        "options": ["True", "False", "SyntaxError", "TypeError"],
        "correct": 0
    },
    {
        "id": 98,
        "topic": "Shartli ifodalar",
        "difficulty": "murakkab",
        "question": "Quyidagi kodda `pass` kalit so'zi qanday vazifani bajaradi?",
        "code": "if x > 10:\n    pass\nelse:\n    print('Kichik')",
        "options": [
            "Bo'sh operator vazifasini bajaradi (hech qanday amal qilmaydi)",
            "Sikldan chiqib ketadi",
            "Dasturni to'xtatadi",
            "Xatolik keltirib chiqaradi"
        ],
        "correct": 0
    },
    {
        "id": 99,
        "topic": "Shartli ifodalar",
        "difficulty": "murakkab",
        "question": "Quyidagi kod natijasini aniqlang:",
        "code": "x = 5\ny = 10\nif x > 0:\n    if y < 10:\n        print('A')\n    else:\n        print('B')\nelse:\n    print('C')",
        "options": ["B", "A", "C", "None"],
        "correct": 0
    },
    {
        "id": 100,
        "topic": "Shartli ifodalar",
        "difficulty": "murakkab",
        "question": "Quyidagi mantiqiy ifoda natijasi nima bo'ladi?",
        "code": "s = ''\nres = s or 'standart'\nprint(res)",
        "options": ["standart", "''", "True", "False"],
        "correct": 0
    }
]

# Mavzular va savollar soni tekshiruvi:
TOPIC_REQUIREMENTS = {
    "Dasturlash tili va dastur kodini yozish": 15,
    "String va sonlar bilan ishlash": 15,
    "While sikli": 14,
    "Lug‘atlar bilan ishlash": 14,
    "Klasslar bilan ishlash": 14,
    "O‘zgaruvchilar va ma’lumot toifalari": 14,
    "Shartli ifodalar": 14
}

# Talaba uchun 30 ta savol tanlash qoidasi:
# 1. Python dasturlash tili: 4 ta
# 2. String va sonlar: 4 ta
# 3. While sikli: 4 ta
# 4. Lug'atlar: 4 ta
# 5. Klasslar: 4 ta
# 6. O'zgaruvchilar va toifalar: 5 ta
# 7. Shartli ifodalar: 5 ta
# Jami: 4 + 4 + 4 + 4 + 4 + 5 + 5 = 30 ta savol
SAMPLE_DISTRIBUTION = {
    "Dasturlash tili va dastur kodini yozish": 4,
    "String va sonlar bilan ishlash": 4,
    "While sikli": 4,
    "Lug‘atlar bilan ishlash": 4,
    "Klasslar bilan ishlash": 4,
    "O‘zgaruvchilar va ma’lumot toifalari": 5,
    "Shartli ifodalar": 5
}
