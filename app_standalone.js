// app_standalone.js - Masofaviy Joriy Nazorat Mustaqil Skripti
// Rasmiy 130 ta talaba (9mt-26, 10mt-26, 11mt-26, 12mt-26, 13mt-26, 14mt-26) va Sinov Talabasi

const STUDENTS_ROSTER = [{"id": "315261102785", "name": "BO‘RONBOYEVA MUXLISA KOMILJON QIZI", "group": "9mt-26 ATT (o‘z)"}, {"id": "315261102788", "name": "BUVAXONOV YAHYOBEK AHRORJON O‘G‘LI", "group": "9mt-26 ATT (o‘z)"}, {"id": "315261102943", "name": "YUSUPOV SAIDMARDONBEK XASAN O‘G‘LI", "group": "9mt-26 ATT (o‘z)"}, {"id": "315261102931", "name": "TO‘YCHIBOYEV NE’MAT SHUXRAT O‘G‘LI", "group": "9mt-26 ATT (o‘z)"}, {"id": "315261102783", "name": "BAXROMOV ELYOR ILXOM O‘G‘LI", "group": "9mt-26 ATT (o‘z)"}, {"id": "315261102880", "name": "NAZAROV SARDOR HUSAN O‘G‘LI", "group": "9mt-26 ATT (o‘z)"}, {"id": "315261102910", "name": "RAXMONBERDIYEV MIRJALOL MUXIDDIN O‘G‘LI", "group": "9mt-26 ATT (o‘z)"}, {"id": "315261102893", "name": "QOZOQBOYEV SARDOR G‘ULOM O‘G‘LI", "group": "9mt-26 ATT (o‘z)"}, {"id": "315261102794", "name": "ESHPO‘LATOV AKBAR ESHNAZAR O‘G‘LI", "group": "9mt-26 ATT (o‘z)"}, {"id": "315261102881", "name": "NIG‘MATOV DOSTON SHUXRATOVICH", "group": "9mt-26 ATT (o‘z)"}, {"id": "315261103106", "name": "BOBONIYOZOV HASAN ABDIMALIK O‘G‘LI", "group": "9mt-26 ATT (o‘z)"}, {"id": "315261103378", "name": "AXMADOV BAXROM AXTAM O‘G‘LI", "group": "9mt-26 ATT (o‘z)"}, {"id": "315261102775", "name": "ALIJONOV OZODBEK AKMALJON O‘G‘LI", "group": "9mt-26 ATT (o‘z)"}, {"id": "315261103030", "name": "SAMADOV DONIYOR BOBIROVICH", "group": "9mt-26 ATT (o‘z)"}, {"id": "315261102885", "name": "OCHILOV MIRKOMIL RAXMONQUL O‘G‘LI", "group": "9mt-26 ATT (o‘z)"}, {"id": "315261102778", "name": "ASOMIDDINOV ASROLXON ASQADXON O‘G‘LI", "group": "9mt-26 ATT (o‘z)"}, {"id": "315261102854", "name": "KUNUZOQOV NURBEK FARXOD O‘G‘LI", "group": "9mt-26 ATT (o‘z)"}, {"id": "315261102799", "name": "IKROMOV ZAXRIDDIN NURIDDIN O‘G‘LI", "group": "9mt-26 ATT (o‘z)"}, {"id": "315261102860", "name": "MAMADALIYEV HOJIAKBAR SHERALI O‘G‘LI", "group": "9mt-26 ATT (o‘z)"}, {"id": "315261102771", "name": "ABDUSHUKUROV OBIDJON ILXOM O‘G‘LI", "group": "9mt-26 ATT (o‘z)"}, {"id": "315261102878", "name": "NAMOZOV ABDULAZIZ ISLOM O‘G‘LI", "group": "9mt-26 ATT (o‘z)"}, {"id": "315261102920", "name": "SHODIYEV ASADBEK SHERALI O‘G‘LI", "group": "9mt-26 ATT (o‘z)"}, {"id": "315261102776", "name": "ANORBOYEV SHERMUHAMMAD VALIJON O‘G‘LI", "group": "9mt-26 ATT (o‘z)"}, {"id": "315261103381", "name": "XOJIYEV AMIRXON MAVLUTJONOVICH", "group": "10mt-26 ATT (o‘z)"}, {"id": "315261102938", "name": "XO‘JABOYEV NODIRBEK DAVRONBEK O‘G‘LI", "group": "10mt-26 ATT (o‘z)"}, {"id": "315261102877", "name": "NAMAZBAYEV ELNUR ARMAN O‘G‘LI", "group": "10mt-26 ATT (o‘z)"}, {"id": "315261102789", "name": "CHUMONBOYEV MUHAMMADQODIR MURODALI O‘G‘LI", "group": "10mt-26 ATT (o‘z)"}, {"id": "315261102774", "name": "ABROROV ABDULLOH ALISHER O‘G‘LI", "group": "10mt-26 ATT (o‘z)"}, {"id": "315261102932", "name": "TOYIROV FARRUH BAHODIR O‘G‘LI", "group": "10mt-26 ATT (o‘z)"}, {"id": "315261102915", "name": "RUSTAMOV ASADBEK ZAFAR O‘G‘LI", "group": "10mt-26 ATT (o‘z)"}, {"id": "315261102780", "name": "BABAJANOVA MUXADDAS TURABAYEVNA", "group": "10mt-26 ATT (o‘z)"}, {"id": "315261102886", "name": "OROLBOYEV OZODBEK OTABEK O‘G‘LI", "group": "10mt-26 ATT (o‘z)"}, {"id": "315261102933", "name": "UMMATKULOV AZAMATBEK GAYRAT O'G'LI", "group": "10mt-26 ATT (o‘z)"}, {"id": "315261102791", "name": "ERKINOV XURSHID BAXTIYOR O‘G‘LI", "group": "10mt-26 ATT (o‘z)"}, {"id": "315261102891", "name": "QILICHOV OZODBEK YORQIN O‘G‘LI", "group": "10mt-26 ATT (o‘z)"}, {"id": "315261102781", "name": "BAHODIROV ISLOMJON ELMURODOVICH", "group": "10mt-26 ATT (o‘z)"}, {"id": "315261102927", "name": "TOGANBEKOV RAMZIDDIN XUSNIDIN O‘G‘LI", "group": "10mt-26 ATT (o‘z)"}, {"id": "315261102800", "name": "ILHOMJONOVA SAODAT OLIMJON QIZI", "group": "10mt-26 ATT (o‘z)"}, {"id": "315261103390", "name": "BAXROMOV SARDOR BAXODIR O‘G‘LI", "group": "10mt-26 ATT (o‘z)"}, {"id": "315261103346", "name": "XAMROYEV MIRSAID SAMAD O‘G‘LI", "group": "10mt-26 ATT (o‘z)"}, {"id": "315261102761", "name": "ABDULLAXONOV FAYZULLOXON ANVARXON O‘G‘LI", "group": "10mt-26 ATT (o‘z)"}, {"id": "315261102906", "name": "RAHIMOV NODIR MUZAFFAR O‘G‘LI", "group": "10mt-26 ATT (o‘z)"}, {"id": "315261102941", "name": "YOQUBOV SHERZODBEK SHUKURALI O‘G‘LI", "group": "10mt-26 ATT (o‘z)"}, {"id": "315261102762", "name": "ABDULLAYEV AKMAL O‘TKIRJON O‘G‘LI", "group": "10mt-26 ATT (o‘z)"}, {"id": "315261102806", "name": "JUMANAZAROV MUHAMMADNOZIM G‘OLIBJONOVICH", "group": "10mt-26 ATT (o‘z)"}, {"id": "315261102869", "name": "MAZBUTOV ASADBEK BAHODIR O‘G‘LI", "group": "10mt-26 ATT (o‘z)"}, {"id": "315261102924", "name": "SOTVOLDIYEV DILSHOD SHERZOD O‘G‘LI", "group": "11mt-26 ATT (o‘z)"}, {"id": "315261102852", "name": "KULMATOV MUHAMMAD ABDURAUF O‘G‘LI", "group": "11mt-26 ATT (o‘z)"}, {"id": "315261102843", "name": "KAMOLOV FAZLIDDIN NIZOMIDDIN O‘G‘LI", "group": "11mt-26 ATT (o‘z)"}, {"id": "315261102917", "name": "SAFAROV AZIZBEK ELMUROD O‘G‘LI", "group": "11mt-26 ATT (o‘z)"}, {"id": "315261102890", "name": "QAHHAROV QILICHBEK ZARIF O'G'LI", "group": "11mt-26 ATT (o‘z)"}, {"id": "315261102758", "name": "ABDIYEV JAMSHID SAMAD O‘G‘LI", "group": "11mt-26 ATT (o‘z)"}, {"id": "315261102802", "name": "JALOLIDDINOV DIYORBEK BAXRIDDIN O‘G‘LI", "group": "11mt-26 ATT (o‘z)"}, {"id": "315261102923", "name": "SODIQOV DILSHODBEK RAXMON O‘G‘LI", "group": "11mt-26 ATT (o‘z)"}, {"id": "315261102795", "name": "FAYZULLOYEV DILSHODBEK XAYRIDDIN O‘G‘LI", "group": "11mt-26 ATT (o‘z)"}, {"id": "315261102909", "name": "RAXIMBERGANOV UCHQUNBEK JAHONGIR O‘G‘LI", "group": "11mt-26 ATT (o‘z)"}, {"id": "315261102857", "name": "MAHKAMOV DAVRON KELDIBEK O‘G‘LI", "group": "11mt-26 ATT (o‘z)"}, {"id": "315261102876", "name": "NAHALBOYEV ODILBEK ASLIDDIN O‘G‘LI", "group": "11mt-26 ATT (o‘z)"}, {"id": "315261102912", "name": "REYIMBOYEV DIYORBEK RAXMONBERGAN O‘G‘LI", "group": "11mt-26 ATT (o‘z)"}, {"id": "315261102904", "name": "QUCHQOROVA SHAHZODA BAXRIDDIN QIZI", "group": "11mt-26 ATT (o‘z)"}, {"id": "315261102930", "name": "TOSHNIYOZOV AZIZBEK SHUHRATILLO O‘G‘LI", "group": "11mt-26 ATT (o‘z)"}, {"id": "315261102871", "name": "MIRVOLIYEV MUROD MIRZATURSINOVICH", "group": "11mt-26 ATT (o‘z)"}, {"id": "315261102777", "name": "ASATULLAYEV SARVARJON SOBIRJON O‘G‘LI", "group": "11mt-26 ATT (o‘z)"}, {"id": "315261102940", "name": "XUDOYBERDIYEVA FOTIMA RUZIMURODOVNA", "group": "11mt-26 ATT (o‘z)"}, {"id": "315261102804", "name": "JO‘RAQULOVA HULKAR ADHAM QIZI", "group": "11mt-26 ATT (o‘z)"}, {"id": "315261102770", "name": "ABDUSATTOROVA O‘G‘ILOY ABDULLA QIZI", "group": "11mt-26 ATT (o‘z)"}, {"id": "315261102759", "name": "ABDUKARIMOV ELYOR BAXTIYOR O‘G‘LI", "group": "11mt-26 ATT (o‘z)"}, {"id": "315261102939", "name": "XUDAYBERGANOV SOBIRJON ADAMBOY O‘G‘LI", "group": "11mt-26 ATT (o‘z)"}, {"id": "315261102892", "name": "QO‘CHQOROV SHUXRAT SHOKIRJON O‘G‘LI", "group": "11mt-26 ATT (o‘z)"}, {"id": "315261102911", "name": "RAXMONOV BEKZOD BURXON O‘G‘LI", "group": "12mt-26 ATT (o‘z)"}, {"id": "315261102864", "name": "MAMIROV BEKNUR TOXIR O‘G‘LI", "group": "12mt-26 ATT (o‘z)"}, {"id": "315261103305", "name": "QURBANOV TOTLIBOY ZAMON O‘G‘LI", "group": "12mt-26 ATT (o‘z)"}, {"id": "315261102887", "name": "O‘ROQBOYEV NODIRBEK LUTFULLA O‘G‘LI", "group": "12mt-26 ATT (o‘z)"}, {"id": "315261102935", "name": "XAKIMOVA SARVINOZ SUXROB QIZI", "group": "12mt-26 ATT (o‘z)"}, {"id": "315261102934", "name": "USMONQULOV OTABEK ULUG‘BEK O‘G‘LI", "group": "12mt-26 ATT (o‘z)"}, {"id": "315261102937", "name": "XAYRULLAYEV XUSAN XABIBULLO O‘G‘LI", "group": "12mt-26 ATT (o‘z)"}, {"id": "315261102862", "name": "MAMARAXIMOV SHOHRUH OZODBEK O‘G‘LI", "group": "12mt-26 ATT (o‘z)"}, {"id": "315261102766", "name": "ABDUQODIROV SHODIYOR KAMOL O‘G‘LI", "group": "12mt-26 ATT (o‘z)"}, {"id": "315261103169", "name": "ABDURASULOV XOJIAKBAR BAHODIR O‘G‘LI", "group": "12mt-26 ATT (o‘z)"}, {"id": "315261103107", "name": "ZOIROV MADRAHIM ABDUMALIK O‘G‘LI", "group": "12mt-26 ATT (o‘z)"}, {"id": "315261102866", "name": "MAVLONOV ABRORXON AKMALXON O‘G‘LI", "group": "12mt-26 ATT (o‘z)"}, {"id": "315261102884", "name": "OBBOSOVA MASHXURAXON SOLIJONOVNA", "group": "12mt-26 ATT (o‘z)"}, {"id": "315261102760", "name": "ABDUKARIMOV MUXAMMADKABIR AZIZ O‘G‘LI", "group": "12mt-26 ATT (o‘z)"}, {"id": "315261102769", "name": "ABDURAXIMOV ASRORBEK ABROR O‘G‘LI", "group": "12mt-26 ATT (o‘z)"}, {"id": "315261102793", "name": "ESHNAZAROV MIRJALOL BAXTIYOR O‘G‘LI", "group": "12mt-26 ATT (o‘z)"}, {"id": "315261102919", "name": "SEYTMURATOV XUSINBAY URAZBAYEVICH", "group": "13mt-26 ATT (o‘z)"}, {"id": "315261102872", "name": "MIRZAXALILOV MUHAMMADDIYOR RASULJON O‘G‘LI", "group": "13mt-26 ATT (o‘z)"}, {"id": "315261102926", "name": "TLEUNIYAZOV AKRAMBEK QABÍL ULÍ", "group": "13mt-26 ATT (o‘z)"}, {"id": "315261102803", "name": "JO‘RABEKOV ZAHIRIDDIN SANJARBEK O‘G‘LI", "group": "13mt-26 ATT (o‘z)"}, {"id": "315261102790", "name": "DAVLATBOYEV SHAHBOZ SIROJIDDIN O‘G‘LI", "group": "13mt-26 ATT (o‘z)"}, {"id": "315261102768", "name": "ABDURASHIDOV RAMAZON ABDURASUL O‘G‘LI", "group": "13mt-26 ATT (o‘z)"}, {"id": "315261102914", "name": "RUSTAMOV ASAD AVAZ O‘G‘LI", "group": "13mt-26 ATT (o‘z)"}, {"id": "315261102870", "name": "MIRKARIMOV BEKZOD MIRZOID O‘G‘LI", "group": "13mt-26 ATT (o‘z)"}, {"id": "315261102853", "name": "KUNIZOQOV OG‘ABEK ZIYODULLAYEVICH", "group": "13mt-26 ATT (o‘z)"}, {"id": "315261102942", "name": "YUSUPBOYEV HUSANBOY AZAMAT O‘G‘LI", "group": "13mt-26 ATT (o‘z)"}, {"id": "315261102929", "name": "TO‘RABOYEVA SEVINCHOY XAMRO QIZI", "group": "13mt-26 ATT (o‘z)"}, {"id": "315261103165", "name": "XAYRULLAYEV ASADBEK FARXOD O‘G‘LI", "group": "13mt-26 ATT (o‘z)"}, {"id": "315261102928", "name": "TOHIROV BEHRUZBEK RAVSHANBEK O‘G‘LI", "group": "13mt-26 ATT (o‘z)"}, {"id": "315261102801", "name": "ISMAILOV MURODBEK SHAVKAT O‘G‘LI", "group": "13mt-26 ATT (o‘z)"}, {"id": "315261102888", "name": "OTABOYEV XURSHID SAYDULLO O‘G‘LI", "group": "13mt-26 ATT (o‘z)"}, {"id": "315261102936", "name": "XAYDAROV NAMOZ SAFAR O‘G‘LI", "group": "13mt-26 ATT (o‘z)"}, {"id": "315261102847", "name": "KARIMOV ISLOM SHARIP O‘G‘LI", "group": "13mt-26 ATT (o‘z)"}, {"id": "315261102850", "name": "KOCHKAROV SHOHRUH KENGESH OG‘LÍ", "group": "13mt-26 ATT (o‘z)"}, {"id": "315261102907", "name": "RAJABQULOV OZODBEK BAHODIRJON O‘G‘LI", "group": "13mt-26 ATT (o‘z)"}, {"id": "315261103068", "name": "SUR‘ATOV MUHAMMAD BURXONBEK O‘G‘LI", "group": "13mt-26 ATT (o‘z)"}, {"id": "315261102848", "name": "KENJAYEV SHOXRUZBEK UTKIR O‘G‘LI", "group": "13mt-26 ATT (o‘z)"}, {"id": "315261102918", "name": "SAYDULLAYEV JAVOHIR AKRAM O‘G‘LI", "group": "13mt-26 ATT (o‘z)"}, {"id": "315261102873", "name": "MUSTAFAQULOV SHAHRIYOR SHAMSIDDIN O‘G‘LI", "group": "13mt-26 ATT (o‘z)"}, {"id": "315261102797", "name": "HABIBULLAYEV DONIYORBEK MA‘RUFJON O‘G‘LI", "group": "13mt-26 ATT (o‘z)"}, {"id": "315261102922", "name": "SOBITOV SHOXRIYOR QUDRATILLO O‘G‘LI", "group": "13mt-26 ATT (o‘z)"}, {"id": "315261102765", "name": "ABDUQAHHOROV ABDULHAY ABDULATIF O‘G‘LI", "group": "13mt-26 ATT (o‘z)"}, {"id": "315261102867", "name": "MAXAMADJONOV ABDULLOH SOLIHJON O‘G‘LI", "group": "13mt-26 ATT (o‘z)"}, {"id": "315261102773", "name": "ABDUXAKIMOV SARDORJON SARVAR O‘G‘LI", "group": "13mt-26 ATT (o‘z)"}, {"id": "315261103372", "name": "NORMURODOV XOLMUROD HAMZAYEVICH", "group": "13mt-26 ATT (o‘z)"}, {"id": "315261102983", "name": "MUHAMMADJONOVA SAODATOY FAXRIDDIN QIZI", "group": "14mt-26 ATT (o‘z)"}, {"id": "315261102786", "name": "BO‘SINOV OZODBEK UMIDJON O‘G‘LI", "group": "14mt-26 ATT (o‘z)"}, {"id": "315261102792", "name": "ESHMAMATOV IBROHIM BAXRIDDIN O‘G‘LI", "group": "14mt-26 ATT (o‘z)"}, {"id": "315261102796", "name": "G‘OFIRJONOV JAHONGIR QOBILJON O‘G‘LI", "group": "14mt-26 ATT (o‘z)"}, {"id": "315261102865", "name": "MARDONOV SARVARBEK JASUR O‘G‘LI", "group": "14mt-26 ATT (o‘z)"}, {"id": "315261102782", "name": "BAHROMQULOV SHOHJAHON OLIMJON O‘G‘LI", "group": "14mt-26 ATT (o‘z)"}, {"id": "315261103012", "name": "MURTAZAYEV NODIRJON UMID O‘G‘LI", "group": "14mt-26 ATT (o‘z)"}, {"id": "315261102921", "name": "SHONAZAROV ANVAR YUSUFBOY O‘G‘LI", "group": "14mt-26 ATT (o‘z)"}, {"id": "315261102763", "name": "ABDULLAYEVA SOHIBA BAROT QIZI", "group": "14mt-26 ATT (o‘z)"}, {"id": "315261102889", "name": "PARDABOYEV OTABEK ALISHER O‘G‘LI", "group": "14mt-26 ATT (o‘z)"}, {"id": "315261102779", "name": "AXMATALIYEV IBROHIM ABRORJON O‘G‘LI", "group": "14mt-26 ATT (o‘z)"}, {"id": "315261102767", "name": "ABDURAHMANOV ASADBEK DILSHOD O‘G‘LI", "group": "14mt-26 ATT (o‘z)"}, {"id": "315261102849", "name": "KENJAYEVA XADICHA SOBIRJON QIZI", "group": "14mt-26 ATT (o‘z)"}, {"id": "315261102863", "name": "MAMIRJONOV MUXAMMADAZIZ MANSURBEK O‘G‘LI", "group": "14mt-26 ATT (o‘z)"}, {"id": "315261102845", "name": "KARIMOV G‘AYRATJON SHUHRAT O‘G‘LI", "group": "14mt-26 ATT (o‘z)"}, {"id": "315261102859", "name": "MAJIDOVA NOZIMA MAJIDOVNA", "group": "14mt-26 ATT (o‘z)"}];
const TEST_STUDENT_ID = "000000000000";

// 1. Mavzular taqsimoti qoidasi (Jami 30 ta savol)
const SAMPLE_RULES = {
    "Dasturlash tili va dastur kodini yozish": 4,
    "String va sonlar bilan ishlash": 4,
    "While sikli": 4,
    "Lug‘atlar bilan ishlash": 4,
    "Klasslar bilan ishlash": 4,
    "O‘zgaruvchilar va ma’lumot toifalari": 5,
    "Shartli ifodalar": 5
};

// Doimiy saqlash (Xavfsiz xotira: iOS Safari, Android, Telegram va Files ilovasi uchun)
const SafeStorage = {
    mem: {},
    getItem(k) {
        try {
            if (typeof localStorage !== "undefined") {
                const v = localStorage.getItem(k);
                if (v !== null) return v;
            }
        } catch(e) {}
        return this.mem[k] || null;
    },
    setItem(k, v) {
        try {
            if (typeof localStorage !== "undefined") {
                localStorage.setItem(k, v);
            }
        } catch(e) {}
        this.mem[k] = String(v);
    },
    removeItem(k) {
        try {
            if (typeof localStorage !== "undefined") {
                localStorage.removeItem(k);
            }
        } catch(e) {}
        delete this.mem[k];
    }
};

const SafeSession = {
    mem: {},
    getItem(k) {
        try {
            if (typeof sessionStorage !== "undefined") {
                const v = sessionStorage.getItem(k);
                if (v !== null) return v;
            }
        } catch(e) {}
        return this.mem[k] || null;
    },
    setItem(k, v) {
        try {
            if (typeof sessionStorage !== "undefined") {
                sessionStorage.setItem(k, v);
            }
        } catch(e) {}
        this.mem[k] = String(v);
    },
    removeItem(k) {
        try {
            if (typeof sessionStorage !== "undefined") {
                sessionStorage.removeItem(k);
            }
        } catch(e) {}
        delete this.mem[k];
    }
};

const STORAGE_KEY_STUDENTS = "py_exam_students_data_v1";
const STORAGE_KEY_AUDIT = "py_exam_audit_logs_v1";
const STORAGE_KEY_TEACHER_AUTH = "py_exam_teacher_auth_v1";
const STORAGE_KEY_TEACHER_PASS_HASH = "py_exam_teacher_hash_v1";
const STORAGE_KEY_ACTIVE_EXAM = "py_exam_active_session_v1";
const STORAGE_KEY_ACTIVE_VIEW = "py_exam_active_view_v1";
const STORAGE_KEY_LAST_RESULT = "py_exam_last_result_v1";
const STORAGE_KEY_PENDING_STUDENT = "py_exam_pending_student_v1";

// Standart o‘qituvchi xeshi
const DEFAULT_TEACHER_HASH = "f1dc2cd6";

// Global holat
let pendingStudent = null; // Kirish qilgan, lekin testni hali boshlamagan talaba
let currentStudent = null; // Testni boshlagan talaba
let currentQuestions = [];
let currentAnswers = {};
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

// Xavfsizlik: noto‘g‘ri urinishlar cheklovi
let failedLoginAttempts = 0;
let loginLockoutUntil = 0;

// Xavfsiz nazorat kodi (Checksum)
function generateChecksum(str) {
    let h1 = 0x811c9dc5, h2 = 0x5b79e234;
    for (let i = 0; i < str.length; i++) {
        const c = str.charCodeAt(i);
        h1 = Math.imul(h1 ^ c, 0x01000193);
        h2 = Math.imul(h2 ^ (c << 3), 0x01000193);
    }
    const part1 = (h1 >>> 0).toString(16).padStart(8, '0');
    const part2 = (h2 >>> 0).toString(16).padStart(8, '0');
    return part1.substring(0, 4) + part2.substring(0, 4);
}

// Sahifalar (View) almashinuvi
function switchView(viewName) {
    const secReg = document.getElementById("sectionRegister");
    const secReady = document.getElementById("sectionReady");
    const secExam = document.getElementById("sectionExam");
    const secRes = document.getElementById("sectionResult");
    const secTeach = document.getElementById("sectionTeacher");

    const all = [secReg, secReady, secExam, secRes, secTeach];
    all.forEach(sec => {
        if (sec) {
            sec.classList.add("hidden");
            sec.style.display = "none";
        }
    });

    let target = null;
    if (viewName === "register") target = secReg;
    else if (viewName === "ready") target = secReady;
    else if (viewName === "exam") target = secExam;
    else if (viewName === "result") target = secRes;
    else if (viewName === "teacher") target = secTeach;

    if (target) {
        target.classList.remove("hidden");
        target.style.display = "block";
    }

    // Aktiv view holatini saqlash (faqat exam yoki result bo‘lsa)
    try {
        if (viewName === "exam" || viewName === "result" || viewName === "teacher") {
            SafeStorage.setItem(STORAGE_KEY_ACTIVE_VIEW, viewName);
        } else {
            SafeStorage.setItem(STORAGE_KEY_ACTIVE_VIEW, "register");
        }
    } catch(e) {}

    // Agar o‘qituvchi panelidan chiqilsa taymerni to'xtatish
    if (viewName !== "teacher") {
        stopTeacherAutoRefresh();
    }

    window.scrollTo({ top: 0, behavior: 'smooth' });
}

// Talaba ID kiritilganda avtomatik ro‘yxatdan qidirish va to'ldirish
function handleStudentIdInput(input) {
    if (!input) return;
    input.value = input.value.replace(/\D/g, '').slice(0, 12);
    const idVal = input.value;
    const statusEl = document.getElementById("idLookupStatus");
    const nameEl = document.getElementById("regFullName");
    const groupEl = document.getElementById("regGroup");
    const dirEl = document.getElementById("regDirection");
    const crsEl = document.getElementById("regCourse");
    const submitBtn = document.getElementById("btnSubmitStart");

    if (idVal.length < 12) {
        if (statusEl) {
            statusEl.innerHTML = '<span class="text-slate-500">12 xonali HEMIS ID kiriting (' + idVal.length + '/12)</span>';
        }
        if (submitBtn) {
            submitBtn.disabled = false;
            submitBtn.classList.remove("opacity-50", "cursor-not-allowed");
        }
        return;
    }

    // Sinov talabasi (O'qituvchi sinov rejimi - CHEKLOVLARSIZ)
    if (idVal === TEST_STUDENT_ID) {
        if (nameEl) nameEl.value = "O'QITUVCHI SINOV TALABASI (TEST REJIMI)";
        if (groupEl) groupEl.value = "SINOV (TEST)";
        if (dirEl) dirEl.value = "Axborot tizimlari va texnologiyalari";
        if (crsEl) crsEl.value = "1";
        if (statusEl) {
            statusEl.innerHTML = '<span class="text-amber-700 font-bold bg-amber-50 px-2 py-0.5 rounded border border-amber-200">🧪 O\'qituvchi sinov rejimi faol (Cheklovlarsiz)</span>';
        }
        if (submitBtn) {
            submitBtn.disabled = false;
            submitBtn.classList.remove("opacity-50", "cursor-not-allowed");
        }
        return;
    }

    const found = STUDENTS_ROSTER.find(s => s.id === idVal);
    if (found) {
        if (nameEl) nameEl.value = found.name;
        if (groupEl) groupEl.value = found.group;
        if (dirEl) dirEl.value = "Axborot tizimlari va texnologiyalari";
        if (crsEl) crsEl.value = "1";

        function processTestedCheck(alreadyTested) {
            if (alreadyTested) {
                if (statusEl) {
                    statusEl.innerHTML = '<span class="text-rose-700 font-bold bg-rose-50 px-2 py-0.5 rounded border border-rose-200">⚠️ Ushbu talaba allaqachon test topshirgan! Qayta topshirish taqiqlanadi.</span>';
                }
                if (submitBtn) {
                    submitBtn.disabled = true;
                    submitBtn.classList.add("opacity-50", "cursor-not-allowed");
                }
                alert("Hurmatli " + found.name + " (ID: " + idVal + ")!\nSiz allaqachon ushbu joriy nazoratni topshirgansiz.\n\nQayta topshirish qat\'iyan taqiqlanadi! Sizga faqat avvalgi natijangiz ko\'rsatiladi.");
                showResultPage(alreadyTested);
            } else {
                if (statusEl) {
                    statusEl.innerHTML = '<span class="text-emerald-700 font-bold bg-emerald-50 px-2 py-0.5 rounded border border-emerald-200">✓ Talaba aniqlandi (' + found.group + ')</span>';
                }
                if (submitBtn) {
                    submitBtn.disabled = false;
                    submitBtn.classList.remove("opacity-50", "cursor-not-allowed");
                }
            }
        }

        // Agar server orqali ishlayotgan bo‘lsa, o‘qituvchi o‘chirganmi yoki yo'qmi tekshirish
        if (window.location.protocol.startsWith('http')) {
            fetch('/api/check_student_status?id=' + encodeURIComponent(idVal))
                .then(r => r.json())
                .then(d => {
                    if (d && d.tested && d.session) {
                        processTestedCheck({
                            studentId: idVal,
                            fullName: d.session.fullName,
                            groupName: d.session.groupName,
                            totalScore: d.session.totalScore,
                            maxScore: 30,
                            statusText: d.session.statusText,
                            finishedAt: d.session.finishedAt
                        });
                    } else {
                        // O'qituvchi o‘chirgan yoki hali topshirmagan bo‘lsa - ruxsat berish
                        const curList = getStoredStudents().filter(s => s.studentId !== idVal);
                        SafeStorage.setItem(STORAGE_KEY_STUDENTS, JSON.stringify(curList));
                        processTestedCheck(null);
                    }
                })
                .catch(() => {
                    const existingList = getStoredStudents();
                    const alreadyTested = existingList.find(s => s.studentId === idVal);
                    processTestedCheck(alreadyTested);
                });
            return;
        } else {
            const existingList = getStoredStudents();
            const alreadyTested = existingList.find(s => s.studentId === idVal);
            processTestedCheck(alreadyTested);
            return;
        }
    } else {
        if (statusEl) {
            statusEl.innerHTML = '<span class="text-rose-700 font-bold bg-rose-50 px-2 py-0.5 rounded border border-rose-200">❌ Ushbu ID rasmiy talabalar ro\'yxatida topilmadi!</span>';
        }
        if (nameEl) nameEl.value = "";
        if (groupEl) groupEl.value = "";
        if (submitBtn) {
            submitBtn.disabled = false;
            submitBtn.classList.remove("opacity-50", "cursor-not-allowed");
        }
    }
}

function setTeacherDemoMode() {
    const idInput = document.getElementById("regStudentId");
    if (idInput) {
        idInput.value = TEST_STUDENT_ID;
        handleStudentIdInput(idInput);
    }
}

// Dastur ishga tushganda (yoki sahifa yangilanganda) holatni tiklash
window.addEventListener("DOMContentLoaded", () => {
    initSecurityListeners();
    restoreStateOnLoad();
});


// Avval topshirilgan, lekin serverga yetib bormay qolgan natijalarni avtomatik qayta yuklash
function autoSyncLocalResultToServer() {
    try {
        if (typeof window === 'undefined' || !window.location.protocol.startsWith('http')) return;
        const lastResRaw = SafeStorage.getItem(STORAGE_KEY_LAST_RESULT);
        if (lastResRaw) {
            const lastRes = JSON.parse(lastResRaw);
            if (lastRes && lastRes.studentId && lastRes.fullName) {
                fetch('/api/direct_submit', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify(lastRes),
                    keepalive: true
                }).then(r => r.json()).then(data => {
                    if (data && data.success) {
                        console.log("Natija serverga muvaffaqiyatli sinxronlandi:", lastRes.studentId);
                    }
                }).catch(() => {});
            }
        }
    } catch(e) {}
}

function restoreStateOnLoad() {
    autoSyncLocalResultToServer();
    // 1. Faol test jarayonini tekshirish (faqat agar test avval boshlangan bo‘lsa)
    const rawExam = SafeStorage.getItem(STORAGE_KEY_ACTIVE_EXAM);
    if (rawExam) {
        try {
            const session = JSON.parse(rawExam);
            if (session && session.student && session.questions && session.questions.length === 30) {
                const now = Date.now();
                const startTime = session.startTimeMs || now;
                const elapsed = Math.floor((now - startTime) / 1000);
                const duration = session.durationSeconds || 3600;
                const remaining = duration - elapsed;

                if (remaining <= 0) {
                    currentStudent = session.student;
                    currentQuestions = session.questions;
                    currentAnswers = session.answers || {};
                    tabSwitchCount = session.tabSwitchCount || 0;
                    alert("Sahifa yangilanganda test vaqti (60 daqiqa) tugaganligi aniqlandi. Natijalaringiz avtomatik hisoblandi!");
                    submitExamNow();
                    return;
                }

                // Testni tiklash (Vaqt o‘z holicha davom etadi)
                currentStudent = session.student;
                currentQuestions = session.questions;
                currentAnswers = session.answers || {};
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

                if (tabSwitchCount > 0) {
                    const badgeSwitches = document.getElementById("badgeTabSwitches");
                    if (badgeSwitches) badgeSwitches.classList.remove("hidden");
                    const textSwitches = document.getElementById("textTabSwitches");
                    if (textSwitches) textSwitches.textContent = tabSwitchCount;
                    const violationCountBadge = document.getElementById("violationCountBadge");
                    if (violationCountBadge) violationCountBadge.textContent = tabSwitchCount;
                }

                switchView("exam");
                renderQuestionsMap();
                loadQuestion(currentQuestionIdx);
                startTimer();
                return;
            }
        } catch(e) {}
    }

    // 2. Oxirgi natija mavjud bo‘lsa
    const rawRes = SafeStorage.getItem(STORAGE_KEY_LAST_RESULT);
    if (rawRes) {
        try {
            const res = JSON.parse(rawRes);
            if (res && res.fullName) {
                showResultPage(res);
                return;
            }
        } catch(e) {}
    }

    // 3. Standart: Ro'yxatdan o'tish (bosh sahifa)
    switchView("register");
}

// Xavfsizlik va Anti-cheat
function initSecurityListeners() {
    document.addEventListener("contextmenu", (e) => {
        if (isExamActive) { e.preventDefault(); return false; }
    });
    document.addEventListener("copy", (e) => {
        if (isExamActive) { e.preventDefault(); return false; }
    });
    document.addEventListener("cut", (e) => {
        if (isExamActive) { e.preventDefault(); return false; }
    });
    document.addEventListener("selectstart", (e) => {
        if (isExamActive) { e.preventDefault(); return false; }
    });

    document.addEventListener("visibilitychange", () => {
        if (isExamActive && document.hidden && !isPageUnloading) {
            triggerTabViolation();
        }
    });

    window.addEventListener("blur", () => {
        if (isExamActive && !isPageUnloading) {
            triggerTabViolation();
        }
    });

    window.addEventListener("beforeunload", () => {
        isPageUnloading = true;
        if (isExamActive) {
            saveActiveExamState();
        }
    });
}

// Faol test holatini doimiy saqlash
function saveActiveExamState() {
    if (!isExamActive || !currentStudent) return;
    try {
        const payload = {
            student: currentStudent,
            questions: currentQuestions,
            answers: currentAnswers,
            currentQuestionIdx: currentQuestionIdx,
            startTimeMs: examStartTimeMs,
            durationSeconds: 3600,
            tabSwitchCount: tabSwitchCount
        };
        SafeStorage.setItem(STORAGE_KEY_ACTIVE_EXAM, JSON.stringify(payload));
    } catch(e) {}
}

// Qoidabuzarlik modalini ochish
function triggerTabViolation() {
    if (isViolationModalOpen || !isExamActive || isPageUnloading) return;
    tabSwitchCount++;
    saveActiveExamState();
    const badgeCount = document.getElementById("violationCountBadge");
    if (badgeCount) badgeCount.textContent = tabSwitchCount;

    const textSwitches = document.getElementById("textTabSwitches");
    if (textSwitches) textSwitches.textContent = tabSwitchCount;

    const badgeSwitches = document.getElementById("badgeTabSwitches");
    if (badgeSwitches) { badgeSwitches.classList.remove("hidden"); badgeSwitches.style.display = "inline-flex"; }

    isViolationModalOpen = true;
    const modal = document.getElementById("modalViolation");
    if (modal) { modal.classList.remove("hidden"); modal.style.display = "flex"; }
}

function closeViolationModal() {
    const modal = document.getElementById("modalViolation");
    if (modal) { modal.classList.add("hidden"); modal.style.display = "none"; }
    isViolationModalOpen = false;
}

// =========================================================================
// 1. RO'YXATDAN O'TISH VA TAYYORGARLIK BOSQICHI (VAQT HALI KETMAYDI!)
// =========================================================================

function handleRegisterSubmit(e) {
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

    // 2. Talaba ID 12 ta raqam bo‘lishi shart!
    if (!/^\d{12}$/.test(studentId)) {
        alert("Xatolik: Talaba ID 12 ta raqamdan iborat bo‘lishi kerak! (Masalan: 315261102911)");
        if (idInput) idInput.focus();
        return false;
    }

    // 3. Rasmiy ro‘yxatda mavjudligini tekshirish
    const isTestMode = (studentId === TEST_STUDENT_ID);
    if (!isTestMode) {
        const foundInRoster = STUDENTS_ROSTER.find(s => s.id === studentId);
        if (!foundInRoster) {
            alert("Xatolik: Kiritilgan Talaba ID (" + studentId + ") rasmiy talabalar ro‘yxatida topilmadi! Faqat ro‘yxatga kiritilgan talabalar test topshira oladi.");
            if (idInput) idInput.focus();
            return false;
        }

        // 4. BIR MARTA TOPSHIRISH QAT'IY TALABI (Faqat testni yakunlagan bo‘lsa bloklanadi!)
        const existingStudents = getStoredStudents();
        const alreadyTested = existingStudents.find(s => s.studentId === studentId);

        if (alreadyTested) {
            alert("Hurmatli " + alreadyTested.fullName + " (ID: " + studentId + ")!\nSiz allaqachon ushbu joriy nazorat testini topshirib, yakunlagansiz.\n\nTo'plangan ball: " + alreadyTested.totalScore + " / 30 (" + alreadyTested.statusText + ").\nTopshirilgan vaqt: " + (alreadyTested.finishedAt || alreadyTested.startedAt) + "\n\nNizomga muvofiq, har bir talaba testni faqat 1 MARTA topshirishi mumkin. Qayta kirish va qayta ishlash qat'iyan taqiqlanadi!");
            showResultPage(alreadyTested);
            return false;
        }
    }

    // Talaba ma'lumotlarini tayyorlash (Lekin test hali boshlanmadi!)
    pendingStudent = {
        studentId: studentId,
        fullName: fullName,
        direction: direction,
        course: parseInt(course) || 1,
        groupName: groupName,
        subject: "Dasturlash"
    };

    // Tayyorgarlik (Ready) oynasiga ma'lumotlarni o'tkazish
    document.getElementById("readyStudentId").textContent = pendingStudent.studentId;
    document.getElementById("readyStudentName").textContent = pendingStudent.fullName;
    document.getElementById("readyStudentGroup").textContent = pendingStudent.groupName;

    // Tayyorgarlik oynasiga o'tish (Vaqt hisoblanmaydi! Talaba chiqib ketsa qayta kirishi mumkin)
    switchView("ready");
    return false;
}

// =========================================================================
// 2. TESTNI HAQIQATDA BOSHLASH (FAQAT SHU TUGMA BOSILGANDAN SO'NG VAQT KETADI)
// =========================================================================

function startExamActual() {
    if (!pendingStudent) {
        switchView("register");
        return;
    }

    currentStudent = Object.assign({}, pendingStudent);
    currentStudent.startedAt = new Date().toLocaleString("uz-UZ");
    currentStudent.tabSwitchCount = 0;

    // 30 ta savolni tanlash
    currentQuestions = generateRandomExamQuestions();
    currentAnswers = {};
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
}

// Mavzu nomini normallashtirish
function normalizeTopicName(s) {
    return (s || "").replace(/[`'‘’ʻʼ]/g, "'").toLowerCase().trim();
}

// 30 ta savolni 7 ta mavzudan tasodifiy tanlash
function generateRandomExamQuestions() {
    const poolByTopic = {};
    ALL_QUESTIONS.forEach(q => {
        const normKey = normalizeTopicName(q.topic);
        if (!poolByTopic[normKey]) poolByTopic[normKey] = [];
        poolByTopic[normKey].push(q);
    });

    const selected = [];
    for (const [topicName, neededCount] of Object.entries(SAMPLE_RULES)) {
        const normKey = normalizeTopicName(topicName);
        const pool = poolByTopic[normKey] || [];
        const shuffled = [...pool].sort(() => 0.5 - Math.random());
        const picked = shuffled.slice(0, neededCount);
        selected.push(...picked);
    }

    // Agar 30 ta to'lmagan bo‘lsa
    if (selected.length < 30) {
        const remaining = ALL_QUESTIONS.filter(q => !selected.includes(q));
        const shuffled = [...remaining].sort(() => 0.5 - Math.random());
        selected.push(...shuffled.slice(0, 30 - selected.length));
    }

    return selected.sort(() => 0.5 - Math.random());
}

// Savollar xaritasini chizish
function renderQuestionsMap() {
    const grid = document.getElementById("questionsMapGrid");
    if (!grid) return;
    grid.innerHTML = "";

    currentQuestions.forEach((q, idx) => {
        const btn = document.createElement("button");
        btn.type = "button";
        btn.id = "mapBtn_" + idx;
        btn.onclick = () => loadQuestion(idx);

        const isAnswered = currentAnswers[idx] !== undefined;
        const isCurrent = currentQuestionIdx === idx;

        let cls = "w-full py-2 rounded-xl text-xs font-bold transition-all border flex items-center justify-center ";
        if (isCurrent) {
            cls += "border-blue-600 bg-blue-50 text-blue-700 ring-2 ring-blue-500/20";
        } else if (isAnswered) {
            cls += "bg-blue-600 border-blue-600 text-white shadow-sm";
        } else {
            cls += "bg-white border-slate-200 text-slate-700 hover:bg-slate-50";
        }

        btn.className = cls;
        btn.textContent = idx + 1;
        grid.appendChild(btn);
    });

    const answeredCount = Object.keys(currentAnswers).length;
    const answeredEl = document.getElementById("mapAnsweredCount");
    if (answeredEl) answeredEl.textContent = answeredCount;
}

// Savolni yuklash
function loadQuestion(idx) {
    if (idx < 0 || idx >= currentQuestions.length) return;
    currentQuestionIdx = idx;

    const q = currentQuestions[idx];
    document.getElementById("qCurrentNumber").textContent = idx + 1;
    document.getElementById("qProgressText").textContent = idx + 1;
    document.getElementById("qTopicBadge").textContent = q.topic;

    const diffBadge = document.getElementById("qDifficultyBadge");
    if (diffBadge) {
        diffBadge.textContent = q.difficulty || "O'rtacha";
        if (q.difficulty === "Oson") diffBadge.className = "text-xs px-2.5 py-0.5 rounded-full font-medium bg-emerald-50 text-emerald-700 border border-emerald-200";
        else if (q.difficulty === "Qiyin") diffBadge.className = "text-xs px-2.5 py-0.5 rounded-full font-medium bg-rose-50 text-rose-700 border border-rose-200";
        else diffBadge.className = "text-xs px-2.5 py-0.5 rounded-full font-medium bg-amber-50 text-amber-700 border border-amber-200";
    }

    document.getElementById("qQuestionText").textContent = q.question;

    const codeBox = document.getElementById("qCodeBlock");
    const codeContent = document.getElementById("qCodeContent");
    if (q.code && q.code.trim()) {
        codeContent.textContent = q.code;
        codeBox.classList.remove("hidden");
        codeBox.style.display = "block";
    } else {
        codeBox.classList.add("hidden");
        codeBox.style.display = "none";
    }

    const optionsContainer = document.getElementById("qOptionsList");
    optionsContainer.innerHTML = "";
    const letters = ["A", "B", "C", "D"];

    q.options.forEach((optText, optIdx) => {
        const isChecked = currentAnswers[idx] === optIdx;
        const optCard = document.createElement("label");
        optCard.className = "option-card flex items-center gap-3 p-3.5 sm:p-4 rounded-2xl border transition-all cursor-pointer select-none " + 
            (isChecked ? "border-blue-600 bg-blue-50/80 shadow-sm" : "border-slate-200 bg-white hover:border-slate-300 hover:bg-slate-50/50");

        optCard.innerHTML = 
            '<input type="radio" name="exam_option" value="' + optIdx + '" class="w-4 h-4 text-blue-600 border-slate-300 focus:ring-blue-500" ' + (isChecked ? "checked" : "") + ' onchange="selectAnswer(' + idx + ', ' + optIdx + ')">' +
            '<span class="w-6 h-6 rounded-lg bg-slate-100 text-slate-700 font-bold text-xs flex items-center justify-center shrink-0">' + letters[optIdx] + '</span>' +
            '<span class="text-xs sm:text-sm font-medium text-slate-800 leading-snug">' + escapeHtml(optText) + '</span>';

        optionsContainer.appendChild(optCard);
    });

    const btnPrev = document.getElementById("btnPrevQ");
    const btnNext = document.getElementById("btnNextQ");
    if (btnPrev) btnPrev.disabled = (idx === 0);
    if (btnNext) {
        if (idx === currentQuestions.length - 1) {
            btnNext.innerHTML = '<span>Yakunlash</span> <i class="fa-solid fa-flag-checkered"></i>';
            btnNext.onclick = confirmFinishModalOpen;
        } else {
            btnNext.innerHTML = '<span>Keyingi</span> <i class="fa-solid fa-arrow-right"></i>';
            btnNext.onclick = nextQuestion;
        }
    }

    renderQuestionsMap();
    saveActiveExamState();
}

function selectAnswer(qIdx, optIdx) {
    currentAnswers[qIdx] = optIdx;
    renderQuestionsMap();
    saveActiveExamState();
}

function nextQuestion() {
    if (currentQuestionIdx < currentQuestions.length - 1) {
        loadQuestion(currentQuestionIdx + 1);
    }
}

function prevQuestion() {
    if (currentQuestionIdx > 0) {
        loadQuestion(currentQuestionIdx - 1);
    }
}

// Taymer (60 daqiqa)
function startTimer() {
    clearInterval(timerInterval);
    updateTimerDisplay();

    timerInterval = setInterval(() => {
        if (!isExamActive) {
            clearInterval(timerInterval);
            return;
        }

        remainingSeconds--;
        updateTimerDisplay();

        if (remainingSeconds <= 0) {
            clearInterval(timerInterval);
            alert("Vaqt tugadi! Test natijalaringiz avtomatik hisoblandi va o‘qituvchiga saqlandi.");
            submitExamNow();
        }
    }, 1000);
}

function updateTimerDisplay() {
    const timerDisplay = document.getElementById("timerDisplay");
    if (!timerDisplay) return;

    const mins = Math.floor(Math.max(0, remainingSeconds) / 60);
    const secs = Math.max(0, remainingSeconds) % 60;
    const formatted = String(mins).padStart(2, '0') + ":" + String(secs).padStart(2, '0');
    timerDisplay.textContent = formatted;

    const timerIcon = document.getElementById("timerIcon");
    if (remainingSeconds < 300) { // 5 daqiqadan kam
        timerDisplay.classList.add("text-rose-600");
        if (timerIcon) timerIcon.className = "w-8 h-8 rounded-lg bg-rose-100 text-rose-600 flex items-center justify-center text-sm animate-bounce";
    } else {
        timerDisplay.classList.remove("text-rose-600");
        if (timerIcon) timerIcon.className = "w-8 h-8 rounded-lg bg-amber-100 text-amber-600 flex items-center justify-center text-sm";
    }
}

// Yakunlash modali
function confirmFinishModalOpen() {
    const answeredCount = Object.keys(currentAnswers).length;
    document.getElementById("modalAnsweredCount").textContent = answeredCount;
    const modal = document.getElementById("modalFinishConfirm");
    if (modal) { modal.classList.remove("hidden"); modal.style.display = "flex"; }
}

function closeFinishModal() {
    const modal = document.getElementById("modalFinishConfirm");
    if (modal) { modal.classList.add("hidden"); modal.style.display = "none"; }
}

// =========================================================================
// 3. TESTNI YAKUNLASH VA NATIJANI SAQLASH (SHUNDAN SO'NG QAYTA KIROLMAYDI)
// =========================================================================

function submitExamNow() {
    closeFinishModal();
    clearInterval(timerInterval);
    isExamActive = false;

    // Faol test seansini tozalash
    try {
        SafeStorage.removeItem(STORAGE_KEY_ACTIVE_EXAM);
    } catch(e) {}

    let correctCount = 0;
    currentQuestions.forEach((q, idx) => {
        if (currentAnswers[idx] === q.correct) {
            correctCount++;
        }
    });

    const incorrectCount = 30 - correctCount;
    const totalScore = correctCount; // 1 ball har bir to‘g‘ri javob uchun
    const statusText = (totalScore >= 18) ? "Joriy nazoratdan o‘tdi" : "Joriy nazoratdan o‘tmadi";
    const finishedAt = new Date().toLocaleString("uz-UZ");

    const completedResult = {
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
    };

    // DARHOL O'QITUVCHI BAZASIGA SAQLASH (SHUNDAN SO'NG BU TALABA ID BLOKLANADI!)
    saveStudentResult(completedResult);

    // Markaziy serverga kafolatli yuborish (keepalive va takroriy urinish bilan)
    function sendResultToServer(payload, retriesLeft = 3) {
        if (!window.location.protocol.startsWith('http')) return;
        fetch('/api/direct_submit', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(payload),
            keepalive: true
        }).then(r => r.json()).then(d => {
            if (d && d.success) {
                console.log("Server natijani qabul qildi ✓");
            } else if (retriesLeft > 0) {
                setTimeout(() => sendResultToServer(payload, retriesLeft - 1), 2000);
            }
        }).catch(() => {
            if (retriesLeft > 0) {
                setTimeout(() => sendResultToServer(payload, retriesLeft - 1), 3000);
            }
        });
    }
    try {
        sendResultToServer(completedResult);
    } catch(e) {}

    try {
        SafeStorage.setItem(STORAGE_KEY_LAST_RESULT, JSON.stringify(completedResult));
        SafeStorage.setItem(STORAGE_KEY_ACTIVE_VIEW, "result");
    } catch(e) {}

    showResultPage(completedResult);
}

// Natija sahifasi
function showResultPage(result) {
    currentResultObject = result;
    switchView("result");
    try {
        SafeStorage.setItem(STORAGE_KEY_LAST_RESULT, JSON.stringify(result));
    } catch(e) {}

    const isPassed = result.totalScore >= 18;
    const idEl = document.getElementById("resStudentId");
    if (idEl) idEl.textContent = result.studentId || "-";

    document.getElementById("resultStatusText").textContent = result.statusText;
    document.getElementById("resultScore").textContent = result.totalScore;
    document.getElementById("resultCorrectCount").textContent = result.correctCount + " ta to‘g‘ri";
    document.getElementById("resultIncorrectCount").textContent = result.incorrectCount + " ta noto‘g‘ri";

    document.getElementById("resStudentName").textContent = result.fullName;
    document.getElementById("resStudentDirection").textContent = result.direction + " (" + result.course + "-kurs)";
    document.getElementById("resStudentGroup").textContent = result.groupName;
    document.getElementById("resDate").textContent = result.finishedAt || result.startedAt;
    document.getElementById("resSwitches").textContent = (result.tabSwitchCount || 0) + " marta";

    const colorBar = document.getElementById("resultColorBar");
    const iconBox = document.getElementById("resultIconBox");
    const icon = document.getElementById("resultIcon");

    if (isPassed) {
        colorBar.className = "absolute top-0 left-0 right-0 h-3 bg-emerald-500";
        iconBox.className = "w-20 h-20 rounded-full bg-emerald-100 text-emerald-600 flex items-center justify-center text-4xl shadow-lg shadow-emerald-500/20 ring-8 ring-emerald-50";
        icon.className = "fa-solid fa-circle-check";
    } else {
        colorBar.className = "absolute top-0 left-0 right-0 h-3 bg-rose-500";
        iconBox.className = "w-20 h-20 rounded-full bg-rose-100 text-rose-600 flex items-center justify-center text-4xl shadow-lg shadow-rose-500/20 ring-8 ring-rose-50";
        icon.className = "fa-solid fa-circle-xmark";
    }
}

function navigateHome() {
    if (isExamActive) {
        if (!confirm("Test jarayonida bosh sahifaga o'tsangiz, test avtomatik yakunlanadi. Davom etasizmi?")) {
            return;
        }
        submitExamNow();
        return;
    }
    try {
        SafeStorage.removeItem(STORAGE_KEY_LAST_RESULT);
    } catch(e) {}
    switchView("register");
}

// =========================================================================
// 4. O'QITUVCHI BOSHQARUVI: VEDOMOST, STATISTIKA VA AMALLAR
// =========================================================================

function toggleTeacherSection() {
    if (isExamActive) {
        alert("Diqqat! Test jarayonida o‘qituvchi bo‘limiga kirish taqiqlanadi!");
        return;
    }
    switchView("teacher");

    const isAuth = (SafeSession.getItem(STORAGE_KEY_TEACHER_AUTH) === "true") ||
                   (SafeStorage.getItem(STORAGE_KEY_TEACHER_AUTH) === "true");
    const loginForm = document.getElementById("teacherLoginForm");
    const dash = document.getElementById("teacherDashboard");

    if (isAuth) {
        if (loginForm) { loginForm.classList.add("hidden"); loginForm.style.display = "none"; }
        if (dash) { dash.classList.remove("hidden"); dash.style.display = "block"; }
        renderTeacherTable();
        startTeacherAutoRefresh();
    } else {
        stopTeacherAutoRefresh();
        if (loginForm) { loginForm.classList.remove("hidden"); loginForm.style.display = "block"; }
        if (dash) { dash.classList.add("hidden"); dash.style.display = "none"; }
        const u = document.getElementById("teachLoginInput");
        const p = document.getElementById("teachPassInput");
        if (u) u.value = "";
        if (p) p.value = "";
    }
}

// O‘qituvchi kirishini tekshirish
function handleTeacherLogin(e) {
    if (e && e.preventDefault) e.preventDefault();

    const u = document.getElementById("teachLoginInput").value.trim();
    const p = document.getElementById("teachPassInput").value.trim();

    if (!u || !p) {
        alert("Login va parolni kiriting!");
        return false;
    }

    // Login: admin, Parol: admin123 (yoki admin 123)
    const storedHash = SafeStorage.getItem(STORAGE_KEY_TEACHER_PASS_HASH) || generateChecksum("admin 123");
    const enteredHash = generateChecksum(p);

    const isDefaultAdmin = (u === "admin" && (p === "admin123" || p === "admin 123"));
    const isCustomAdmin = (u === "admin" && enteredHash === storedHash);

    if (isDefaultAdmin || isCustomAdmin) {
        SafeSession.setItem(STORAGE_KEY_TEACHER_AUTH, "true");
        SafeStorage.setItem(STORAGE_KEY_TEACHER_AUTH, "true");
        const loginForm = document.getElementById("teacherLoginForm");
        const dash = document.getElementById("teacherDashboard");
        if (loginForm) { loginForm.classList.add("hidden"); loginForm.style.display = "none"; }
        if (dash) { dash.classList.remove("hidden"); dash.style.display = "block"; }
        renderTeacherTable();
        startTeacherAutoRefresh();
    } else {
        alert("Xatolik: Login yoki parol noto‘g‘ri! Ruxsatsiz kirish taqiqlanadi.");
    }
    return false;
}

function teacherLogout() {
    SafeSession.removeItem(STORAGE_KEY_TEACHER_AUTH);
    SafeStorage.removeItem(STORAGE_KEY_TEACHER_AUTH);
    stopTeacherAutoRefresh();
    const loginForm = document.getElementById("teacherLoginForm");
    const dash = document.getElementById("teacherDashboard");
    if (loginForm) { loginForm.classList.remove("hidden"); loginForm.style.display = "block"; }
    if (dash) { dash.classList.add("hidden"); dash.style.display = "none"; }
    try {
        SafeStorage.setItem(STORAGE_KEY_ACTIVE_VIEW, "register");
    } catch(e) {}
    switchView("register");
}

// O‘qituvchi parolini o‘zgartirish
function changeTeacherPassword() {
    const oldPass = prompt("Joriy parolingizni kiriting:");
    if (!oldPass) return;

    const oldHash = generateChecksum(oldPass.trim());
    const currentHash = SafeStorage.getItem(STORAGE_KEY_TEACHER_PASS_HASH) || generateChecksum("admin 123");

    const isStandardOld = (oldPass.trim() === "admin 123" || oldPass.trim() === "admin123");
    if (!isStandardOld && oldHash !== currentHash) {
        alert("Joriy parol noto‘g‘ri!");
        return;
    }

    const newPass = prompt("Yangi maxfiy parolni kiriting (kamida 6 ta belgi):");
    if (!newPass || newPass.trim().length < 6) {
        alert("Parol kamida 6 ta belgidan iborat bo‘lishi kerak!");
        return;
    }

    const confirmPass = prompt("Yangi parolni takrorlang:");
    if (newPass.trim() !== confirmPass.trim()) {
        alert("Parollar mos kelmadi!");
        return;
    }

    const newHash = generateChecksum(newPass.trim());
    SafeStorage.setItem(STORAGE_KEY_TEACHER_PASS_HASH, newHash);
    alert("Parolingiz muvaffaqiyatli o‘zgartirildi! Yangi parolingizni eslab qoling.");
}

let isSyncingServer = false;
function syncResultsFromServer() {
    if (isSyncingServer || typeof window === 'undefined' || !window.location.protocol.startsWith('http')) return;
    isSyncingServer = true;
    fetch('/api/teacher_results')
        .then(r => r.json())
        .then(data => {
            isSyncingServer = false;
            if (data && data.success && Array.isArray(data.results)) {
                // Har bir talaba bo'yicha FAQAT eng so'nggi natijani olish (eski natijalar ustiga yozilmasligi uchun)
                const seenKeys = new Set();
                const serverList = [];
                data.results.forEach(sr => {
                    const key = (sr.student_id_number && sr.student_id_number !== '000000000000') 
                        ? sr.student_id_number 
                        : (sr.full_name + '__' + sr.group_name);
                    
                    // Agar 000000000000 bo‘lsa, har birini alohida emas, faqat eng oxirgisini olish
                    if (sr.student_id_number === '000000000000') {
                        if (!seenKeys.has('__TEST_STUDENT__')) {
                            seenKeys.add('__TEST_STUDENT__');
                            serverList.push(sr);
                        }
                    } else if (!seenKeys.has(key)) {
                        seenKeys.add(key);
                        serverList.push(sr);
                    }
                });

                // Serverdagi ro‘yxatni formatlash
                const formattedServerStudents = serverList.map(sr => ({
                    id: sr.session_id || Date.now(),
                    sessionId: sr.session_id,
                    studentId: sr.student_id_number || "",
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
                }));

                // Serverdan kelgan eng so'nggi ro‘yxatni asosiy qilib saqlash
                SafeStorage.setItem(STORAGE_KEY_STUDENTS, JSON.stringify(formattedServerStudents));

                const teachDash = document.getElementById("teacherDashboard");
                if (teachDash && teachDash.style.display !== "none") {
                    renderTeacherTable(true);
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

    const filtered = students.filter(s => {
        const q = searchQuery;
        const matchSearch = !q || 
            (s.studentId && s.studentId.includes(q)) ||
            s.fullName.toLowerCase().includes(q) ||
            String(s.groupName).toLowerCase().includes(q) ||
            (s.direction && s.direction.toLowerCase().includes(q));
        const matchGroup = !groupFilter || String(s.groupName) === groupFilter;
        return matchSearch && matchGroup;
    });

    const tbody = document.getElementById("teacherTableBody");
    tbody.innerHTML = "";

    if (filtered.length === 0) {
        tbody.innerHTML = '<tr><td colspan="10" class="py-8 text-center text-slate-400">Hech qanday natija topilmadi.</td></tr>';
        return;
    }

    filtered.forEach((st, idx) => {
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
                    '<button onclick="openDetailModal(' + st.id + ')" title="Batafsil ko‘rish" class="w-8 h-8 rounded-lg bg-blue-50 hover:bg-blue-100 text-blue-700 flex items-center justify-center transition-colors"><i class="fa-solid fa-eye"></i></button>' +
                    '<button onclick="openEditScoreModal(' + st.id + ')" title="Natijani tahrirlash (Audit)" class="w-8 h-8 rounded-lg bg-amber-50 hover:bg-amber-100 text-amber-700 flex items-center justify-center transition-colors"><i class="fa-solid fa-pen-to-square"></i></button>' +
                    '<button onclick="deleteStudentResult(' + st.id + ')" title="Talaba natijasini o‘chirish (qayta topshirishga ruxsat)" class="w-8 h-8 rounded-lg bg-rose-50 hover:bg-rose-100 text-rose-600 flex items-center justify-center transition-colors"><i class="fa-solid fa-trash-can"></i></button>' +
                '</div>' +
            '</td>';
        tbody.appendChild(tr);
    });
}

// 1. BATAFSIL KO'RISH MODALI
function openDetailModal(studentId) {
    const students = getStoredStudents();
    const st = students.find(s => s.id === studentId);
    if (!st) return;

    document.getElementById("detailModalName").textContent = st.fullName + " (ID: " + (st.studentId || "-") + ")";
    document.getElementById("detailModalMeta").textContent = st.groupName + " | " + st.direction + " (" + st.course + "-kurs) • Ball: " + st.totalScore + "/30 • Chiqishlar: " + (st.tabSwitchCount || 0) + " marta";

    const listContainer = document.getElementById("detailModalQuestionsList");
    listContainer.innerHTML = "";
    const letters = ["A", "B", "C", "D"];

    (st.questions || []).forEach((q, idx) => {
        const userChoice = st.answers ? st.answers[idx] : undefined;
        const isCorrect = userChoice === q.correct;
        const answered = userChoice !== undefined;

        const card = document.createElement("div");
        card.className = "p-4 rounded-2xl border " + (isCorrect ? "border-emerald-200 bg-emerald-50/30" : (answered ? "border-rose-200 bg-rose-50/30" : "border-slate-200 bg-slate-50/50"));
        
        let cardHTML = 
            '<div class="flex items-center justify-between mb-2">' +
                '<span class="font-bold text-slate-800">№ ' + (idx + 1) + '. [' + q.topic + ']</span>' +
                '<span class="px-2 py-0.5 rounded text-[10px] font-bold ' + (isCorrect ? 'bg-emerald-100 text-emerald-800' : 'bg-rose-100 text-rose-800') + '">' + (isCorrect ? "To‘g‘ri (+1 ball)" : "Noto‘g‘ri (0 ball)") + '</span>' +
            '</div>' +
            '<div class="font-medium text-slate-900 mb-2">' + escapeHtml(q.question) + '</div>';

        if (q.code) {
            cardHTML += '<pre class="p-3 bg-slate-900 text-slate-100 rounded-xl text-xs font-mono overflow-x-auto mb-3"><code>' + escapeHtml(q.code) + '</code></pre>';
        }

        cardHTML += '<div class="grid grid-cols-1 sm:grid-cols-2 gap-2">';
        q.options.forEach((opt, optIdx) => {
            const isUser = userChoice === optIdx;
            const isRight = optIdx === q.correct;
            let style = "border-slate-200 bg-white text-slate-700";
            let tag = "";
            if (isRight) {
                style = "border-emerald-500 bg-emerald-100/70 text-emerald-900 font-bold";
                tag = '<i class="fa-solid fa-check text-emerald-600"></i> (To‘g‘ri)';
            }
            if (isUser && !isRight) {
                style = "border-rose-500 bg-rose-100/70 text-rose-900 font-bold";
                tag = '<i class="fa-solid fa-xmark text-rose-600"></i> (Tanlangan)';
            }
            cardHTML += '<div class="p-2 rounded-lg border text-xs flex items-center justify-between ' + style + '">' +
                '<span><b>' + letters[optIdx] + ')</b> ' + escapeHtml(opt) + '</span>' +
                '<span class="text-[10px]">' + tag + '</span>' +
            '</div>';
        });
        cardHTML += '</div>';

        card.innerHTML = cardHTML;
        listContainer.appendChild(card);
    });

    const m = document.getElementById("modalDetail");
    if (m) { m.classList.remove("hidden"); m.style.display = "flex"; }
}

function closeDetailModal() {
    const m = document.getElementById("modalDetail");
    if (m) { m.classList.add("hidden"); m.style.display = "none"; }
}

// 2. TALABA NATIJASINI O'ZGARTIRISH (TAHRIRLASH)
function openEditScoreModal(studentId) {
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
    if (m) { m.classList.remove("hidden"); m.style.display = "flex"; }
}

function closeEditScoreModal() {
    const m = document.getElementById("modalEditScore");
    if (m) { m.classList.add("hidden"); m.style.display = "none"; }
}

function saveScoreEdit(e) {
    if (e && e.preventDefault) e.preventDefault();
    const studentId = parseInt(document.getElementById("editStudentIndex").value);
    const newFullName = document.getElementById("editStudentFullNameVal").value.trim();
    const newGroup = document.getElementById("editStudentGroupVal").value.trim();
    const newScore = parseInt(document.getElementById("editNewScoreVal").value);
    const reason = document.getElementById("editReasonVal").value.trim();

    if (!newFullName || !newGroup) {
        alert("F.I.Sh. va Guruh bo‘sh bo‘lishi mumkin emas!");
        return false;
    }

    if (isNaN(newScore) || newScore < 0 || newScore > 30 || !reason) {
        alert("Ball 0 dan 30 gacha bo‘lishi va o‘zgartirish sababi to'ldirilishi shart!");
        return false;
    }

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
    auditLogs.unshift({
        id: Date.now(),
        studentName: st.fullName + " (ID: " + (st.studentId || "-") + ")",
        oldScore: oldScore,
        newScore: newScore,
        oldStatus: oldStatus,
        newStatus: newStatus,
        reason: reason,
        teacher: "o‘qituvchi",
        time: new Date().toLocaleString("uz-UZ")
    });

    SafeStorage.setItem(STORAGE_KEY_STUDENTS, JSON.stringify(students));
    SafeStorage.setItem(STORAGE_KEY_AUDIT, JSON.stringify(auditLogs));

    closeEditScoreModal();
    renderTeacherTable();
    alert("Talaba ma'lumotlari va balli muvaffaqiyatli saqlandi!");
    return false;
}

// 3. TALABA NATIJASINI O'CHIRISH (QAYTA TOPSHIRISHGA RUXSAT BERISH)
function deleteStudentResult(studentId) {
    const students = getStoredStudents();
    const st = students.find(s => s.id === studentId || s.sessionId === studentId);
    if (!st) return;

    const confirmMsg = "Haqiqatan ham quyidagi talaba natijasini o‘chirmoqchimisiz?\n\n" +
        "• Talaba ID: " + (st.studentId || "-") + "\n" +
        "• F.I.Sh.: " + st.fullName + "\n" +
        "• Guruh: " + st.groupName + "\n" +
        "• Ball: " + st.totalScore + " / 30 (" + st.statusText + ")\n\n" +
        "DIQQAT: Natija o‘chirilgach, ushbu talaba testni qaytadan topshira oladi!";

    if (!confirm(confirmMsg)) {
        return;
    }

    // Server bazasidan ham to'liq o‘chirish (talaba qayta topshira olishi uchun)
    if (window.location.protocol.startsWith('http')) {
        fetch('/api/teacher/delete_student', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                sessionId: st.sessionId || st.id,
                studentId: st.studentId || "",
                fullName: st.fullName,
                groupName: st.groupName
            })
        }).then(r => r.json()).then(() => {
            syncResultsFromServer();
        }).catch(() => {});
    }

    // Mahalliy xotiradan o‘chirish
    const updatedStudents = students.filter(s => s.id !== studentId && s.sessionId !== studentId);
    SafeStorage.setItem(STORAGE_KEY_STUDENTS, JSON.stringify(updatedStudents));

    // Audit jurnaliga qayd etish
    const auditLogs = getStoredAudit();
    auditLogs.unshift({
        id: Date.now(),
        studentName: st.fullName + " (ID: " + (st.studentId || "-") + ", " + st.groupName + ")",
        oldScore: st.totalScore,
        newScore: 0,
        oldStatus: st.statusText,
        newStatus: "NATIJA O'CHIRILDI",
        reason: "O‘qituvchi tomonidan natija o‘chirildi (qayta topshirishga ruxsat berildi)",
        teacher: "o‘qituvchi",
        time: new Date().toLocaleString("uz-UZ")
    });
    SafeStorage.setItem(STORAGE_KEY_AUDIT, JSON.stringify(auditLogs));

    renderTeacherTable(true);
    alert("Talaba (" + st.fullName + ") natijasi muvaffaqiyatli o‘chirildi! Endi u testni qayta topshirishi mumkin.");
}

// Barcha natijalarni tozalash
function clearAllResults() {
    const students = getStoredStudents();
    if (students.length === 0) {
        alert("Jadval allaqachon bo‘sh!");
        return;
    }

    if (!confirm("DIQQAT! Barcha talabalar natijalarini tozalab tashlamoqchimisiz? Bu amal qaytarilmaydi!")) {
        return;
    }

    const checkPrompt = prompt("Tasdiqlash uchun 'TOZALASH' so‘zini yozing:");
    if (checkPrompt === "TOZALASH") {
        SafeStorage.removeItem(STORAGE_KEY_STUDENTS);
        renderTeacherTable();
        alert("Barcha talabalar natijalari muvaffaqiyatli tozalandi!");
    } else {
        alert("Tasdiqlash bekor qilindi.");
    }
}

function toggleAuditModal() {
    const modal = document.getElementById("modalAudit");
    if (!modal) return;
    if (modal.classList.contains("hidden") || modal.style.display === "none") {
        const logs = getStoredAudit();
        const tbody = document.getElementById("auditTableBody");
        tbody.innerHTML = "";
        if (logs.length === 0) {
            tbody.innerHTML = '<tr><td colspan="6" class="py-8 text-center text-slate-400">Audit jurnali hozircha bo\'sh.</td></tr>';
        } else {
            logs.forEach(l => {
                const tr = document.createElement("tr");
                tr.innerHTML = 
                    '<td class="py-2.5 px-3 font-semibold text-slate-900">' + escapeHtml(l.studentName) + '</td>' +
                    '<td class="py-2.5 px-3 text-center font-mono text-slate-500">' + l.oldScore + ' / 30</td>' +
                    '<td class="py-2.5 px-3 text-center font-mono font-bold text-blue-600">' + (l.newStatus === "NATIJA O'CHIRILDI" ? '-' : l.newScore + ' / 30') + '</td>' +
                    '<td class="py-2.5 px-3 text-center"><span class="px-2 py-0.5 rounded text-xs font-bold ' + (l.newStatus === "NATIJA O'CHIRILDI" ? 'bg-slate-200 text-slate-700' : (l.newScore >= 18 ? 'bg-emerald-100 text-emerald-800' : 'bg-rose-100 text-rose-800')) + '">' + l.newStatus + '</span></td>' +
                    '<td class="py-2.5 px-3 text-slate-700 italic">' + escapeHtml(l.reason) + '</td>' +
                    '<td class="py-2.5 px-3 text-center text-xs text-slate-500 font-mono">' + l.time + '</td>';
                tbody.appendChild(tr);
            });
        }
        modal.classList.remove("hidden");
        modal.style.display = "flex";
    } else {
        modal.classList.add("hidden");
        modal.style.display = "none";
    }
}

function exportToExcel() {
    const students = getStoredStudents();
    if (students.length === 0) {
        alert("Eksport qilish uchun talabalar natijalari mavjud emas!");
        return;
    }

    let csv = "\uFEFF"; // UTF-8 BOM
    csv += "№;Talaba ID;F.I.Sh.;Yo'nalish;Kurs;Guruh;To‘g‘ri;Noto‘g‘ri;To'plangan ball;Natija;Sana va vaqt;Sahifadan chiqishlar\n";

    students.forEach((s, idx) => {
        csv += '"' + (idx + 1) + '";"' + (s.studentId || "") + '";"' + s.fullName + '";"' + s.direction + '";"' + s.course + '-kurs";"' + s.groupName + '";"' + s.correctCount + '";"' + s.incorrectCount + '";"' + s.totalScore + ' / 30";"' + s.statusText + '";"' + (s.finishedAt || s.startedAt) + '";"' + (s.tabSwitchCount || 0) + ' marta"\n';
    });

    const blob = new Blob([csv], { type: "text/csv;charset=utf-8;" });
    const link = document.createElement("a");
    const url = URL.createObjectURL(blob);
    link.setAttribute("href", url);
    link.setAttribute("download", "Joriy_nazorat_natijalari_" + new Date().toISOString().slice(0, 10) + ".csv");
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
}

function getStoredStudents() {
    try {
        return JSON.parse(SafeStorage.getItem(STORAGE_KEY_STUDENTS)) || [];
    } catch(e) { return []; }
}

function saveStudentResult(res) {
    const list = getStoredStudents();
    const existingIdx = list.findIndex(s => 
        (res.studentId && s.studentId && s.studentId === res.studentId) ||
        (s.fullName.toLowerCase() === res.fullName.toLowerCase() && 
         String(s.groupName).trim() === String(res.groupName).trim())
    );
    if (existingIdx !== -1) {
        list[existingIdx] = res;
    } else {
        list.unshift(res);
    }
    SafeStorage.setItem(STORAGE_KEY_STUDENTS, JSON.stringify(list));
}

function getStoredAudit() {
    try {
        return JSON.parse(SafeStorage.getItem(STORAGE_KEY_AUDIT)) || [];
    } catch(e) { return []; }
}

function escapeHtml(text) {
    if (!text) return "";
    const div = document.createElement("div");
    div.textContent = text;
    return div.innerHTML;
}

function startTeacherAutoRefresh() {
    if (teacherAutoRefreshTimer) return;
    teacherAutoRefreshTimer = setInterval(() => {
        const dash = document.getElementById("teacherDashboard");
        if (dash && !dash.classList.contains("hidden") && dash.style.display !== "none") {
            renderTeacherTable();
        }
    }, 2500);
}

function stopTeacherAutoRefresh() {
    clearInterval(teacherAutoRefreshTimer);
    teacherAutoRefreshTimer = null;
}


// Tezkor natija kiritish (Guruhdagi skrinshotlar bo'yicha)
function openAddStudentModal() {
    const modal = document.getElementById("modalAddStudentResult");
    if (modal) {
        modal.classList.remove("hidden");
        modal.style.display = "flex";
        document.getElementById("manualStudentId").value = "";
        document.getElementById("manualFullName").value = "";
        document.getElementById("manualGroup").value = "";
        document.getElementById("manualScore").value = "";
        document.getElementById("manualLookupStatus").innerHTML = "";
    }
}

function closeAddStudentModal() {
    const modal = document.getElementById("modalAddStudentResult");
    if (modal) {
        modal.classList.add("hidden");
        modal.style.display = "none";
    }
}

function handleManualIdInput(inp) {
    if (!inp) return;
    inp.value = inp.value.replace(/\D/g, '').slice(0, 12);
    const idVal = inp.value;
    const statusEl = document.getElementById("manualLookupStatus");
    const nameEl = document.getElementById("manualFullName");
    const groupEl = document.getElementById("manualGroup");

    if (idVal.length === 12) {
        const found = STUDENTS_ROSTER.find(s => s.id === idVal);
        if (found) {
            nameEl.value = found.name;
            groupEl.value = found.group;
            statusEl.innerHTML = '<span class="text-emerald-600 font-bold text-xs">✓ ' + found.name + ' (' + found.group + ')</span>';
        } else {
            statusEl.innerHTML = '<span class="text-rose-500 font-bold text-xs">Ushbu ID ro‘yxatda topilmadi</span>';
        }
    } else {
        statusEl.innerHTML = '<span class="text-slate-400 text-xs">' + idVal.length + '/12 raqam</span>';
    }
}

function saveManualStudentResult(e) {
    if (e && e.preventDefault) e.preventDefault();
    const idVal = document.getElementById("manualStudentId").value.trim();
    const nameVal = document.getElementById("manualFullName").value.trim();
    const groupVal = document.getElementById("manualGroup").value.trim();
    const scoreVal = parseInt(document.getElementById("manualScore").value);

    if (!idVal || !nameVal || !groupVal || isNaN(scoreVal) || scoreVal < 0 || scoreVal > 30) {
        alert("Iltimos, Talaba ID (12 ta raqam), F.I.Sh., Guruh va ballni (0 dan 30 gacha) to‘g‘ri kiriting!");
        return false;
    }

    const payload = {
        studentId: idVal,
        fullName: nameVal,
        groupName: groupVal,
        direction: "Axborot tizimlari va texnologiyalari",
        course: 1,
        totalScore: scoreVal,
        maxScore: 30,
        correctCount: scoreVal,
        incorrectCount: 30 - scoreVal,
        statusText: scoreVal >= 18 ? "Joriy nazoratdan o‘tdi" : "Joriy nazoratdan o‘tmadi",
        startedAt: new Date().toLocaleString("uz-UZ"),
        finishedAt: new Date().toLocaleString("uz-UZ"),
        tabSwitchCount: 0
    };

    saveStudentResult(payload);

    if (window.location.protocol.startsWith('http')) {
        fetch('/api/direct_submit', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(payload),
            keepalive: true
        }).then(r => r.json()).then(() => {
            syncResultsFromServer();
        }).catch(() => {});
    }

    closeAddStudentModal();
    renderTeacherTable(true);
    alert(nameVal + " natijasi muvaffaqiyatli saqlandi!");
    return false;
}

// =========================================================================
// 5. GURUH VEDOMOSTI (PDF, EXCEL, CHOP ETISH)
// =========================================================================

function openVedomostModal(preselectGroup) {
    const modal = document.getElementById("vedomostModal");
    if (!modal) return;

    const currentFilter = document.getElementById("teachGroupFilter") ? document.getElementById("teachGroupFilter").value.trim() : "";
    const groupSelect = document.getElementById("vedomostGroupSelect");
    if (groupSelect) {
        if (preselectGroup) {
            groupSelect.value = preselectGroup;
        } else if (currentFilter) {
            groupSelect.value = currentFilter;
        } else {
            groupSelect.value = "9mt-26 ATT (o'z)";
        }
    }

    updateVedomostModalView();
    modal.classList.remove("hidden");
    modal.style.display = "flex";
}

function closeVedomostModal() {
    const modal = document.getElementById("vedomostModal");
    if (modal) {
        modal.classList.add("hidden");
        modal.style.display = "none";
    }
}

function normalizeGroupStr(g) {
    if (!g) return "";
    return String(g).toLowerCase().replace(/[‘`’']/g, "'").replace(/\s+/g, " ").trim();
}

function getVedomostDataForGroup(groupName) {
    const stored = getStoredStudents();
    const studentMap = {};
    stored.forEach(function(s) {
        if (s.studentId) studentMap[String(s.studentId).trim()] = s;
        if (s.fullName) studentMap[s.fullName.toUpperCase().trim()] = s;
    });

    const normTarget = normalizeGroupStr(groupName);
    let list = [];

    if (normTarget && typeof STUDENTS_ROSTER !== "undefined") {
        const groupRoster = STUDENTS_ROSTER.filter(function(r) {
            const normR = normalizeGroupStr(r.group);
            return normR === normTarget || normR.startsWith(normTarget) || normTarget.startsWith(normR);
        });
        if (groupRoster.length > 0) {
            groupRoster.forEach(function(r) {
                const sub = studentMap[String(r.id).trim()] || studentMap[r.name.toUpperCase().trim()] || null;
                list.push({
                    id: r.id,
                    name: r.name,
                    group: r.group,
                    score: sub ? sub.totalScore : null,
                    status: sub ? sub.statusText : "Topshirmagan"
                });
            });
        }
    }

    if (list.length === 0) {
        const filteredStored = stored.filter(function(s) {
            if (!normTarget) return true;
            const normS = normalizeGroupStr(s.groupName);
            return normS === normTarget || normS.startsWith(normTarget) || normTarget.startsWith(normS);
        });
        filteredStored.forEach(function(s) {
            list.push({
                id: s.studentId || "-",
                name: s.fullName,
                group: s.groupName,
                score: s.totalScore,
                status: s.statusText
            });
        });
    }

    // Sort alphabetically by full name
    list.sort(function(a, b) {
        return a.name.localeCompare(b.name);
    });
    return list;
}

function updateVedomostModalView() {
    const groupSelect = document.getElementById("vedomostGroupSelect");
    const selectedGroup = groupSelect ? groupSelect.value.trim() : "";
    const grpTitle = selectedGroup || "Barcha guruhlar";

    const docGroupElem = document.getElementById("vDocGroup");
    if (docGroupElem) docGroupElem.textContent = grpTitle;

    const todayStr = new Date().toLocaleDateString("uz-UZ");
    const docDateElem = document.getElementById("vDocDate");
    if (docDateElem) docDateElem.textContent = todayStr;

    const docSignDateElem = document.getElementById("vDocSignDate");
    if (docSignDateElem) docSignDateElem.textContent = todayStr;

    const vedomostData = getVedomostDataForGroup(selectedGroup);
    const tbody = document.getElementById("vedomostTableBody");
    if (!tbody) return;

    tbody.innerHTML = "";

    if (vedomostData.length === 0) {
        tbody.innerHTML = '<tr><td colspan="5" class="py-6 text-center text-slate-400">Ushbu guruh bo‘yicha maʼlumot topilmadi.</td></tr>';
        return;
    }

    vedomostData.forEach(function(row, idx) {
        const hasScore = (typeof row.score === "number");
        const isPass = hasScore && row.score >= 18;
        const scoreColorClass = hasScore ? (isPass ? "text-emerald-700 font-bold" : "text-rose-700 font-bold") : "text-slate-400 italic";
        const scoreText = hasScore ? (row.score + " ball") : '<span class="text-slate-400 italic text-[11px]">Topshirmagan</span>';

        const tr = document.createElement("tr");
        tr.className = (idx % 2 === 1) ? "bg-slate-50/60" : "bg-white";
        tr.innerHTML = 
            '<td class="py-2 px-3 text-center border border-slate-300 font-semibold text-slate-500">' + (idx + 1) + '</td>' +
            '<td class="py-2 px-3 text-center border border-slate-300 font-mono font-bold text-slate-800">' + escapeHtml(row.id) + '</td>' +
            '<td class="py-2 px-3 border border-slate-300 font-medium text-slate-900">' + escapeHtml(row.name) + '</td>' +
            '<td class="py-2 px-3 text-center border border-slate-300 text-slate-700">' + escapeHtml(row.group) + '</td>' +
            '<td class="py-2 px-3 text-center border border-slate-300 font-mono text-sm ' + scoreColorClass + '">' + scoreText + '</td>';
        tbody.appendChild(tr);
    });
}

function printVedomostDoc() {
    window.print();
}

function downloadVedomostExcelFromModal() {
    const groupSelect = document.getElementById("vedomostGroupSelect");
    const selectedGroup = groupSelect ? groupSelect.value.trim() : "";
    exportVedomostExcel(selectedGroup);
}

function exportVedomostExcel(targetGroup) {
    const groupFilter = (targetGroup !== undefined) ? targetGroup : (document.getElementById("teachGroupFilter") ? document.getElementById("teachGroupFilter").value.trim() : "");
    const grpTitle = groupFilter || "Barcha guruhlar";

    const vedomostData = getVedomostDataForGroup(groupFilter);
    if (vedomostData.length === 0) {
        alert("Tanlangan guruh bo‘yicha talabalar natijasi topilmadi!");
        return;
    }

    const todayStr = new Date().toLocaleDateString("uz-UZ");
    let csv = "\uFEFF"; // UTF-8 BOM
    csv += "DASTURLASH FANIDAN JORIY NAZORAT JADVALI (VEDOMOST)\n";
    csv += "Guruh: " + grpTitle + " | Fan: Dasturlash | Maksimal ball: 30 ball | Sana: " + todayStr + "\n\n";
    csv += "№;Talaba ID;F.I.O;Guruh;Joriy nazorat bali\n";

    vedomostData.forEach(function(row, idx) {
        const sc = (typeof row.score === "number") ? (row.score + " ball") : (row.score || "Topshirmagan");
        csv += '"' + (idx + 1) + '";"' + row.id + '";"' + row.name + '";"' + row.group + '";"' + sc + '"\n';
    });

    csv += "\n";
    csv += ';;;"O‘qituvchi: _______________________ (imzo)";"";""\n';
    csv += ';;;"Sana: ' + todayStr + '";"";""\n';

    const cleanGrp = grpTitle.replace(/[\s\/\']/g, "_");
    const blob = new Blob([csv], { type: "text/csv;charset=utf-8;" });
    const link = document.createElement("a");
    const url = URL.createObjectURL(blob);
    link.setAttribute("href", url);
    link.setAttribute("download", "Vedomost_Dasturlash_" + cleanGrp + "_" + new Date().toISOString().slice(0, 10) + ".csv");
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
}
