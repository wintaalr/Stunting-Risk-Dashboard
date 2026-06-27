import streamlit as st
from pathlib import Path

# =====================================================
# CSS
# =====================================================

css_path = Path("assets/style.css")

if css_path.exists():
    with open(css_path) as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

# =====================================================
# HEADER
# =====================================================

st.title("ℹ Tentang Dashboard")

st.markdown("""
Dashboard ini dikembangkan sebagai **Decision Support System**
untuk membantu proses identifikasi tingkat risiko stunting
Kabupaten/Kota di Provinsi Jawa Timur.
""")

st.divider()

# =====================================================
# TUJUAN
# =====================================================

st.subheader("🎯 Tujuan Penelitian")

st.write("""
Penelitian ini bertujuan untuk membangun model prediksi
tingkat stunting menggunakan pendekatan Machine Learning
serta menyajikannya dalam bentuk dashboard interaktif
yang dapat digunakan sebagai pendukung pengambilan keputusan.
""")

st.divider()

# =====================================================
# METODOLOGI
# =====================================================

st.subheader("⚙ Metodologi")

st.markdown("""

1. Pengumpulan Data

↓

2. Data Cleaning

↓

3. Missing Value Imputation

↓

4. Principal Component Analysis (PCA)

↓

5. K-Means Clustering

↓

6. Linear Regression

↓

7. Dashboard Visualization

""")

st.divider()

# =====================================================
# DATASET
# =====================================================

st.subheader("📂 Dataset")

st.markdown("""

Sumber data berasal dari publikasi resmi BPS
dan instansi pemerintah terkait.

Variabel yang digunakan:

- Sanitasi
- Air Bersih
- Imunisasi
- IKP
- Rata-rata Lama Sekolah
- Pengeluaran Per Kapita
- Kemiskinan

Target:

- Persentase Stunting

""")

st.divider()

# =====================================================
# MODEL
# =====================================================

st.subheader("🤖 Model Machine Learning")

st.info("""

Model Final

✔ Linear Regression

Evaluasi menggunakan:

• MAE

• RMSE

• R² Score

""")

st.divider()

# =====================================================
# FOOTER
# =====================================================

st.caption("""

Business Statistics

Institut Teknologi Sepuluh Nopember

2026

""")