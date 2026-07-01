"""
=========================================================================
SISTEM PERPUSTAKAAN DIGITAL - Streamlit Web App
=========================================================================
"""

import streamlit as st
import pandas as pd

# =========================================================================
# PAGE CONFIG
# =========================================================================
st.set_page_config(
    page_title="Perpustakaan Digital",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded",
)

# =========================================================================
# CUSTOM CSS - Dark blueprint theme sesuai slide asli
# =========================================================================
st.markdown("""
<style>
/* Import font */
@import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;600&family=Inter:wght@400;500;600;700&display=swap');

/* ---- Base ---- */
html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background-color: #0d1117;
    color: #c9d1d9;
}

/* ---- Sidebar ---- */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #161b22 0%, #0d1117 100%);
    border-right: 1px solid #21262d;
}
[data-testid="stSidebar"] .block-container { padding-top: 1rem; }

/* ---- Headings ---- */
h1, h2, h3 { font-family: 'Inter', sans-serif; font-weight: 700; }
h1 { color: #58a6ff; font-size: 1.8rem; }
h2 { color: #c9d1d9; font-size: 1.25rem; border-bottom: 1px solid #21262d; padding-bottom: .5rem; }
h3 { color: #8b949e; font-size: 1rem; }

/* ---- Cards / metric boxes ---- */
.metric-card {
    background: #161b22;
    border: 1px solid #21262d;
    border-radius: 10px;
    padding: 1.2rem 1.4rem;
    text-align: center;
    transition: border-color .2s;
}
.metric-card:hover { border-color: #388bfd; }
.metric-card .metric-value {
    font-family: 'JetBrains Mono', monospace;
    font-size: 2.2rem;
    font-weight: 600;
    color: #58a6ff;
    line-height: 1;
}
.metric-card .metric-label {
    font-size: .8rem;
    color: #8b949e;
    margin-top: .4rem;
    text-transform: uppercase;
    letter-spacing: .08em;
}
.metric-card .metric-icon { font-size: 1.6rem; margin-bottom: .3rem; }

/* ---- Tag badges ---- */
.badge {
    display: inline-block;
    font-family: 'JetBrains Mono', monospace;
    font-size: .72rem;
    padding: .2rem .55rem;
    border-radius: 4px;
    background: #1c2d40;
    color: #79c0ff;
    border: 1px solid #1f6feb;
}
.badge-orange { background: #2d1e00; color: #e3b341; border-color: #9e6a03; }
.badge-green  { background: #0f2a1a; color: #3fb950; border-color: #238636; }
.badge-purple { background: #1a1240; color: #bc8cff; border-color: #6e40c9; }
.badge-red    { background: #2d0f0f; color: #ff7b72; border-color: #da3633; }

/* ---- Section header ---- */
.section-header {
    display: flex;
    align-items: center;
    gap: .6rem;
    font-family: 'JetBrains Mono', monospace;
    font-size: .85rem;
    color: #e3b341;
    margin-bottom: 1rem;
    letter-spacing: .04em;
}
.section-header::before {
    content: '';
    display: block;
    width: 4px;
    height: 18px;
    background: #e3b341;
    border-radius: 2px;
}

/* ---- Table ---- */
[data-testid="stDataFrame"] {
    border: 1px solid #21262d !important;
    border-radius: 8px;
}

/* ---- Buttons ---- */
.stButton > button {
    background: #1c2d40;
    color: #79c0ff;
    border: 1px solid #1f6feb;
    border-radius: 6px;
    font-family: 'JetBrains Mono', monospace;
    font-size: .82rem;
    padding: .45rem 1.1rem;
    transition: all .15s;
    width: 100%;
}
.stButton > button:hover {
    background: #1f6feb;
    color: #fff;
    border-color: #58a6ff;
}

/* ---- Inputs ---- */
.stTextInput > div > div > input,
.stNumberInput > div > div > input,
.stSelectbox > div > div {
    background: #161b22 !important;
    border: 1px solid #30363d !important;
    color: #c9d1d9 !important;
    border-radius: 6px !important;
    font-family: 'JetBrains Mono', monospace !important;
    font-size: .85rem !important;
}
.stTextInput > div > div > input:focus,
.stNumberInput > div > div > input:focus {
    border-color: #388bfd !important;
    box-shadow: 0 0 0 3px rgba(56,139,253,.2) !important;
}

/* ---- Forms ---- */
[data-testid="stForm"] {
    background: #161b22;
    border: 1px solid #21262d;
    border-radius: 10px;
    padding: 1.4rem;
}

/* ---- Alerts / info boxes ---- */
.stSuccess > div { background: #0f2a1a !important; color: #3fb950 !important; border-color: #238636 !important; border-radius: 8px !important; }
.stError   > div { background: #2d0f0f !important; color: #ff7b72 !important; border-color: #da3633 !important; border-radius: 8px !important; }
.stWarning > div { background: #2d1e00 !important; color: #e3b341 !important; border-color: #9e6a03 !important; border-radius: 8px !important; }
.stInfo    > div { background: #1c2d40 !important; color: #79c0ff !important; border-color: #1f6feb !important; border-radius: 8px !important; }

/* ---- Sidebar nav ---- */
.nav-item {
    display: flex;
    align-items: center;
    gap: .7rem;
    padding: .6rem .9rem;
    border-radius: 8px;
    cursor: pointer;
    font-size: .88rem;
    color: #8b949e;
    margin-bottom: .25rem;
    transition: all .15s;
    border: 1px solid transparent;
}
.nav-item:hover, .nav-item.active {
    background: #1c2d40;
    color: #79c0ff;
    border-color: #1f6feb;
}

/* ---- Result / log box ---- */
.log-box {
    background: #0d1117;
    border: 1px solid #21262d;
    border-radius: 8px;
    padding: 1rem;
    font-family: 'JetBrains Mono', monospace;
    font-size: .8rem;
    color: #3fb950;
    min-height: 60px;
    max-height: 220px;
    overflow-y: auto;
    white-space: pre-wrap;
}

/* ---- Algorithm pill ---- */
.algo-pill {
    display: inline-block;
    font-family: 'JetBrains Mono', monospace;
    font-size: .72rem;
    padding: .25rem .7rem;
    border-radius: 20px;
    background: #21262d;
    color: #c9d1d9;
    border: 1px solid #30363d;
    margin: .2rem;
}

/* ---- Divider ---- */
hr { border-color: #21262d !important; margin: 1rem 0 !important; }

/* ---- Radio ---- */
[data-testid="stRadio"] label { color: #c9d1d9 !important; font-size: .88rem; }

/* ---- Sidebar title ---- */
.sidebar-title {
    font-family: 'JetBrains Mono', monospace;
    font-size: 1.05rem;
    font-weight: 600;
    color: #58a6ff;
    padding: .5rem .5rem 1rem;
    border-bottom: 1px solid #21262d;
    margin-bottom: 1rem;
}
</style>
""", unsafe_allow_html=True)

# =========================================================================
# DATA STRUCTURES
# =========================================================================
class BukuNode:
    def __init__(self, id_buku, judul, penulis, stok):
        self.id = id_buku
        self.judul = judul
        self.penulis = penulis
        self.stok = stok
        self.next = None

class InventarisBuku:
    def __init__(self):
        self.head = None
        self.id_counter = 1

    def tambah(self, judul, penulis, stok):
        baru = BukuNode(self.id_counter, judul, penulis, stok)
        self.id_counter += 1
        if self.head is None:
            self.head = baru
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = baru
        return baru

    def cari_by_id(self, id_buku):
        cur = self.head
        while cur:
            if cur.id == id_buku:
                return cur
            cur = cur.next
        return None

    def hapus(self, id_buku):
        cur, prev = self.head, None
        while cur:
            if cur.id == id_buku:
                if prev is None:
                    self.head = cur.next
                else:
                    prev.next = cur.next
                return True
            prev, cur = cur, cur.next
        return False

    def ke_list(self):
        hasil, cur = [], self.head
        while cur:
            hasil.append(cur)
            cur = cur.next
        return hasil

    def jumlah(self):
        return len(self.ke_list())


class AntrianNode:
    def __init__(self, id_buku, peminjam):
        self.id_buku = id_buku
        self.peminjam = peminjam
        self.next = None

class AntrianPeminjaman:
    def __init__(self):
        self.front = self.rear = None

    def enqueue(self, id_buku, peminjam):
        baru = AntrianNode(id_buku, peminjam)
        if self.rear is None:
            self.front = self.rear = baru
        else:
            self.rear.next = baru
            self.rear = baru

    def dequeue(self):
        if self.front is None:
            return None
        node = self.front
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return node

    def ke_list(self):
        hasil, cur = [], self.front
        while cur:
            hasil.append(cur)
            cur = cur.next
        return hasil

    def jumlah(self):
        return len(self.ke_list())


class RiwayatNode:
    def __init__(self, aktivitas):
        self.aktivitas = aktivitas
        self.prev = self.next = None

class RiwayatAktivitas:
    def __init__(self):
        self.head = self.tail = None

    def tambah(self, aktivitas):
        baru = RiwayatNode(aktivitas)
        baru.prev = self.tail
        if self.tail is None:
            self.head = baru
        else:
            self.tail.next = baru
        self.tail = baru

    def ke_list_maju(self):
        hasil, cur = [], self.head
        while cur:
            hasil.append(cur.aktivitas)
            cur = cur.next
        return hasil

    def ke_list_mundur(self):
        return list(reversed(self.ke_list_maju()))

    def jumlah(self):
        return len(self.ke_list_maju())


class FavNode:
    def __init__(self, id_buku, judul):
        self.id_buku = id_buku
        self.judul = judul
        self.next = None

class BukuFavorit:
    def __init__(self):
        self.tail = None

    def tambah(self, id_buku, judul):
        baru = FavNode(id_buku, judul)
        if self.tail is None:
            baru.next = baru
            self.tail = baru
        else:
            baru.next = self.tail.next
            self.tail.next = baru
            self.tail = baru

    def ke_list(self):
        if self.tail is None:
            return []
        head = self.tail.next
        cur, hasil = head, []
        while True:
            hasil.append(cur)
            cur = cur.next
            if cur is head:
                break
        return hasil

    def jumlah(self):
        return len(self.ke_list())


class RekomNode:
    def __init__(self, id_buku, judul):
        self.id_buku = id_buku
        self.judul = judul
        self.prev = self.next = None

class SistemRekomendasi:
    def __init__(self):
        self.head = None

    def tambah(self, id_buku, judul):
        baru = RekomNode(id_buku, judul)
        if self.head is None:
            baru.next = baru.prev = baru
            self.head = baru
        else:
            tail = self.head.prev
            tail.next = baru
            baru.prev = tail
            baru.next = self.head
            self.head.prev = baru

    def ke_list(self):
        if self.head is None:
            return []
        cur, hasil = self.head, []
        while True:
            hasil.append(cur)
            cur = cur.next
            if cur is self.head:
                break
        return hasil

    def jumlah(self):
        return len(self.ke_list())


class TreeNode:
    def __init__(self, id_buku, judul):
        self.id_buku = id_buku
        self.judul = judul
        self.kiri = self.kanan = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, id_buku, judul):
        self.root = self._insert(self.root, id_buku, judul)

    def _insert(self, node, id_buku, judul):
        if node is None:
            return TreeNode(id_buku, judul)
        if id_buku < node.id_buku:
            node.kiri = self._insert(node.kiri, id_buku, judul)
        elif id_buku > node.id_buku:
            node.kanan = self._insert(node.kanan, id_buku, judul)
        return node

    def search(self, id_buku):
        return self._search(self.root, id_buku)

    def _search(self, node, id_buku):
        if node is None or node.id_buku == id_buku:
            return node
        if id_buku < node.id_buku:
            return self._search(node.kiri, id_buku)
        return self._search(node.kanan, id_buku)

    def inorder(self):
        hasil = []
        self._inorder(self.root, hasil)
        return hasil

    def _inorder(self, node, hasil):
        if node:
            self._inorder(node.kiri, hasil)
            hasil.append(node)
            self._inorder(node.kanan, hasil)

    def preorder(self):
        hasil = []
        self._preorder(self.root, hasil)
        return hasil

    def _preorder(self, node, hasil):
        if node:
            hasil.append(node)
            self._preorder(node.kiri, hasil)
            self._preorder(node.kanan, hasil)

    def postorder(self):
        hasil = []
        self._postorder(self.root, hasil)
        return hasil

    def _postorder(self, node, hasil):
        if node:
            self._postorder(node.kiri, hasil)
            self._postorder(node.kanan, hasil)
            hasil.append(node)


# =========================================================================
# ALGORITMA SORTING
# =========================================================================
def bubble_sort(arr):
    arr = arr[:]
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if arr[j].judul > arr[j + 1].judul:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def insertion_sort(arr):
    arr = arr[:]
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j].judul > key.judul:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def selection_sort(arr):
    arr = arr[:]
    n = len(arr)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j].judul < arr[min_idx].judul:
                min_idx = j
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def shell_sort(arr):
    arr = arr[:]
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap].judul > temp.judul:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2
    return arr

def merge_sort(arr):
    if len(arr) <= 1:
        return arr[:]
    mid = len(arr) // 2
    kiri = merge_sort(arr[:mid])
    kanan = merge_sort(arr[mid:])
    hasil, i, j = [], 0, 0
    while i < len(kiri) and j < len(kanan):
        if kiri[i].judul <= kanan[j].judul:
            hasil.append(kiri[i]); i += 1
        else:
            hasil.append(kanan[j]); j += 1
    hasil.extend(kiri[i:])
    hasil.extend(kanan[j:])
    return hasil

def quick_sort(arr):
    if len(arr) <= 1:
        return arr[:]
    pivot = arr[-1]
    kiri  = [x for x in arr[:-1] if x.judul < pivot.judul]
    kanan = [x for x in arr[:-1] if x.judul >= pivot.judul]
    return quick_sort(kiri) + [pivot] + quick_sort(kanan)

SORT_MAP = {
    "Bubble Sort — O(n²)": bubble_sort,
    "Insertion Sort — O(n²)": insertion_sort,
    "Selection Sort — O(n²)": selection_sort,
    "Quick Sort — O(n log n)": quick_sort,
    "Merge Sort — O(n log n)": merge_sort,
    "Shell Sort — O(n log n)": shell_sort,
}

# =========================================================================
# SESSION STATE INIT
# =========================================================================
def init_state():
    if "inventaris" not in st.session_state:
        st.session_state.inventaris  = InventarisBuku()
        st.session_state.antrian     = AntrianPeminjaman()
        st.session_state.riwayat     = RiwayatAktivitas()
        st.session_state.favorit     = BukuFavorit()
        st.session_state.rekomendasi = SistemRekomendasi()
        st.session_state.tree        = BinarySearchTree()
        st.session_state.halaman     = "Dashboard"
        st.session_state.rekom_idx   = 0

        # Sample data
        for judul, penulis, stok in [
            ("Clean Code", "Robert C. Martin", 5),
            ("The Pragmatic Programmer", "David Thomas", 3),
            ("Introduction to Algorithms", "Cormen et al.", 7),
            ("Design Patterns", "Gang of Four", 4),
            ("Python Crash Course", "Eric Matthes", 10),
        ]:
            st.session_state.inventaris.tambah(judul, penulis, stok)

init_state()
inv  = st.session_state.inventaris
ant  = st.session_state.antrian
riw  = st.session_state.riwayat
fav  = st.session_state.favorit
rek  = st.session_state.rekomendasi
tree = st.session_state.tree

# =========================================================================
# HELPER
# =========================================================================
def log(msg):
    riw.tambah(msg)

def buku_df(data=None):
    src = data if data is not None else inv.ke_list()
    if not src:
        return pd.DataFrame(columns=["ID", "Judul", "Penulis", "Stok"])
    return pd.DataFrame([{
        "ID": b.id, "Judul": b.judul, "Penulis": b.penulis, "Stok": b.stok
    } for b in src])

def section(label):
    st.markdown(f'<div class="section-header">{label}</div>', unsafe_allow_html=True)

def metric_card(icon, value, label):
    return f"""
    <div class="metric-card">
        <div class="metric-icon">{icon}</div>
        <div class="metric-value">{value}</div>
        <div class="metric-label">{label}</div>
    </div>"""

# =========================================================================
# SIDEBAR
# =========================================================================
with st.sidebar:
    st.markdown('<div class="sidebar-title">📚 Perpustakaan Digital</div>', unsafe_allow_html=True)

    MENU = [
        ("🏠", "Dashboard"),
        ("📖", "Kelola Buku"),
        ("🔄", "Peminjaman"),
        ("↩️", "Pengembalian"),
        ("🔍", "Searching Engine"),
        ("🔢", "Sorting Engine"),
        ("🌳", "Operasi Tree"),
        ("⭐", "Buku Favorit"),
        ("💡", "Rekomendasi"),
        ("📜", "Riwayat Aktivitas"),
    ]

    for icon, nama in MENU:
        active = "active" if st.session_state.halaman == nama else ""
        if st.button(f"{icon}  {nama}", key=f"nav_{nama}"):
            st.session_state.halaman = nama
            st.rerun()

    st.markdown("---")
    st.markdown("""
    <div style="font-family: 'JetBrains Mono'; font-size:.7rem; color:#484f58; padding:.5rem;">
    Struktur data:<br>
    <span style="color:#79c0ff">SLL · Queue · DLL</span><br>
    <span style="color:#bc8cff">CSLL · CDLL · BST</span>
    </div>""", unsafe_allow_html=True)

# =========================================================================
# HALAMAN: DASHBOARD
# =========================================================================
def halaman_dashboard():
    st.markdown("## 🏠 Dashboard")
    st.markdown('<hr>', unsafe_allow_html=True)

    c1, c2, c3, c4, c5 = st.columns(5)
    cards = [
        ("📚", inv.jumlah(), "Total Buku"),
        ("🔄", ant.jumlah(), "Antrian Pinjam"),
        ("📜", riw.jumlah(), "Riwayat"),
        ("⭐", fav.jumlah(), "Buku Favorit"),
        ("💡", rek.jumlah(), "Rekomendasi"),
    ]
    for col, (icon, val, label) in zip([c1, c2, c3, c4, c5], cards):
        col.markdown(metric_card(icon, val, label), unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    col_inv, col_log = st.columns([2, 1])

    with col_inv:
        section("INVENTARIS BUKU (Single Linked List)")
        df = buku_df()
        if df.empty:
            st.info("Belum ada buku dalam inventaris.")
        else:
            st.dataframe(df, use_container_width=True, hide_index=True)

    with col_log:
        section("RIWAYAT TERBARU (Double Linked List)")
        logs = riw.ke_list_mundur()[:8]
        if logs:
            isi = "\n".join(f"• {l}" for l in logs)
        else:
            isi = "Belum ada aktivitas."
        st.markdown(f'<div class="log-box">{isi}</div>', unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    section("ANTRIAN PEMINJAMAN (Queue — FIFO)")
    antrian_data = ant.ke_list()
    if antrian_data:
        df_ant = pd.DataFrame([{"#": i+1, "Peminjam": n.peminjam, "ID Buku": n.id_buku}
                                for i, n in enumerate(antrian_data)])
        st.dataframe(df_ant, use_container_width=True, hide_index=True)
    else:
        st.info("Tidak ada antrian peminjaman.")


# =========================================================================
# HALAMAN: KELOLA BUKU
# =========================================================================
def halaman_kelola_buku():
    st.markdown("## 📖 Kelola Buku")
    st.markdown('<span class="badge">Single Linked List</span>', unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    tab_tambah, tab_hapus, tab_daftar = st.tabs(["➕ Tambah Buku", "🗑️ Hapus Buku", "📋 Daftar Buku"])

    with tab_tambah:
        with st.form("form_tambah_buku", clear_on_submit=True):
            section("TAMBAH BUKU BARU")
            col1, col2 = st.columns(2)
            judul   = col1.text_input("Judul Buku", placeholder="Contoh: Clean Code")
            penulis = col2.text_input("Penulis", placeholder="Contoh: Robert C. Martin")
            stok = st.number_input("Stok", min_value=1, value=1)
            submitted = st.form_submit_button("➕ Tambah Buku")
            if submitted:
                if judul and penulis:
                    b = inv.tambah(judul, penulis, stok)
                    log(f"Buku ditambahkan: [{b.id}] {judul} oleh {penulis}")
                    st.success(f'✅ Buku "{judul}" berhasil ditambahkan dengan ID {b.id}')
                else:
                    st.error("⛔ Judul dan Penulis tidak boleh kosong.")

    with tab_hapus:
        section("HAPUS BUKU")
        data = inv.ke_list()
        if not data:
            st.info("Inventaris kosong.")
        else:
            pilihan = {f"[{b.id}] {b.judul}": b.id for b in data}
            selected = st.selectbox("Pilih Buku", list(pilihan.keys()))
            if st.button("🗑️ Hapus Buku"):
                id_hapus = pilihan[selected]
                nama_hapus = selected
                if inv.hapus(id_hapus):
                    log(f"Buku dihapus: {nama_hapus}")
                    st.success(f"✅ {nama_hapus} berhasil dihapus.")
                    st.rerun()
                else:
                    st.error("⛔ Buku tidak ditemukan.")

    with tab_daftar:
        section("SELURUH BUKU (Single Linked List)")
        df = buku_df()
        if df.empty:
            st.info("Belum ada buku.")
        else:
            st.dataframe(df, use_container_width=True, hide_index=True)
            st.caption(f"Total: {inv.jumlah()} buku dalam linked list")


# =========================================================================
# HALAMAN: PEMINJAMAN
# =========================================================================
def halaman_peminjaman():
    st.markdown("## 🔄 Peminjaman Buku")
    st.markdown('<span class="badge badge-orange">Queue — FIFO</span>', unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    col_form, col_ant = st.columns([1, 1])

    with col_form:
        with st.form("form_pinjam", clear_on_submit=True):
            section("FORM PEMINJAMAN")
            data = inv.ke_list()
            if not data:
                st.warning("Inventaris kosong, tambahkan buku terlebih dahulu.")
            else:
                pilihan = {f"[{b.id}] {b.judul}": b.id for b in data}
                selected = st.selectbox("Pilih Buku", list(pilihan.keys()))
                peminjam = st.text_input("Nama Peminjam", placeholder="Nama lengkap...")
                submitted = st.form_submit_button("🔄 Pinjam Buku")
                if submitted:
                    if peminjam:
                        id_buku = pilihan[selected]
                        ant.enqueue(id_buku, peminjam)
                        log(f"Peminjaman: {peminjam} meminjam buku ID {id_buku}")
                        st.success(f"✅ {peminjam} masuk antrian peminjaman!")
                        st.rerun()
                    else:
                        st.error("⛔ Nama peminjam tidak boleh kosong.")

    with col_ant:
        section("ANTRIAN SAAT INI (Queue)")
        antrian = ant.ke_list()
        if not antrian:
            st.info("Antrian kosong.")
        else:
            for i, node in enumerate(antrian):
                label = "🟢 DEPAN" if i == 0 else f"#{i+1}"
                st.markdown(f"""
                <div style="background:#161b22; border:1px solid {'#238636' if i==0 else '#21262d'};
                     border-radius:8px; padding:.7rem 1rem; margin-bottom:.4rem;
                     font-family: 'JetBrains Mono'; font-size:.82rem;">
                    <span style="color:#8b949e">{label}</span>&nbsp;&nbsp;
                    <span style="color:#c9d1d9">{node.peminjam}</span>&nbsp;
                    <span style="color:#8b949e">→ Buku ID</span>&nbsp;
                    <span style="color:#58a6ff">{node.id_buku}</span>
                </div>""", unsafe_allow_html=True)


# =========================================================================
# HALAMAN: PENGEMBALIAN
# =========================================================================
def halaman_pengembalian():
    st.markdown("## ↩️ Pengembalian Buku")
    st.markdown('<span class="badge badge-orange">Queue — FIFO</span>', unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    antrian = ant.ke_list()
    if not antrian:
        st.info("Tidak ada antrian peminjaman yang perlu diproses.")
        return

    section("PROSES PENGEMBALIAN (Dequeue dari FIFO)")
    node = antrian[0]
    b = inv.cari_by_id(node.id_buku)
    judul = b.judul if b else f"ID {node.id_buku}"

    st.markdown(f"""
    <div style="background:#0f2a1a; border:1px solid #238636; border-radius:10px;
         padding:1.2rem; font-family:'JetBrains Mono'; margin-bottom:1rem;">
        <div style="color:#8b949e; font-size:.75rem; margin-bottom:.5rem;">BERIKUTNYA DI ANTRIAN</div>
        <div style="color:#3fb950; font-size:1.1rem; font-weight:600;">👤 {node.peminjam}</div>
        <div style="color:#c9d1d9; font-size:.88rem; margin-top:.3rem;">📚 {judul} (ID {node.id_buku})</div>
    </div>""", unsafe_allow_html=True)

    if st.button("↩️ Proses Pengembalian (Dequeue)"):
        processed = ant.dequeue()
        if processed:
            log(f"Pengembalian: {processed.peminjam} mengembalikan buku ID {processed.id_buku}")
            st.success(f"✅ {processed.peminjam} telah mengembalikan buku ID {processed.id_buku}")
            st.rerun()

    st.markdown("<br>", unsafe_allow_html=True)
    section("SISA ANTRIAN")
    if len(antrian) > 1:
        df = pd.DataFrame([{"#": i+1, "Peminjam": n.peminjam, "ID Buku": n.id_buku}
                           for i, n in enumerate(antrian[1:])])
        st.dataframe(df, use_container_width=True, hide_index=True)
    else:
        st.caption("Hanya 1 antrian (yang sedang diproses).")


# =========================================================================
# HALAMAN: SEARCHING
# =========================================================================
def halaman_searching():
    st.markdown("## 🔍 Searching Engine")
    st.markdown("""
    <span class="algo-pill">Linear Search — O(n)</span>
    <span class="algo-pill">Binary Search — O(log n)</span>
    """, unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    data = inv.ke_list()
    if not data:
        st.warning("Inventaris kosong. Tambahkan buku terlebih dahulu.")
        return

    tab_linear, tab_binary = st.tabs(["🔎 Linear Search", "⚡ Binary Search"])

    with tab_linear:
        section("LINEAR SEARCH — PENCARIAN SEKUENSIAL O(n)")
        kata_kunci = st.text_input("Kata kunci judul", placeholder="Contoh: Python", key="ls_kw")
        if st.button("🔎 Cari", key="btn_linear"):
            if kata_kunci:
                hasil, langkah_ditemukan, log_steps = [], [], []
                for i, b in enumerate(data):
                    langkah = i + 1
                    match = kata_kunci.lower() in b.judul.lower()
                    icon = "✅" if match else "·"
                    log_steps.append(f"[{langkah:02d}] {icon} {b.judul}")
                    if match:
                        hasil.append(b)
                        langkah_ditemukan.append(langkah)

                col_res, col_steps = st.columns([1, 1])
                with col_res:
                    if hasil:
                        st.success(f"✅ Ditemukan {len(hasil)} buku")
                        st.dataframe(buku_df(hasil), use_container_width=True, hide_index=True)
                    else:
                        st.error("❌ Tidak ditemukan.")
                with col_steps:
                    st.caption("Jejak pencarian:")
                    st.markdown(f'<div class="log-box">{chr(10).join(log_steps)}</div>', unsafe_allow_html=True)
            else:
                st.warning("Masukkan kata kunci terlebih dahulu.")

    with tab_binary:
        section("BINARY SEARCH — PENCARIAN LOGARITMIK O(log n)")
        target_id = st.number_input("ID Buku yang dicari", min_value=1, value=1, key="bs_id")
        if st.button("⚡ Cari by ID", key="btn_binary"):
            arr = sorted(data, key=lambda b: b.id)
            low, high, langkah, steps = 0, len(arr) - 1, 0, []
            hasil = None
            while low <= high:
                langkah += 1
                mid = (low + high) // 2
                steps.append(f"[{langkah:02d}] mid={mid} → ID {arr[mid].id} ({arr[mid].judul})")
                if arr[mid].id == target_id:
                    hasil = arr[mid]
                    steps[-1] += "  ✅ FOUND"
                    break
                elif arr[mid].id < target_id:
                    steps[-1] += "  → kanan"
                    low = mid + 1
                else:
                    steps[-1] += "  ← kiri"
                    high = mid - 1

            col_res, col_steps = st.columns([1, 1])
            with col_res:
                if hasil:
                    st.success(f"✅ Ditemukan dalam {langkah} langkah")
                    st.dataframe(buku_df([hasil]), use_container_width=True, hide_index=True)
                else:
                    st.error(f"❌ ID {target_id} tidak ditemukan setelah {langkah} langkah.")
            with col_steps:
                st.caption("Jejak Binary Search:")
                st.markdown(f'<div class="log-box">{chr(10).join(steps)}</div>', unsafe_allow_html=True)


# =========================================================================
# HALAMAN: SORTING
# =========================================================================
def halaman_sorting():
    st.markdown("## 🔢 Sorting Engine")
    st.markdown("""
    <span class="algo-pill badge-orange">O(n²): Bubble · Insertion · Selection</span>
    <span class="algo-pill badge-green" style="color:#3fb950">O(n log n): Quick · Merge · Shell</span>
    """, unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    data = inv.ke_list()
    if not data:
        st.warning("Inventaris kosong.")
        return

    section("PILIH ALGORITMA SORTING")
    algo = st.selectbox("Algoritma", list(SORT_MAP.keys()))

    if st.button("▶️ Jalankan Sorting"):
        fn = SORT_MAP[algo]
        hasil = fn(data)
        kompleksitas = "O(n²)" if "O(n²)" in algo else "O(n log n)"
        st.success(f"✅ Berhasil diurutkan dengan **{algo}** [{kompleksitas}]")
        st.dataframe(buku_df(hasil), use_container_width=True, hide_index=True)
        log(f"Sorting dilakukan: {algo}")


# =========================================================================
# HALAMAN: OPERASI TREE
# =========================================================================
def halaman_tree():
    st.markdown("## 🌳 Operasi Tree")
    st.markdown('<span class="badge badge-green">Binary Search Tree</span>', unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    col_insert, col_ops = st.columns([1, 1])

    with col_insert:
        section("INSERT KE BST")
        data = inv.ke_list()
        if not data:
            st.info("Inventaris kosong.")
        else:
            pilihan = {f"[{b.id}] {b.judul}": b.id for b in data}
            selected = st.selectbox("Pilih Buku", list(pilihan.keys()))
            if st.button("🌱 Insert ke Tree"):
                id_buku = pilihan[selected]
                b = inv.cari_by_id(id_buku)
                tree.insert(id_buku, b.judul)
                log(f"BST insert: [{id_buku}] {b.judul}")
                st.success(f"✅ [{id_buku}] {b.judul} dimasukkan ke BST")

        st.markdown("<br>", unsafe_allow_html=True)
        section("SEARCH DI BST")
        cari_id = st.number_input("ID yang dicari", min_value=1, value=1, key="tree_search")
        if st.button("🔎 Cari di BST"):
            hasil = tree.search(cari_id)
            if hasil:
                st.success(f"✅ Ditemukan: [{hasil.id_buku}] {hasil.judul}")
            else:
                st.error(f"❌ ID {cari_id} tidak ada di BST.")

    with col_ops:
        section("TRAVERSAL")
        mode = st.radio("Mode Traversal", ["Inorder (ID naik)", "Preorder", "Postorder"])

        if st.button("🔁 Jalankan Traversal"):
            if mode == "Inorder (ID naik)":
                nodes = tree.inorder()
            elif mode == "Preorder":
                nodes = tree.preorder()
            else:
                nodes = tree.postorder()

            if not nodes:
                st.info("BST masih kosong, insert buku terlebih dahulu.")
            else:
                hasil_tree = "\n".join(f"[{n.id_buku:03d}] {n.judul}" for n in nodes)
                st.markdown(f'<div class="log-box">{hasil_tree}</div>', unsafe_allow_html=True)
                st.caption(f"Total node di BST: {len(nodes)}")


# =========================================================================
# HALAMAN: BUKU FAVORIT
# =========================================================================
def halaman_favorit():
    st.markdown("## ⭐ Buku Favorit")
    st.markdown('<span class="badge badge-purple">Circular Singly Linked List</span>', unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    col_form, col_list = st.columns([1, 1])

    with col_form:
        section("TAMBAH KE FAVORIT")
        data = inv.ke_list()
        if not data:
            st.info("Inventaris kosong.")
        else:
            pilihan = {f"[{b.id}] {b.judul}": b.id for b in data}
            selected = st.selectbox("Pilih Buku", list(pilihan.keys()))
            if st.button("⭐ Tambah Favorit"):
                id_buku = pilihan[selected]
                b = inv.cari_by_id(id_buku)
                fav.tambah(id_buku, b.judul)
                log(f"Favorit: [{id_buku}] {b.judul}")
                st.success(f'✅ "{b.judul}" ditambahkan ke favorit!')
                st.rerun()

    with col_list:
        section("DAFTAR FAVORIT (Circular SLL)")
        favs = fav.ke_list()
        if not favs:
            st.info("Belum ada buku favorit.")
        else:
            for i, f_node in enumerate(favs):
                st.markdown(f"""
                <div style="background:#161b22; border:1px solid #21262d; border-radius:8px;
                     padding:.6rem 1rem; margin-bottom:.35rem; font-family:'JetBrains Mono'; font-size:.82rem;
                     display:flex; justify-content:space-between;">
                    <span style="color:#e3b341">⭐ {i+1}</span>
                    <span style="color:#c9d1d9">{f_node.judul}</span>
                    <span style="color:#8b949e">ID {f_node.id_buku}</span>
                </div>""", unsafe_allow_html=True)
            st.caption(f"🔁 Circular — node terakhir kembali ke node pertama")


# =========================================================================
# HALAMAN: REKOMENDASI
# =========================================================================
def halaman_rekomendasi():
    st.markdown("## 💡 Sistem Rekomendasi")
    st.markdown('<span class="badge badge-purple">Circular Doubly Linked List</span>', unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    col_form, col_jelajah = st.columns([1, 1])

    with col_form:
        section("TAMBAH REKOMENDASI")
        data = inv.ke_list()
        if not data:
            st.info("Inventaris kosong.")
        else:
            pilihan = {f"[{b.id}] {b.judul}": b.id for b in data}
            selected = st.selectbox("Pilih Buku", list(pilihan.keys()))
            if st.button("💡 Tambah Rekomendasi"):
                id_buku = pilihan[selected]
                b = inv.cari_by_id(id_buku)
                rek.tambah(id_buku, b.judul)
                log(f"Rekomendasi: [{id_buku}] {b.judul}")
                st.success(f'✅ "{b.judul}" ditambahkan ke rekomendasi!')
                st.rerun()

    with col_jelajah:
        section("JELAJAHI REKOMENDASI (CDLL)")
        rekoms = rek.ke_list()
        if not rekoms:
            st.info("Belum ada rekomendasi.")
        else:
            idx = st.session_state.rekom_idx % len(rekoms)
            cur = rekoms[idx]

            st.markdown(f"""
            <div style="background:#1a1240; border:1px solid #6e40c9; border-radius:12px;
                 padding:1.5rem; text-align:center; font-family:'JetBrains Mono'; margin-bottom:.7rem;">
                <div style="color:#8b949e; font-size:.72rem;">REKOMENDASI {idx+1} / {len(rekoms)}</div>
                <div style="color:#bc8cff; font-size:1.15rem; font-weight:600; margin-top:.5rem;">{cur.judul}</div>
                <div style="color:#8b949e; font-size:.8rem; margin-top:.3rem;">ID Buku: {cur.id_buku}</div>
            </div>""", unsafe_allow_html=True)

            c1, c2 = st.columns(2)
            if c1.button("◀ Sebelumnya"):
                st.session_state.rekom_idx = (idx - 1) % len(rekoms)
                st.rerun()
            if c2.button("Berikutnya ▶"):
                st.session_state.rekom_idx = (idx + 1) % len(rekoms)
                st.rerun()


# =========================================================================
# HALAMAN: RIWAYAT AKTIVITAS
# =========================================================================
def halaman_riwayat():
    st.markdown("## 📜 Riwayat Aktivitas")
    st.markdown('<span class="badge">Double Linked List</span>', unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    arah = st.radio("Urutan tampilan:", ["Terbaru → Terlama", "Terlama → Terbaru"], horizontal=True)

    logs = riw.ke_list_mundur() if arah == "Terbaru → Terlama" else riw.ke_list_maju()

    if not logs:
        st.info("Belum ada riwayat aktivitas.")
    else:
        for i, l in enumerate(logs):
            icon = "🟢" if "Tambah" in l or "tambah" in l or "ditambahkan" in l else \
                   "🔵" if "Peminjaman" in l else \
                   "🟠" if "Pengembalian" in l or "kembali" in l else \
                   "🟣" if "Favorit" in l or "Rekomendasi" in l else \
                   "⚪"
            st.markdown(f"""
            <div style="background:#161b22; border:1px solid #21262d; border-left:3px solid #388bfd;
                 border-radius:6px; padding:.55rem 1rem; margin-bottom:.3rem;
                 font-family:'JetBrains Mono'; font-size:.8rem; color:#c9d1d9;">
                {icon} <span style="color:#8b949e">[{i+1:02d}]</span> {l}
            </div>""", unsafe_allow_html=True)
        st.caption(f"Total {riw.jumlah()} aktivitas tersimpan dalam Double Linked List")


# =========================================================================
# ROUTER
# =========================================================================
halaman = st.session_state.halaman

if halaman == "Dashboard":
    halaman_dashboard()
elif halaman == "Kelola Buku":
    halaman_kelola_buku()
elif halaman == "Peminjaman":
    halaman_peminjaman()
elif halaman == "Pengembalian":
    halaman_pengembalian()
elif halaman == "Searching Engine":
    halaman_searching()
elif halaman == "Sorting Engine":
    halaman_sorting()
elif halaman == "Operasi Tree":
    halaman_tree()
elif halaman == "Buku Favorit":
    halaman_favorit()
elif halaman == "Rekomendasi":
    halaman_rekomendasi()
elif halaman == "Riwayat Aktivitas":
    halaman_riwayat()