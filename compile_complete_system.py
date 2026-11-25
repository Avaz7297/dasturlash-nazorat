# -*- coding: utf-8 -*-
# Compile complete system


import os
import shutil
import json
import students_roster as sr
import questions_data as qd

base_dir = os.path.dirname(os.path.abspath(__file__))

# =========================================================================
# 1. WRITE app_standalone.js
# =========================================================================

app_js_code = f"""// app_standalone.js - Masofaviy Joriy Nazorat Mustaqil Skripti
// Rasmiy 130 ta talaba (9mt-26, 10mt-26, 11mt-26, 12mt-26, 13mt-26, 14mt-26) va Sinov Talabasi

const STUDENTS_ROSTER = {json.dumps(sr.STUDENTS_ROSTER, ensure_ascii=False)};
const TEST_STUDENT_ID = "000000000000";

// 1. Mavzular taqsimoti qoidasi (Jami 30 ta savol)
const SAMPLE_RULES = {{
    "Python dasturlash tili va dastur kodini yozish": 4,
    "String va sonlar bilan ishlash": 4,
    "While sikli": 4,
    "Lug‘atlar bilan ishlash": 4,
    "Klasslar bilan ishlash": 4,
    "O‘zgaruvchilar va ma’lumot toifalari": 5,
    "Shartli ifodalar": 5
}};

// Doimiy saqlash (Xavfsiz xotira: iOS Safari, Android, Telegram va Files ilovasi uchun)
const SafeStorage = {{
    mem: {{}},
    getItem(k) {{
        try {{
            if (typeof localStorage !== "undefined") {{
                const v = localStorage.getItem(k);
                if (v !== null) return v;
            }}
        }} catch(e) {{}}
        return this.mem[k] || null;
    }},
    setItem(k, v) {{
        try {{
            if (typeof localStorage !== "undefined") {{
                localStorage.setItem(k, v);
            }}
        }} catch(e) {{}}
        this.mem[k] = String(v);
    }},
    removeItem(k) {{
        try {{
            if (typeof localStorage !== "undefined") {{
                localStorage.removeItem(k);
            }}
        }} catch(e) {{}}
        delete this.mem[k];
    }}
}};

const SafeSession = {{
    mem: {{}},
    getItem(k) {{
        try {{
            if (typeof sessionStorage !== "undefined") {{
                const v = sessionStorage.getItem(k);
                if (v !== null) return v;
            }}
        }} catch(e) {{}}
        return this.mem[k] || null;
    }},
    setItem(k, v) {{
        try {{
            if (typeof sessionStorage !== "undefined") {{
                sessionStorage.setItem(k, v);
            }}
        }} catch(e) {{}}
        this.mem[k] = String(v);
    }},
    removeItem(k) {{
        try {{
            if (typeof sessionStorage !== "undefined") {{
                sessionStorage.removeItem(k);
            }}
        }} catch(e) {{}}
        delete this.mem[k];
    }}
}};

const STORAGE_KEY_STUDENTS = "py_exam_students_data_v1";
const STORAGE_KEY_AUDIT = "py_exam_audit_logs_v1";
const STORAGE_KEY_TEACHER_AUTH = "py_exam_teacher_auth_v1";
const STORAGE_KEY_TEACHER_PASS_HASH = "py_exam_teacher_hash_v1";
const STORAGE_KEY_ACTIVE_EXAM = "py_exam_active_session_v1";
const STORAGE_KEY_ACTIVE_VIEW = "py_exam_active_view_v1";
const STORAGE_KEY_LAST_RESULT = "py_exam_last_result_v1";
const STORAGE_KEY_PENDING_STUDENT = "py_exam_pending_student_v1";

// Standart o'qituvchi xeshi
const DEFAULT_TEACHER_HASH = "f1dc2cd6";

// Global holat
let pendingStudent = null; // Kirish qilgan, lekin testni hali boshlamagan talaba
let currentStudent = null; // Testni boshlagan talaba
let currentQuestions = [];
let currentAnswers = {{}};
let currentQuestionIdx = 0;
let timerInterval = null;
let remainingSeconds = 3600; // 60 daqiqa
let examStartTimeMs = null;
let tabSwitchCount = 0;
let isExamActive = false;
let isViolationModalOpen = false;
let isPageUnloading = false;
let currentResultObject = null;
let teacherAutoRefreshTimer = null;

// Xavfsizlik: noto'g'ri urinishlar cheklovi
let failedLoginAttempts = 0;
let loginLockoutUntil = 0;

// Xavfsiz nazorat kodi (Checksum)
function generateChecksum(str) {{
    let h1 = 0x811c9dc5, h2 = 0x5b79e234;
    for (let i = 0; i < str.length; i++) {{
        const c = str.charCodeAt(i);
        h1 = Math.imul(h1 ^ c, 0x01000193);
        h2 = Math.imul(h2 ^ (c << 3), 0x01000193);
    }}
    const part1 = (h1 >>> 0).toString(16).padStart(8, '0');
    const part2 = (h2 >>> 0).toString(16).padStart(8, '0');
    return part1.substring(0, 4) + part2.substring(0, 4);
}}

// Sahifalar (View) almashinuvi
function switchView(viewName) {{
    const secReg = document.getElementById("sectionRegister");
    const secReady = document.getElementById("sectionReady");
    const secExam = document.getElementById("sectionExam");
    const secRes = document.getElementById("sectionResult");
    const secTeach = document.getElementById("sectionTeacher");

    const all = [secReg, secReady, secExam, secRes, secTeach];
    all.forEach(sec => {{
        if (sec) {{
            sec.classList.add("hidden");
            sec.style.display = "none";
        }}
    }});

    let target = null;
    if (viewName === "register") target = secReg;
    else if (viewName === "ready") target = secReady;
    else if (viewName === "exam") target = secExam;
    else if (viewName === "result") target = secRes;
    else if (viewName === "teacher") target = secTeach;

    if (target) {{
        target.classList.remove("hidden");
        target.style.display = "block";
    }}

    // Aktiv view holatini saqlash (faqat exam yoki result bo'lsa)
    try {{
        if (viewName === "exam" || viewName === "result" || viewName === "teacher") {{
            SafeStorage.setItem(STORAGE_KEY_ACTIVE_VIEW, viewName);
        }} else {{
            SafeStorage.setItem(STORAGE_KEY_ACTIVE_VIEW, "register");
        }}
    }} catch(e) {{}}

    // Agar o'qituvchi panelidan chiqilsa taymerni to'xtatish
    if (viewName !== "teacher") {{
        stopTeacherAutoRefresh();
    }}

    window.scrollTo({{ top: 0, behavior: 'smooth' }});
}}

// Talaba ID kiritilganda avtomatik ro'yxatdan qidirish va to'ldirish
function handleStudentIdInput(input) {{
    if (!input) return;
    input.value = input.value.replace(/\\D/g, '').slice(0, 12);
    const idVal = input.value;
    const statusEl = document.getElementById("idLookupStatus");
    const nameEl = document.getElementById("regFullName");
    const groupEl = document.getElementById("regGroup");
    const dirEl = document.getElementById("regDirection");
    const crsEl = document.getElementById("regCourse");

    if (idVal.length < 12) {{
        if (statusEl) {{
            statusEl.innerHTML = '<span class="text-slate-500">12 xonali HEMIS ID kiriting (' + idVal.length + '/12)</span>';
        }}
        return;
    }}

    // Sinov talabasi
    if (idVal === TEST_STUDENT_ID) {{
        if (nameEl) nameEl.value = "O'QITUVCHI SINOV TALABASI (TEST REJIMI)";
        if (groupEl) groupEl.value = "SINOV (TEST)";
        if (dirEl) dirEl.value = "Telekommunikatsiya texnologiyalari (ATT)";
        if (crsEl) crsEl.value = "1";
        if (statusEl) {{
            statusEl.innerHTML = '<span class="text-amber-700 font-bold bg-amber-50 px-2 py-0.5 rounded border border-amber-200">🧪 O\\'qituvchi sinov rejimi faol (Cheklovlarsiz)</span>';
        }}
        return;
    }}

    const found = STUDENTS_ROSTER.find(s => s.id === idVal);
    if (found) {{
        if (nameEl) nameEl.value = found.name;
        if (groupEl) groupEl.value = found.group;
        if (dirEl) dirEl.value = "Telekommunikatsiya texnologiyalari (ATT)";
        if (crsEl) crsEl.value = "1";

        // Tekshirish: Talaba testni yakunlab, natija olganmi?
        const existingList = getStoredStudents();
        const alreadyTested = existingList.find(s => s.studentId === idVal);
        if (alreadyTested) {{
            if (statusEl) {{
                statusEl.innerHTML = '<span class="text-rose-700 font-bold bg-rose-50 px-2 py-0.5 rounded border border-rose-200">⚠️ Ushbu talaba allaqachon test topshirgan (' + alreadyTested.totalScore + ' ball)! Qayta topshirish taqiqlanadi.</span>';
            }}
        }} else {{
            if (statusEl) {{
                statusEl.innerHTML = '<span class="text-emerald-700 font-bold bg-emerald-50 px-2 py-0.5 rounded border border-emerald-200">✅ Tasdiqlandi: ' + found.name + ' (' + found.group + ')</span>';
            }}
        }}
    }} else {{
        if (statusEl) {{
            statusEl.innerHTML = '<span class="text-rose-700 font-bold bg-rose-50 px-2 py-0.5 rounded border border-rose-200">❌ Ushbu ID rasmiy talabalar ro\\'yxatida topilmadi!</span>';
        }}
    }}
}}

// O'qituvchi sinov rejimini tezkor faollashtirish
function setTeacherDemoMode() {{
    const idInput = document.getElementById("regStudentId");
    if (idInput) {{
        idInput.value = TEST_STUDENT_ID;
        handleStudentIdInput(idInput);
    }}
}}

// Dastur ishga tushganda (yoki sahifa yangilanganda) holatni tiklash
window.addEventListener("DOMContentLoaded", () => {{
    initSecurityListeners();
    restoreStateOnLoad();
}});

function restoreStateOnLoad() {{
    // 1. Faol test jarayonini tekshirish (faqat agar test avval boshlangan bo'lsa)
    const rawExam = SafeStorage.getItem(STORAGE_KEY_ACTIVE_EXAM);
    if (rawExam) {{
        try {{
            const session = JSON.parse(rawExam);
            if (session && session.student && session.questions && session.questions.length === 30) {{
                const now = Date.now();
                const startTime = session.startTimeMs || now;
                const elapsed = Math.floor((now - startTime) / 1000);
                const duration = session.durationSeconds || 3600;
                const remaining = duration - elapsed;

                if (remaining <= 0) {{
                    currentStudent = session.student;
                    currentQuestions = session.questions;
                    currentAnswers = session.answers || {{}};
                    tabSwitchCount = session.tabSwitchCount || 0;
                    alert("Sahifa yangilanganda test vaqti (60 daqiqa) tugaganligi aniqlandi. Natijalaringiz avtomatik hisoblandi!");
                    submitExamNow();
                    return;
                }}

                // Testni tiklash (Vaqt o'z holicha davom etadi)
                currentStudent = session.student;
                currentQuestions = session.questions;
                currentAnswers = session.answers || {{}};
                currentQuestionIdx = (typeof session.currentQuestionIdx === "number") ? session.currentQuestionIdx : 0;
                tabSwitchCount = session.tabSwitchCount || 0;
                examStartTimeMs = startTime;
                remainingSeconds = remaining;
                isExamActive = true;

                // Talaba ma'lumotlarini to'ldirish
                const nameEl = document.getElementById("examStudentName");
                const idEl = document.getElementById("examStudentIdBadge");
                const grpEl = document.getElementById("examStudentGroup");
                const crsEl = document.getElementById("examStudentCourse");
                if (nameEl) nameEl.textContent = currentStudent.fullName;
                if (idEl) idEl.textContent = "ID: " + (currentStudent.studentId || "-");
                if (grpEl) grpEl.textContent = currentStudent.groupName;
                if (crsEl) crsEl.textContent = currentStudent.course + "-kurs";

                if (tabSwitchCount > 0) {{
                    const badgeSwitches = document.getElementById("badgeTabSwitches");
                    if (badgeSwitches) badgeSwitches.classList.remove("hidden");
                    const textSwitches = document.getElementById("textTabSwitches");
                    if (textSwitches) textSwitches.textContent = tabSwitchCount;
                    const violationCountBadge = document.getElementById("violationCountBadge");
                    if (violationCountBadge) violationCountBadge.textContent = tabSwitchCount;
                }}

                switchView("exam");
                renderQuestionsMap();
                loadQuestion(currentQuestionIdx);
                startTimer();
                return;
            }}
        }} catch(e) {{}}
    }}

    // 2. Oxirgi natija mavjud bo'lsa
    const rawRes = SafeStorage.getItem(STORAGE_KEY_LAST_RESULT);
    if (rawRes) {{
        try {{
            const res = JSON.parse(rawRes);
            if (res && res.fullName) {{
                showResultPage(res);
                return;
            }}
        }} catch(e) {{}}
    }}

    // 3. Standart: Ro'yxatdan o'tish (bosh sahifa)
    switchView("register");
}}

// Xavfsizlik va Anti-cheat
function initSecurityListeners() {{
    document.addEventListener("contextmenu", (e) => {{
        if (isExamActive) {{ e.preventDefault(); return false; }}
    }});
    document.addEventListener("copy", (e) => {{
        if (isExamActive) {{ e.preventDefault(); return false; }}
    }});
    document.addEventListener("cut", (e) => {{
        if (isExamActive) {{ e.preventDefault(); return false; }}
    }});
    document.addEventListener("selectstart", (e) => {{
        if (isExamActive) {{ e.preventDefault(); return false; }}
    }});

    document.addEventListener("visibilitychange", () => {{
        if (isExamActive && document.hidden && !isPageUnloading) {{
            triggerTabViolation();
        }}
    }});

    window.addEventListener("blur", () => {{
        if (isExamActive && !isPageUnloading) {{
            triggerTabViolation();
        }}
    }});

    window.addEventListener("beforeunload", () => {{
        isPageUnloading = true;
        if (isExamActive) {{
            saveActiveExamState();
        }}
    }});
}}

// Faol test holatini doimiy saqlash
function saveActiveExamState() {{
    if (!isExamActive || !currentStudent) return;
    try {{
        const payload = {{
            student: currentStudent,
            questions: currentQuestions,
            answers: currentAnswers,
            currentQuestionIdx: currentQuestionIdx,
            startTimeMs: examStartTimeMs,
            durationSeconds: 3600,
            tabSwitchCount: tabSwitchCount
        }};
        SafeStorage.setItem(STORAGE_KEY_ACTIVE_EXAM, JSON.stringify(payload));
    }} catch(e) {{}}
}}

// Qoidabuzarlik modalini ochish
function triggerTabViolation() {{
    if (isViolationModalOpen || !isExamActive || isPageUnloading) return;
    tabSwitchCount++;
    saveActiveExamState();
    const badgeCount = document.getElementById("violationCountBadge");
    if (badgeCount) badgeCount.textContent = tabSwitchCount;

    const textSwitches = document.getElementById("textTabSwitches");
    if (textSwitches) textSwitches.textContent = tabSwitchCount;

    const badgeSwitches = document.getElementById("badgeTabSwitches");
    if (badgeSwitches) {{ badgeSwitches.classList.remove("hidden"); badgeSwitches.style.display = "inline-flex"; }}

    isViolationModalOpen = true;
    const modal = document.getElementById("modalViolation");
    if (modal) {{ modal.classList.remove("hidden"); modal.style.display = "flex"; }}
}}

function closeViolationModal() {{
    const modal = document.getElementById("modalViolation");
    if (modal) {{ modal.classList.add("hidden"); modal.style.display = "none"; }}
    isViolationModalOpen = false;
}}

// =========================================================================
// 1. RO'YXATDAN O'TISH VA TAYYORGARLIK BOSQICHI (VAQT HALI KETMAYDI!)
// =========================================================================

function handleRegisterSubmit(e) {{
    if (e && e.preventDefault) e.preventDefault();

    const idInput = document.getElementById("regStudentId");
    const fullNameInput = document.getElementById("regFullName");
    const directionInput = document.getElementById("regDirection");
    const courseInput = document.getElementById("regCourse");
    const groupInput = document.getElementById("regGroup");

    const studentId = idInput ? idInput.value.trim() : "";
    const fullName = fullNameInput ? fullNameInput.value.trim() : "";
    const direction = directionInput ? directionInput.value.trim() : "";
    const course = courseInput ? courseInput.value.trim() : "";
    let groupName = groupInput ? groupInput.value.trim() : "";

    // 1. Maydonlar to'ldirilganligi tekshiruvi
    if (!studentId || !fullName || !direction || !course || !groupName) {{
        alert("Iltimos, barcha maydonlarni (Talaba ID, F.I.Sh., Guruh) to'ldiring!");
        return false;
    }}

    // 2. Talaba ID 12 ta raqam bo'lishi shart!
    if (!/^\\d{{12}}$/.test(studentId)) {{
        alert("Xatolik: Talaba ID 12 ta raqamdan iborat bo'lishi kerak! (Masalan: 315261102911)");
        if (idInput) idInput.focus();
        return false;
    }}

    // 3. Rasmiy ro'yxatda mavjudligini tekshirish
    const isTestMode = (studentId === TEST_STUDENT_ID);
    if (!isTestMode) {{
        const foundInRoster = STUDENTS_ROSTER.find(s => s.id === studentId);
        if (!foundInRoster) {{
            alert("Xatolik: Kiritilgan Talaba ID (" + studentId + ") rasmiy talabalar ro'yxatida topilmadi! Faqat ro'yxatga kiritilgan talabalar test topshira oladi.");
            if (idInput) idInput.focus();
            return false;
        }}

        // 4. BIR MARTA TOPSHIRISH QAT'IY TALABI (Faqat testni yakunlagan bo'lsa bloklanadi!)
        const existingStudents = getStoredStudents();
        const alreadyTested = existingStudents.find(s => s.studentId === studentId);

        if (alreadyTested) {{
            alert("Hurmatli " + alreadyTested.fullName + " (ID: " + studentId + ")!\\nSiz allaqachon ushbu joriy nazorat testini topshirib, yakunlagansiz.\\n\\nTo'plangan ball: " + alreadyTested.totalScore + " / 30 (" + alreadyTested.statusText + ").\\nTopshirilgan vaqt: " + (alreadyTested.finishedAt || alreadyTested.startedAt) + "\\n\\nNizomga muvofiq, har bir talaba testni faqat 1 MARTA topshirishi mumkin. Qayta kirish va qayta ishlash qat'iyan taqiqlanadi!");
            showResultPage(alreadyTested);
            return false;
        }}
    }}

    // Talaba ma'lumotlarini tayyorlash (Lekin test hali boshlanmadi!)
    pendingStudent = {{
        studentId: studentId,
        fullName: fullName,
        direction: direction,
        course: parseInt(course) || 1,
        groupName: groupName,
        subject: "Dasturlash"
    }};

    // Tayyorgarlik (Ready) oynasiga ma'lumotlarni o'tkazish
    document.getElementById("readyStudentId").textContent = pendingStudent.studentId;
    document.getElementById("readyStudentName").textContent = pendingStudent.fullName;
    document.getElementById("readyStudentGroup").textContent = pendingStudent.groupName;

    // Tayyorgarlik oynasiga o'tish (Vaqt hisoblanmaydi! Talaba chiqib ketsa qayta kirishi mumkin)
    switchView("ready");
    return false;
}}

// =========================================================================
// 2. TESTNI HAQIQATDA BOSHLASH (FAQAT SHU TUGMA BOSILGANDAN SO'NG VAQT KETADI)
// =========================================================================

function startExamActual() {{
    if (!pendingStudent) {{
        switchView("register");
        return;
    }}

    currentStudent = Object.assign({{}}, pendingStudent);
    currentStudent.startedAt = new Date().toLocaleString("uz-UZ");
    currentStudent.tabSwitchCount = 0;

    // 30 ta savolni tanlash
    currentQuestions = generateRandomExamQuestions();
    currentAnswers = {{}};
    currentQuestionIdx = 0;
    remainingSeconds = 3600; // 60 daqiqa
    examStartTimeMs = Date.now();
    tabSwitchCount = 0;
    isExamActive = true;

    // UI ni test oynasiga o'tkazish
    const nameEl = document.getElementById("examStudentName");
    const idEl = document.getElementById("examStudentIdBadge");
    const grpEl = document.getElementById("examStudentGroup");
    const crsEl = document.getElementById("examStudentCourse");
    if (nameEl) nameEl.textContent = currentStudent.fullName;
    if (idEl) idEl.textContent = "ID: " + currentStudent.studentId;
    if (grpEl) grpEl.textContent = currentStudent.groupName;
    if (crsEl) crsEl.textContent = currentStudent.course + "-kurs";

    switchView("exam");
    saveActiveExamState();

    renderQuestionsMap();
    loadQuestion(0);
    startTimer(); // VAQT FAQAT SHU YERDA ISHGA TUSHADI!
}}

// Mavzu nomini normallashtirish
function normalizeTopicName(s) {{
    return (s || "").replace(/[`'‘’ʻʼ]/g, "'").toLowerCase().trim();
}}

// 30 ta savolni 7 ta mavzudan tasodifiy tanlash
function generateRandomExamQuestions() {{
    const poolByTopic = {{}};
    ALL_QUESTIONS.forEach(q => {{
        const normKey = normalizeTopicName(q.topic);
        if (!poolByTopic[normKey]) poolByTopic[normKey] = [];
        poolByTopic[normKey].push(q);
    }});

    const selected = [];
    for (const [topicName, neededCount] of Object.entries(SAMPLE_RULES)) {{
        const normKey = normalizeTopicName(topicName);
        const pool = poolByTopic[normKey] || [];
        const shuffled = [...pool].sort(() => 0.5 - Math.random());
        const picked = shuffled.slice(0, neededCount);
        selected.push(...picked);
    }}

    // Agar 30 ta to'lmagan bo'lsa
    if (selected.length < 30) {{
        const remaining = ALL_QUESTIONS.filter(q => !selected.includes(q));
        const shuffled = [...remaining].sort(() => 0.5 - Math.random());
        selected.push(...shuffled.slice(0, 30 - selected.length));
    }}

    return selected.sort(() => 0.5 - Math.random());
}}

// Savollar xaritasini chizish
function renderQuestionsMap() {{
    const grid = document.getElementById("questionsMapGrid");
    if (!grid) return;
    grid.innerHTML = "";

    currentQuestions.forEach((q, idx) => {{
        const btn = document.createElement("button");
        btn.type = "button";
        btn.id = "mapBtn_" + idx;
        btn.onclick = () => loadQuestion(idx);

        const isAnswered = currentAnswers[idx] !== undefined;
        const isCurrent = currentQuestionIdx === idx;

        let cls = "w-full py-2 rounded-xl text-xs font-bold transition-all border flex items-center justify-center ";
        if (isCurrent) {{
            cls += "border-blue-600 bg-blue-50 text-blue-700 ring-2 ring-blue-500/20";
        }} else if (isAnswered) {{
            cls += "bg-blue-600 border-blue-600 text-white shadow-sm";
        }} else {{
            cls += "bg-white border-slate-200 text-slate-700 hover:bg-slate-50";
        }}

        btn.className = cls;
        btn.textContent = idx + 1;
        grid.appendChild(btn);
    }});

    const answeredCount = Object.keys(currentAnswers).length;
    const answeredEl = document.getElementById("mapAnsweredCount");
    if (answeredEl) answeredEl.textContent = answeredCount;
}}

// Savolni yuklash
function loadQuestion(idx) {{
    if (idx < 0 || idx >= currentQuestions.length) return;
    currentQuestionIdx = idx;

    const q = currentQuestions[idx];
    document.getElementById("qCurrentNumber").textContent = idx + 1;
    document.getElementById("qProgressText").textContent = idx + 1;
    document.getElementById("qTopicBadge").textContent = q.topic;

    const diffBadge = document.getElementById("qDifficultyBadge");
    if (diffBadge) {{
        diffBadge.textContent = q.difficulty || "O'rtacha";
        if (q.difficulty === "Oson") diffBadge.className = "text-xs px-2.5 py-0.5 rounded-full font-medium bg-emerald-50 text-emerald-700 border border-emerald-200";
        else if (q.difficulty === "Qiyin") diffBadge.className = "text-xs px-2.5 py-0.5 rounded-full font-medium bg-rose-50 text-rose-700 border border-rose-200";
        else diffBadge.className = "text-xs px-2.5 py-0.5 rounded-full font-medium bg-amber-50 text-amber-700 border border-amber-200";
    }}

    document.getElementById("qQuestionText").textContent = q.question;

    const codeBox = document.getElementById("qCodeBlock");
    const codeContent = document.getElementById("qCodeContent");
    if (q.code && q.code.trim()) {{
        codeContent.textContent = q.code;
        codeBox.classList.remove("hidden");
        codeBox.style.display = "block";
    }} else {{
        codeBox.classList.add("hidden");
        codeBox.style.display = "none";
    }}

    const optionsContainer = document.getElementById("qOptionsList");
    optionsContainer.innerHTML = "";
    const letters = ["A", "B", "C", "D"];

    q.options.forEach((optText, optIdx) => {{
        const isChecked = currentAnswers[idx] === optIdx;
        const optCard = document.createElement("label");
        optCard.className = "option-card flex items-center gap-3 p-3.5 sm:p-4 rounded-2xl border transition-all cursor-pointer select-none " + 
            (isChecked ? "border-blue-600 bg-blue-50/80 shadow-sm" : "border-slate-200 bg-white hover:border-slate-300 hover:bg-slate-50/50");

        optCard.innerHTML = 
            '<input type="radio" name="exam_option" value="' + optIdx + '" class="w-4 h-4 text-blue-600 border-slate-300 focus:ring-blue-500" ' + (isChecked ? "checked" : "") + ' onchange="selectAnswer(' + idx + ', ' + optIdx + ')">' +
            '<span class="w-6 h-6 rounded-lg bg-slate-100 text-slate-700 font-bold text-xs flex items-center justify-center shrink-0">' + letters[optIdx] + '</span>' +
            '<span class="text-xs sm:text-sm font-medium text-slate-800 leading-snug">' + escapeHtml(optText) + '</span>';

        optionsContainer.appendChild(optCard);
    }});

    const btnPrev = document.getElementById("btnPrevQ");
    const btnNext = document.getElementById("btnNextQ");
    if (btnPrev) btnPrev.disabled = (idx === 0);
    if (btnNext) {{
        if (idx === currentQuestions.length - 1) {{
            btnNext.innerHTML = '<span>Yakunlash</span> <i class="fa-solid fa-flag-checkered"></i>';
            btnNext.onclick = confirmFinishModalOpen;
        }} else {{
            btnNext.innerHTML = '<span>Keyingi</span> <i class="fa-solid fa-arrow-right"></i>';
            btnNext.onclick = nextQuestion;
        }}
    }}

    renderQuestionsMap();
    saveActiveExamState();
}}

function selectAnswer(qIdx, optIdx) {{
    currentAnswers[qIdx] = optIdx;
    renderQuestionsMap();
    saveActiveExamState();
}}

function nextQuestion() {{
    if (currentQuestionIdx < currentQuestions.length - 1) {{
        loadQuestion(currentQuestionIdx + 1);
    }}
}}

function prevQuestion() {{
    if (currentQuestionIdx > 0) {{
        loadQuestion(currentQuestionIdx - 1);
    }}
}}

// Taymer (60 daqiqa)
function startTimer() {{
    clearInterval(timerInterval);
    updateTimerDisplay();

    timerInterval = setInterval(() => {{
        if (!isExamActive) {{
            clearInterval(timerInterval);
            return;
        }}

        remainingSeconds--;
        updateTimerDisplay();

        if (remainingSeconds <= 0) {{
            clearInterval(timerInterval);
            alert("Vaqt tugadi! Test natijalaringiz avtomatik hisoblandi va o'qituvchiga saqlandi.");
            submitExamNow();
        }}
    }}, 1000);
}}

function updateTimerDisplay() {{
    const timerDisplay = document.getElementById("timerDisplay");
    if (!timerDisplay) return;

    const mins = Math.floor(Math.max(0, remainingSeconds) / 60);
    const secs = Math.max(0, remainingSeconds) % 60;
    const formatted = String(mins).padStart(2, '0') + ":" + String(secs).padStart(2, '0');
    timerDisplay.textContent = formatted;

    const timerIcon = document.getElementById("timerIcon");
    if (remainingSeconds < 300) {{ // 5 daqiqadan kam
        timerDisplay.classList.add("text-rose-600");
        if (timerIcon) timerIcon.className = "w-8 h-8 rounded-lg bg-rose-100 text-rose-600 flex items-center justify-center text-sm animate-bounce";
    }} else {{
        timerDisplay.classList.remove("text-rose-600");
        if (timerIcon) timerIcon.className = "w-8 h-8 rounded-lg bg-amber-100 text-amber-600 flex items-center justify-center text-sm";
    }}
}}

// Yakunlash modali
function confirmFinishModalOpen() {{
    const answeredCount = Object.keys(currentAnswers).length;
    document.getElementById("modalAnsweredCount").textContent = answeredCount;
    const modal = document.getElementById("modalFinishConfirm");
    if (modal) {{ modal.classList.remove("hidden"); modal.style.display = "flex"; }}
}}

function closeFinishModal() {{
    const modal = document.getElementById("modalFinishConfirm");
    if (modal) {{ modal.classList.add("hidden"); modal.style.display = "none"; }}
}}

// =========================================================================
// 3. TESTNI YAKUNLASH VA NATIJANI SAQLASH (SHUNDAN SO'NG QAYTA KIROLMAYDI)
// =========================================================================

function submitExamNow() {{
    closeFinishModal();
    clearInterval(timerInterval);
    isExamActive = false;

    // Faol test seansini tozalash
    try {{
        SafeStorage.removeItem(STORAGE_KEY_ACTIVE_EXAM);
    }} catch(e) {{}}

    let correctCount = 0;
    currentQuestions.forEach((q, idx) => {{
        if (currentAnswers[idx] === q.correct) {{
            correctCount++;
        }}
    }});

    const incorrectCount = 30 - correctCount;
    const totalScore = correctCount; // 1 ball har bir to'g'ri javob uchun
    const statusText = (totalScore >= 18) ? "Joriy nazoratdan o‘tdi" : "Joriy nazoratdan o‘tmadi";
    const finishedAt = new Date().toLocaleString("uz-UZ");

    const completedResult = {{
        id: Date.now(),
        studentId: currentStudent.studentId || "",
        fullName: currentStudent.fullName,
        direction: currentStudent.direction,
        course: currentStudent.course,
        groupName: currentStudent.groupName,
        subject: "Dasturlash",
        startedAt: currentStudent.startedAt,
        finishedAt: finishedAt,
        totalScore: totalScore,
        maxScore: 30,
        correctCount: correctCount,
        incorrectCount: incorrectCount,
        statusText: statusText,
        tabSwitchCount: tabSwitchCount,
        questions: currentQuestions,
        answers: currentAnswers,
        isModified: false
    }};

    // DARHOL O'QITUVCHI BAZASIGA SAQLASH (SHUNDAN SO'NG BU TALABA ID BLOKLANADI!)
    saveStudentResult(completedResult);

    // Agar Flask server orqali ishlayotgan bo'lsa, markaziy serverga ham uzatish
    try {{
        fetch('/api/direct_submit', {{
            method: 'POST',
            headers: {{ 'Content-Type': 'application/json' }},
            body: JSON.stringify(completedResult)
        }}).catch(() => {{}});
    }} catch(e) {{}}

    try {{
        SafeStorage.setItem(STORAGE_KEY_LAST_RESULT, JSON.stringify(completedResult));
        SafeStorage.setItem(STORAGE_KEY_ACTIVE_VIEW, "result");
    }} catch(e) {{}}

    showResultPage(completedResult);
}}

// Natija sahifasi
function showResultPage(result) {{
    currentResultObject = result;
    switchView("result");
    try {{
        SafeStorage.setItem(STORAGE_KEY_LAST_RESULT, JSON.stringify(result));
    }} catch(e) {{}}

    const isPassed = result.totalScore >= 18;
    const idEl = document.getElementById("resStudentId");
    if (idEl) idEl.textContent = result.studentId || "-";

    document.getElementById("resultStatusText").textContent = result.statusText;
    document.getElementById("resultScore").textContent = result.totalScore;
    document.getElementById("resultCorrectCount").textContent = result.correctCount + " ta to'g'ri";
    document.getElementById("resultIncorrectCount").textContent = result.incorrectCount + " ta noto'g'ri";

    document.getElementById("resStudentName").textContent = result.fullName;
    document.getElementById("resStudentDirection").textContent = result.direction + " (" + result.course + "-kurs)";
    document.getElementById("resStudentGroup").textContent = result.groupName;
    document.getElementById("resDate").textContent = result.finishedAt || result.startedAt;
    document.getElementById("resSwitches").textContent = (result.tabSwitchCount || 0) + " marta";

    const colorBar = document.getElementById("resultColorBar");
    const iconBox = document.getElementById("resultIconBox");
    const icon = document.getElementById("resultIcon");

    if (isPassed) {{
        colorBar.className = "absolute top-0 left-0 right-0 h-3 bg-emerald-500";
        iconBox.className = "w-20 h-20 rounded-full bg-emerald-100 text-emerald-600 flex items-center justify-center text-4xl shadow-lg shadow-emerald-500/20 ring-8 ring-emerald-50";
        icon.className = "fa-solid fa-circle-check";
    }} else {{
        colorBar.className = "absolute top-0 left-0 right-0 h-3 bg-rose-500";
        iconBox.className = "w-20 h-20 rounded-full bg-rose-100 text-rose-600 flex items-center justify-center text-4xl shadow-lg shadow-rose-500/20 ring-8 ring-rose-50";
        icon.className = "fa-solid fa-circle-xmark";
    }}
}}

function navigateHome() {{
    if (isExamActive) {{
        if (!confirm("Test jarayonida bosh sahifaga o'tsangiz, test avtomatik yakunlanadi. Davom etasizmi?")) {{
            return;
        }}
        submitExamNow();
        return;
    }}
    try {{
        SafeStorage.removeItem(STORAGE_KEY_LAST_RESULT);
    }} catch(e) {{}}
    switchView("register");
}}

// =========================================================================
// 4. O'QITUVCHI BOSHQARUVI: VEDOMOST, STATISTIKA VA AMALLAR
// =========================================================================

function toggleTeacherSection() {{
    if (isExamActive) {{
        alert("Diqqat! Test jarayonida o'qituvchi bo'limiga kirish taqiqlanadi!");
        return;
    }}
    switchView("teacher");

    const isAuth = (SafeSession.getItem(STORAGE_KEY_TEACHER_AUTH) === "true") ||
                   (SafeStorage.getItem(STORAGE_KEY_TEACHER_AUTH) === "true");
    const loginForm = document.getElementById("teacherLoginForm");
    const dash = document.getElementById("teacherDashboard");

    if (isAuth) {{
        if (loginForm) {{ loginForm.classList.add("hidden"); loginForm.style.display = "none"; }}
        if (dash) {{ dash.classList.remove("hidden"); dash.style.display = "block"; }}
        renderTeacherTable();
        startTeacherAutoRefresh();
    }} else {{
        stopTeacherAutoRefresh();
        if (loginForm) {{ loginForm.classList.remove("hidden"); loginForm.style.display = "block"; }}
        if (dash) {{ dash.classList.add("hidden"); dash.style.display = "none"; }}
        const u = document.getElementById("teachLoginInput");
        const p = document.getElementById("teachPassInput");
        if (u) u.value = "";
        if (p) p.value = "";
    }}
}}

// O'qituvchi kirishini tekshirish
function handleTeacherLogin(e) {{
    if (e && e.preventDefault) e.preventDefault();

    const u = document.getElementById("teachLoginInput").value.trim();
    const p = document.getElementById("teachPassInput").value.trim();

    if (!u || !p) {{
        alert("Login va parolni kiriting!");
        return false;
    }}

    // Login: admin, Parol: admin123 (yoki admin 123)
    const storedHash = SafeStorage.getItem(STORAGE_KEY_TEACHER_PASS_HASH) || generateChecksum("admin 123");
    const enteredHash = generateChecksum(p);

    const isDefaultAdmin = (u === "admin" && (p === "admin123" || p === "admin 123"));
    const isCustomAdmin = (u === "admin" && enteredHash === storedHash);

    if (isDefaultAdmin || isCustomAdmin) {{
        SafeSession.setItem(STORAGE_KEY_TEACHER_AUTH, "true");
        SafeStorage.setItem(STORAGE_KEY_TEACHER_AUTH, "true");
        const loginForm = document.getElementById("teacherLoginForm");
        const dash = document.getElementById("teacherDashboard");
        if (loginForm) {{ loginForm.classList.add("hidden"); loginForm.style.display = "none"; }}
        if (dash) {{ dash.classList.remove("hidden"); dash.style.display = "block"; }}
        renderTeacherTable();
        startTeacherAutoRefresh();
    }} else {{
        alert("Xatolik: Login yoki parol noto'g'ri! Ruxsatsiz kirish taqiqlanadi.");
    }}
    return false;
}}

function teacherLogout() {{
    SafeSession.removeItem(STORAGE_KEY_TEACHER_AUTH);
    SafeStorage.removeItem(STORAGE_KEY_TEACHER_AUTH);
    stopTeacherAutoRefresh();
    const loginForm = document.getElementById("teacherLoginForm");
    const dash = document.getElementById("teacherDashboard");
    if (loginForm) {{ loginForm.classList.remove("hidden"); loginForm.style.display = "block"; }}
    if (dash) {{ dash.classList.add("hidden"); dash.style.display = "none"; }}
    try {{
        SafeStorage.setItem(STORAGE_KEY_ACTIVE_VIEW, "register");
    }} catch(e) {{}}
    switchView("register");
}}

// O'qituvchi parolini o'zgartirish
function changeTeacherPassword() {{
    const oldPass = prompt("Joriy parolingizni kiriting:");
    if (!oldPass) return;

    const oldHash = generateChecksum(oldPass.trim());
    const currentHash = SafeStorage.getItem(STORAGE_KEY_TEACHER_PASS_HASH) || generateChecksum("admin 123");

    const isStandardOld = (oldPass.trim() === "admin 123" || oldPass.trim() === "admin123");
    if (!isStandardOld && oldHash !== currentHash) {{
        alert("Joriy parol noto'g'ri!");
        return;
    }}

    const newPass = prompt("Yangi maxfiy parolni kiriting (kamida 6 ta belgi):");
    if (!newPass || newPass.trim().length < 6) {{
        alert("Parol kamida 6 ta belgidan iborat bo'lishi kerak!");
        return;
    }}

    const confirmPass = prompt("Yangi parolni takrorlang:");
    if (newPass.trim() !== confirmPass.trim()) {{
        alert("Parollar mos kelmadi!");
        return;
    }}

    const newHash = generateChecksum(newPass.trim());
    SafeStorage.setItem(STORAGE_KEY_TEACHER_PASS_HASH, newHash);
    alert("Parolingiz muvaffaqiyatli o'zgartirildi! Yangi parolingizni eslab qoling.");
}}

// O'qituvchi jadvalini chizish
function renderTeacherTable() {{
    const students = getStoredStudents();
    const searchQuery = document.getElementById("teachSearchInput").value.toLowerCase().trim();
    const groupFilter = document.getElementById("teachGroupFilter").value.trim();

    const total = students.length;
    const passed = students.filter(s => s.totalScore >= 18).length;
    const failed = total - passed;
    const avg = total > 0 ? (students.reduce((a, b) => a + b.totalScore, 0) / total).toFixed(1) : 0;

    const totalRoster = STUDENTS_ROSTER.length; // 130
    document.getElementById("statTotalStudents").textContent = total + " / " + totalRoster + " (" + (totalRoster > 0 ? Math.round(total / totalRoster * 100) : 0) + "%)";
    document.getElementById("statPassed").textContent = passed + " (" + (total > 0 ? Math.round(passed / total * 100) : 0) + "%)";
    document.getElementById("statFailed").textContent = failed;
    document.getElementById("statAvgScore").textContent = avg + " / 30";

    const filtered = students.filter(s => {{
        const q = searchQuery;
        const matchSearch = !q || 
            (s.studentId && s.studentId.includes(q)) ||
            s.fullName.toLowerCase().includes(q) ||
            String(s.groupName).toLowerCase().includes(q) ||
            (s.direction && s.direction.toLowerCase().includes(q));
        const matchGroup = !groupFilter || String(s.groupName) === groupFilter;
        return matchSearch && matchGroup;
    }});

    const tbody = document.getElementById("teacherTableBody");
    tbody.innerHTML = "";

    if (filtered.length === 0) {{
        tbody.innerHTML = '<tr><td colspan="10" class="py-8 text-center text-slate-400">Hech qanday natija topilmadi.</td></tr>';
        return;
    }}

    filtered.forEach((st, idx) => {{
        const isPass = st.totalScore >= 18;
        const tr = document.createElement("tr");
        tr.className = "hover:bg-slate-50/80 transition-colors";
        tr.innerHTML = 
            '<td class="py-3 px-3 text-center font-bold text-slate-400">' + (idx + 1) + '</td>' +
            '<td class="py-3 px-3 text-center font-mono font-bold text-slate-900">' +
                '<span class="px-2 py-0.5 rounded bg-slate-100 text-slate-800 text-xs border border-slate-200">' + escapeHtml(st.studentId || "-") + '</span>' +
            '</td>' +
            '<td class="py-3 px-3 font-semibold text-slate-900">' +
                '<div>' + escapeHtml(st.fullName) + '</div>' +
                (st.isModified ? '<span class="text-[10px] bg-amber-100 text-amber-800 px-1.5 py-0.5 rounded font-bold">Tahrirlangan</span>' : '') +
            '</td>' +
            '<td class="py-3 px-3 text-center"><span class="font-bold text-blue-700 bg-blue-50 px-2 py-0.5 rounded text-xs">' + escapeHtml(String(st.groupName)) + '</span></td>' +
            '<td class="py-3 px-3 text-center font-bold text-emerald-600 font-mono">' + st.correctCount + '</td>' +
            '<td class="py-3 px-3 text-center font-bold text-rose-600 font-mono">' + st.incorrectCount + '</td>' +
            '<td class="py-3 px-3 text-center font-bold font-mono text-base ' + (isPass ? 'text-emerald-600' : 'text-rose-600') + '">' + st.totalScore + ' <span class="text-xs font-normal text-slate-400">/ 30</span></td>' +
            '<td class="py-3 px-3 text-center">' +
                '<span class="inline-flex items-center gap-1 px-2.5 py-0.5 rounded-full text-xs font-bold ' + (isPass ? 'bg-emerald-50 text-emerald-700 border border-emerald-200' : 'bg-rose-50 text-rose-700 border border-rose-200') + '">' + st.statusText + '</span>' +
            '</td>' +
            '<td class="py-3 px-3 text-center text-xs text-slate-500 font-mono">' +
                (st.finishedAt || st.startedAt) +
                (st.tabSwitchCount > 0 ? '<div class="text-[11px] text-amber-600 font-bold"><i class="fa-solid fa-triangle-exclamation"></i> ' + st.tabSwitchCount + ' ta chiqish</div>' : '') +
            '</td>' +
            '<td class="py-3 px-3 text-center whitespace-nowrap no-print">' +
                '<div class="flex items-center justify-center gap-1.5">' +
                    '<button onclick="openDetailModal(' + st.id + ')" title="Batafsil ko\'rish" class="w-8 h-8 rounded-lg bg-blue-50 hover:bg-blue-100 text-blue-700 flex items-center justify-center transition-colors"><i class="fa-solid fa-eye"></i></button>' +
                    '<button onclick="openEditScoreModal(' + st.id + ')" title="Natijani tahrirlash (Audit)" class="w-8 h-8 rounded-lg bg-amber-50 hover:bg-amber-100 text-amber-700 flex items-center justify-center transition-colors"><i class="fa-solid fa-pen-to-square"></i></button>' +
                    '<button onclick="deleteStudentResult(' + st.id + ')" title="Talaba natijasini o\'chirish (qayta topshirishga ruxsat)" class="w-8 h-8 rounded-lg bg-rose-50 hover:bg-rose-100 text-rose-600 flex items-center justify-center transition-colors"><i class="fa-solid fa-trash-can"></i></button>' +
                '</div>' +
            '</td>';
        tbody.appendChild(tr);
    }});
}}

// 1. BATAFSIL KO'RISH MODALI
function openDetailModal(studentId) {{
    const students = getStoredStudents();
    const st = students.find(s => s.id === studentId);
    if (!st) return;

    document.getElementById("detailModalName").textContent = st.fullName + " (ID: " + (st.studentId || "-") + ")";
    document.getElementById("detailModalMeta").textContent = st.groupName + " | " + st.direction + " (" + st.course + "-kurs) • Ball: " + st.totalScore + "/30 • Chiqishlar: " + (st.tabSwitchCount || 0) + " marta";

    const listContainer = document.getElementById("detailModalQuestionsList");
    listContainer.innerHTML = "";
    const letters = ["A", "B", "C", "D"];

    (st.questions || []).forEach((q, idx) => {{
        const userChoice = st.answers ? st.answers[idx] : undefined;
        const isCorrect = userChoice === q.correct;
        const answered = userChoice !== undefined;

        const card = document.createElement("div");
        card.className = "p-4 rounded-2xl border " + (isCorrect ? "border-emerald-200 bg-emerald-50/30" : (answered ? "border-rose-200 bg-rose-50/30" : "border-slate-200 bg-slate-50/50"));
        
        let cardHTML = 
            '<div class="flex items-center justify-between mb-2">' +
                '<span class="font-bold text-slate-800">№ ' + (idx + 1) + '. [' + q.topic + ']</span>' +
                '<span class="px-2 py-0.5 rounded text-[10px] font-bold ' + (isCorrect ? 'bg-emerald-100 text-emerald-800' : 'bg-rose-100 text-rose-800') + '">' + (isCorrect ? "To'g'ri (+1 ball)" : "Noto'g'ri (0 ball)") + '</span>' +
            '</div>' +
            '<div class="font-medium text-slate-900 mb-2">' + escapeHtml(q.question) + '</div>';

        if (q.code) {{
            cardHTML += '<pre class="p-3 bg-slate-900 text-slate-100 rounded-xl text-xs font-mono overflow-x-auto mb-3"><code>' + escapeHtml(q.code) + '</code></pre>';
        }}

        cardHTML += '<div class="grid grid-cols-1 sm:grid-cols-2 gap-2">';
        q.options.forEach((opt, optIdx) => {{
            const isUser = userChoice === optIdx;
            const isRight = optIdx === q.correct;
            let style = "border-slate-200 bg-white text-slate-700";
            let tag = "";
            if (isRight) {{
                style = "border-emerald-500 bg-emerald-100/70 text-emerald-900 font-bold";
                tag = '<i class="fa-solid fa-check text-emerald-600"></i> (To\'g\'ri)';
            }}
            if (isUser && !isRight) {{
                style = "border-rose-500 bg-rose-100/70 text-rose-900 font-bold";
                tag = '<i class="fa-solid fa-xmark text-rose-600"></i> (Tanlangan)';
            }}
            cardHTML += '<div class="p-2 rounded-lg border text-xs flex items-center justify-between ' + style + '">' +
                '<span><b>' + letters[optIdx] + ')</b> ' + escapeHtml(opt) + '</span>' +
                '<span class="text-[10px]">' + tag + '</span>' +
            '</div>';
        }});
        cardHTML += '</div>';

        card.innerHTML = cardHTML;
        listContainer.appendChild(card);
    }});

    const m = document.getElementById("modalDetail");
    if (m) {{ m.classList.remove("hidden"); m.style.display = "flex"; }}
}}

function closeDetailModal() {{
    const m = document.getElementById("modalDetail");
    if (m) {{ m.classList.add("hidden"); m.style.display = "none"; }}
}}

// 2. TALABA NATIJASINI O'ZGARTIRISH (TAHRIRLASH)
function openEditScoreModal(studentId) {{
    const students = getStoredStudents();
    const st = students.find(s => s.id === studentId);
    if (!st) return;

    document.getElementById("editStudentIndex").value = st.id;
    document.getElementById("editStudentIdVal").value = st.studentId || "-";
    document.getElementById("editStudentFullNameVal").value = st.fullName;
    document.getElementById("editStudentGroupVal").value = st.groupName;
    document.getElementById("editNewScoreVal").value = st.totalScore;
    document.getElementById("editReasonVal").value = "";

    const m = document.getElementById("modalEditScore");
    if (m) {{ m.classList.remove("hidden"); m.style.display = "flex"; }}
}}

function closeEditScoreModal() {{
    const m = document.getElementById("modalEditScore");
    if (m) {{ m.classList.add("hidden"); m.style.display = "none"; }}
}}

function saveScoreEdit(e) {{
    if (e && e.preventDefault) e.preventDefault();
    const studentId = parseInt(document.getElementById("editStudentIndex").value);
    const newFullName = document.getElementById("editStudentFullNameVal").value.trim();
    const newGroup = document.getElementById("editStudentGroupVal").value.trim();
    const newScore = parseInt(document.getElementById("editNewScoreVal").value);
    const reason = document.getElementById("editReasonVal").value.trim();

    if (!newFullName || !newGroup) {{
        alert("F.I.Sh. va Guruh bo'sh bo'lishi mumkin emas!");
        return false;
    }}

    if (isNaN(newScore) || newScore < 0 || newScore > 30 || !reason) {{
        alert("Ball 0 dan 30 gacha bo'lishi va o'zgartirish sababi to'ldirilishi shart!");
        return false;
    }}

    const students = getStoredStudents();
    const st = students.find(s => s.id === studentId);
    if (!st) return false;

    const oldScore = st.totalScore;
    const oldStatus = st.statusText;
    const newStatus = (newScore >= 18) ? "Joriy nazoratdan o‘tdi" : "Joriy nazoratdan o‘tmadi";

    st.fullName = newFullName;
    st.groupName = newGroup;
    st.totalScore = newScore;
    st.correctCount = newScore;
    st.incorrectCount = 30 - newScore;
    st.statusText = newStatus;
    st.isModified = true;

    // Audit jurnaliga yozish
    const auditLogs = getStoredAudit();
    auditLogs.unshift({{
        id: Date.now(),
        studentName: st.fullName + " (ID: " + (st.studentId || "-") + ")",
        oldScore: oldScore,
        newScore: newScore,
        oldStatus: oldStatus,
        newStatus: newStatus,
        reason: reason,
        teacher: "o'qituvchi",
        time: new Date().toLocaleString("uz-UZ")
    }});

    SafeStorage.setItem(STORAGE_KEY_STUDENTS, JSON.stringify(students));
    SafeStorage.setItem(STORAGE_KEY_AUDIT, JSON.stringify(auditLogs));

    closeEditScoreModal();
    renderTeacherTable();
    alert("Talaba ma'lumotlari va balli muvaffaqiyatli saqlandi!");
    return false;
}}

// 3. TALABA NATIJASINI O'CHIRISH (QAYTA TOPSHIRISHGA RUXSAT BERISH)
function deleteStudentResult(studentId) {{
    const students = getStoredStudents();
    const st = students.find(s => s.id === studentId);
    if (!st) return;

    const confirmMsg = "Haqiqatan ham quyidagi talaba natijasini o'chirmoqchimisiz?\\n\\n" +
        "• Talaba ID: " + (st.studentId || "-") + "\\n" +
        "• F.I.Sh.: " + st.fullName + "\\n" +
        "• Guruh: " + st.groupName + "\\n" +
        "• Ball: " + st.totalScore + " / 30 (" + st.statusText + ")\\n\\n" +
        "DIQQAT: Natija o'chirilgach, ushbu talaba testni qaytadan boshidan topshira oladi!";

    if (!confirm(confirmMsg)) {{
        return;
    }}

    // Ro'yxatdan o'chirish
    const updatedStudents = students.filter(s => s.id !== studentId);
    SafeStorage.setItem(STORAGE_KEY_STUDENTS, JSON.stringify(updatedStudents));

    // Audit jurnaliga qayd etish
    const auditLogs = getStoredAudit();
    auditLogs.unshift({{
        id: Date.now(),
        studentName: st.fullName + " (ID: " + (st.studentId || "-") + ", " + st.groupName + ")",
        oldScore: st.totalScore,
        newScore: 0,
        oldStatus: st.statusText,
        newStatus: "NATIJA O'CHIRILDI",
        reason: "O'qituvchi tomonidan natija o'chirildi (qayta topshirishga ruxsat berildi)",
        teacher: "o'qituvchi",
        time: new Date().toLocaleString("uz-UZ")
    }});
    SafeStorage.setItem(STORAGE_KEY_AUDIT, JSON.stringify(auditLogs));

    renderTeacherTable();
    alert("Talaba (" + st.fullName + ") natijasi muvaffaqiyatli o'chirildi! Endi u testni qayta topshirishi mumkin.");
}}

// Barcha natijalarni tozalash
function clearAllResults() {{
    const students = getStoredStudents();
    if (students.length === 0) {{
        alert("Jadval allaqachon bo'sh!");
        return;
    }}

    if (!confirm("DIQQAT! Barcha talabalar natijalarini tozalab tashlamoqchimisiz? Bu amal qaytarilmaydi!")) {{
        return;
    }}

    const checkPrompt = prompt("Tasdiqlash uchun 'TOZALASH' so'zini yozing:");
    if (checkPrompt === "TOZALASH") {{
        SafeStorage.removeItem(STORAGE_KEY_STUDENTS);
        renderTeacherTable();
        alert("Barcha talabalar natijalari muvaffaqiyatli tozalandi!");
    }} else {{
        alert("Tasdiqlash bekor qilindi.");
    }}
}}

function toggleAuditModal() {{
    const modal = document.getElementById("modalAudit");
    if (!modal) return;
    if (modal.classList.contains("hidden") || modal.style.display === "none") {{
        const logs = getStoredAudit();
        const tbody = document.getElementById("auditTableBody");
        tbody.innerHTML = "";
        if (logs.length === 0) {{
            tbody.innerHTML = '<tr><td colspan="6" class="py-8 text-center text-slate-400">Audit jurnali hozircha bo\\'sh.</td></tr>';
        }} else {{
            logs.forEach(l => {{
                const tr = document.createElement("tr");
                tr.innerHTML = 
                    '<td class="py-2.5 px-3 font-semibold text-slate-900">' + escapeHtml(l.studentName) + '</td>' +
                    '<td class="py-2.5 px-3 text-center font-mono text-slate-500">' + l.oldScore + ' / 30</td>' +
                    '<td class="py-2.5 px-3 text-center font-mono font-bold text-blue-600">' + (l.newStatus === "NATIJA O'CHIRILDI" ? '-' : l.newScore + ' / 30') + '</td>' +
                    '<td class="py-2.5 px-3 text-center"><span class="px-2 py-0.5 rounded text-xs font-bold ' + (l.newStatus === "NATIJA O'CHIRILDI" ? 'bg-slate-200 text-slate-700' : (l.newScore >= 18 ? 'bg-emerald-100 text-emerald-800' : 'bg-rose-100 text-rose-800')) + '">' + l.newStatus + '</span></td>' +
                    '<td class="py-2.5 px-3 text-slate-700 italic">' + escapeHtml(l.reason) + '</td>' +
                    '<td class="py-2.5 px-3 text-center text-xs text-slate-500 font-mono">' + l.time + '</td>';
                tbody.appendChild(tr);
            }});
        }}
        modal.classList.remove("hidden");
        modal.style.display = "flex";
    }} else {{
        modal.classList.add("hidden");
        modal.style.display = "none";
    }}
}}

function exportToExcel() {{
    const students = getStoredStudents();
    if (students.length === 0) {{
        alert("Eksport qilish uchun talabalar natijalari mavjud emas!");
        return;
    }}

    let csv = "\\uFEFF"; // UTF-8 BOM
    csv += "№;Talaba ID;F.I.Sh.;Yo'nalish;Kurs;Guruh;To'g'ri;Noto'g'ri;To'plangan ball;Natija;Sana va vaqt;Sahifadan chiqishlar\\n";

    students.forEach((s, idx) => {{
        csv += '"' + (idx + 1) + '";"' + (s.studentId || "") + '";"' + s.fullName + '";"' + s.direction + '";"' + s.course + '-kurs";"' + s.groupName + '";"' + s.correctCount + '";"' + s.incorrectCount + '";"' + s.totalScore + ' / 30";"' + s.statusText + '";"' + (s.finishedAt || s.startedAt) + '";"' + (s.tabSwitchCount || 0) + ' marta"\\n';
    }});

    const blob = new Blob([csv], {{ type: "text/csv;charset=utf-8;" }});
    const link = document.createElement("a");
    const url = URL.createObjectURL(blob);
    link.setAttribute("href", url);
    link.setAttribute("download", "Joriy_nazorat_natijalari_" + new Date().toISOString().slice(0, 10) + ".csv");
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
}}

function getStoredStudents() {{
    try {{
        return JSON.parse(SafeStorage.getItem(STORAGE_KEY_STUDENTS)) || [];
    }} catch(e) {{ return []; }}
}}

function saveStudentResult(res) {{
    const list = getStoredStudents();
    const existingIdx = list.findIndex(s => 
        (res.studentId && s.studentId && s.studentId === res.studentId) ||
        (s.fullName.toLowerCase() === res.fullName.toLowerCase() && 
         String(s.groupName).trim() === String(res.groupName).trim())
    );
    if (existingIdx !== -1) {{
        list[existingIdx] = res;
    }} else {{
        list.unshift(res);
    }}
    SafeStorage.setItem(STORAGE_KEY_STUDENTS, JSON.stringify(list));
}}

function getStoredAudit() {{
    try {{
        return JSON.parse(SafeStorage.getItem(STORAGE_KEY_AUDIT)) || [];
    }} catch(e) {{ return []; }}
}}

function escapeHtml(text) {{
    if (!text) return "";
    const div = document.createElement("div");
    div.textContent = text;
    return div.innerHTML;
}}

function startTeacherAutoRefresh() {{
    if (teacherAutoRefreshTimer) return;
    teacherAutoRefreshTimer = setInterval(() => {{
        const dash = document.getElementById("teacherDashboard");
        if (dash && !dash.classList.contains("hidden") && dash.style.display !== "none") {{
            renderTeacherTable();
        }}
    }}, 2500);
}}

function stopTeacherAutoRefresh() {{
    clearInterval(teacherAutoRefreshTimer);
    teacherAutoRefreshTimer = null;
}}
"""

# Write app_standalone.js
js_file_path = os.path.join(base_dir, "app_standalone.js")
with open(js_file_path, "w", encoding="utf-8") as f:
    f.write(app_js_code)
print(f"app_standalone.js written successfully ({len(app_js_code)} bytes).")

# =========================================================================
# 2. WRITE generate_standalone.py and python_nazorat.html
# =========================================================================

# The standalone HTML embeds app_standalone.js directly inside <script>
full_html = html_content.replace(
    '<script src="app_standalone.js"></script>',
    f'<script>\n{app_js_code}\n</script>'
)

html_file_path = os.path.join(base_dir, "python_nazorat.html")
with open(html_file_path, "w", encoding="utf-8") as f:
    f.write(full_html)
print(f"python_nazorat.html written successfully ({len(full_html)} bytes).")

# Copy to Desktop
desktop_path = "C:/Users/Asus/Desktop/python_nazorat.html"
try:
    shutil.copyfile(html_file_path, desktop_path)
    print(f"Desktop copy created: {desktop_path}")
except Exception as e:
    print(f"Could not copy to Desktop: {e}")

# Also update generate_standalone.py so it can be re-run whenever needed
gen_file_path = os.path.join(base_dir, "generate_standalone.py")
gen_script_content = f"""# -*- coding: utf-8 -*-
import os
import shutil
import json
import students_roster as sr
import questions_data as qd

base_dir = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(base_dir, "app_standalone.js"), "r", encoding="utf-8") as f:
    app_js_code = f.read()

questions_json = json.dumps(qd.QUESTIONS, ensure_ascii=False)
students_roster_json = json.dumps(sr.STUDENTS_ROSTER, ensure_ascii=False)

html_template = f\"\"\"<!DOCTYPE html>
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
    <!-- Navbar -->
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

    <main class="flex-1 max-w-7xl w-full mx-auto px-4 sm:px-6 py-6">
        <!-- Register Section -->
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

                <div class="lg:col-span-7 bg-white p-6 sm:p-8 rounded-3xl border border-slate-200 shadow-lg">
                    <div class="border-b border-slate-100 pb-3 mb-5">
                        <h2 class="text-lg sm:text-xl font-bold text-slate-900 flex items-center gap-2">
                            <i class="fa-solid fa-id-card text-blue-600"></i>
                            <span>Talaba Identifikatsiyasi</span>
                        </h2>
                        <p class="text-xs text-slate-500 mt-0.5">HEMIS ID orqali tizimga kiring.</p>
                    </div>

                    <form id="studentRegisterForm" onsubmit="return handleRegisterSubmit(event)" class="space-y-4">
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

                        <div>
                            <label for="regFullName" class="block text-xs font-bold text-slate-700 uppercase tracking-wider mb-1">
                                Familiya, Ism va Sharifingiz <span class="text-red-500">*</span>
                            </label>
                            <input type="text" id="regFullName" required placeholder="Talaba ID kiritilganda avtomatik to'ldiriladi"
                                class="w-full px-4 py-2.5 bg-white border border-slate-300 rounded-xl text-slate-900 text-sm focus:ring-2 focus:ring-blue-500 outline-none transition-all">
                        </div>

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

                        <div>
                            <label for="regDirection" class="block text-xs font-bold text-slate-700 uppercase tracking-wider mb-1">
                                Ta'lim Yo'nalishi <span class="text-red-500">*</span>
                            </label>
                            <input type="text" id="regDirection" required value="Telekommunikatsiya texnologiyalari (ATT)"
                                class="w-full px-4 py-2.5 bg-white border border-slate-300 rounded-xl text-slate-900 text-sm focus:ring-2 focus:ring-blue-500 outline-none transition-all">
                        </div>

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

        <!-- Ready Section -->
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

                <div class="p-4 rounded-2xl bg-amber-50 border border-amber-200 text-left mb-6 text-xs text-amber-900 space-y-1.5">
                    <div class="font-bold flex items-center gap-2 text-amber-800">
                        <i class="fa-solid fa-triangle-exclamation"></i>
                        <span>Muhim Eslatma:</span>
                    </div>
                    <p>• <strong>Vaqt hisobi:</strong> Quyidagi "Testni Ishlashni Boshlash" tugmasini bosishingiz bilanoq 60 daqiqalik vaqt ortga sanay boshlaydi.</p>
                    <p>• <strong>Erkin chiqish:</strong> Agar hozir testni boshlamay chiqib ketsangiz, istalgan vaqtda qayta kirishingiz mumkin.</p>
                    <p>• <strong>Natija va bloklash:</strong> Testni ishlab, yakunlab natija olganingizdan keyingina tizimga qayta kirish qat'iyan taqiqlanadi!</p>
                </div>

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

        <!-- Exam Section -->
        <section id="sectionExam" class="max-w-6xl mx-auto hidden" style="display: none;">
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

                <div class="flex items-center gap-3 bg-slate-50 px-4 py-2 rounded-xl border border-slate-200">
                    <div class="w-8 h-8 rounded-lg bg-amber-100 text-amber-600 flex items-center justify-center text-sm" id="timerIcon">
                        <i class="fa-solid fa-stopwatch animate-pulse"></i>
                    </div>
                    <div>
                        <div class="text-[10px] font-bold uppercase tracking-wider text-slate-400">Qolgan vaqt</div>
                        <div class="text-xl sm:text-2xl font-mono font-extrabold text-slate-900" id="timerDisplay">60:00</div>
                    </div>
                </div>

                <button type="button" onclick="confirmFinishModalOpen()"
                    class="px-5 py-2.5 rounded-xl bg-emerald-600 hover:bg-emerald-700 text-white font-semibold text-xs sm:text-sm shadow-md shadow-emerald-600/20 flex items-center gap-2 transition-all">
                    <i class="fa-solid fa-check-double"></i>
                    <span>Testni Yakunlash</span>
                </button>
            </div>

            <div class="grid grid-cols-1 lg:grid-cols-12 gap-6 items-start">
                <div class="lg:col-span-8">
                    <div class="bg-white border border-slate-200 rounded-3xl p-5 sm:p-7 shadow-sm">
                        <div class="flex items-center justify-between border-b border-slate-100 pb-3 mb-4">
                            <div class="flex items-center gap-2">
                                <span class="w-8 h-8 rounded-lg bg-blue-600 text-white flex items-center justify-center font-bold text-sm" id="qCurrentNumber">1</span>
                                <span class="text-xs font-semibold px-2.5 py-0.5 rounded-full bg-slate-100 text-slate-700" id="qTopicBadge">Mavzu</span>
                            </div>
                            <span class="text-xs px-2.5 py-0.5 rounded-full font-medium" id="qDifficultyBadge">Daraja</span>
                        </div>

                        <div class="text-slate-900 text-base sm:text-lg font-medium leading-relaxed mb-4" id="qQuestionText">
                            Savol yuklanmoqda...
                        </div>

                        <div id="qCodeBlock" class="mb-5 rounded-2xl bg-slate-900 text-slate-100 p-4 font-mono text-xs sm:text-sm overflow-x-auto border border-slate-800 shadow-inner hidden" style="display: none;">
                            <div class="flex items-center justify-between text-[11px] text-slate-400 border-b border-slate-800 pb-2 mb-2 select-none">
                                <span class="flex items-center gap-1.5"><i class="fa-brands fa-python text-amber-400"></i> Python</span>
                                <span>Kod parchasi</span>
                            </div>
                            <pre class="whitespace-pre"><code id="qCodeContent"></code></pre>
                        </div>

                        <div class="space-y-3" id="qOptionsList"></div>

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

                        <div class="grid grid-cols-5 sm:grid-cols-6 gap-2 mb-4" id="questionsMapGrid"></div>

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

        <!-- Result Section -->
        <section id="sectionResult" class="max-w-2xl mx-auto py-4 hidden" style="display: none;">
            <div class="bg-white border border-slate-200 rounded-3xl p-6 sm:p-10 shadow-xl text-center relative overflow-hidden">
                <div id="resultColorBar" class="absolute top-0 left-0 right-0 h-3 bg-emerald-500"></div>

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

        <!-- Teacher Section -->
        <section id="sectionTeacher" class="space-y-6 hidden" style="display: none;">
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

            <div id="teacherDashboard" class="space-y-6 hidden" style="display: none;">
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
                            <tbody id="teacherTableBody" class="divide-y divide-slate-100"></tbody>
                        </table>
                    </div>
                </div>
            </div>
        </section>
    </main>

    <!-- Modals -->
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
            <div class="p-6 overflow-y-auto space-y-4 flex-1 text-xs sm:text-sm" id="detailModalQuestionsList"></div>
            <div class="p-4 border-t border-slate-100 flex justify-end">
                <button onclick="closeDetailModal()" class="px-5 py-2 rounded-xl bg-slate-100 hover:bg-slate-200 text-slate-700 font-semibold text-xs">
                    Yopish
                </button>
            </div>
        </div>
    </div>

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
                    <tbody id="auditTableBody" class="divide-y divide-slate-100"></tbody>
                </table>
            </div>
            <div class="p-4 border-t border-slate-100 flex justify-end">
                <button onclick="toggleAuditModal()" class="px-5 py-2 rounded-xl bg-slate-100 hover:bg-slate-200 text-slate-700 font-semibold text-xs">
                    Yopish
                </button>
            </div>
        </div>
    </div>

    <!-- Skript bloki: Mustaqil ishlash uchun to'liq kod ichida -->
    <script>
        const ALL_QUESTIONS = {questions_json};
{app_js_code}
    </script>
</body>
</html>
\"\"\"

output_path = os.path.join(base_dir, "python_nazorat.html")
with open(output_path, "w", encoding="utf-8") as f:
    f.write(html_template)
print(f"python_nazorat.html successfully compiled: {{output_path}} ({{len(html_template)}} bytes)")

desktop_path = "C:/Users/Asus/Desktop/python_nazorat.html"
try:
    shutil.copyfile(output_path, desktop_path)
    print(f"Desktop copy updated: {{desktop_path}}")
except Exception as e:
    print(f"Desktop copy error: {{e}}")
"""

with open(gen_file_path, "w", encoding="utf-8") as f:
    f.write(gen_script_content)
print("generate_standalone.py created.")
