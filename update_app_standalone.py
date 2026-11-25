# -*- coding: utf-8 -*-
import re

with open("app_standalone.js", "r", encoding="utf-8") as f:
    content = f.read()

# Replace localStorage with SafeStorage (except inside SafeStorage itself)
# We find all localStorage outside lines 1-40
lines = content.split("\n")
new_lines = []
for i, line in enumerate(lines):
    if i > 40:
        line = line.replace("localStorage.", "SafeStorage.")
        line = line.replace("sessionStorage.", "SafeSession.")
    new_lines.append(line)

content = "\n".join(new_lines)

# Now check submitExamNow and showResultPage
sharing_functions = """
// =========================================================================
// TALABA NATIJASINI O'QITUVCHIGA YUBORISH VA IMPORT QILISH (CROSS-DEVICE)
// =========================================================================

function generateResultPackage(res) {
    if (!res) return "";
    const p = {
        n: res.fullName,
        d: res.direction,
        c: res.course,
        g: String(res.groupName),
        s: res.totalScore,
        st: res.statusText,
        t: res.finishedAt || res.startedAt,
        sw: res.tabSwitchCount || 0,
        id: res.id || Date.now()
    };
    const jsonStr = JSON.stringify(p);
    const b64 = btoa(encodeURIComponent(jsonStr).replace(/%([0-9A-F]{2})/g, function(match, p1) {
        return String.fromCharCode('0x' + p1);
    }));
    const chk = generateChecksum(b64 + "PYTHON_EXAM_SALT_2026");
    return "RESULT#" + b64 + "#" + chk;
}

function parseResultPackage(rawInput) {
    if (!rawInput) return null;
    const match = rawInput.match(/RESULT#([A-Za-z0-9+/=]+)#([a-f0-9]{8})/);
    if (!match) return null;
    const b64 = match[1];
    const chk = match[2];
    const expected = generateChecksum(b64 + "PYTHON_EXAM_SALT_2026");
    if (chk !== expected) {
        throw new Error("Xavfsizlik xatoligi: Ushbu natija kodi buzilgan yoki o'zgartirilgan!");
    }
    const jsonStr = decodeURIComponent(Array.prototype.map.call(atob(b64), function(c) {
        return '%' + ('00' + c.charCodeAt(0).toString(16)).slice(-2);
    }).join(''));
    return JSON.parse(jsonStr);
}

function sendResultViaTelegram() {
    const res = currentResultObject;
    if (!res) {
        alert("Natija topilmadi!");
        return;
    }
    const code = generateResultPackage(res);
    const msg = 
`Assalomu alaykum ustoz!\\n` +
`Python dasturlash fanidan joriy nazorat natijam:\\n\\n` +
`👤 Talaba: ${res.fullName}\\n` +
`📚 Yo'nalish: ${res.direction} (${res.course}-kurs)\\n` +
`👥 Guruh: ${res.groupName}\\n` +
`🎯 To'plangan ball: ${res.totalScore} / 30\\n` +
`📊 Natija: ${res.statusText}\\n` +
`⏱ Sana: ${res.finishedAt || res.startedAt}\\n\\n` +
`🔐 Maxsus natija kodi (O'qituvchi paneli uchun):\\n${code}`;

    const tgUrl = "https://t.me/share/url?url=" + encodeURIComponent(msg);
    window.open(tgUrl, "_blank");
}

function copyResultCode() {
    const res = currentResultObject;
    if (!res) return;
    const code = generateResultPackage(res);
    if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(code).then(() => {
            const btn = document.getElementById("btnCopyText");
            if (btn) btn.textContent = "Nusxalandi! (Ustozga jo'nating)";
            alert("Natija kodi nusxalandi! Endi uni o'qituvchingizga (Telegram orqali) jo'nating.");
        }).catch(() => {
            prompt("Natija kodini nusxalab oling:", code);
        });
    } else {
        prompt("Natija kodini nusxalab oling:", code);
    }
}

function downloadResultJson() {
    const res = currentResultObject;
    if (!res) return;
    const code = generateResultPackage(res);
    const exportData = {
        student: res,
        verificationCode: code,
        exportedAt: new Date().toISOString()
    };
    const blob = new Blob([JSON.stringify(exportData, null, 2)], { type: "application/json" });
    const link = document.createElement("a");
    link.href = URL.createObjectURL(blob);
    link.download = `Natija_${res.groupName}_${res.fullName.replace(/\\s+/g, '_')}.json`;
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
}

function openImportResultModal() {
    const modal = document.getElementById("modalImportResult");
    if (modal) modal.classList.remove("hidden");
    const input = document.getElementById("importCodeInput");
    if (input) input.value = "";
    const file = document.getElementById("importFileInput");
    if (file) file.value = "";
}

function closeImportResultModal() {
    const modal = document.getElementById("modalImportResult");
    if (modal) modal.classList.add("hidden");
}

function handleImportSubmit(e) {
    if (e && e.preventDefault) e.preventDefault();
    const input = document.getElementById("importCodeInput");
    const rawVal = input ? input.value.trim() : "";
    if (!rawVal) {
        alert("Iltimos, talaba yuborgan xabar matnini yoki natija kodini kiriting!");
        return false;
    }

    try {
        const payload = parseResultPackage(rawVal);
        if (!payload) {
            alert("Xatolik: Matn ichida maxsus natija kodi (RESULT#...) topilmadi!");
            return false;
        }

        const studentRes = {
            id: payload.id || Date.now(),
            fullName: payload.n,
            direction: payload.d,
            course: payload.c,
            groupName: payload.g,
            subject: "Dasturlash",
            startedAt: payload.t,
            finishedAt: payload.t,
            totalScore: payload.s,
            maxScore: 30,
            correctCount: payload.s,
            incorrectCount: 30 - payload.s,
            statusText: payload.st,
            tabSwitchCount: payload.sw || 0,
            questions: [],
            answers: {},
            isModified: false,
            resultCode: rawVal
        };

        saveStudentResult(studentRes);
        renderTeacherTable();
        closeImportResultModal();
        alert(`Muvaffaqiyatli qo'shildi!\\nTalaba: ${studentRes.fullName}\\nGuruh: ${studentRes.groupName}\\nBall: ${studentRes.totalScore} / 30`);
    } catch(err) {
        alert("Xatolik: " + err.message);
    }
    return false;
}

function handleImportFile(e) {
    const file = e.target.files[0];
    if (!file) return;

    const reader = new FileReader();
    reader.onload = function(evt) {
        try {
            const data = JSON.parse(evt.target.result);
            let payload = null;
            if (data.verificationCode) {
                payload = parseResultPackage(data.verificationCode);
            } else if (data.fullName && data.groupName) {
                payload = {
                    n: data.fullName,
                    d: data.direction,
                    c: data.course,
                    g: data.groupName,
                    s: data.totalScore,
                    st: data.statusText,
                    t: data.finishedAt || data.startedAt,
                    sw: data.tabSwitchCount || 0,
                    id: data.id || Date.now()
                };
            }

            if (!payload) {
                alert("Xatolik: JSON faylda to'g'ri natija ma'lumotlari topilmadi!");
                return;
            }

            const studentRes = {
                id: payload.id || Date.now(),
                fullName: payload.n,
                direction: payload.d,
                course: payload.c,
                groupName: payload.g,
                subject: "Dasturlash",
                startedAt: payload.t,
                finishedAt: payload.t,
                totalScore: payload.s,
                maxScore: 30,
                correctCount: payload.s,
                incorrectCount: 30 - payload.s,
                statusText: payload.st,
                tabSwitchCount: payload.sw || 0,
                questions: [],
                answers: {},
                isModified: false
            };

            saveStudentResult(studentRes);
            renderTeacherTable();
            closeImportResultModal();
            alert(`Fayl orqali muvaffaqiyatli qo'shildi!\\nTalaba: ${studentRes.fullName}\\nGuruh: ${studentRes.groupName}\\nBall: ${studentRes.totalScore} / 30`);
        } catch(err) {
            alert("Faylni o'qishda xatolik: " + err.message);
        }
    };
    reader.readAsText(file);
}
"""

if "function sendResultViaTelegram" not in content:
    content += "\n" + sharing_functions

# Update showResultPage to store currentResultObject and display resultCodeDisplay
old_show_result = """function showResultPage(result) {
    switchView("result");
    try {
        SafeStorage.setItem(STORAGE_KEY_LAST_RESULT, JSON.stringify(result));
    } catch(e) {}"""

new_show_result = """function showResultPage(result) {
    currentResultObject = result;
    switchView("result");
    try {
        SafeStorage.setItem(STORAGE_KEY_LAST_RESULT, JSON.stringify(result));
    } catch(e) {}

    const code = generateResultPackage(result);
    const codeDisplay = document.getElementById("resultCodeDisplay");
    if (codeDisplay) codeDisplay.value = code;"""

content = content.replace(old_show_result, new_show_result)

# Update saveStudentResult to prevent duplicates
old_save_student = """function saveStudentResult(res) {
    const list = getStoredStudents();
    list.unshift(res);
    SafeStorage.setItem(STORAGE_KEY_STUDENTS, JSON.stringify(list));
}"""

new_save_student = """function saveStudentResult(res) {
    const list = getStoredStudents();
    const existingIdx = list.findIndex(s => 
        s.fullName.toLowerCase() === res.fullName.toLowerCase() && 
        String(s.groupName).trim() === String(res.groupName).trim()
    );
    if (existingIdx !== -1) {
        list[existingIdx] = res;
    } else {
        list.unshift(res);
    }
    SafeStorage.setItem(STORAGE_KEY_STUDENTS, JSON.stringify(list));
}"""

content = content.replace(old_save_student, new_save_student)

with open("app_standalone.js", "w", encoding="utf-8") as f:
    f.write(content)

print("app_standalone.js muvaffaqiyatli yangilandi!")
