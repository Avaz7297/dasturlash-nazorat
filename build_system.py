# -*- coding: utf-8 -*-
import os
import json
import students_roster as sr
import questions_data as qd

base_dir = os.path.dirname(os.path.abspath(__file__))

# 1. Update app_standalone.js
js_path = os.path.join(base_dir, "app_standalone.js")
with open(js_path, "r", encoding="utf-8") as f:
    js_code = f.read()

# Embed STUDENTS_ROSTER at the top if not already present
roster_js = f"// Rasmiy 130 ta talaba va sinov talabasi\nconst STUDENTS_ROSTER = {json.dumps(sr.STUDENTS_ROSTER, ensure_ascii=False)};\nconst TEST_STUDENT_ID = '000000000000';\n"

# Replace or insert STUDENTS_ROSTER
if "const STUDENTS_ROSTER" not in js_code:
    # Insert before SAMPLE_RULES
    js_code = roster_js + "\n" + js_code
else:
    # Replace existing
    import re
    js_code = re.sub(r'const STUDENTS_ROSTER = \[.*?\];\nconst TEST_STUDENT_ID = [\'"][0-9]+[\'"];\n?', roster_js, js_code, flags=re.DOTALL)

# Add helper functions: handleStudentIdInput and setTeacherDemoMode
helpers_js = """
// Talaba ID kiritilganda avtomatik ro'yxatdan qidirish va to'ldirish
function handleStudentIdInput(input) {
    if (!input) return;
    input.value = input.value.replace(/\\D/g, '').slice(0, 12);
    const idVal = input.value;
    const statusEl = document.getElementById("idLookupStatus");
    const nameEl = document.getElementById("regFullName");
    const groupEl = document.getElementById("regGroup");
    const dirEl = document.getElementById("regDirection");
    const crsEl = document.getElementById("regCourse");

    if (idVal.length < 12) {
        if (statusEl) {
            statusEl.innerHTML = '<span class="text-slate-500">12 xonali HEMIS ID kiriting (' + idVal.length + '/12)</span>';
        }
        return;
    }

    if (idVal === TEST_STUDENT_ID) {
        if (nameEl) nameEl.value = "O'QITUVCHI SINOV TALABASI (TEST REJIMI)";
        if (groupEl) groupEl.value = "SINOV (TEST)";
        if (dirEl) dirEl.value = "Telekommunikatsiya texnologiyalari (ATT)";
        if (crsEl) crsEl.value = "1";
        if (statusEl) {
            statusEl.innerHTML = '<span class="text-amber-700 font-bold bg-amber-50 px-2 py-0.5 rounded border border-amber-200">🧪 O\\'qituvchi sinov rejimi faol (Cheklovlarsiz)</span>';
        }
        return;
    }

    const found = STUDENTS_ROSTER.find(s => s.id === idVal);
    if (found) {
        if (nameEl) nameEl.value = found.name;
        if (groupEl) groupEl.value = found.group;
        if (dirEl) dirEl.value = "Telekommunikatsiya texnologiyalari (ATT)";
        if (crsEl) crsEl.value = "1";

        // Tekshirish: Talaba avval test topshirganmi?
        const existingList = getStoredStudents();
        const alreadyTested = existingList.find(s => s.studentId === idVal);
        if (alreadyTested) {
            if (statusEl) {
                statusEl.innerHTML = '<span class="text-rose-700 font-bold bg-rose-50 px-2 py-0.5 rounded border border-rose-200">⚠️ Ushbu talaba allaqachon test topshirgan (' + alreadyTested.totalScore + ' ball)! Qayta topshirish taqiqlanadi.</span>';
            }
        } else {
            if (statusEl) {
                statusEl.innerHTML = '<span class="text-emerald-700 font-bold bg-emerald-50 px-2 py-0.5 rounded border border-emerald-200">✅ Tasdiqlandi: ' + found.name + ' (' + found.group + ')</span>';
            }
        }
    } else {
        if (statusEl) {
            statusEl.innerHTML = '<span class="text-rose-700 font-bold bg-rose-50 px-2 py-0.5 rounded border border-rose-200">❌ Ushbu ID rasmiy talabalar ro\\'yxatida topilmadi!</span>';
        }
    }
}

// O'qituvchi sinov rejimini avtomatik faollashtirish
function setTeacherDemoMode() {
    const idInput = document.getElementById("regStudentId");
    if (idInput) {
        idInput.value = TEST_STUDENT_ID;
        handleStudentIdInput(idInput);
    }
}
"""

if "function handleStudentIdInput" not in js_code:
    # Insert after generateChecksum
    pos = js_code.find("function generateChecksum")
    if pos != -1:
        end_pos = js_code.find("}", pos)
        end_pos = js_code.find("}", end_pos + 1) # inner and outer
        js_code = js_code[:end_pos+1] + "\n" + helpers_js + "\n" + js_code[end_pos+1:]
    else:
        js_code += "\n" + helpers_js

with open(js_path, "w", encoding="utf-8") as f:
    f.write(js_code)

print("Updated app_standalone.js successfully.")
