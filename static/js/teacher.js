// teacher.js - O'qituvchi paneli interfeysi va amallari

// 1. Batafsil ko'rish modali
function openDetailModal(sessionId) {
    const modal = document.getElementById('detailModal');
    const questionsContainer = document.getElementById('detailQuestionsList');
    const nameSpan = document.getElementById('detailStudentName');
    const infoSpan = document.getElementById('detailStudentInfo');

    modal.classList.remove('hidden');
    questionsContainer.innerHTML = `
        <div class="text-center py-8 text-slate-400">
            <i class="fa-solid fa-spinner fa-spin text-2xl mb-2"></i>
            <p class="text-xs">Yuklanmoqda...</p>
        </div>
    `;

    fetch(`/api/teacher/student/${sessionId}`)
        .then(res => res.json())
        .then(res => {
            if (!res.success) {
                questionsContainer.innerHTML = `<p class="text-red-500 text-center text-sm py-4">Xatolik: ${res.error}</p>`;
                return;
            }

            const data = res.data;
            nameSpan.textContent = data.full_name;
            infoSpan.textContent = `${data.group_name} | ${data.direction} (${data.course}-kurs) • Ball: ${data.total_score}/${data.max_score} • Natija: ${data.status_text} • Chiqishlar: ${data.tab_switch_count} marta`;

            const questions = data.questions || [];
            const answers = data.answers || {};

            let html = '';
            questions.forEach((q, idx) => {
                const userChosenIdx = answers[idx.toString()];
                const isCorrect = userChosenIdx !== undefined && parseInt(userChosenIdx) === q.correct;
                const answered = userChosenIdx !== undefined;

                html += `
                    <div class="p-4 rounded-xl border ${isCorrect ? 'border-emerald-200 bg-emerald-50/30' : (answered ? 'border-rose-200 bg-rose-50/30' : 'border-slate-200 bg-slate-50/50')} text-xs sm:text-sm">
                        <div class="flex items-center justify-between mb-2">
                            <span class="font-bold text-slate-700">№ ${idx + 1}. [${q.topic}]</span>
                            <span class="px-2 py-0.5 rounded text-[10px] font-bold ${isCorrect ? 'bg-emerald-100 text-emerald-800' : (answered ? 'bg-rose-100 text-rose-800' : 'bg-slate-200 text-slate-600')}">
                                ${isCorrect ? 'To\'g\'ri (+1 ball)' : (answered ? 'Noto\'g\'ri (0 ball)' : 'Javob berilmagan')}
                            </span>
                        </div>
                        <div class="font-medium text-slate-900 mb-2">${q.question}</div>
                        ${q.code ? `<pre class="p-3 bg-slate-900 text-slate-100 rounded-lg text-xs font-mono overflow-x-auto mb-3"><code>${escapeHtml(q.code)}</code></pre>` : ''}
                        
                        <div class="grid grid-cols-1 sm:grid-cols-2 gap-2 mt-2">
                            ${q.options.map((opt, optIdx) => {
                                const isUserChoice = userChosenIdx !== undefined && parseInt(userChosenIdx) === optIdx;
                                const isRightChoice = optIdx === q.correct;

                                let optClass = "border-slate-200 bg-white text-slate-700";
                                let icon = "";

                                if (isRightChoice) {
                                    optClass = "border-emerald-500 bg-emerald-100/60 text-emerald-900 font-semibold";
                                    icon = "<i class='fa-solid fa-check text-emerald-600 ml-1'></i> (To'g'ri javob)";
                                }
                                if (isUserChoice && !isRightChoice) {
                                    optClass = "border-rose-500 bg-rose-100/60 text-rose-900 font-semibold";
                                    icon = "<i class='fa-solid fa-xmark text-rose-600 ml-1'></i> (Talaba tanlagan)";
                                } else if (isUserChoice && isRightChoice) {
                                    icon = "<i class='fa-solid fa-circle-check text-emerald-600 ml-1'></i> (Talaba to'g'ri topgan)";
                                }

                                const letters = ["A", "B", "C", "D"];
                                return `
                                    <div class="p-2 rounded-lg border text-xs flex items-center justify-between ${optClass}">
                                        <span><strong>${letters[optIdx]})</strong> ${escapeHtml(opt)}</span>
                                        <span class="text-[10px]">${icon}</span>
                                    </div>
                                `;
                            }).join('')}
                        </div>
                    </div>
                `;
            });

            questionsContainer.innerHTML = html;
        })
        .catch(err => {
            questionsContainer.innerHTML = `<p class="text-red-500 text-center text-sm py-4">Tarmoq xatosi</p>`;
        });
}

function closeDetailModal() {
    document.getElementById('detailModal').classList.add('hidden');
}

// 2. Ballni tahrirlash modali
function openEditScoreModal(sessionId, studentName, currentScore) {
    document.getElementById('editSessionId').value = sessionId;
    document.getElementById('editStudentName').textContent = studentName;
    document.getElementById('editNewScore').value = currentScore;
    document.getElementById('editReason').value = '';

    document.getElementById('editScoreModal').classList.remove('hidden');
}

function closeEditScoreModal() {
    document.getElementById('editScoreModal').classList.add('hidden');
}

function handleScoreUpdate(event) {
    event.preventDefault();
    const sessionId = document.getElementById('editSessionId').value;
    const newScore = document.getElementById('editNewScore').value;
    const reason = document.getElementById('editReason').value;
    const submitBtn = document.getElementById('btnSubmitScoreChange');

    submitBtn.disabled = true;
    submitBtn.innerHTML = `<i class="fa-solid fa-spinner fa-spin"></i> Saqlanmoqda...`;

    fetch('/api/teacher/update_score', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            session_id: parseInt(sessionId),
            new_score: parseInt(newScore),
            reason: reason
        })
    })
    .then(res => res.json())
    .then(data => {
        if (data.success) {
            alert(data.message);
            window.location.reload();
        } else {
            alert("Xatolik: " + data.error);
            submitBtn.disabled = false;
            submitBtn.textContent = "Saqlash & Auditga yozish";
        }
    })
    .catch(err => {
        alert("Tarmoq xatoligi!");
        submitBtn.disabled = false;
        submitBtn.textContent = "Saqlash & Auditga yozish";
    });
}

function escapeHtml(text) {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
}
