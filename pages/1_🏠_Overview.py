import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from pathlib import Path

# Load CSS
css_path = Path("assets/style.css")
if css_path.exists():
    with open(css_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Load Data
df = pd.read_excel("data/dashboard_stunting.xlsx")

# ==================== HEADER ====================
st.title("📊 Dashboard Overview")
st.write("Ringkasan hasil analisis risiko stunting Kabupaten/Kota di Provinsi Jawa Timur.")

st.divider()

# ==================== FILTER ====================
col1, col2 = st.columns(2)

with col1:
    kabupaten = st.selectbox(
        "Pilih Kabupaten/Kota",
        sorted(df["Kabupaten_Kota"].unique())
    )

with col2:
    tahun = st.selectbox(
        "Pilih Tahun",
        sorted(df["Tahun"].unique()),
        index=1  # default 2024
    )

# Filter data
selected_df = df[(df["Kabupaten_Kota"] == kabupaten) & (df["Tahun"] == tahun)]

if selected_df.empty:
    st.error("Data tidak ditemukan untuk kabupaten dan tahun tersebut.")
    st.stop()

selected = selected_df.iloc[0]

# ==================== KATEGORI RISIKO ====================
prediksi = selected["Prediksi_Stunting"]

if prediksi >= 30:
    status = "🔴 Sangat Tinggi"
elif prediksi >= 25:
    status = "🟠 Tinggi"
elif prediksi >= 20:
    status = "🟡 Sedang"
elif prediksi >= 15:
    status = "🟢 Rendah"
else:
    status = "🟢 Sangat Rendah"

# ==================== KPI ====================
c1, c2, c3, c4 = st.columns(4)

c1.metric("Prediksi", f"{prediksi:.2f}%")
c2.metric("Aktual", f"{selected['Stunting']:.2f}%")
c3.metric("Cluster", str(selected.get("Cluster", "N/A")))
c4.metric("Risiko", status)

st.divider()

# ==================== PROFIL & INDIKATOR ====================
left, right = st.columns(2)

with left:
    st.subheader("📍 Profil Wilayah")
    st.write(f"**Kabupaten/Kota :** {selected['Kabupaten_Kota']}")
    st.write(f"**Tahun :** {selected['Tahun']}")
    st.write(f"**Residual :** {selected['Residual']:.2f}")

with right:
    st.subheader("📋 Nilai Indikator")
    st.write(f"Sanitasi : {selected['Sanitasi']:.2f}%")
    st.write(f"Air Bersih : {selected['Air Bersih']:.2f}%")
    st.write(f"Imunisasi : {selected['Imunisasi']:.2f}%")
    st.write(f"IKP : {selected['IKP']:.2f}")
    st.write(f"RLS : {selected['RLS']:.2f} tahun")
    st.write(f"Kemiskinan : {selected['Kemiskinan']:.2f}%")

st.divider()

# ==================== RADAR CHART ====================
st.subheader("📈 Profil Indikator")

kategori = ["Sanitasi", "Air Bersih", "Imunisasi", "IKP", "RLS", "Kemiskinan"]
nilai = [
    selected["Sanitasi"],
    selected["Air Bersih"],
    selected["Imunisasi"],
    selected["IKP"],
    selected["RLS"] * 10,
    100 - selected["Kemiskinan"] * 2.5
]

fig = go.Figure()
fig.add_trace(go.Scatterpolar(
    r=nilai,
    theta=kategori,
    fill="toself",
    line=dict(color="#48CAE4", width=3),
    fillcolor="rgba(72,202,228,0.30)"
))

fig.update_layout(
    height=450,
    showlegend=False,
    polar=dict(radialaxis=dict(visible=True, range=[0,100]))
)

st.plotly_chart(fig, use_container_width=True)

# ==================== PROGRESS ====================
st.subheader("📊 Kondisi Indikator")

indikator = {
    "Sanitasi": selected["Sanitasi"],
    "Air Bersih": selected["Air Bersih"],
    "Imunisasi": selected["Imunisasi"],
    "IKP": selected["IKP"],
    "RLS": selected["RLS"] * 10,
    "Kemiskinan": 100 - selected["Kemiskinan"] * 2.5
}

for nama, nilai in indikator.items():
    st.write(f"**{nama}**")
    st.progress(int(max(0, min(nilai, 100))))
    st.caption(f"{nilai:.1f}")

st.divider()

# ==================== INSIGHT & REKOMENDASI ====================
st.subheader("🧠 Insight")
prioritas = min(indikator, key=indikator.get)
st.info(f"Indikator yang perlu perhatian utama adalah **{prioritas}**.")

st.subheader("🎯 Rekomendasi")
if status == "🔴 Sangat Tinggi":
    st.error("Prioritaskan peningkatan sanitasi, air bersih, imunisasi, dan penurunan kemiskinan.")
elif status == "🟠 Tinggi":
    st.warning("Perlu peningkatan kualitas pelayanan dasar dan monitoring berkala.")
else:
    st.success("Kondisi relatif baik. Pertahankan capaian yang ada.")

st.divider()

# ==================== DETAIL DATA ====================
st.subheader("📄 Detail Data")
st.dataframe(selected.to_frame().T, use_container_width=True, hide_index=True)