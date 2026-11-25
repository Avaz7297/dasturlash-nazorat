# -*- coding: utf-8 -*-
import os
import json
import students_roster as sr
import questions_data as qd

base_dir = os.path.dirname(os.path.abspath(__file__))

# 1. Roster and questions JSON
students_roster_json = json.dumps(sr.STUDENTS_ROSTER, ensure_ascii=False)
test_student_json = json.dumps(sr.TEST_STUDENT, ensure_ascii=False)
questions_json = json.dumps(qd.QUESTIONS, ensure_ascii=False)

html_content = f"""<!DOCTYPE html>
<html lang="uz">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no, viewport-fit=cover">
    <title>Python Dasturlash | Masofaviy Joriy Nazorat Platformasi</title>
    <!-- Tailwind CSS & FontAwesome CDN -->
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600;700&display=swap" rel="stylesheet">
    
    <style>
        * {{
            -webkit-tap-highlight-color: transparent;
            box-sizing: border-box;
        }}
        .hidden, [hidden] {{
            display: none !important;
        }}
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'SF Pro Text', 'Inter', system-ui, sans-serif;
            background-color: #f8fafc;
            color: #1e293b;
            min-height: 100vh;
            min-height: 100dvh;
            -webkit-touch-callout: none;
        }}
        /* iOS Safari va Android da inputlar to'g'ri ishlashi uchun */
        input, select, textarea, button, label {{
            -webkit-user-select: auto !important;
            user-select: auto !important;
            -webkit-touch-callout: default !important;
        }}
        input, select, textarea {{
            font-size: 16px !important;
            -webkit-appearance: none;
            appearance: none;
        }}
        .mono-font {{
            font-family: 'JetBrains Mono', monospace, Courier, monospace;
        }}
        .option-card:has(input[type="radio"]:checked) {{
            border-color: #2563eb !important;
            background-color: #eff6ff !important;
            box-shadow: 0 4px 6px -1px rgba(37, 99, 235, 0.1), 0 2px 4px -2px rgba(37, 99, 235, 0.1);
        }}
        @media print {{
            .no-print {{ display: none !important; }}
            body {{ background: white !important; }}
        }}
    </style>
</head>
<body class="min-h-screen flex flex-col antialiased">

    <!-- Yuqori Navbar -->
    <header class="bg-white border-b border-slate-200 sticky top-0 z-40 shadow-sm backdrop-blur-md bg-white/95 no-print">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 h-16 flex items-center justify-between">
            <div class="flex items-center space-x-3 cursor-pointer" onclick="navigateHome()">
                <div class="w-10 h-10 rounded-xl bg-gradient-to-tr from-blue-700 via-blue-600 to-indigo-600 flex items-center justify-center text-white shadow-md shadow-blue-500/20">
                    <i class="fa-brands fa-python text-2xl"></i>
                </div>
                <div>
                    <span class="text-base sm:text-lg font-bold text-slate-900 tracking-tight flex items-center gap-1.5">
                        PythonTest <span class="text-[10px] px-2 py-0.5 rounded-full bg-blue-100 text-blue-700 font-bold uppercase tracking-wider">Joriy Nazorat</span>
                    </span>
                    <p class="text-[11px] text-slate-500 hidden sm:block">Masofaviy joriy baholash axborot tizimi</p>
                </div>
            </div>

            <div class="flex items-center space-x-2">
                <button type="button" id="navTeacherBtn" onclick="toggleTeacherSection()"
                    class="inline-flex items-center gap-1.5 px-3 py-1.5 text-xs sm:text-sm font-semibold text-slate-600 bg-slate-100 hover:bg-slate-200 rounded-xl transition-all">
                    <i class="fa-solid fa-lock text-slate-500"></i>
                    <span id="navTeacherText">O'qituvchi Paneli</span>
                </button>
            </div>
        </div>
    </header>

    <!-- Asosiy Konteyner -->
    <main class="flex-1 max-w-7xl w-full mx-auto px-4 sm:px-6 py-6">

        <!-- =================================================================== -->
        <!-- 1-SAHIFA: TALABA KIRISHI VA RO'YXATDAN O'TISH                      -->
        <!-- =================================================================== -->
        <section id="sectionRegister" class="max-w-4xl mx-auto">
            <div class="text-center mb-8">
                <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-blue-50 border border-blue-200 text-blue-700 text-xs font-semibold mb-3">
                    <i class="fa-solid fa-graduation-cap"></i>
                    <span>Masofaviy Joriy Nazorat Platformasi</span>
                </div>
                <h1 class="text-2xl sm:text-4xl font-extrabold text-slate-900 tracking-tight">
                    Python Dasturlash Fanidan Joriy Nazorat
                </h1>
                <p class="mt-2 text-slate-600 max-w-xl mx-auto text-xs sm:text-sm">
                    Rasmiy 12 xonali Talaba ID (HEMIS ID) ni kiriting. Ma'lumotlaringiz ro'yxatdan avtomatik aniqlanadi.
                </p>
            </div>

            <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-start">
                <!-- Qoidalar kartasi (5 ustun) -->
                <div class="lg:col-span-5 space-y-4">
                    <div class="bg-gradient-to-br from-slate-900 via-blue-950 to-slate-900 text-white p-6 rounded-3xl shadow-xl border border-slate-800">
                        <h2 class="text-base font-bold flex items-center gap-2 mb-4 text-blue-300">
                            <i class="fa-solid fa-shield-halved text-blue-400"></i>
                            <span>Test Qoidalari va Nizomi</span>
                        </h2>
                        <ul class="space-y-3.5 text-xs sm:text-sm text-slate-300">
                            <li class="flex items-start gap-2.5">
                                <i class="fa-solid fa-clock text-amber-400 mt-1"></i>
                                <span><strong>Vaqt:</strong> 60 daqiqa (testni boshlaganingizdan so'ng hisoblanadi).</span>
                            </li>
                            <li class="flex items-start gap-2.5">
                                <i class="fa-solid fa-list-check text-emerald-400 mt-1"></i>
                                <span><strong>Savollar:</strong> 30 ta savol (har biri 4 variantli).</span>
                            </li>
                            <li class="flex items-start gap-2.5">
                                <i class="fa-solid fa-award text-indigo-400 mt-1"></i>
                                <span><strong>Baholash:</strong> Maksimal 30 ball (18–30: O'tdi, 0–17: O'tmadi).</span>
                            </li>
                            <li class="flex items-start gap-2.5">
                                <i class="fa-solid fa-fingerprint text-rose-400 mt-1"></i>
                                <span><strong>1 marta topshirish:</strong> Testni yakunlab natija olganingizdan so'ng qayta topshirish qat'iyan taqiqlanadi!</span>
                            </li>
                            <li class="flex items-start gap-2.5">
                                <i class="fa-solid fa-arrow-right-from-bracket text-cyan-400 mt-1"></i>
                                <span><strong>Erkin kirish:</strong> Testni boshlamasdan tizimdan chiqsangiz, keyinroq bemalol qayta kirishingiz mumkin.</span>
                            </li>
                        </ul>
                    </div>

                    <!-- Ro'yxat ma'lumoti -->
                    <div class="bg-white p-4 rounded-2xl border border-slate-200 shadow-sm text-xs text-slate-600">
                        <div class="font-bold text-slate-800 mb-1 flex items-center gap-1.5">
                            <i class="fa-solid fa-users text-blue-600"></i>
                            <span>Qamrab olingan akademik guruhlar:</span>
                        </div>
                        <div class="flex flex-wrap gap-1.5 mt-2">
                            <span class="px-2 py-0.5 rounded bg-blue-50 text-blue-700 font-semibold">9mt-26 ATT</span>
                            <span class="px-2 py-0.5 rounded bg-blue-50 text-blue-700 font-semibold">10mt-26 ATT</span>
                            <span class="px-2 py-0.5 rounded bg-blue-50 text-blue-700 font-semibold">11mt-26 ATT</span>
                            <span class="px-2 py-0.5 rounded bg-blue-50 text-blue-700 font-semibold">12mt-26 ATT</span>
                            <span class="px-2 py-0.5 rounded bg-blue-50 text-blue-700 font-semibold">13mt-26 ATT</span>
                            <span class="px-2 py-0.5 rounded bg-blue-50 text-blue-700 font-semibold">14mt-26 ATT</span>
                        </div>
                    </div>
                </div>

                <!-- Kirish formasi (7 ustun) -->
                <div class="lg:col-span-7 bg-white p-6 sm:p-8 rounded-3xl border border-slate-200 shadow-lg">
                    <div class="border-b border-slate-100 pb-3 mb-5">
                        <h2 class="text-lg sm:text-xl font-bold text-slate-900 flex items-center gap-2">
                            <i class="fa-solid fa-id-card text-blue-600"></i>
                            <span>Talaba Identifikatsiyasi</span>
                        </h2>
                        <p class="text-xs text-slate-500 mt-0.5">HEMIS ID orqali tizimga kiring.</p>
                    </div>

                    <form id="studentRegisterForm" onsubmit="return handleRegisterSubmit(event)" class="space-y-4">
                        <!-- Talaba ID (12 xonali HEMIS ID) -->
                        <div>
                            <div class="flex items-center justify-between mb-1">
                                <label for="regStudentId" class="block text-xs font-bold text-slate-700 uppercase tracking-wider">
                                    Talaba ID (12 xonali HEMIS ID) <span class="text-red-500">*</span>
                                </label>
                                <span id="idLookupStatus" class="text-[11px] font-semibold text-slate-500">12 ta raqam kiriting</span>
                            </div>
                            <div class="relative">
                                <input type="text" id="regStudentId" required inputmode="numeric" maxlength="12"
                                    oninput="handleStudentIdInput(this)"
                                    placeholder="Masalan: 315261102911"
                                    class="w-full px-4 py-2.5 bg-white border border-slate-300 rounded-xl text-slate-900 text-sm font-mono font-bold tracking-wider focus:ring-2 focus:ring-blue-500 outline-none transition-all">
                                <div class="absolute right-3 top-2.5 text-slate-400">
                                    <i class="fa-solid fa-barcode text-lg"></i>
                                </div>
                            </div>
                            <div class="mt-2 flex items-center justify-between">
                                <span class="text-[11px] text-slate-400">ID kiritilganda F.I.Sh. va guruh avtomatik chiqadi</span>
                                <button type="button" onclick="setTeacherDemoMode()"
                                    class="inline-flex items-center gap-1.5 px-2.5 py-1 text-[11px] font-bold text-amber-700 bg-amber-50 hover:bg-amber-100 rounded-lg border border-amber-200 transition-all">
                                    <i class="fa-solid fa-vial"></i>
                                    <span>🧪 O'qituvchi Sinovi (Test)</span>
                                </button>
                            </div>
                        </div>

                        <!-- F.I.Sh. -->
                        <div>
                            <label for="regFullName" class="block text-xs font-bold text-slate-700 uppercase tracking-wider mb-1">
                                Familiya, Ism va Sharifingiz <span class="text-red-500">*</span>
                            </label>
                            <input type="text" id="regFullName" required placeholder="Talaba ID kiritilganda avtomatik to'ldiriladi"
                                class="w-full px-4 py-2.5 bg-white border border-slate-300 rounded-xl text-slate-900 text-sm focus:ring-2 focus:ring-blue-500 outline-none transition-all">
                        </div>

                        <!-- Guruh va Kurs (2 ustun) -->
                        <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
                            <div>
                                <label for="regGroup" class="block text-xs font-bold text-slate-700 uppercase tracking-wider mb-1">
                                    Akademik Guruh <span class="text-red-500">*</span>
                                </label>
                                <select id="regGroup" required class="w-full px-4 py-2.5 bg-white border border-slate-300 rounded-xl text-slate-900 text-sm focus:ring-2 focus:ring-blue-500 outline-none">
                                    <option value="" disabled selected>Guruhni tanlang</option>
                                    <option value="9mt-26 ATT (o'z)">9mt-26 ATT (o'z)</option>
                                    <option value="10mt-26 ATT (o'z)">10mt-26 ATT (o'z)</option>
                                    <option value="11mt-26 ATT (o'z)">11mt-26 ATT (o'z)</option>
                                    <option value="12mt-26 ATT (o'z)">12mt-26 ATT (o'z)</option>
                                    <option value="13mt-26 ATT (o'z)">13mt-26 ATT (o'z)</option>
                                    <option value="14mt-26 ATT (o'z)">14mt-26 ATT (o'z)</option>
                                    <option value="SINOV (TEST)">SINOV (TEST - O'qituvchi)</option>
                                </select>
                            </div>
                            <div>
                                <label for="regCourse" class="block text-xs font-bold text-slate-700 uppercase tracking-wider mb-1">
                                    Kurs <span class="text-red-500">*</span>
                                </label>
                                <select id="regCourse" required class="w-full px-4 py-2.5 bg-white border border-slate-300 rounded-xl text-slate-900 text-sm focus:ring-2 focus:ring-blue-500 outline-none">
                                    <option value="1" selected>1-kurs</option>
                                    <option value="2">2-kurs</option>
                                    <option value="3">3-kurs</option>
                                    <option value="4">4-kurs</option>
                                </select>
                            </div>
                        </div>

                        <!-- Fan va Yo'nalish -->
                        <div>
                            <label for="regDirection" class="block text-xs font-bold text-slate-700 uppercase tracking-wider mb-1">
                                Ta'lim Yo'nalishi <span class="text-red-500">*</span>
                            </label>
                            <input type="text" id="regDirection" required value="Telekommunikatsiya texnologiyalari (ATT)"
                                class="w-full px-4 py-2.5 bg-white border border-slate-300 rounded-xl text-slate-900 text-sm focus:ring-2 focus:ring-blue-500 outline-none transition-all">
                        </div>

                        <!-- Tasdiqlash va Kirish tugmasi -->
                        <div class="pt-3">
                            <button type="submit" id="btnSubmitStart"
                                class="w-full py-3.5 px-6 rounded-xl bg-gradient-to-r from-blue-600 to-indigo-600 hover:from-blue-700 hover:to-indigo-700 text-white font-bold text-sm sm:text-base shadow-lg shadow-blue-500/25 flex items-center justify-center gap-2 transition-all">
                                <span>Tizimga Kirish (Ma'lumotlarni Tasdiqlash)</span>
                                <i class="fa-solid fa-arrow-right"></i>
                            </button>
                        </div>
                    </form>
                </div>
            </div>
        </section>

        <!-- =================================================================== -->
        <!-- 2-SAHIFA: TESTGA TAYYORGARLIK VA YO'RIQNOMA (VAQT HALI KETMAYDI)     -->
        <!-- =================================================================== -->
        <section id="sectionReady" class="max-w-3xl mx-auto hidden" style="display: none;">
            <div class="bg-white border border-slate-200 rounded-3xl p-6 sm:p-10 shadow-xl text-center relative overflow-hidden">
                <div class="w-16 h-16 rounded-2xl bg-blue-100 text-blue-600 flex items-center justify-center mx-auto mb-4 text-3xl shadow-sm">
                    <i class="fa-solid fa-clipboard-question"></i>
                </div>
                
                <h2 class="text-2xl sm:text-3xl font-extrabold text-slate-900 tracking-tight mb-2">
                    Testga Tayyorgarlik
                </h2>
                <p class="text-xs sm:text-sm text-slate-500 mb-6">
                    Ma'lumotlaringizni tasdiqlang. Testni boshlaganingizdan keyingina 60 daqiqalik vaqt orqaga qarab hisoblana boshlaydi.
                </p>

                <!-- Talaba rekvizitlari kartasi -->
                <div class="bg-slate-50 border border-slate-200 rounded-2xl p-5 text-left mb-6 space-y-2.5 text-xs sm:text-sm">
                    <div class="flex items-center justify-between py-1.5 border-b border-slate-200">
                        <span class="text-slate-500 font-medium">Talaba ID (HEMIS):</span>
                        <span class="font-bold font-mono text-slate-900 bg-white px-2.5 py-0.5 rounded border border-slate-300" id="readyStudentId">-</span>
                    </div>
                    <div class="flex items-center justify-between py-1.5 border-b border-slate-200">
                        <span class="text-slate-500 font-medium">Talaba F.I.Sh.:</span>
                        <span class="font-bold text-slate-900" id="readyStudentName">-</span>
                    </div>
                    <div class="flex items-center justify-between py-1.5 border-b border-slate-200">
                        <span class="text-slate-500 font-medium">Akademik Guruh:</span>
                        <span class="font-bold text-blue-700 bg-blue-100 px-2.5 py-0.5 rounded" id="readyStudentGroup">-</span>
                    </div>
                    <div class="flex items-center justify-between py-1.5 border-b border-slate-200">
                        <span class="text-slate-500 font-medium">Fan Nomi:</span>
                        <span class="font-semibold text-slate-800">Dasturlash (Python)</span>
                    </div>
                    <div class="flex items-center justify-between py-1.5 border-b border-slate-200">
                        <span class="text-slate-500 font-medium">Savollar soni:</span>
                        <span class="font-bold text-slate-900">30 ta savol</span>
                    </div>
                    <div class="flex items-center justify-between py-1.5 border-b border-slate-200">
                        <span class="text-slate-500 font-medium">Ajratilgan vaqt:</span>
                        <span class="font-bold text-amber-600">60 daqiqa (1 soat)</span>
                    </div>
                    <div class="flex items-center justify-between py-1.5">
                        <span class="text-slate-500 font-medium">O'tish bali:</span>
                        <span class="font-bold text-emerald-600">18 ball (maksimal 30 ball)</span>
                    </div>
                </div>

                <!-- Muhim eslatma -->
                <div class="p-4 rounded-2xl bg-amber-50 border border-amber-200 text-left mb-6 text-xs text-amber-900 space-y-1.5">
                    <div class="font-bold flex items-center gap-2 text-amber-800">
                        <i class="fa-solid fa-triangle-exclamation"></i>
                        <span>Muhim Eslatma:</span>
                    </div>
                    <p>• <strong>Vaqt hisobi:</strong> Quyidagi "Testni Ishlashni Boshlash" tugmasini bosishingiz bilanoq 60 daqiqalik vaqt ortga sanay boshlaydi.</p>
                    <p>• <strong>Erkin chiqish:</strong> Agar hozir testni boshlamay chiqib ketsangiz, istalgan vaqtda qayta kirishingiz mumkin.</p>
                    <p>• <strong>Natija va bloklash:</strong> Testni ishlab, yakunlab natija olganingizdan keyingina tizimga qayta kirish qat'iyan taqiqlanadi!</p>
                </div>

                <!-- Tugmalar -->
                <div class="flex flex-col sm:flex-row items-center justify-center gap-3">
                    <button type="button" onclick="navigateHome()"
                        class="w-full sm:w-auto px-6 py-3 rounded-xl border border-slate-300 hover:bg-slate-50 text-slate-700 font-semibold text-xs sm:text-sm flex items-center justify-center gap-2">
                        <i class="fa-solid fa-arrow-left"></i>
                        <span>Chiqish / Orqaga</span>
                    </button>
                    <button type="button" onclick="startExamActual()"
                        class="w-full sm:w-auto px-8 py-3.5 rounded-xl bg-gradient-to-r from-emerald-600 to-green-600 hover:from-emerald-700 hover:to-green-700 text-white font-bold text-sm sm:text-base shadow-lg shadow-emerald-500/25 flex items-center justify-center gap-2 transition-all">
                        <i class="fa-solid fa-play"></i>
                        <span>Testni Ishlashni Boshlash (60 daqiqa)</span>
                    </button>
                </div>
            </div>
        </section>

        <!-- =================================================================== -->
        <!-- 3-SAHIFA: TEST TOPSHIRISH OYNASI (FAOL TEST, VAQT KETMOQDA)        -->
        <!-- =================================================================== -->
        <section id="sectionExam" class="max-w-6xl mx-auto hidden" style="display: none;">
            <!-- Yuqori nazorat paneli -->
            <div class="bg-white border border-slate-200 rounded-2xl p-3.5 sm:p-5 shadow-sm mb-4 sm:mb-6 flex flex-col sm:flex-row items-center justify-between gap-3 sm:gap-4 relative">
                <div class="flex items-center gap-3 w-full sm:w-auto">
                    <div class="w-10 h-10 rounded-xl bg-blue-50 text-blue-600 flex items-center justify-center font-bold text-base shrink-0">
                        <i class="fa-solid fa-user-graduate"></i>
                    </div>
                    <div class="overflow-hidden">
                        <div class="flex items-center gap-2">
                            <h3 class="font-bold text-slate-900 text-sm sm:text-base truncate" id="examStudentName">Talaba F.I.Sh.</h3>
                            <span id="examStudentIdBadge" class="text-[11px] font-mono px-2 py-0.5 rounded bg-slate-100 text-slate-700 font-bold">ID</span>
                        </div>
                        <div class="flex items-center gap-2 text-xs text-slate-500">
                            <span id="examStudentGroup" class="font-semibold text-blue-600">Guruh</span>
                            <span>•</span>
                            <span id="examStudentCourse">Kurs</span>
                        </div>
                    </div>
                </div>

                <!-- Taymer: 60:00 (Faqat test boshlangandan keyin orqaga sanaydi) -->
                <div class="flex items-center gap-3 bg-slate-50 px-4 py-2 rounded-xl border border-slate-200">
                    <div class="w-8 h-8 rounded-lg bg-amber-100 text-amber-600 flex items-center justify-center text-sm" id="timerIcon">
                        <i class="fa-solid fa-stopwatch animate-pulse"></i>
                    </div>
                    <div>
                        <div class="text-[10px] font-bold uppercase tracking-wider text-slate-400">Qolgan vaqt</div>
                        <div class="text-xl sm:text-2xl font-mono font-extrabold text-slate-900" id="timerDisplay">60:00</div>
                    </div>
                </div>

                <!-- Yakunlash tugmasi -->
                <button type="button" onclick="confirmFinishModalOpen()"
                    class="px-5 py-2.5 rounded-xl bg-emerald-600 hover:bg-emerald-700 text-white font-semibold text-xs sm:text-sm shadow-md shadow-emerald-600/20 flex items-center gap-2 transition-all">
                    <i class="fa-solid fa-check-double"></i>
                    <span>Testni Yakunlash</span>
                </button>
            </div>

            <!-- Asosiy savol va xarita qismi -->
            <div class="grid grid-cols-1 lg:grid-cols-12 gap-6 items-start">
                <!-- Chap: Savol kartasi (8 ustun) -->
                <div class="lg:col-span-8">
                    <div class="bg-white border border-slate-200 rounded-3xl p-5 sm:p-7 shadow-sm">
                        <!-- Header -->
                        <div class="flex items-center justify-between border-b border-slate-100 pb-3 mb-4">
                            <div class="flex items-center gap-2">
                                <span class="w-8 h-8 rounded-lg bg-blue-600 text-white flex items-center justify-center font-bold text-sm" id="qCurrentNumber">1</span>
                                <span class="text-xs font-semibold px-2.5 py-0.5 rounded-full bg-slate-100 text-slate-700" id="qTopicBadge">Mavzu</span>
                            </div>
                            <span class="text-xs px-2.5 py-0.5 rounded-full font-medium" id="qDifficultyBadge">Daraja</span>
                        </div>

                        <!-- Savol matni -->
                        <div class="text-slate-900 text-base sm:text-lg font-medium leading-relaxed mb-4" id="qQuestionText">
                            Savol yuklanmoqda...
                        </div>

                        <!-- Kod bloki -->
                        <div id="qCodeBlock" class="mb-5 rounded-2xl bg-slate-900 text-slate-100 p-4 font-mono text-xs sm:text-sm overflow-x-auto border border-slate-800 shadow-inner hidden" style="display: none;">
                            <div class="flex items-center justify-between text-[11px] text-slate-400 border-b border-slate-800 pb-2 mb-2 select-none">
                                <span class="flex items-center gap-1.5"><i class="fa-brands fa-python text-amber-400"></i> Python</span>
                                <span>Kod parchasi</span>
                            </div>
                            <pre class="whitespace-pre"><code id="qCodeContent"></code></pre>
                        </div>

                        <!-- 4 ta variant -->
                        <div class="space-y-3" id="qOptionsList">
                            <!-- JS orqali joylanadi -->
                        </div>

                        <!-- Navigatsiya tugmalari -->
                        <div class="flex items-center justify-between pt-6 mt-6 border-t border-slate-100">
                            <button type="button" id="btnPrevQ" onclick="prevQuestion()"
                                class="px-4 py-2 rounded-xl border border-slate-300 text-slate-700 hover:bg-slate-50 font-medium text-xs sm:text-sm flex items-center gap-2 transition-all disabled:opacity-40">
                                <i class="fa-solid fa-arrow-left"></i>
                                <span>Oldingi</span>
                            </button>

                            <div class="text-xs text-slate-500 font-medium">
                                Savol: <strong class="text-slate-800" id="qProgressText">1</strong> / 30
                            </div>

                            <button type="button" id="btnNextQ" onclick="nextQuestion()"
                                class="px-4 py-2 rounded-xl bg-blue-600 hover:bg-blue-700 text-white font-medium text-xs sm:text-sm flex items-center gap-2 transition-all">
                                <span>Keyingi</span>
                                <i class="fa-solid fa-arrow-right"></i>
                            </button>
                        </div>
                    </div>
                </div>

                <!-- O'ng: Savollar xaritasi (4 ustun) -->
                <div class="lg:col-span-4 space-y-4">
                    <div class="bg-white border border-slate-200 rounded-3xl p-5 shadow-sm sticky top-44">
                        <div class="flex items-center justify-between mb-3 border-b border-slate-100 pb-2">
                            <h3 class="font-bold text-slate-800 text-sm flex items-center gap-2">
                                <i class="fa-solid fa-grip text-blue-600"></i>
                                <span>Savollar Xaritasi</span>
                            </h3>
                            <span class="text-xs font-semibold text-slate-500">
                                <span id="mapAnsweredCount">0</span> / 30 belgilandi
                            </span>
                        </div>

                        <!-- 30 ta savol tugmasi paneli -->
                        <div class="grid grid-cols-5 sm:grid-cols-6 gap-2 mb-4" id="questionsMapGrid">
                            <!-- JS orqali yaratiladi -->
                        </div>

                        <!-- Belgilar tavsifi -->
                        <div class="flex items-center justify-between text-[11px] text-slate-500 border-t border-slate-100 pt-3">
                            <div class="flex items-center gap-1.5">
                                <span class="w-3 h-3 rounded bg-blue-600 inline-block"></span>
                                <span>Javob berilgan</span>
                            </div>
                            <div class="flex items-center gap-1.5">
                                <span class="w-3 h-3 rounded bg-slate-100 border border-slate-300 inline-block"></span>
                                <span>Kutilmoqda</span>
                            </div>
                            <div class="flex items-center gap-1.5">
                                <span class="w-3 h-3 rounded border-2 border-blue-500 bg-blue-50 inline-block"></span>
                                <span>Joriy</span>
                            </div>
                        </div>

                        <!-- Xavfsizlik ko'rsatkichi -->
                        <div class="mt-4 pt-3 border-t border-slate-100 flex items-center justify-between text-xs text-slate-500">
                            <span class="flex items-center gap-1.5"><i class="fa-solid fa-shield-halved text-emerald-500"></i> Anti-cheat faol</span>
                            <span id="badgeTabSwitches" class="text-rose-600 font-semibold hidden" style="display: none;">
                                <i class="fa-solid fa-triangle-exclamation"></i>
                                <span id="textTabSwitches">0</span> ta chiqish
                            </span>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- =================================================================== -->
        <!-- 4-SAHIFA: NATIJA SAHIFASI (NATIJA CHIQQANDAN SO'NG QAYTA KIROLMAYDI)-->
        <!-- =================================================================== -->
        <section id="sectionResult" class="max-w-2xl mx-auto py-4 hidden" style="display: none;">
            <div class="bg-white border border-slate-200 rounded-3xl p-6 sm:p-10 shadow-xl text-center relative overflow-hidden">
                <div id="resultColorBar" class="absolute top-0 left-0 right-0 h-3 bg-emerald-500"></div>

                <!-- Status icon -->
                <div class="mb-5 inline-flex items-center justify-center">
                    <div id="resultIconBox" class="w-20 h-20 rounded-full flex items-center justify-center text-4xl shadow-lg ring-8">
                        <i id="resultIcon" class="fa-solid fa-circle-check"></i>
                    </div>
                </div>

                <h1 class="text-2xl sm:text-3xl font-extrabold text-slate-900 tracking-tight mb-2" id="resultStatusText">
                    Joriy nazoratdan o‘tdi
                </h1>
                <p class="text-xs sm:text-sm text-slate-500 mb-6">
                    Python dasturlash fanidan masofaviy joriy nazorat sinovi yakunlandi.
                </p>

                <!-- Ball qutisi -->
                <div class="bg-slate-50 border border-slate-200 rounded-2xl p-6 mb-6">
                    <div class="text-xs font-bold uppercase tracking-wider text-slate-400 mb-1">To'plangan Ball</div>
                    <div class="flex items-baseline justify-center gap-2 font-mono">
                        <span class="text-5xl font-extrabold" id="resultScore">25</span>
                        <span class="text-2xl text-slate-400 font-semibold">/ 30</span>
                    </div>
                    <div class="mt-4 flex items-center justify-center gap-6 text-xs sm:text-sm font-semibold">
                        <div class="flex items-center gap-2 text-emerald-600">
                            <i class="fa-solid fa-circle-check"></i>
                            <span id="resultCorrectCount">25 ta to'g'ri</span>
                        </div>
                        <div class="w-px h-4 bg-slate-300"></div>
                        <div class="flex items-center gap-2 text-rose-600">
                            <i class="fa-solid fa-circle-xmark"></i>
                            <span id="resultIncorrectCount">5 ta noto'g'ri</span>
                        </div>
                    </div>
                </div>

                <!-- Talaba rekvizitlari -->
                <div class="bg-white border border-slate-100 rounded-2xl p-5 shadow-sm text-left mb-6 space-y-2 text-xs sm:text-sm">
                    <div class="flex items-center justify-between py-1.5 border-b border-slate-100">
                        <span class="text-slate-500">Talaba ID (HEMIS):</span>
                        <span class="font-bold font-mono text-slate-900 bg-slate-100 px-2.5 py-0.5 rounded border border-slate-200" id="resStudentId">-</span>
                    </div>
                    <div class="flex items-center justify-between py-1.5 border-b border-slate-100">
                        <span class="text-slate-500">Talaba F.I.Sh.:</span>
                        <span class="font-bold text-slate-900" id="resStudentName">-</span>
                    </div>
                    <div class="flex items-center justify-between py-1.5 border-b border-slate-100">
                        <span class="text-slate-500">Akademik Guruh:</span>
                        <span class="font-bold text-blue-700 bg-blue-50 px-2.5 py-0.5 rounded" id="resStudentGroup">-</span>
                    </div>
                    <div class="flex items-center justify-between py-1.5 border-b border-slate-100">
                        <span class="text-slate-500">Yo'nalish va Kurs:</span>
                        <span class="font-semibold text-slate-800" id="resStudentDirection">-</span>
                    </div>
                    <div class="flex items-center justify-between py-1.5 border-b border-slate-100">
                        <span class="text-slate-500">Fan:</span>
                        <span class="font-semibold text-slate-800">Dasturlash (Python)</span>
                    </div>
                    <div class="flex items-center justify-between py-1.5 border-b border-slate-100">
                        <span class="text-slate-500">Topshirilgan vaqt:</span>
                        <span class="font-mono text-slate-700" id="resDate">-</span>
                    </div>
                    <div class="flex items-center justify-between py-1.5">
                        <span class="text-slate-500">Sahifadan chiqishlar soni:</span>
                        <span class="font-bold" id="resSwitches">0 marta</span>
                    </div>
                </div>

                <!-- Natija muvaffaqiyatli saqlanganligi haqida xabarnoma -->
                <div class="p-5 rounded-2xl bg-emerald-50 border border-emerald-200 text-left space-y-2 mb-6 no-print">
                    <div class="flex items-center gap-3">
                        <div class="w-10 h-10 rounded-xl bg-emerald-600 text-white flex items-center justify-center text-base shadow-sm shrink-0">
                            <i class="fa-solid fa-check-double"></i>
                        </div>
                        <div>
                            <h3 class="font-bold text-sm text-emerald-950">Natijangiz O'qituvchiga Avtomatik Saqlandi!</h3>
                            <p class="text-xs text-emerald-700 mt-0.5">Sizning natijangiz o'qituvchi boshqaruv paneliga avtomatik yozildi. Sinov yakunlandi va tizim qayta topshirish uchun qulflanadi.</p>
                        </div>
                    </div>
                </div>

                <!-- Tugmalar -->
                <div class="flex flex-col sm:flex-row items-center justify-center gap-3 no-print">
                    <button onclick="window.print()" class="w-full sm:w-auto px-5 py-2.5 rounded-xl border border-slate-300 hover:bg-slate-50 text-slate-700 font-semibold text-xs sm:text-sm flex items-center justify-center gap-2">
                        <i class="fa-solid fa-print"></i>
                        <span>Natijani Chop Etish / PDF</span>
                    </button>
                    <button onclick="navigateHome()" class="w-full sm:w-auto px-5 py-2.5 rounded-xl bg-slate-900 hover:bg-slate-800 text-white font-semibold text-xs sm:text-sm flex items-center justify-center gap-2">
                        <i class="fa-solid fa-house"></i>
                        <span>Bosh Sahifaga Qaytish</span>
                    </button>
                </div>
            </div>
        </section>

        <!-- =================================================================== -->
        <!-- 5-SAHIFA: O'QITUVCHI BOSHQARUV PANELI                              -->
        <!-- =================================================================== -->
        <section id="sectionTeacher" class="space-y-6 hidden" style="display: none;">
            <!-- Login qutisi -->
            <div id="teacherLoginForm" class="max-w-md mx-auto bg-white p-8 rounded-3xl border border-slate-200 shadow-xl">
                <div class="text-center mb-6">
                    <div class="w-14 h-14 rounded-2xl bg-slate-900 text-white flex items-center justify-center mx-auto mb-3 text-2xl shadow-md">
                        <i class="fa-solid fa-lock"></i>
                    </div>
                    <h2 class="text-xl font-bold text-slate-900">Mas'ul O'qituvchi Kirishi</h2>
                    <p class="text-xs text-slate-500 mt-1">Ushbu bo'lim faqat fan o'qituvchisi uchun mo'ljallangan.</p>
                </div>

                <form onsubmit="return handleTeacherLogin(event)" class="space-y-4">
                    <div>
                        <label class="block text-xs font-bold text-slate-700 uppercase tracking-wider mb-1">Login</label>
                        <input type="text" id="teachLoginInput" required autocomplete="off"
                            class="w-full px-4 py-2.5 bg-white border border-slate-300 rounded-xl text-slate-900 text-sm focus:ring-2 focus:ring-blue-500 outline-none">
                    </div>
                    <div>
                        <label class="block text-xs font-bold text-slate-700 uppercase tracking-wider mb-1">Maxfiy Parol</label>
                        <input type="password" id="teachPassInput" required autocomplete="off"
                            class="w-full px-4 py-2.5 bg-white border border-slate-300 rounded-xl text-slate-900 text-sm focus:ring-2 focus:ring-blue-500 outline-none">
                    </div>
                    <div class="pt-2">
                        <button type="submit" class="w-full py-3 px-4 rounded-xl bg-slate-900 hover:bg-slate-800 text-white font-bold text-sm shadow-md transition-all flex items-center justify-center gap-2">
                            <i class="fa-solid fa-shield-halved"></i>
                            <span>Tizimga Kirish</span>
                        </button>
                    </div>
                </form>
            </div>

            <!-- Dashboard (Login muvaffaqiyatli bo'lsa) -->
            <div id="teacherDashboard" class="space-y-6 hidden" style="display: none;">
                <!-- Yuqori qator: Export va Amallar -->
                <div class="flex flex-col md:flex-row md:items-center justify-between gap-4 bg-white p-6 rounded-3xl border border-slate-200 shadow-sm">
                    <div>
                        <div class="flex items-center gap-2">
                            <span class="px-2.5 py-0.5 rounded-full bg-blue-100 text-blue-700 font-bold text-xs">O'qituvchi Boshqaruvi</span>
                            <span class="text-xs text-slate-400">•</span>
                            <span class="text-xs font-medium text-slate-600">Fan: <strong>Dasturlash (Python)</strong></span>
                        </div>
                        <h2 class="text-2xl font-extrabold text-slate-900 tracking-tight mt-1">
                            Joriy Nazorat Vedomosti & Natijalar
                        </h2>
                    </div>

                    <div class="flex flex-wrap items-center gap-2.5">
                        <button onclick="setTeacherDemoMode(); navigateHome();" class="px-3.5 py-2 rounded-xl bg-amber-500 hover:bg-amber-600 text-white font-semibold text-xs flex items-center gap-2 shadow-sm" title="O'qituvchi sifatida tizimni sinab ko'rish">
                            <i class="fa-solid fa-vial"></i>
                            <span>🧪 Sinov Rejimini Ochish</span>
                        </button>
                        <button onclick="changeTeacherPassword()" class="px-3.5 py-2 rounded-xl border border-slate-300 hover:bg-slate-50 text-slate-700 font-semibold text-xs flex items-center gap-2 shadow-sm" title="O'qituvchi parolini o'zgartirish">
                            <i class="fa-solid fa-key text-blue-600"></i>
                            <span>Parolni O'zgartirish</span>
                        </button>
                        <button onclick="toggleAuditModal()" class="px-3.5 py-2 rounded-xl border border-slate-300 hover:bg-slate-50 text-slate-700 font-semibold text-xs flex items-center gap-2 shadow-sm">
                            <i class="fa-solid fa-clock-rotate-left text-amber-500"></i>
                            <span>Audit Jurnali</span>
                        </button>
                        <button onclick="exportToExcel()" class="px-3.5 py-2 rounded-xl bg-emerald-600 hover:bg-emerald-700 text-white font-semibold text-xs flex items-center gap-2 shadow-sm">
                            <i class="fa-solid fa-file-excel"></i>
                            <span>Excel (.xlsx / CSV) Yuklab Olish</span>
                        </button>
                        <button onclick="window.print()" class="px-3.5 py-2 rounded-xl bg-rose-600 hover:bg-rose-700 text-white font-semibold text-xs flex items-center gap-2 shadow-sm">
                            <i class="fa-solid fa-print"></i>
                            <span>Vedomostni Chop Etish</span>
                        </button>
                        <button onclick="clearAllResults()" class="px-3.5 py-2 rounded-xl bg-slate-100 hover:bg-rose-100 text-rose-700 font-semibold text-xs flex items-center gap-1.5 shadow-sm" title="Barcha natijalarni tozalash">
                            <i class="fa-solid fa-trash"></i>
                            <span>Tozalash</span>
                        </button>
                        <button onclick="teacherLogout()" class="px-3 py-2 rounded-xl bg-slate-100 hover:bg-red-50 text-red-600 font-semibold text-xs transition-colors" title="Chiqish">
                            <i class="fa-solid fa-right-from-bracket"></i>
                        </button>
                    </div>
                </div>

                <!-- Statistika widgetlari -->
                <div class="grid grid-cols-2 lg:grid-cols-4 gap-4">
                    <div class="bg-white p-5 rounded-2xl border border-slate-200 shadow-sm flex items-center gap-4">
                        <div class="w-12 h-12 rounded-xl bg-blue-50 text-blue-600 flex items-center justify-center text-xl shrink-0">
                            <i class="fa-solid fa-users"></i>
                        </div>
                        <div>
                            <div class="text-xs font-semibold text-slate-500 uppercase">Topshirgan Talabalar</div>
                            <div class="text-2xl font-extrabold text-slate-900 font-mono" id="statTotalStudents">0 / 130 (0%)</div>
                        </div>
                    </div>

                    <div class="bg-white p-5 rounded-2xl border border-slate-200 shadow-sm flex items-center gap-4">
                        <div class="w-12 h-12 rounded-xl bg-emerald-50 text-emerald-600 flex items-center justify-center text-xl shrink-0">
                            <i class="fa-solid fa-circle-check"></i>
                        </div>
                        <div>
                            <div class="text-xs font-semibold text-slate-500 uppercase">O'tganlar (18–30)</div>
                            <div class="text-2xl font-extrabold text-emerald-600 font-mono" id="statPassed">0</div>
                        </div>
                    </div>

                    <div class="bg-white p-5 rounded-2xl border border-slate-200 shadow-sm flex items-center gap-4">
                        <div class="w-12 h-12 rounded-xl bg-rose-50 text-rose-600 flex items-center justify-center text-xl shrink-0">
                            <i class="fa-solid fa-circle-xmark"></i>
                        </div>
                        <div>
                            <div class="text-xs font-semibold text-slate-500 uppercase">O'tmaganlar (0–17)</div>
                            <div class="text-2xl font-extrabold text-rose-600 font-mono" id="statFailed">0</div>
                        </div>
                    </div>

                    <div class="bg-white p-5 rounded-2xl border border-slate-200 shadow-sm flex items-center gap-4">
                        <div class="w-12 h-12 rounded-xl bg-amber-50 text-amber-600 flex items-center justify-center text-xl shrink-0">
                            <i class="fa-solid fa-chart-line"></i>
                        </div>
                        <div>
                            <div class="text-xs font-semibold text-slate-500 uppercase">O'rtacha Ball</div>
                            <div class="text-2xl font-extrabold text-slate-900 font-mono" id="statAvgScore">0</div>
                        </div>
                    </div>
                </div>

                <!-- Filtrlar -->
                <div class="bg-white p-4 rounded-2xl border border-slate-200 shadow-sm flex flex-col sm:flex-row items-center gap-3">
                    <div class="relative flex-1 w-full">
                        <input type="text" id="teachSearchInput" oninput="renderTeacherTable()"
                            placeholder="Talaba ID, F.I.Sh. yoki guruh bo'yicha qidirish..."
                            class="w-full pl-4 pr-4 py-2 bg-slate-50 border border-slate-300 rounded-xl text-xs sm:text-sm focus:ring-2 focus:ring-blue-500 outline-none">
                    </div>
                    <div class="w-full sm:w-64">
                        <select id="teachGroupFilter" onchange="renderTeacherTable()"
                            class="w-full px-3 py-2 bg-slate-50 border border-slate-300 rounded-xl text-xs sm:text-sm focus:ring-2 focus:ring-blue-500 outline-none">
                            <option value="">Barcha guruhlar</option>
                            <option value="9mt-26 ATT (o'z)">9mt-26 ATT (o'z)</option>
                            <option value="10mt-26 ATT (o'z)">10mt-26 ATT (o'z)</option>
                            <option value="11mt-26 ATT (o'z)">11mt-26 ATT (o'z)</option>
                            <option value="12mt-26 ATT (o'z)">12mt-26 ATT (o'z)</option>
                            <option value="13mt-26 ATT (o'z)">13mt-26 ATT (o'z)</option>
                            <option value="14mt-26 ATT (o'z)">14mt-26 ATT (o'z)</option>
                            <option value="SINOV (TEST)">SINOV (TEST)</option>
                        </select>
                    </div>
                </div>

                <!-- Natijalar Jadvali -->
                <div class="bg-white border border-slate-200 rounded-2xl shadow-sm overflow-hidden">
                    <div class="overflow-x-auto">
                        <table class="w-full text-left border-collapse text-xs sm:text-sm">
                            <thead>
                                <tr class="bg-slate-50 border-b border-slate-200 text-slate-500 uppercase tracking-wider text-[11px] font-bold">
                                    <th class="py-3 px-3 text-center">№</th>
                                    <th class="py-3 px-3 text-center">Talaba ID</th>
                                    <th class="py-3 px-3">F.I.Sh.</th>
                                    <th class="py-3 px-3 text-center">Guruh</th>
                                    <th class="py-3 px-3 text-center">To‘g‘ri</th>
                                    <th class="py-3 px-3 text-center">Noto‘g‘ri</th>
                                    <th class="py-3 px-3 text-center">To‘plangan ball</th>
                                    <th class="py-3 px-3 text-center">Natija</th>
                                    <th class="py-3 px-3 text-center">Test sanasi va vaqti</th>
                                    <th class="py-3 px-3 text-center no-print">Amallar (Ko'rish / Tahrirlash / O'chirish)</th>
                                </tr>
                            </thead>
                            <tbody id="teacherTableBody" class="divide-y divide-slate-100">
                                <!-- JS orqali to'ldiriladi -->
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
        </section>

    </main>

    <!-- =================================================================== -->
    <!-- MODALLAR                                                            -->
    <!-- =================================================================== -->

    <!-- Modal: Boshqa oynaga o'tish ogohlantirishi -->
    <div id="modalViolation" class="fixed inset-0 z-50 flex items-center justify-center bg-slate-900/60 backdrop-blur-sm hidden p-4" style="display: none;">
        <div class="bg-white rounded-3xl max-w-md w-full p-6 shadow-2xl border border-red-200 text-center animate-bounce-short">
            <div class="w-14 h-14 rounded-full bg-red-100 text-red-600 flex items-center justify-center mx-auto mb-4 text-2xl">
                <i class="fa-solid fa-triangle-exclamation"></i>
            </div>
            <h3 class="text-lg font-bold text-slate-900 mb-2">Qat'iy Ogohlantirish!</h3>
            <p class="text-xs sm:text-sm text-slate-600 mb-4">
                Siz test oynasidan boshqa sahifa yoki ilovaga o'tdingiz. Bu holat <strong class="text-red-600">qoidabuzarlik</strong> sifatida qayd etildi va o'qituvchining audit hisobotida ko'rsatiladi!
            </p>
            <div class="bg-red-50 p-3 rounded-xl border border-red-200 text-xs text-red-700 font-medium mb-4">
                Boshqa sahifaga o'tishlar soni: <span id="violationCountBadge" class="font-bold text-sm">1</span> marta
            </div>
            <button type="button" onclick="closeViolationModal()"
                class="w-full py-2.5 px-4 rounded-xl bg-red-600 hover:bg-red-700 text-white font-semibold text-xs sm:text-sm shadow transition-all">
                Tushundim, testni davom ettirish
            </button>
        </div>
    </div>

    <!-- Modal: Testni yakunlashni tasdiqlash -->
    <div id="modalFinishConfirm" class="fixed inset-0 z-50 flex items-center justify-center bg-slate-900/60 backdrop-blur-sm hidden p-4" style="display: none;">
        <div class="bg-white rounded-3xl max-w-md w-full p-6 shadow-2xl border border-slate-200 text-center">
            <div class="w-14 h-14 rounded-full bg-emerald-100 text-emerald-600 flex items-center justify-center mx-auto mb-4 text-2xl">
                <i class="fa-solid fa-clipboard-check"></i>
            </div>
            <h3 class="text-lg font-bold text-slate-900 mb-2">Testni Yakunlaysizmi?</h3>
            <p class="text-xs sm:text-sm text-slate-600 mb-4">
                Siz <strong id="modalAnsweredCount">0</strong> / 30 ta savolga javob berdingiz. Testni yakunlagandan so'ng uni qayta topshirish imkoniyati bo'lmaydi.
            </p>
            <div class="flex items-center gap-3">
                <button type="button" onclick="closeFinishModal()"
                    class="flex-1 py-2.5 px-4 rounded-xl border border-slate-300 hover:bg-slate-50 text-slate-700 font-semibold text-xs sm:text-sm">
                    Orqaga
                </button>
                <button type="button" onclick="submitExamNow()"
                    class="flex-1 py-2.5 px-4 rounded-xl bg-emerald-600 hover:bg-emerald-700 text-white font-semibold text-xs sm:text-sm shadow-md">
                    Yakunlash
                </button>
            </div>
        </div>
    </div>

    <!-- Modal 1: Batafsil Natijalar (KO'RISH) -->
    <div id="modalDetail" class="fixed inset-0 z-50 flex items-center justify-center bg-slate-900/60 backdrop-blur-sm hidden p-4" style="display: none;">
        <div class="bg-white rounded-3xl max-w-3xl w-full max-h-[90vh] flex flex-col shadow-2xl border border-slate-200">
            <div class="p-5 border-b border-slate-100 flex items-center justify-between">
                <div>
                    <h3 class="text-base sm:text-lg font-bold text-slate-900" id="detailModalName">Talaba Natijasi</h3>
                    <p class="text-xs text-slate-500" id="detailModalMeta">Guruh va Natijalar</p>
                </div>
                <button onclick="closeDetailModal()" class="w-8 h-8 rounded-lg bg-slate-100 hover:bg-slate-200 text-slate-500 flex items-center justify-center">
                    <i class="fa-solid fa-xmark"></i>
                </button>
            </div>
            <div class="p-6 overflow-y-auto space-y-4 flex-1 text-xs sm:text-sm" id="detailModalQuestionsList">
                <!-- JS orqali to'ldiriladi -->
            </div>
            <div class="p-4 border-t border-slate-100 flex justify-end">
                <button onclick="closeDetailModal()" class="px-5 py-2 rounded-xl bg-slate-100 hover:bg-slate-200 text-slate-700 font-semibold text-xs">
                    Yopish
                </button>
            </div>
        </div>
    </div>

    <!-- Modal 2: Talaba ma'lumotlari va ballini tahrirlash (O'ZGARTIRISH) -->
    <div id="modalEditScore" class="fixed inset-0 z-50 flex items-center justify-center bg-slate-900/60 backdrop-blur-sm hidden p-4" style="display: none;">
        <div class="bg-white rounded-3xl max-w-md w-full p-6 shadow-2xl border border-slate-200">
            <div class="flex items-center justify-between border-b border-slate-100 pb-3 mb-4">
                <h3 class="text-base font-bold text-slate-900 flex items-center gap-2">
                    <i class="fa-solid fa-pen-to-square text-amber-500"></i>
                    <span>Talaba Natijasini Tahrirlash (Audit)</span>
                </h3>
                <button onclick="closeEditScoreModal()" class="text-slate-400 hover:text-slate-600">
                    <i class="fa-solid fa-xmark"></i>
                </button>
            </div>

            <form onsubmit="return saveScoreEdit(event)" class="space-y-4">
                <input type="hidden" id="editStudentIndex">
                <div>
                    <label class="block text-xs font-semibold text-slate-700 mb-1">Talaba ID</label>
                    <input type="text" id="editStudentIdVal" readonly
                        class="w-full px-3.5 py-2 border border-slate-300 rounded-xl text-slate-700 bg-slate-100 text-sm font-mono font-bold outline-none cursor-not-allowed">
                </div>
                <div>
                    <label class="block text-xs font-semibold text-slate-700 mb-1">Talaba F.I.Sh. *</label>
                    <input type="text" id="editStudentFullNameVal" required
                        class="w-full px-3.5 py-2 border border-slate-300 rounded-xl text-slate-900 text-sm font-semibold focus:ring-2 focus:ring-blue-500 outline-none">
                </div>
                <div>
                    <label class="block text-xs font-semibold text-slate-700 mb-1">Guruh *</label>
                    <input type="text" id="editStudentGroupVal" required
                        class="w-full px-3.5 py-2 border border-slate-300 rounded-xl text-slate-900 text-sm font-semibold focus:ring-2 focus:ring-blue-500 outline-none">
                </div>
                <div>
                    <label class="block text-xs font-semibold text-slate-700 mb-1">To'plangan Ball (0 dan 30 gacha) *</label>
                    <input type="number" id="editNewScoreVal" min="0" max="30" required
                        class="w-full px-3.5 py-2 border border-slate-300 rounded-xl text-slate-900 text-sm font-bold font-mono focus:ring-2 focus:ring-blue-500 outline-none">
                    <span class="text-[11px] text-slate-400 mt-1 block">18–30: O'tdi, 0–17: O'tmadi</span>
                </div>
                <div>
                    <label class="block text-xs font-semibold text-slate-700 mb-1">O'zgartirish Sababi (Audit jurnali uchun majburiy) *</label>
                    <textarea id="editReasonVal" rows="3" required placeholder="Masalan: Apellyatsiya natijasiga ko'ra qo'shimcha ball berildi..."
                        class="w-full px-3.5 py-2 border border-slate-300 rounded-xl text-slate-900 text-xs sm:text-sm focus:ring-2 focus:ring-blue-500 outline-none"></textarea>
                </div>
                <div class="flex items-center gap-3 pt-2">
                    <button type="button" onclick="closeEditScoreModal()" class="flex-1 py-2 px-4 rounded-xl border border-slate-300 hover:bg-slate-50 text-slate-700 font-semibold text-xs">
                        Bekor qilish
                    </button>
                    <button type="submit" class="flex-1 py-2 px-4 rounded-xl bg-amber-600 hover:bg-amber-700 text-white font-semibold text-xs shadow">
                        Saqlash & Auditga yozish
                    </button>
                </div>
            </form>
        </div>
    </div>

    <!-- Modal 3: Audit Jurnali -->
    <div id="modalAudit" class="fixed inset-0 z-50 flex items-center justify-center bg-slate-900/60 backdrop-blur-sm hidden p-4" style="display: none;">
        <div class="bg-white rounded-3xl max-w-4xl w-full max-h-[85vh] flex flex-col shadow-2xl border border-slate-200">
            <div class="p-5 border-b border-slate-100 flex items-center justify-between">
                <div>
                    <h3 class="text-lg font-bold text-slate-900 flex items-center gap-2">
                        <i class="fa-solid fa-clock-rotate-left text-amber-500"></i>
                        <span>Audit Jurnali (O'zgartirishlar Tarixi)</span>
                    </h3>
                    <p class="text-xs text-slate-500">Ballarni tahrirlash va o'chirish bo'yicha barcha qaydlar</p>
                </div>
                <button onclick="toggleAuditModal()" class="w-8 h-8 rounded-lg bg-slate-100 hover:bg-slate-200 text-slate-500 flex items-center justify-center">
                    <i class="fa-solid fa-xmark"></i>
                </button>
            </div>
            <div class="p-6 overflow-y-auto flex-1">
                <table class="w-full text-left border-collapse text-xs sm:text-sm">
                    <thead>
                        <tr class="bg-slate-50 border-b border-slate-200 text-slate-500 uppercase tracking-wider text-[11px] font-bold">
                            <th class="py-2.5 px-3">Talaba F.I.Sh.</th>
                            <th class="py-2.5 px-3 text-center">Eski Ball</th>
                            <th class="py-2.5 px-3 text-center">Yangi Ball</th>
                            <th class="py-2.5 px-3 text-center">Yangi Natija</th>
                            <th class="py-2.5 px-3">O'zgartirish Sababi</th>
                            <th class="py-2.5 px-3 text-center">Vaqt</th>
                        </tr>
                    </thead>
                    <tbody id="auditTableBody" class="divide-y divide-slate-100">
                        <!-- JS orqali to'ldiriladi -->
                    </tbody>
                </table>
            </div>
            <div class="p-4 border-t border-slate-100 flex justify-end">
                <button onclick="toggleAuditModal()" class="px-5 py-2 rounded-xl bg-slate-100 hover:bg-slate-200 text-slate-700 font-semibold text-xs">
                    Yopish
                </button>
            </div>
        </div>
    </div>

    <!-- Skript bloki -->
    <script>
        const ALL_QUESTIONS = {questions_json};
        const STUDENTS_ROSTER = {students_roster_json};
        const TEST_STUDENT_ID = '000000000000';
    </script>
    <script src="app_standalone.js"></script>
</body>
</html>
"""

# Write to python_nazorat.html with embedded script or write app_standalone.js logic directly
# To make it a 100% standalone single-file HTML, we read app_standalone.js and embed it!
print("HTML template prepared.")
