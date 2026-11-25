# -*- coding: utf-8 -*-
import os

base_dir = r"C:\Users\Asus\.gemini\antigravity\scratch\python_exam_system"

# 1. Update app.py
app_path = os.path.join(base_dir, "app.py")
with open(app_path, "r", encoding="utf-8") as f:
    app_code = f.read()

old_route = """@app.route('/')
def index():
    return render_template('index.html')"""

new_route = """@app.route('/')
def index():
    return send_file(os.path.join(os.path.dirname(__file__), 'python_nazorat.html'))"""

if old_route in app_code:
    app_code = app_code.replace(old_route, new_route)
    with open(app_path, "w", encoding="utf-8") as f:
        f.write(app_code)
    print("Updated app.py root route")

# 2. Update app_standalone.js
js_path = os.path.join(base_dir, "app_standalone.js")
with open(js_path, "r", encoding="utf-8") as f:
    js_code = f.read()

sync_block = """let isSyncingServer = false;
function syncResultsFromServer() {
    if (isSyncingServer || typeof window === 'undefined' || !window.location.protocol.startsWith('http')) return;
    isSyncingServer = true;
    fetch('/api/teacher_results')
        .then(r => r.json())
        .then(data => {
            isSyncingServer = false;
            if (data && data.success && Array.isArray(data.results)) {
                const current = getStoredStudents();
                let changed = false;
                data.results.forEach(sr => {
                    const idx = current.findIndex(c => 
                        (sr.student_id_number && c.studentId === sr.student_id_number) ||
                        (c.fullName.toLowerCase() === (sr.full_name||'').toLowerCase() && String(c.groupName).trim() === String(sr.group_name).trim())
                    );
                    const formatted = {
                        studentId: sr.student_id_number,
                        fullName: sr.full_name,
                        direction: sr.direction || "Axborot tizimlari va texnologiyalari",
                        course: String(sr.course || "1"),
                        groupName: sr.group_name,
                        totalScore: sr.total_score,
                        maxScore: sr.max_score || 30,
                        correctCount: sr.correct_count,
                        incorrectCount: sr.incorrect_count,
                        statusText: sr.status_text || (sr.total_score >= 18 ? "Joriy nazoratdan o‘tdi" : "Joriy nazoratdan o‘tmadi"),
                        finishedAt: sr.finished_at || sr.started_at,
                        tabSwitchCount: sr.tab_switch_count || 0,
                        isModified: !!sr.is_modified_by_teacher
                    };
                    if (idx !== -1) {
                        if (current[idx].totalScore !== formatted.totalScore || current[idx].finishedAt !== formatted.finishedAt) {
                            current[idx] = formatted;
                            changed = true;
                        }
                    } else {
                        current.unshift(formatted);
                        changed = true;
                    }
                });
                if (changed) {
                    SafeStorage.setItem(STORAGE_KEY_STUDENTS, JSON.stringify(current));
                    const teachDash = document.getElementById("teacherDashboard");
                    if (teachDash && teachDash.style.display !== "none") {
                        renderTeacherTable(true);
                    }
                }
            }
        })
        .catch(() => { isSyncingServer = false; });
}

// O‘qituvchi jadvalini chizish
function renderTeacherTable(skipSync = false) {
    if (!skipSync) {
        syncResultsFromServer();
    }
"""

if "function syncResultsFromServer()" not in js_code:
    js_code = js_code.replace("// O‘qituvchi jadvalini chizish\nfunction renderTeacherTable() {", sync_block)
    with open(js_path, "w", encoding="utf-8") as f:
        f.write(js_code)
    print("Added syncResultsFromServer to app_standalone.js")

print("Sync update complete.")
