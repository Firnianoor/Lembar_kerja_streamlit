import streamlit as st
import pandas as pd
import numpy as np
import requests
import matplotlib.pyplot as plt
import altair as alt
import plotly.express as px
from datetime import date, time
from PIL import Image

#4.5 Visualisasi st.plotly_chart(akan error jika tidak di letakkan di awal sebagai perintah streamlit pertama)
st.set_page_config(page_title="Dashboard Analisis Nilai Ujian Siswa", layout="wide")

#1. elemen text
st.title("Portofolio Tugas Aplikasi Streamlit")
st.header("Simulasi Aplikasi Streamlit")
st.subheader('Data Pengguna')
st.caption('untuk tujuan demonstrasi.')
st.code('import pandas as pd')
st.text('Ini adalah teks biasa tanpa format atau penekanan.')
st.latex(r"Y = \beta_0 + \beta_1 X + \epsilon")
st.markdown('_[Tautan Utama](https://streamlit.io)_')
st.divider()

#2. Data frame Input
#2.1 API
st.title('Data dari API')

url = 'https://jsonplaceholder.typicode.com/users' # API contoh
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    df = pd.DataFrame(data)
    st.dataframe(df)
    print(data)
else:
    print(f"Error: {response.status_code}")
    st.error('Gagal mengambil data dari API')

#2.2 CSV UPLOAD FILE
uploaded_file = st.file_uploader("Pilih file XLSX", type="xlsx")

if uploaded_file is not None:
    df = pd.read_excel(uploaded_file)
    st.dataframe(df)
    
else:
    st.write("Tidak ada file yang diunggah.")

#2.3 Simple Data
data = {
    'Nama': ['Mingyu', 'San', 'Ian'],
    'Umur': [28, 25, 34],
    'Kota': ['Bandung', 'Surabaya', 'Jakarta']
}

# Membuat DataFrame
df = pd.DataFrame(data)

# Menampilkan DataFrame
st.write("Tabel Data:")
st.write(df)

# Membuat DataFrame random
df = pd.DataFrame(
    np.random.randn(10, 5),
    columns=('col %d' % i for i in range(5))
)

# Menampilkan DataFrame di Streamlit
st.write("Tabel DataFrame Random:")
st.dataframe(df)

#3. metric Streamlit
st.title("Ringkasan Status Proyek")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(label="Progress Proyek", value="75%", delta="+10%")
    st.write("Pencapaian target utama proyek.")

with col2:
    st.metric(label="Tugas Selesai", value="42", delta="+5")
    st.write("Menunjukkan produktivitas tim.")

with col3:
    st.metric(label="Sisa Waktu", value="15 Hari", delta="-2 Hari")
    st.write("Waktu yang tersisa sebelum deadline.")

#4. CHARTS
#4.1 LINE CHARTS
chart_data = pd.DataFrame(
    np.random.randn(75,3),
    columns=['a', 'b', 'c']
)

st.line_chart(chart_data)

#4.2 Bar Chart
st.bar_chart(chart_data, color= ["#808080", "#FFC0CB", "#000080"])

#4.3 Altair Chart 
data = pd.DataFrame(
    np.random.randn(100, 3),
    columns=['a', 'b', 'c']
)

chart = alt.Chart(data.reset_index()).mark_line().encode(
    x='index',
    y='a'
)

st.altair_chart(chart, use_container_width=True)

#4.4 Map
# Koordinat perkiraan UNM FEB
latitude_unm_feb = -5.1494
longitude_unm_feb = 119.4232

chart_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [latitude_unm_feb, longitude_unm_feb],
    columns=['lat', 'lon'])

st.subheader("Peta Titik di Sekitar UNM FEB Makassar")
st.map(chart_data)

#4.5 Visualisasi st.plotly_chart()
st.title("Dashboard Analisis Nilai Ujian Siswa") # Mengganti st.title() saja sudah cukup

# Kode selanjutnya (pembuatan DataFrame, chart, layout, dll.)
data_ujian = pd.DataFrame({
    'Siswa': ['Andi', 'Budi', 'Citra', 'Dedi', 'Eka', 'Andi', 'Budi', 'Citra', 'Dedi', 'Eka'],
    'Mata Pelajaran': ['Matematika', 'Matematika', 'Matematika', 'Matematika', 'Matematika',
                       'Fisika', 'Fisika', 'Fisika', 'Fisika', 'Fisika'],
    'Nilai': [85, 78, 92, 65, 88, 76, 82, 90, 70, 85]
})

fig_nilai_siswa = px.bar(
    data_ujian,
    x='Siswa',
    y='Nilai',
    color='Mata Pelajaran',
    barmode='group',
    title='Perbandingan Nilai Ujian per Siswa',
    labels={'Nilai': 'Nilai Ujian', 'Siswa': 'Nama Siswa', 'Mata Pelajaran': 'Mata Pelajaran'},
    template='plotly_white'
)
fig_nilai_siswa.update_layout(title_x=0.5)

fig_distribusi_mapel = px.box(
    data_ujian,
    x='Mata Pelajaran',
    y='Nilai',
    color='Mata Pelajaran',
    title='Distribusi Nilai Ujian per Mata Pelajaran',
    labels={'Nilai': 'Nilai Ujian', 'Mata Pelajaran': 'Mata Pelajaran'},
    template='plotly_dark'
)
fig_distribusi_mapel.update_layout(title_x=0.5)

col1, col2 = st.columns(2)

with col1:
    st.plotly_chart(fig_nilai_siswa, use_container_width=True)

with col2:
    st.plotly_chart(fig_distribusi_mapel, use_container_width=True)

st.divider()
st.caption("Dibuat dengan ❤️ menggunakan Streamlit dan Plotly")

#5. Input Form
st.title("Formulir Pemesanan Tiket Konser SEVENTEEN di Korea")

with st.form("form_input"):
    nama_pemesan = st.text_input("Nama Pemesan (Sesuai KTP/Paspor):")
    alamat_email = st.text_area("Alamat Email:")
    usia = st.number_input("usia:", min_value=0)
    tanggal_konser = st.date_input("Tanggal Konser yang Dipilih:", date(2025, 12, 25))  
    waktu_konser = st.time_input("Waktu Konser yang Dipilih:", time(20, 00)) 
    jenis_tiket = st.radio("Jenis Tiket:", ("VIP", "STANDING", "CAT 1", "CAT 2", "CAT 3"))
    jumlah_tiket = st.number_input("Jumlah Tiket:", min_value=1, step=1)
    nomor_identitas = st.text_input("Nomor Identitas (KTP/Paspor):")
    warna_gelang = st.color_picker("Pilih Warna Gelang Konser:", "#0000FF")  
    bukti_bayar = st.file_uploader("Unggah Bukti Pembayaran:", type=["jpg", "png", "pdf"])
    foto_selfie_id = st.camera_input("Ambil Foto Selfie dengan Kartu Identitas:")
    tingkat_antusiasme = st.slider("Tingkat Antisipasi Konser (1-10):", 1, 10)

    submitted = st.form_submit_button("Pesan Tiket")

if submitted:
    st.success(f"Pesanan tiket konser SEVENTEEN untuk {nama_pemesan} berhasil dikirim!")
    st.write("Informasi yang Anda berikan:")
    st.write(f"Alamat Email: {alamat_email}")
    st.write(f"usia: {usia}")
    st.write(f"Tanggal Konser: {tanggal_konser}")
    st.write(f"Waktu Konser: {waktu_konser}")
    st.write(f"Jenis Tiket: {jenis_tiket}")
    st.write(f"Jumlah Tiket: {jumlah_tiket}")
    st.write(f"Warna Gelang Konser yang Dipilih: {warna_gelang}")
    st.write(f"Nomor Identitas: {nomor_identitas}")
    if bukti_bayar:
        st.write(f"Bukti Pembayaran Diunggah: {bukti_bayar.name}")
    if foto_selfie_id:
        st.image(foto_selfie_id, caption="Foto Selfie dengan Kartu Identitas", use_column_width=True)
        st.write(f"Tingkat Antisipasi Konser: {tingkat_antusiasme}/10")
    st.info("Pastikan Anda telah melakukan pembayaran sesuai dengan jumlah tiket yang dipesan.")   
    st.success("form.submitted!")

#6. Menampilkan Media
#6.1 Menampilkan photo dari file lokal
st.title("Photo dari File Lokal")
st.image("gambarst.jpg", caption="Foto Lokal Saya")

#6.2 menampilkan video lokal
st.title("Video dari File Lokal")
st.video('video.mp4') 

#6.3 Menampilkan photo dari url
st.title("Photo dari Tautan URL")
st.image('https://foto.kontan.co.id/ruYCYEC9Dz_zvQRaH4HZh1VK-7A=/smart/2025/04/28/460736263p.jpg', caption='Gambar dari URL', use_container_width=True)

#6.4 Menampilkan video dari url
st.title("video dari URL")
st.video('https://youtu.be/HB1sQUmMUXE?si=KK4V9WiIOcGtIl_a') 

#6.5 Menampilkan audio dari file lokal
st.title("Audio dari File Lokal")
st.audio('lagu.mp3')

#6.6 Menampilkan audio dari URL
st.title("Audio dari URL")
st.audio('https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3')

#7. Menampilkan Layout dan Container
#7.1. Menampilkan Layout Menggunakan Kolom
# Membuat dua kolom
col1, col2 = st.columns(2)

# Menampilkan konten di kolom pertama
with col1:
    st.header("Kolom 1")
    st.write("Ini adalah konten di kolom pertama.")
    st.button("Tombol Kolom 1")

# Menampilkan konten di kolom kedua
with col2:
    st.header("Kolom 2")
    st.write("Ini adalah konten di kolom kedua.")
    st.button("Tombol Kolom 2")

#7.2 Menggunakan st.expander() untuk Konten yang Bisa Dilipat
with st.expander("Klik untuk melihat lebih banyak"):
    st.write("Ini adalah konten tersembunyi yang bisa dilihat saat pengguna klik expander.")
    st.image("https://via.placeholder.com/150", caption="Contoh Gambar")

#7.3 Layout Menggunakan st.container()
# Membuat container
container = st.container()

# Menambahkan elemen ke dalam container
with container:
    st.header("Konten di dalam Container")
    st.write("Ini adalah elemen-elemen yang ada dalam container.")
    st.button("Tombol dalam Container")

#7.4 Menggunakan Sidebar
# Menambahkan elemen ke Sidebar
st.sidebar.header("Ini Sidebar")
st.sidebar.radio("Pilih Opsi", ["Opsi 1", "Opsi 2", "Opsi 3"])

# Konten utama
st.title("Konten Utama")
st.write("Ini adalah konten utama yang ditampilkan di layar.")


import streamlit as st

# Menambahkan elemen navigasi di Sidebar
st.sidebar.header("Navigasi")
selection = st.sidebar.radio("Pilih Halaman", ["Beranda", "Tentang", "Kontak"])

# Konten berdasarkan pilihan
if selection == "Beranda":
    st.title("Beranda")
    st.write("Ini adalah halaman beranda.")
elif selection == "Tentang":
    st.title("Tentang")
    st.write("Ini adalah halaman tentang.")
else:
    st.title("Kontak")
    st.write("Ini adalah halaman kontak.")

# Menambahkan elemen navigasi dengan dropdown di Sidebar
st.sidebar.header("Navigasi")
selection = st.sidebar.selectbox("Pilih Halaman", ["Beranda", "Tentang", "Galeri", "Kontak"])

# Konten berdasarkan pilihan
if selection == "Beranda":
    st.title("Beranda")
    st.write("Ini adalah halaman beranda.")
elif selection == "Tentang":
    st.title("Tentang")
    st.write("Ini adalah halaman tentang.")
elif selection == "Galeri":
    st.title("Galeri")
    st.write("Ini adalah halaman galeri.")
else:
    st.title("Kontak")
    st.write("Ini adalah halaman kontak.")

# Menambahkan tombol untuk navigasi di Sidebar
st.sidebar.header("Navigasi")
if st.sidebar.button("Beranda"):
    st.title("Beranda")
    st.write("Ini adalah halaman beranda.")
elif st.sidebar.button("Tentang"):
    st.title("Tentang")
    st.write("Ini adalah halaman tentang.")
elif st.sidebar.button("Kontak"):
    st.title("Kontak")
    st.write("Ini adalah halaman kontak.")

# Menambahkan tautan navigasi di Sidebar
st.sidebar.header("Navigasi")
st.sidebar.markdown("[Beranda](#beranda)")
st.sidebar.markdown("[Tentang](#tentang)")
st.sidebar.markdown("[Kontak](#kontak)")

# Konten halaman berdasarkan tautan
st.title("Beranda")
st.write("Ini adalah halaman beranda.")

st.title("Tentang")
st.write("Ini adalah halaman tentang.")

st.title("Kontak")
st.write("Ini adalah halaman kontak.")