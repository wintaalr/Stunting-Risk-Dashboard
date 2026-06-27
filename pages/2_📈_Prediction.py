import streamlit as st
import joblib
import numpy as np
import pandas as pd
from pathlib import Path

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="Prediction",
    page_icon="📈",
    layout="wide"
)

# =====================================================
# LOAD CSS
# =====================================================

css_path = Path("assets/style.css")

if css_path.exists():
    with open(css_path) as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

# =====================================================
# LOAD MODEL
# =====================================================

model = joblib.load("model/linear_regression_stunting.pkl")

# =====================================================
# HEADER
# =====================================================

st.title("📈 Prediksi Risiko Stunting")

st.write(
    "Masukkan nilai indikator untuk memperoleh prediksi persentase stunting."
)

st.divider()

# =====================================================
# INPUT
# =====================================================

col1, col2 = st.columns(2)

with col1:

    sanitasi = st.slider(
        "Sanitasi (%)",
        0.0,
        100.0,
        80.0
    )

    air = st.slider(
        "Air Bersih (%)",
        0.0,
        100.0,
        80.0
    )

    imunisasi = st.slider(
        "Imunisasi (%)",
        0.0,
        100.0,
        90.0
    )

    ikp = st.slider(
        "IKP",
        0.0,
        100.0,
        75.0
    )

with col2:

    rls = st.slider(
        "Rata-rata Lama Sekolah",
        0.0,
        15.0,
        8.0
    )

    pengeluaran = st.slider(
        "Log Pengeluaran",
        12.0,
        16.0,
        14.0
    )

    kemiskinan = st.slider(
        "Kemiskinan (%)",
        0.0,
        40.0,
        10.0
    )

st.divider()

# =====================================================
# BUTTON
# =====================================================

if st.button(
    "🔮 Prediksi Risiko",
    use_container_width=True
):

    X = np.array([[
        sanitasi,
        air,
        imunisasi,
        ikp,
        rls,
        pengeluaran,
        kemiskinan
    ]])

    hasil = model.predict(X)[0]

    hasil = max(0, hasil)

    # =====================================================
    # KATEGORI
    # =====================================================

    if hasil >= 30:

        kategori = "🔴 Sangat Tinggi"
        warna = "error"

    elif hasil >= 25:

        kategori = "🟠 Tinggi"
        warna = "warning"

    elif hasil >= 20:

        kategori = "🟡 Sedang"
        warna = "info"

    elif hasil >= 15:

        kategori = "🟢 Rendah"
        warna = "success"

    else:

        kategori = "🟢 Sangat Rendah"
        warna = "success"

    # =====================================================
    # HASIL
    # =====================================================

    st.subheader("📊 Hasil Prediksi")

    c1, c2 = st.columns(2)

    c1.metric(
        "Prediksi Stunting",
        f"{hasil:.2f}%"
    )

    c2.metric(
        "Kategori Risiko",
        kategori
    )

    st.divider()

    # =====================================================
    # RINGKASAN INPUT
    # =====================================================

    st.subheader("📋 Ringkasan Input")

    ringkasan = pd.DataFrame({

        "Indikator":[

            "Sanitasi",
            "Air Bersih",
            "Imunisasi",
            "IKP",
            "RLS",
            "Pengeluaran Log",
            "Kemiskinan"

        ],

        "Nilai":[

            sanitasi,
            air,
            imunisasi,
            ikp,
            rls,
            pengeluaran,
            kemiskinan

        ]

    })

    st.dataframe(
        ringkasan,
        use_container_width=True,
        hide_index=True
    )

    st.divider()

    # =====================================================
    # REKOMENDASI
    # =====================================================

    st.subheader("🎯 Rekomendasi")

    if hasil >= 30:

        st.error("""
Prioritaskan intervensi kesehatan masyarakat.

Fokus pada:

• Peningkatan Sanitasi

• Akses Air Bersih

• Imunisasi

• Penurunan Kemiskinan
""")

    elif hasil >= 25:

        st.warning("""
Risiko cukup tinggi.

Perlu peningkatan layanan kesehatan dasar
dan monitoring berkala.
""")

    elif hasil >= 20:

        st.info("""
Risiko sedang.

Pertahankan program yang berjalan dan
lakukan evaluasi secara rutin.
""")

    else:

        st.success("""
Risiko relatif rendah.

Pertahankan kualitas pelayanan
dan lakukan monitoring berkala.
""")

    st.divider()

    # =====================================================
    # CATATAN
    # =====================================================

    st.caption(
        """
Prediksi diperoleh menggunakan model
Linear Regression yang telah dilatih
menggunakan data Kabupaten/Kota
Provinsi Jawa Timur.
"""
    )