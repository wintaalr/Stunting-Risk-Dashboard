import streamlit as st
from pathlib import Path

# ======================================================
# PAGE CONFIG
# ======================================================

st.set_page_config(
    page_title="Stunting Risk Dashboard",
    page_icon="👶",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ======================================================
# LOAD CSS
# ======================================================

css_file = Path("assets/style.css")

if css_file.exists():
    with open(css_file) as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

# ======================================================
# SIDEBAR
# ======================================================

st.sidebar.image(
    "https://cdn-icons-png.flaticon.com/512/2966/2966481.png",
    width=110
)

st.sidebar.markdown("# 👶 Stunting Analytics")

st.sidebar.markdown("---")

st.sidebar.success(
    "Machine Learning Decision Support System"
)

st.sidebar.markdown("---")

st.sidebar.info(
"""
📊 Dashboard Features

• Overview

• Prediction

• About
"""
)

st.sidebar.markdown("---")

st.sidebar.caption(
"""
Business Statistics ITS

© 2026
"""
)

# ======================================================
# HEADER
# ======================================================

st.markdown(
"""
<div class='main-title'>
👶 Stunting Risk Analytics Dashboard
</div>

<div class='sub-title'>
Machine Learning Based Decision Support System
</div>
""",
unsafe_allow_html=True
)

st.markdown("---")

# ======================================================
# HERO
# ======================================================

left, right = st.columns([2,1])

with left:

    st.markdown("""

### Welcome 👋

Dashboard ini dikembangkan untuk membantu
analisis dan prediksi risiko stunting
Kabupaten/Kota di Provinsi Jawa Timur
menggunakan pendekatan Machine Learning.

Metode yang digunakan:

- Principal Component Analysis (PCA)

- K-Means Clustering

- Linear Regression

Silakan pilih menu pada sidebar
untuk mulai melakukan analisis.

""")

with right:

    st.info("""

📌 Data Source

Badan Pusat Statistik

Provinsi Jawa Timur

Tahun 2023 - 2024

""")

st.markdown("---")

# ======================================================
# INFORMASI SINGKAT
# ======================================================

c1, c2, c3, c4 = st.columns(4)

c1.metric(
    "Provinsi",
    "Jawa Timur"
)

c2.metric(
    "Model",
    "Linear Regression"
)

c3.metric(
    "Metode",
    "PCA + K-Means"
)

c4.metric(
    "Dashboard",
    "Ready"
)

st.markdown("---")

st.success(
"""
Silakan pilih halaman melalui sidebar
untuk mulai mengeksplorasi hasil analisis dan prediksi risiko stunting.
"""
)

st.caption(
"""
Dashboard ini dikembangkan sebagai bagian dari project akhir mata kuliah pembelajaran mesin
Business Statistics Institut Teknologi Sepuluh Nopember.
"""
)

