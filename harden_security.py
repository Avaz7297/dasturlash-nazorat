# -*- coding: utf-8 -*-
with open("build_html.py", "r", encoding="utf-8") as f:
    code = f.read()

# Let's inspect isTeacherAuthenticated helper
security_code = """
// O'qituvchi autentifikatsiyasini qat'iy tekshirish
function isTeacherAuthenticated() {
    return (SafeSession.getItem(STORAGE_KEY_TEACHER_AUTH) === "true") ||
           (SafeStorage.getItem(STORAGE_KEY_TEACHER_AUTH) === "true");
}
"""

if "function isTeacherAuthenticated" not in code:
    code = code.replace("function toggleTeacherSection() {", security_code + "\nfunction toggleTeacherSection() {")

# Add auth check in renderTeacherTable
old_render_start = """function renderTeacherTable() {
    const students = getStoredStudents();"""

new_render_start = """function renderTeacherTable() {
    if (!isTeacherAuthenticated()) {
        const dash = document.getElementById("teacherDashboard");
        if (dash) { dash.classList.add("hidden"); dash.style.display = "none"; }
        const loginForm = document.getElementById("teacherLoginForm");
        if (loginForm) { loginForm.classList.remove("hidden"); loginForm.style.display = "block"; }
        const tbody = document.getElementById("teacherTableBody");
        if (tbody) tbody.innerHTML = "";
        return;
    }
    const students = getStoredStudents();"""

code = code.replace(old_render_start, new_render_start)

# Add auth check in exportToExcel
old_export_start = """function exportToExcel() {
    const students = getStoredStudents();"""

new_export_start = """function exportToExcel() {
    if (!isTeacherAuthenticated()) {
        alert("Kirish taqiqlangan! Faqat o'qituvchi login va paroli bilan kirgan shaxs ma'lumotlarni yuklab olishi mumkin.");
        return;
    }
    const students = getStoredStudents();"""

code = code.replace(old_export_start, new_export_start)

# Add auth check in openDetailModal
old_detail_start = """function openDetailModal(studentId) {
    const students = getStoredStudents();"""

new_detail_start = """function openDetailModal(studentId) {
    if (!isTeacherAuthenticated()) return;
    const students = getStoredStudents();"""

code = code.replace(old_detail_start, new_detail_start)

# Add auth check in openEditScoreModal
old_edit_start = """function openEditScoreModal(studentId) {
    const students = getStoredStudents();"""

new_edit_start = """function openEditScoreModal(studentId) {
    if (!isTeacherAuthenticated()) return;
    const students = getStoredStudents();"""

code = code.replace(old_edit_start, new_edit_start)

# Add auth check in deleteStudentResult
old_del_start = """function deleteStudentResult(studentId) {
    const students = getStoredStudents();"""

new_del_start = """function deleteStudentResult(studentId) {
    if (!isTeacherAuthenticated()) return;
    const students = getStoredStudents();"""

code = code.replace(old_del_start, new_del_start)

# Add auth check in clearAllResults
old_clear_start = """function clearAllResults() {
    const students = getStoredStudents();"""

new_clear_start = """function clearAllResults() {
    if (!isTeacherAuthenticated()) return;
    const students = getStoredStudents();"""

code = code.replace(old_clear_start, new_clear_start)

# Add auth check in toggleAuditModal
old_audit_start = """function toggleAuditModal() {
    const modal = document.getElementById("modalAudit");"""

new_audit_start = """function toggleAuditModal() {
    if (!isTeacherAuthenticated()) return;
    const modal = document.getElementById("modalAudit");"""

code = code.replace(old_audit_start, new_audit_start)

# When a student starts an exam, clear any teacher auth so shared device is clean
old_start_actual = """function startExamActual() {
    if (!pendingStudent) {
        switchView("register");
        return;
    }"""

new_start_actual = """function startExamActual() {
    // Talaba testni boshlaganda o'qituvchi sessiyasini xavfsiz tozalash
    SafeSession.removeItem(STORAGE_KEY_TEACHER_AUTH);
    SafeStorage.removeItem(STORAGE_KEY_TEACHER_AUTH);

    if (!pendingStudent) {
        switchView("register");
        return;
    }"""

code = code.replace(old_start_actual, new_start_actual)

with open("build_html.py", "w", encoding="utf-8") as f:
    f.write(code)

print("build_html.py security hardened successfully.")
