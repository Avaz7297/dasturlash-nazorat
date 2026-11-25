// exam.js - Talaba testi interfeysi va xavfsizlik nazorati

document.addEventListener('DOMContentLoaded', () => {
    const examContainer = document.getElementById('examContainer');
    if (!examContainer) return;

    const sessionId = parseInt(examContainer.dataset.sessionId);
    let remainingSeconds = parseInt(examContainer.dataset.remainingSeconds);
    let tabSwitchCount = parseInt(examContainer.dataset.tabSwitches) || 0;

    let currentQuestionIndex = 0;
    const totalQuestions = 30;
    let studentAnswers = {};

    // 1. Taymerni ishga tushirish
    const timerDisplay = document.getElementById('timerDisplay');
    const timerIcon = document.getElementById('timerIcon');

    function updateTimer() {
        if (remainingSeconds <= 0) {
            timerDisplay.textContent = "00:00";
            alert("Test vaqti tugadi! Javoblaringiz avtomatik hisoblanmoqda...");
            submitExam(true);
            return;
        }

        const mins = Math.floor(remainingSeconds / 60);
        const secs = remainingSeconds % 60;
        timerDisplay.textContent = `${mins.toString().padStart(2, '0')}:${secs.toString().padStart(2, '0')}`;

        // Oxirgi 5 daqiqada taymer qizil rangga kiradi
        if (remainingSeconds < 300) {
            timerDisplay.classList.add('text-red-600');
            timerIcon.classList.remove('bg-amber-100', 'text-amber-600');
            timerIcon.classList.add('bg-red-100', 'text-red-600');
        }

        remainingSeconds--;
    }

    updateTimer();
    const timerInterval = setInterval(updateTimer, 1000);

    // 2. Savollar navigatsiyasi
    const questionCards = document.querySelectorAll('.question-card');
    const mapButtons = document.querySelectorAll('.map-btn');

    function showQuestion(index) {
        if (index < 0 || index >= totalQuestions) return;

        questionCards.forEach(c => c.classList.add('hidden'));
        const targetCard = document.getElementById(`qCard_${index}`);
        if (targetCard) {
            targetCard.classList.remove('hidden');
        }

        currentQuestionIndex = index;

        // Xaritadagi joriy ko'rsatkichni yangilash
        mapButtons.forEach((btn, i) => {
            btn.classList.remove('ring-2', 'ring-brand-500', 'border-brand-500');
            if (i === index) {
                btn.classList.add('ring-2', 'ring-brand-500', 'border-brand-500');
            }
        });
    }

    // Xarita tugmalari orqali o'tish
    mapButtons.forEach(btn => {
        btn.addEventListener('click', () => {
            const idx = parseInt(btn.dataset.targetIdx);
            showQuestion(idx);
        });
    });

    // Oldingi tugmalari
    document.querySelectorAll('.btn-prev').forEach(btn => {
        btn.addEventListener('click', () => {
            if (currentQuestionIndex > 0) {
                showQuestion(currentQuestionIndex - 1);
            }
        });
    });

    // Keyingi tugmalari
    document.querySelectorAll('.btn-next').forEach(btn => {
        btn.addEventListener('click', () => {
            if (currentQuestionIndex < totalQuestions - 1) {
                showQuestion(currentQuestionIndex + 1);
            }
        });
    });

    // 3. Variant tanlanganda
    const radioInputs = document.querySelectorAll('.option-radio');
    const answeredCountSpan = document.getElementById('answeredCount');

    radioInputs.forEach(radio => {
        radio.addEventListener('change', (e) => {
            const qIdx = e.target.dataset.qidx;
            const chosenVal = parseInt(e.target.value);
            studentAnswers[qIdx] = chosenVal;

            // Xaritada tugmani bo'yash
            const mapBtn = document.getElementById(`mapBtn_${qIdx}`);
            if (mapBtn) {
                mapBtn.classList.remove('bg-slate-50', 'text-slate-600');
                mapBtn.classList.add('bg-brand-600', 'text-white', 'border-brand-600');
            }

            // Javob berilganlar soni
            const count = Object.keys(studentAnswers).length;
            answeredCountSpan.textContent = count;

            // Oraliq saqlash (Serverga yuborish)
            saveProgressToServer();
        });
    });

    // 4. Oraliq natijalarni serverga avtomatik saqlash
    function saveProgressToServer() {
        fetch('/api/save_progress', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                session_id: sessionId,
                answers: studentAnswers,
                tab_switch_count: tabSwitchCount
            })
        }).catch(err => console.error("Avtosave xatosi:", err));
    }

    // 5. SHAFFOFLIK VA XAVFSIZLIK: Copy/Paste va O'ng tugmani taqiqlash
    document.addEventListener('contextmenu', (e) => {
        e.preventDefault();
        return false;
    });

    document.addEventListener('copy', (e) => {
        e.preventDefault();
        return false;
    });

    document.addEventListener('cut', (e) => {
        e.preventDefault();
        return false;
    });

    document.addEventListener('selectstart', (e) => {
        e.preventDefault();
        return false;
    });

    // 6. SHAFFOFLIK: Boshqa sahifaga/tabga o'tishni aniqlash
    const violationModal = document.getElementById('violationModal');
    const modalViolationCount = document.getElementById('modalViolationCount');
    const switchWarningBadge = document.getElementById('switchWarningBadge');
    const switchCountText = document.getElementById('switchCountText');
    const btnAckViolation = document.getElementById('btnAckViolation');

    let isModalActive = false;

    function handleTabSwitch() {
        if (isModalActive) return;

        tabSwitchCount++;
        modalViolationCount.textContent = tabSwitchCount;
        switchCountText.textContent = tabSwitchCount;
        switchWarningBadge.classList.remove('hidden');

        isModalActive = true;
        violationModal.classList.remove('hidden');

        saveProgressToServer();
    }

    document.addEventListener('visibilitychange', () => {
        if (document.hidden) {
            handleTabSwitch();
        }
    });

    window.addEventListener('blur', () => {
        handleTabSwitch();
    });

    btnAckViolation.addEventListener('click', () => {
        violationModal.classList.add('hidden');
        isModalActive = false;
    });

    // 7. Testni yakunlash modali va jo'natish
    const btnFinishExam = document.getElementById('btnFinishExam');
    const finishConfirmModal = document.getElementById('finishConfirmModal');
    const btnCancelFinish = document.getElementById('btnCancelFinish');
    const btnConfirmFinish = document.getElementById('btnConfirmFinish');
    const confirmAnswered = document.getElementById('confirmAnswered');

    function openFinishModal() {
        confirmAnswered.textContent = Object.keys(studentAnswers).length;
        finishConfirmModal.classList.remove('hidden');
    }

    btnFinishExam.addEventListener('click', openFinishModal);

    document.querySelectorAll('.btn-goto-finish').forEach(btn => {
        btn.addEventListener('click', openFinishModal);
    });

    btnCancelFinish.addEventListener('click', () => {
        finishConfirmModal.classList.add('hidden');
    });

    btnConfirmFinish.addEventListener('click', () => {
        finishConfirmModal.classList.add('hidden');
        submitExam(false);
    });

    function submitExam(autoTimeExpired = false) {
        clearInterval(timerInterval);

        // Tugmani kutish rejimiga o'tkazish
        btnConfirmFinish.disabled = true;
        btnConfirmFinish.innerHTML = `<i class="fa-solid fa-spinner fa-spin"></i> Tekshirilmoqda...`;

        fetch('/api/submit_exam', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                session_id: sessionId,
                answers: studentAnswers,
                tab_switch_count: tabSwitchCount
            })
        })
        .then(res => res.json())
        .then(data => {
            if (data.success && data.redirect) {
                window.location.href = data.redirect;
            } else {
                alert("Xatolik yuz berdi: " + (data.error || "Noma'lum xato"));
            }
        })
        .catch(err => {
            console.error("Testni yakunlashda xatolik:", err);
            alert("Tarmoq xatosi! Iltimos, qayta urinib ko'ring.");
        });
    }

});
