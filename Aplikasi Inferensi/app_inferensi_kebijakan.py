# ============================================================
# app_inferensi_kebijakan.py
# ============================================================
# Aplikasi GUI berbasis Streamlit untuk:
# - Menjalankan inferensi logika (First Order Logic)
# - Mengintegrasikan Python dengan SWI-Prolog
# - Menguji rule-based reasoning pada optimasi playlist musik
#
# Teknologi:
# - Python (GUI & kontrol alur)
# - Streamlit (User Interface)
# - SWI-Prolog + pyswip (Knowledge Base & Inferensi)
#
# Tujuan akademik:
# - Demonstrasi reasoning berbasis aturan (rule-based system)
# - Menunjukkan chaining inferensi logika
# - Visualisasi hasil query Prolog dalam bentuk tabel
# ============================================================

# ============================================================
# IMPORT LIBRARY
# ============================================================
# pandas
# Digunakan untuk mengubah hasil query Prolog (list of dict)
# menjadi DataFrame agar mudah ditampilkan dalam GUI
import pandas as pd

# streamlit
# Framework GUI berbasis web untuk Python
# Digunakan untuk:
# - Layout halaman
# - Tombol
# - Tabel
# - Expander
# - Input user
import streamlit as st

# pyswip.Prolog
# Library Python untuk berinteraksi dengan SWI-Prolog
# Digunakan untuk:
# - Load knowledge base (.pl)
# - Menjalankan query Prolog
from pyswip import Prolog

# ============================================================
# 1. SETUP APLIKASI & LOAD KNOWLEDGE BASE
# ============================================================

# Nama file Knowledge Base Prolog
# Berisi fakta dan aturan inferensi playlist
KB_FILE = "prolog_kb.pl"

# Konfigurasi halaman Streamlit
# layout="wide" agar tampilan lebih lebar dan nyaman
st.set_page_config(layout="wide")

# Judul utama aplikasi
st.title("🎵 Logic Programming GUI: Optimasi Urutan Playlist Musik")

# ============================================================
# Inisialisasi Engine Prolog
# ============================================================
# Menggunakan st.session_state agar:
# - Prolog hanya di-load sekali
# - Tidak reload setiap interaksi tombol
# - Lebih efisien
if "prolog" not in st.session_state:
    try:
        # Membuat instance Prolog
        prolog = Prolog()

        # Load knowledge base (.pl)
        prolog.consult(KB_FILE)

        # Simpan ke session_state
        st.session_state.prolog = prolog
        st.session_state.kb_loaded = True

    except Exception as e:
        # Jika gagal load KB:
        # - tampilkan error
        # - hentikan aplikasi
        st.error("Gagal memuat SWI-Prolog atau Knowledge Base.")
        st.error(e)
        st.stop()

# Ambil instance Prolog dari session
prolog = st.session_state.prolog

# Notifikasi sukses load KB
st.success(f"Knowledge Base `{KB_FILE}` berhasil dimuat")

# ============================================================
# 2. DAFTAR INFERENSI (QUERY WAJIB)
# ============================================================
# Setiap inferensi merepresentasikan:
# - Satu rule atau kesimpulan logika
# - Query Prolog
# - Penjelasan konseptual
#
# Inferensi ini digunakan untuk menunjukkan:
# - Rule dasar
# - Chaining inferensi
# - Reasoning bertingkat
inferensi_list = [
    {
        "nama": "Inferensi 1: Lagu Ekstrem",
        "query": "lagu_ekstrem(X)",
        "deskripsi": "Rule 1 – Lagu dengan energi sangat tinggi atau rendah",
    },
    {
        "nama": "Inferensi 2: Pembentuk Outlier",
        "query": "pembentuk_outlier(X)",
        "deskripsi": "Rule 2 – Lagu ekstrem berpotensi menjadi outlier",
    },
    {
        "nama": "Inferensi 3: Wajib Kurasi Manual",
        "query": "wajib_kurasi_manual(X)",
        "deskripsi": "Rule 3 – Rantai inferensi (ekstrem → outlier → kurasi)",
    },
    {
        "nama": "Inferensi 4: Energi Kontras",
        "query": "energi_kontras(X, Y)",
        "deskripsi": "Rule 5 – Perbedaan energi lagu signifikan",
    },
    {
        "nama": "Inferensi 5: Transisi Kasar",
        "query": "transisi_kasar(X, Y)",
        "deskripsi": "Rule 6 – Energi kontras atau jarak graf besar",
    },
    {
        "nama": "Inferensi 6: Butuh Lagu Bridge",
        "query": "butuh_lagu_bridge(X, Y)",
        "deskripsi": "Rule 8 – Kesimpulan dari transisi kasar",
    },
    {
        "nama": "Inferensi 7: Transisi Harmonis",
        "query": "transisi_harmonis(X, Y)",
        "deskripsi": "Rule 7 – Jarak graf kecil (transisi halus)",
    },
    {
        "nama": "Inferensi 8: Rekomendasi Urutan Playlist",
        "query": "rekomendasi_urutan(X, Y)",
        "deskripsi": "Rule 9 – Pasangan lagu ideal",
    },
]


# ============================================================
# 3. FUNGSI EKSEKUSI QUERY PROLOG
# ============================================================
def run_query(query):
    """
    Menjalankan query Prolog dan menginterpretasikan hasilnya.

    Kemungkinan hasil:
    1. False → tidak ada solusi
    2. True  → query valid tanpa variabel
    3. Binding variabel → ditampilkan sebagai tabel
    """
    try:
        # Jalankan query Prolog
        results = list(prolog.query(query))

        # Jika tidak ada hasil → False
        if not results:
            return "TIDAK VALID (False)"

        # Jika hanya True tanpa binding variabel
        if len(results) == 1 and results[0] == {}:
            return "VALID (True)"

        # Jika ada binding variabel
        # Konversi ke list of dict agar bisa jadi DataFrame
        table = []
        for res in results:
            row = {k: str(v) for k, v in res.items()}
            table.append(row)

        return table

    except Exception as e:
        # Tangani error query Prolog
        return f"ERROR Query Prolog: {e}"


# ============================================================
# 4. TAMPILAN GUI
# ============================================================

# Layout dua kolom:
# - Kiri  : Knowledge Base
# - Kanan : Inferensi & Query
col_kb, col_query = st.columns([1, 2])

# ============================================================
# KOLOM KIRI – KNOWLEDGE BASE
# ============================================================
with col_kb:
    st.header("📚 Knowledge Base Prolog")

    # Tampilkan isi file Prolog
    try:
        with open(KB_FILE, "r") as f:
            kb_content = f.read()
        st.code(kb_content, language="prolog")
    except FileNotFoundError:
        st.warning("File KB tidak ditemukan.")

# ============================================================
# KOLOM KANAN – INFERENSI & QUERY
# ============================================================
with col_query:
    st.header("🧠 Uji Inferensi Logika (FOL)")
    st.info("Klik tombol untuk menjalankan inferensi dari Knowledge Base")

    # Loop setiap inferensi
    for i, item in enumerate(inferensi_list):
        with st.expander(item["nama"], expanded=False):
            st.markdown(f"**Tujuan:** {item['deskripsi']}")
            st.code(item["query"], language="prolog")

            # Tombol eksekusi inferensi
            if st.button(f"UJI INFERENSI {i + 1}", key=f"btn_{i}"):
                result = run_query(item["query"])

                if isinstance(result, list):
                    st.success(f"Ditemukan {len(result)} hasil:")
                    st.dataframe(pd.DataFrame(result), use_container_width=True)
                else:
                    st.info(result)

    # ========================================================
    # QUERY KUSTOM
    # ========================================================
    st.markdown("---")
    st.subheader("🔍 Query Prolog Kustom")

    # Input query bebas dari user
    custom_query = st.text_input("Masukkan Query Prolog (contoh: beda_genre(X, Y).)")

    # Tombol eksekusi query kustom
    if st.button("JALANKAN QUERY KUSTOM"):
        if custom_query.strip():
            result = run_query(custom_query)

            if isinstance(result, list):
                st.success("Hasil Query Kustom:")
                st.dataframe(pd.DataFrame(result), use_container_width=True)
            else:
                st.info(result)
        else:
            st.warning("Query tidak boleh kosong.")
