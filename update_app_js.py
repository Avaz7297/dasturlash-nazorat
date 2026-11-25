# -*- coding: utf-8 -*-
import os
import re
import json
import students_roster as sr

base_dir = os.path.dirname(os.path.abspath(__file__))

# =========================================================================
# 1. UPDATE app_standalone.js
# =========================================================================
js_path = os.path.join(base_dir, "app_standalone.js")
with open(js_path, "r", encoding="utf-8") as f:
    js = f.read()

# Replace or ensure STUDENTS_ROSTER is at the top
roster_block = f"""// Rasmiy 130 ta talaba va sinov talabasi
const STUDENTS_ROSTER = {json.dumps(sr.STUDENTS_ROSTER, ensure_ascii=False)};
const TEST_STUDENT_ID = '000000000000';
"""

if "const STUDENTS_ROSTER" in js:
    js = re.sub(r'// Rasmiy.*?\nconst STUDENTS_ROSTER = \[.*?\];\nconst TEST_STUDENT_ID = [\'"][0-9]+[\'"];\n?', roster_block, js, flags=re.DOTALL)
    if "const STUDENTS_ROSTER" not in js:
        js = roster_block + "\n" + js
else:
    js = roster_block + "\n" + js

# Replace startExamHandler with 12-digit student ID check and strict 1-attempt check
new_start_exam_handler = """// TALABA RO'YXATDAN O'TISHI VA TESTNI BOSHLASH
function startExamHandler(e) {
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
    if (!studentId || !fullName || !direction || !course || !groupName) {
        alert("Iltimos, barcha maydonlarni (Talaba ID, F.I.Sh., Guruh) to'ldiring!");
        return false;
    }

    // 2. Talaba ID 12 ta raqam bo'lishi shart!
    if (!/^\\d{12}$/.test(studentId)) {
        alert("Xatolik: Talaba ID 12 ta raqamdan iborat bo'lishi kerak! (Masalan: 315261102911)");
        if (idInput) idInput.focus();
        return false;
    }

    // 3. Rasmiy ro'yxatda mavjudligini tekshirish (faqat test rejimiga ruxsat)
    const isTestMode = (studentId === TEST_STUDENT_ID);
    if (!isTestMode) {
        const foundInRoster = STUDENTS_ROSTER.find(s => s.id === studentId);
        if (!foundInRoster) {
            alert("Xatolik: Kiritilgan Talaba ID (" + studentId + ") rasmiy talabalar ro'yxatida topilmadi! Faqat ro'yxatga kiritilgan talabalar test topshira oladi.");
            if (idInput) idInput.focus();
            return false;
        }

        // 4. BIR MARTA TOPSHIRISH QAT'IY TALABI (Talaba ID orqali)
        const existingStudents = getStoredStudents();
        const alreadyTested = existingStudents.find(s => 
            s.studentId === studentId ||
            (s.fullName.toLowerCase() === fullName.toLowerCase() && String(s.groupName).trim() === groupName)
        );

        if (alreadyTested) {
            alert("Hurmatli " + alreadyTested.fullName + " (ID: " + studentId + ")!\\nSiz allaqachon ushbu joriy nazorat testini topshirgansiz.\\n\\nTo'plangan ball: " + alreadyTested.totalScore + " / 30 (" + alreadyTested.statusText + ").\\nTopshirilgan vaqt: " + (alreadyTested.finishedAt || alreadyTested.startedAt) + "\\n\\nNizomga muvofiq, har bir talaba testni faqat 1 MARTA topshirishi mumkin. Qayta kirish va qayta ishlash qat'iyan taqiqlanadi!");
            showResultPage(alreadyTested);
            return false;
        }
    }

    currentStudent = {
        studentId: studentId,
        fullName: fullName,
        direction: direction,
        course: parseInt(course) || 1,
        groupName: groupName,
        subject: "Dasturlash",
        startedAt: new Date().toLocaleString("uz-UZ"),
        tabSwitchCount: 0
    };

    // 30 ta savolni tanlash
    currentQuestions = generateRandomExamQuestions();
    currentAnswers = {};
    currentQuestionIdx = 0;
    remainingSeconds = 3600;
    examStartTimeMs = Date.now();
    tabSwitchCount = 0;
    isExamActive = true;

    // UI ni test oynasiga o'tkazish
    const nameEl = document.getElementById("examStudentName");
    const grpEl = document.getElementById("examStudentGroup");
    const crsEl = document.getElementById("examStudentCourse");
    if (nameEl) nameEl.textContent = currentStudent.fullName;
    if (grpEl) grpEl.textContent = currentStudent.groupName;
    if (crsEl) crsEl.textContent = currentStudent.course + "-kurs";

    switchView("exam");
    saveActiveExamState();

    renderQuestionsMap();
    loadQuestion(0);
    startTimer();
    return false;
}"""

# Replace startExamHandler function
js = re.sub(r'// TALABA RO\'YXATDAN O\'TISHI VA TESTNI BOSHLASH\nfunction startExamHandler\(e\) \{.*?\n    return false;\n\}', new_start_exam_handler, js, flags=re.DOTALL)

# Ensure completedResult has studentId
old_completed_result = """    const completedResult = {
        id: Date.now(),
        fullName: currentStudent.fullName,"""

new_completed_result = """    const completedResult = {
        id: Date.now(),
        studentId: currentStudent.studentId || "",
        fullName: currentStudent.fullName,"""

if old_completed_result in js:
    js = js.replace(old_completed_result, new_completed_result)

# Ensure showResultPage updates resStudentId
old_show_result = """    document.getElementById("resStudentName").textContent = result.fullName;"""
new_show_result = """    const idEl = document.getElementById("resStudentId");
    if (idEl) idEl.textContent = result.studentId || "-";
    document.getElementById("resStudentName").textContent = result.fullName;"""

if old_show_result in js and "resStudentId" not in js[js.find("function showResultPage"):js.find("function showResultPage")+600]:
    js = js.replace(old_show_result, new_show_result)

# Update renderTeacherTable
# 1. Update statTotalStudents: total + " / 130 (" + Math.round(total / 130 * 100) + "%)"
js = re.sub(
    r'document\.getElementById\("statTotalStudents"\)\.textContent = total;',
    'document.getElementById("statTotalStudents").textContent = total + " / 130 (" + (total > 0 ? Math.round(total / 130 * 100) : 0) + "%)";',
    js
)

# 2. Update search filter in renderTeacherTable to match studentId
old_search_filter = """        const matchSearch = !searchQuery || 
            s.fullName.toLowerCase().includes(searchQuery) ||
            String(s.groupName).toLowerCase().includes(searchQuery) ||
            s.direction.toLowerCase().includes(searchQuery);"""

new_search_filter = """        const matchSearch = !searchQuery || 
            (s.studentId && s.studentId.includes(searchQuery)) ||
            s.fullName.toLowerCase().includes(searchQuery) ||
            String(s.groupName).toLowerCase().includes(searchQuery) ||
            (s.direction && s.direction.toLowerCase().includes(searchQuery));"""

if old_search_filter in js:
    js = js.replace(old_search_filter, new_search_filter)

# 3. Update table row generation in renderTeacherTable to include Talaba ID column
old_tr_start = """        tr.innerHTML = 
            '<td class="py-3 px-3 text-center font-bold text-slate-400">' + (idx + 1) + '</td>' +
            '<td class="py-3 px-3 font-semibold text-slate-900">' +"""

new_tr_start = """        tr.innerHTML = 
            '<td class="py-3 px-3 text-center font-bold text-slate-400">' + (idx + 1) + '</td>' +
            '<td class="py-3 px-3 text-center font-mono font-bold text-slate-900">' +
                '<span class="px-2 py-0.5 rounded bg-slate-100 text-slate-800 text-xs border border-slate-200">' + escapeHtml(st.studentId || "-") + '</span>' +
            '</td>' +
            '<td class="py-3 px-3 font-semibold text-slate-900">' +"""

if old_tr_start in js:
    js = js.replace(old_tr_start, new_tr_start)

# Update saveStudentResult to check studentId
old_save_student = """    const existingIdx = list.findIndex(s => 
        s.fullName.toLowerCase() === res.fullName.toLowerCase() && 
        String(s.groupName).trim() === String(res.groupName).trim()
    );"""

new_save_student = """    const existingIdx = list.findIndex(s => 
        (res.studentId && s.studentId && s.studentId === res.studentId) ||
        (s.fullName.toLowerCase() === res.fullName.toLowerCase() && 
         String(s.groupName).trim() === String(res.groupName).trim())
    );"""

if old_save_student in js:
    js = js.replace(old_save_student, new_save_student)

# Update exportToExcel to include Talaba ID
old_csv_header = """    csv += "№;F.I.Sh.;Yo'nalish;Kurs;Guruh;To'g'ri;Noto'g'ri;To'plangan ball;Natija;Sana va vaqt;Sahifadan chiqishlar\\n";"""
new_csv_header = """    csv += "№;Talaba ID;F.I.Sh.;Yo'nalish;Kurs;Guruh;To'g'ri;Noto'g'ri;To'plangan ball;Natija;Sana va vaqt;Sahifadan chiqishlar\\n";"""
if old_csv_header in js:
    js = js.replace(old_csv_header, new_csv_header)

old_csv_row = """    students.forEach((s, idx) => {
        csv += '\"' + (idx + 1) + '\";\"' + s.fullName + '\";\"' + s.direction + '\";\"' + s.course + '-kurs\";\"' + s.groupName + '\";\"' + s.correctCount + '\";\"' + s.incorrectCount + '\";\"' + s.totalScore + ' / 30\";\"' + s.statusText + '\";\"' + (s.finishedAt || s.startedAt) + '\";\"' + (s.tabSwitchCount || 0) + ' marta\"\\n';
    });"""

new_csv_row = """    students.forEach((s, idx) => {
        csv += '\"' + (idx + 1) + '\";\"' + (s.studentId || "") + '\";\"' + s.fullName + '\";\"' + s.direction + '\";\"' + s.course + '-kurs\";\"' + s.groupName + '\";\"' + s.correctCount + '\";\"' + s.incorrectCount + '\";\"' + s.totalScore + ' / 30\";\"' + s.statusText + '\";\"' + (s.finishedAt || s.startedAt) + '\";\"' + (s.tabSwitchCount || 0) + ' marta\"\\n';
    });"""

if old_csv_row in js:
    js = js.replace(old_csv_row, new_csv_row)

with open(js_path, "w", encoding="utf-8") as f:
    f.write(js)

print("app_standalone.js successfully updated.")
