"""
╔══════════════════════════════════════════════════════════╗
║              🤖  CHATBOT PYTHON  v1.0                   ║
║  Features: DB Q&A, Kalkulator, Tanggal, Konteks Memori  ║
╚══════════════════════════════════════════════════════════╝
"""

import json
import os
import re
import sys
import time
import random
from datetime import datetime
from difflib import SequenceMatcher

# ───────────────────────────── KONFIGURASI ──────────────────────────────
DB_FILE = "portfolio/src/components/_py/database.json"
SIMILARITY_THRESHOLD = 0.50   # 50% kemiripan minimum
MAX_HISTORY = 2               # jumlah percakapan yang diingat
WORD_DELAY = 0.12             # delay per-kata (detik) untuk animasi typing

# ─────────────────────────────── WARNA ──────────────────────────────────
class C:
    CYAN    = '\033[96m'
    GREEN   = '\033[92m'
    YELLOW  = '\033[93m'
    RED     = '\033[91m'
    BLUE    = '\033[94m'
    MAGENTA = '\033[95m'
    WHITE   = '\033[97m'
    RESET   = '\033[0m'
    BOLD    = '\033[1m'
    DIM     = '\033[2m'

# ─────────────────────────── ANIMASI TYPING ─────────────────────────────
def type_print(text: str, delay: float = WORD_DELAY, color: str = ""):
    """Tampilkan teks word-by-word dengan animasi typing."""
    prefix = color if color else ""
    suffix = C.RESET if color else ""
    words = text.split(' ')
    print(prefix, end='', flush=True)
    for i, word in enumerate(words):
        # cetak per-kata
        print(word, end='', flush=True)
        if i < len(words) - 1:
            print(' ', end='', flush=True)
        time.sleep(delay)
    print(suffix, flush=True)

# ───────────────────────────── DATABASE ─────────────────────────────────
DEFAULT_DB = {
    "conversations": [
        {
            "question": "siapa presiden pertama indonesia",
            "answers": [
                "Presiden pertama Indonesia adalah Ir. Soekarno, menjabat 1945–1967."
            ]
        },
        {
            "question": "siapa presiden kedua indonesia",
            "answers": [
                "Presiden kedua Indonesia adalah Soeharto, menjabat 1967–1998."
            ]
        },
        {
            "question": "siapa presiden ketiga indonesia",
            "answers": [
                "Presiden ketiga Indonesia adalah B.J. Habibie, menjabat 1998–1999."
            ]
        },
        {
            "question": "apa ibu kota indonesia",
            "answers": [
                "Ibu kota Indonesia saat ini adalah Jakarta, namun sedang dipindahkan ke Nusantara di Kalimantan Timur.",
                "Jakarta adalah ibu kota Indonesia, tetapi ibu kota baru yaitu Nusantara sedang dibangun di Kalimantan Timur."
            ]
        },
        {
            "question": "apa itu python",
            "answers": [
                "Python adalah bahasa pemrograman tingkat tinggi yang terkenal karena sintaksnya yang bersih dan mudah dibaca.",
                "Python adalah bahasa pemrograman serbaguna yang banyak digunakan untuk web, data science, AI, dan otomasi."
            ]
        },
        {
            "question": "berapa jumlah pulau di indonesia",
            "answers": [
                "Indonesia memiliki sekitar 17.000 pulau, menjadikannya negara kepulauan terbesar di dunia."
            ]
        },
        {
            "question": "apa bahasa resmi indonesia",
            "answers": [
                "Bahasa resmi Indonesia adalah Bahasa Indonesia."
            ]
        },
        {
            "question": "siapa penemu listrik",
            "answers": [
                "Michael Faraday dianggap sebagai penemu listrik praktis melalui penemuannya tentang induksi elektromagnetik."
            ]
        }
    ]
}

def load_db() -> dict:
    """Muat database dari file JSON."""
    if not os.path.exists(DB_FILE):
        save_db(DEFAULT_DB)
        return DEFAULT_DB
    try:
        with open(DB_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
        if "conversations" not in data:
            data["conversations"] = []
        return data
    except (json.JSONDecodeError, IOError):
        print(f"{C.RED}⚠  Gagal membaca {DB_FILE}, membuat ulang...{C.RESET}")
        save_db(DEFAULT_DB)
        return DEFAULT_DB

def save_db(db: dict):
    """Simpan database ke file JSON."""
    with open(DB_FILE, 'w', encoding='utf-8') as f:
        json.dump(db, f, ensure_ascii=False, indent=2)

# ──────────────────────────── KEMIRIPAN TEKS ────────────────────────────
def similarity(a: str, b: str) -> float:
    """
    Hitung kemiripan dua string menggunakan SequenceMatcher.
    Mempertimbangkan huruf dan urutan huruf yang sama (50% = threshold).
    """
    return SequenceMatcher(None, a.lower().strip(), b.lower().strip()).ratio()

def normalize(text: str) -> str:
    """Normalisasi teks: huruf kecil, hapus tanda baca berlebihan."""
    text = text.lower().strip()
    text = re.sub(r'[?!.,;:]+', '', text)
    text = re.sub(r'\s+', ' ', text)
    return text

def find_best_match(query: str, db: dict, threshold: float = SIMILARITY_THRESHOLD):
    """
    Cari entry terbaik di database berdasarkan kemiripan teks.
    Return: (entry_dict, score) atau (None, 0.0) jika tidak ada.
    """
    best_score = 0.0
    best_entry = None
    q_norm = normalize(query)

    for entry in db.get("conversations", []):
        e_norm = normalize(entry["question"])
        score = similarity(q_norm, e_norm)

        # Bonus: cek apakah semua kata kunci query ada di pertanyaan DB
        q_words = set(q_norm.split())
        e_words = set(e_norm.split())
        overlap = len(q_words & e_words) / max(len(q_words), 1)
        combined = (score * 0.7) + (overlap * 0.3)

        if combined > best_score:
            best_score = combined
            best_entry = entry

    if best_score >= threshold:
        return best_entry, best_score
    return None, best_score

# ─────────────────────────────── KALKULATOR ─────────────────────────────
_SAFE_MATH_PATTERN = re.compile(r'^[\d\s\+\-\*\/\(\)\.\%\*\s]+$')

def safe_eval(expr: str):
    """Evaluasi ekspresi matematika secara aman (tanpa builtins berbahaya)."""
    expr = expr.strip()
    expr = expr.replace('^', '**')
    if not re.match(r'^[\d\s\+\-\*\/\(\)\.\%\*]+$', expr):
        return None
    try:
        result = eval(expr, {"__builtins__": {}}, {})  # noqa: S307
        return result
    except Exception:
        return None

WORD_TO_OP = {
    'ditambah'  : '+',
    'tambah'    : '+',
    'plus'      : '+',
    'dikurangi' : '-',
    'kurangi'   : '-',
    'minus'     : '-',
    'dikali'    : '*',
    'kali'      : '*',
    'times'     : '*',
    'dibagi'    : '/',
    'bagi'      : '/',
    'persen'    : '%',
    'pangkat'   : '**',
    'kuadrat'   : '**2',
}

def translate_words_to_ops(text: str) -> str:
    """Ganti kata operasi matematika ke simbol."""
    for word, op in WORD_TO_OP.items():
        text = re.sub(r'\b' + word + r'\b', op, text, flags=re.IGNORECASE)
    return text

def is_calc_query(text: str) -> bool:
    """Deteksi apakah input adalah pertanyaan kalkulator."""
    # Ekspresi murni angka + operator
    if re.match(r'^[\d\s\+\-\*\/\(\)\.\%\^\*]+$', text.strip()):
        return True
    # Mengandung angka dan operator kata
    has_number = bool(re.search(r'\d', text))
    has_op_word = any(w in text.lower() for w in WORD_TO_OP.keys())
    has_op_sym = bool(re.search(r'[\+\-\*\/\%\^]', text))
    if has_number and (has_op_word or has_op_sym):
        return True
    # Kata trigger kalkulator
    calc_triggers = ['hitung', 'berapa hasil', 'kalkulator']
    return any(t in text.lower() for t in calc_triggers)

def extract_and_calc(text: str, prev_number=None) -> tuple:
    """
    Ekstrak dan hitung ekspresi dari teks.
    Return: (result, expression_string) atau (None, None)
    """
    t = text.lower()

    # Substitusi referensi ke hasil sebelumnya
    ref_keywords = ['sebelumnya', 'tadi', 'hasilnya', 'itu']
    if prev_number is not None and any(k in t for k in ref_keywords):
        for k in ref_keywords:
            t = t.replace(k, str(prev_number))

    # Terjemahkan kata ke operator
    t = translate_words_to_ops(t)

    # Hapus kata-kata non-matematik
    t = re.sub(r'(berapa|hitung|hasil|dari|adalah|sama\s+dengan|=|nilai)', '', t, flags=re.IGNORECASE)

    # Ambil bagian yang matematis
    match = re.search(r'[\d\s\+\-\*\/\(\)\.\%\*]+', t)
    if not match:
        return None, None

    expr = match.group().strip()
    if len(expr) < 1:
        return None, None

    result = safe_eval(expr)
    if result is None:
        return None, None

    # Format hasil (hilangkan desimal jika bilangan bulat)
    if isinstance(result, float) and result.is_integer():
        result = int(result)

    return result, expr.strip()

# ──────────────────────────── TANGGAL & WAKTU ───────────────────────────
HARI   = ['Senin','Selasa','Rabu','Kamis','Jumat','Sabtu','Minggu']
BULAN  = ['Januari','Februari','Maret','April','Mei','Juni',
          'Juli','Agustus','September','Oktober','November','Desember']

def is_date_query(text: str) -> bool:
    keywords = ['tanggal', 'hari ini', 'sekarang', 'bulan ini',
                'tahun ini', 'jam', 'waktu', 'date', 'time', 'now']
    t = text.lower()
    return any(k in t for k in keywords)

def get_datetime_response() -> str:
    now = datetime.now()
    hari  = HARI[now.weekday()]
    bulan = BULAN[now.month - 1]
    return (f"📅 Sekarang adalah {hari}, {now.day} {bulan} {now.year} "
            f"— 🕐 Pukul {now.strftime('%H:%M:%S')}")

# ──────────────────────────── TEKS BANTUAN ──────────────────────────────
HELP_TEXT = f"""
{C.BOLD}{C.CYAN}
╔══════════════════════════════════════════════════════════════╗
║                    🤖  PANDUAN CHATBOT                       ║
╠══════════════════════════════════════════════════════════════╣
║                                                              ║
║  PERINTAH KHUSUS                                             ║
║  ─────────────────────────────────────────────────────────  ║
║  help              Tampilkan panduan ini                     ║
║  quit / exit       Keluar dari chatbot                       ║
║                                                              ║
║  KALKULATOR 🔢                                               ║
║  ─────────────────────────────────────────────────────────  ║
║  Langsung ketik ekspresi matematika:                         ║
║    • 10 + 5 * 2                                              ║
║    • 100 / 4                                                 ║
║    • 2 ^ 8  (pangkat)                                        ║
║  Atau gunakan kata:                                          ║
║    • 5 ditambah 3                                            ║
║    • 10 dikali 4 dikurangi 2                                 ║
║  Referensi hasil sebelumnya:                                 ║
║    • hasil sebelumnya ditambah 3                             ║
║    • tadi dikali 2                                           ║
║                                                              ║
║  TANGGAL & WAKTU 📅                                          ║
║  ─────────────────────────────────────────────────────────  ║
║  Ketik: tanggal, hari ini, jam, sekarang                     ║
║                                                              ║
║  DATABASE Q&A 💬                                             ║
║  ─────────────────────────────────────────────────────────  ║
║  • Tanyakan apa saja – bot cocokkan ≥50% kemiripan           ║
║  • Jawaban baru bisa ditambahkan jika pertanyaan sudah ada   ║
║  • Pertanyaan baru akan disimpan ke database.json            ║
║                                                              ║
║  MEMORI KONTEKS 🧠                                           ║
║  ─────────────────────────────────────────────────────────  ║
║  Bot mengingat 2 percakapan terakhir:                        ║
║    • "1 + 1" → "2", lalu "tadi ditambah 3" → "5"            ║
║    • "presiden pertama?" → "Soekarno"                        ║
║      lalu "yang kedua?" → mencari konteks presiden           ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
{C.RESET}"""

# ─────────────────────────────── CHATBOT ────────────────────────────────
class Chatbot:
    def __init__(self):
        self.db = load_db()
        # history: list of {"user": str, "bot": str, "number": float|None}
        self.history: list[dict] = []
        # Simpan topik utama (dari pertanyaan non-followup terakhir)
        self._root_topic: str = ""

    # ── Manajemen Riwayat ──
    def add_history(self, user_input: str, bot_answer: str, number=None):
        self.history.append({
            "user"  : user_input,
            "bot"   : bot_answer,
            "number": number
        })
        if len(self.history) > MAX_HISTORY:
            self.history.pop(0)

    def last_number(self):
        """Ambil angka terakhir dari riwayat percakapan."""
        for h in reversed(self.history):
            if h["number"] is not None:
                return h["number"]
            # Coba ekstrak angka dari jawaban bot sebelumnya
            nums = re.findall(r'\b\d+(?:\.\d+)?\b', h["bot"])
            if nums:
                return float(nums[-1])
        return None

    def last_topic_words(self) -> str:
        """Ambil kata-kata topik dari root_topic (bukan dari follow-up)."""
        if self._root_topic:
            return self._root_topic
        if not self.history:
            return ""
        last_q = self.history[-1]["user"]
        stop   = {'siapa','apa','berapa','dimana','kapan','bagaimana',
                  'yang','dan','di','ke','dari','adalah','itu','ini',
                  'apakah','bisa','tolong','mohon','kasih','tahu'}
        words  = [w for w in normalize(last_q).split() if w not in stop]
        return ' '.join(words[:4])

    # ── Deteksi Follow-up ──
    def is_followup(self, text: str) -> bool:
        """Deteksi apakah input adalah pertanyaan lanjutan dari konteks sebelumnya."""
        if not self.history:
            return False
        followup_hints = {
            'yang', 'ke-', 'kedua', 'ketiga', 'keempat', 'kelima',
            'berikutnya', 'selanjutnya', 'sesudahnya', 'lanjutnya',
            'dia', 'nya', 'tersebut', 'itu', 'sama', 'lainnya'
        }
        t_words = set(normalize(text).split())
        short   = len(text.split()) <= 4
        has_hint = bool(t_words & followup_hints)
        return short and has_hint

    # ── Augmentasi Query dengan Konteks ──
    ORDINALS = ['pertama','kedua','ketiga','keempat','kelima',
                'keenam','ketujuh','kedelapan','kesembilan','kesepuluh',
                '1','2','3','4','5','6','7','8','9','10']

    def augment_with_context(self, query: str) -> str:
        """
        Gabungkan query dengan kata kunci topik dari percakapan sebelumnya.
        Jika query mengandung ordinal baru (kedua, ketiga...), ganti ordinal
        lama di topik agar pencarian lebih tepat.
        """
        topic = self.last_topic_words()
        if not topic:
            return query

        q_lower = query.lower()

        # Deteksi ordinal di query baru
        new_ordinal = None
        for o in self.ORDINALS:
            if re.search(r'\b' + o + r'\b', q_lower):
                new_ordinal = o
                break

        # Jika ada ordinal baru, ganti ordinal lama di topik
        if new_ordinal:
            for o in self.ORDINALS:
                if re.search(r'\b' + o + r'\b', topic):
                    topic = re.sub(r'\b' + o + r'\b', new_ordinal, topic)
                    break
            # Bangun query augmented tanpa mengulangi ordinal
            topic_no_ord = re.sub(r'\b(' + '|'.join(self.ORDINALS) + r')\b', '', topic).strip()
            return f"{topic_no_ord} {query}"

        return f"{topic} {query}"

    # ── Tambah Data ke DB ──
    def learn(self, question: str) -> str:
        """Tanyakan ke user apakah ingin menambah jawaban ke DB."""
        print(f"\n{C.YELLOW}{'─'*60}{C.RESET}")
        print(f"{C.YELLOW}⚠  Saya belum tahu jawaban untuk pertanyaan tersebut.{C.RESET}")
        print(f"{C.CYAN}Apakah Anda ingin mengajarkan saya? {C.DIM}(ya/tidak){C.RESET}: ", end='')
        choice = input().strip().lower()

        if choice not in ('ya', 'y', 'yes', 'iya'):
            return "Baik, mungkin lain kali saya bisa membantu! 😊"

        print(f"{C.CYAN}Masukkan jawaban untuk «{question}»: {C.RESET}", end='')
        new_answer = input().strip()
        if not new_answer:
            return "Jawaban tidak boleh kosong. Tidak ada yang disimpan."

        q_norm = normalize(question)

        # Cek apakah sudah ada entry serupa (≥90% mirip)
        entry, score = find_best_match(q_norm, self.db, threshold=0.90)

        if entry and score >= 0.90:
            if new_answer in entry["answers"]:
                return "Jawaban tersebut sudah ada di database. ✅"
            entry["answers"].append(new_answer)
            save_db(self.db)
            return f"✅ Jawaban baru berhasil ditambahkan ke pertanyaan yang sudah ada!"
        else:
            self.db["conversations"].append({
                "question": q_norm,
                "answers" : [new_answer]
            })
            save_db(self.db)
            return f"🎉 Terima kasih! Saya telah mempelajari Q&A baru dan menyimpannya di database.json!"

    # ── Proses Input Utama ──
    def respond(self, user_input: str) -> tuple[str | None, bool]:
        """
        Proses input user dan kembalikan (response, should_exit).
        response = None berarti tidak ada jawaban → perlu belajar.
        """
        raw   = user_input.strip()
        t     = raw.lower().strip()

        # ── PERINTAH SISTEM ──
        if t == 'help':
            return HELP_TEXT, False

        if t in ('quit', 'exit', 'keluar', 'bye', 'selamat tinggal'):
            return "Sampai jumpa! Semoga hari Anda menyenangkan 👋😊", True

        # ── TANGGAL & WAKTU ──
        if is_date_query(t):
            resp = get_datetime_response()
            self.add_history(raw, resp)
            return resp, False

        # ── KALKULATOR ──
        # Referensi ke hasil sebelumnya (meski tidak ada angka di input)
        ref_only = any(k in t for k in ['sebelumnya','tadi','hasilnya']) and \
                   bool(re.search(r'[\+\-\*\/dikali\s]', t))

        if is_calc_query(t) or ref_only:
            prev = self.last_number()
            result, expr = extract_and_calc(raw, prev_number=prev)
            if result is not None:
                resp = f"🔢 Hasil: {expr.strip()} = {C.BOLD}{result}{C.RESET}"
                self.add_history(raw, str(result), number=float(result))
                return resp, False

        # ── DATABASE Q&A ──
        followup = self.is_followup(raw)

        # Coba match langsung dulu
        entry, score = find_best_match(raw, self.db)

        # Jika gagal & terdeteksi follow-up → augmentasi konteks
        if entry is None and followup:
            augmented = self.augment_with_context(raw)
            entry, score = find_best_match(augmented, self.db)

        if entry:
            answer = random.choice(entry["answers"])
            score_pct = int(score * 100)
            resp = f"{answer}  {C.DIM}[cocok {score_pct}%]{C.RESET}"
            self.add_history(raw, answer)

            # Perbarui root_topic HANYA jika bukan follow-up
            if not followup:
                stop = {'siapa','apa','berapa','dimana','kapan','bagaimana',
                        'yang','dan','di','ke','dari','adalah','itu','ini',
                        'apakah','bisa','tolong','mohon','kasih','tahu'}
                words = [w for w in normalize(raw).split() if w not in stop]
                self._root_topic = ' '.join(words[:4])

            return resp, False

        # ── TIDAK DITEMUKAN ──
        return None, False


# ─────────────────────────────── MAIN ───────────────────────────────────
def print_banner():
    print(f"{C.BOLD}{C.CYAN}")
    print("  ╔══════════════════════════════════════════════╗")
    print("  ║         🤖  CHATBOT PYTHON  v1.0            ║")
    print("  ║  Database: database.json  |  Ketik: help    ║")
    print("  ╚══════════════════════════════════════════════╝")
    print(f"{C.RESET}")

def main():
    print_banner()
    bot = Chatbot()

    while True:
        # ── Prompt Input ──
        print(f"\n{C.GREEN}{C.BOLD}Anda ›{C.RESET} ", end='')
        try:
            user_input = input().strip()
        except (KeyboardInterrupt, EOFError):
            print(f"\n{C.YELLOW}Chatbot dihentikan.{C.RESET}")
            break

        if not user_input:
            continue

        # ── Proses ──
        response, should_exit = bot.respond(user_input)

        print(f"\n{C.CYAN}{C.BOLD}Bot  ›{C.RESET} ", end='')

        if response is None:
            # Tidak ada jawaban → proses belajarkamu
            learn_resp = bot.learn(user_input)
            print(f"\n{C.CYAN}{C.BOLD}Bot  ›{C.RESET} ", end='')
            type_print(learn_resp, color=C.WHITE)

        elif user_input.lower() == 'help':
            print(response)  # cetak langsung (sudah berformat)

        else:
            type_print(response, color=C.WHITE)

        if should_exit:
            break

    print(f"\n{C.DIM}{'─'*50}{C.RESET}")
    print(f"{C.DIM}Session berakhir. Database tersimpan di: {DB_FILE}{C.RESET}\n")


if __name__ == "__main__":
    main()