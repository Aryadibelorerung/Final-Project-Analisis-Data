# Final Project Data Analytics: Bike Rentals

## Deskripsi
Proyek ini merupakan bagian dari tugas akhir dalam kursus "Belajar Analisis Data dengan Python" di Dicoding. Dalam proyek ini, saya melakukan eksplorasi dan analisis mendalam terhadap dataset bike sharing, serta mengembangkan sebuah dashboard interaktif untuk memvisualisasikan hasil analisis.

Pada notebook ini, saya telah mendokumentasikan seluruh tahapan proses analisis, dimulai dari Data Wrangling, Exploratory Data Analysis (EDA), hingga Visualisasi Data. Setiap langkah dilakukan secara sistematis untuk menggali wawasan berharga dari dataset. Selain itu, saya juga mengembangkan sebuah dashboard interaktif menggunakan Streamlit, yang memungkinkan pengguna untuk melihat dan berinteraksi dengan hasil analisis secara lebih intuitif.

Untuk memahami lebih dalam mengenai latar belakang dataset, karakteristik data, struktur file, serta informasi lainnya, silakan merujuk pada Readme file yang telah disediakan. Oleh karena itu, saya tidak akan menguraikannya lebih lanjut di bagian ini.

## 1 Struktur File
<pre>
submission
├── dashboard
│   ├── dashboard.py
│   ├── day_clean.csv
│   └── hour_clean.csv
├── data
│   ├── Readme.txt
│   ├── day.csv
|   └── hour.csv
├── README.md
├── notebook.ipynb
├── requirements.txt
└── url.txt
</pre>

## 2. Siklus Kerja Proyek

1. Data Wrangling:
Mengumpulkan dataset yang akan dianalisis.
Melakukan penilaian terhadap kualitas dan kelengkapan data.
Membersihkan data untuk memastikan konsistensi dan akurasi.
2. Eksplorasi Data (Exploratory Data Analysis):
Menentukan pertanyaan bisnis utama yang akan dijawab melalui analisis data.
Melakukan eksplorasi data secara mendalam untuk menemukan pola dan wawasan.
3. Visualisasi Data:
Membuat visualisasi yang relevan untuk menjawab pertanyaan bisnis yang telah ditentukan.
Menyajikan data dalam bentuk grafik dan diagram yang mudah dipahami.
4. Pengembangan Dashboard:
Menyiapkan DataFrame yang akan digunakan dalam dashboard.
Membuat komponen filter interaktif untuk meningkatkan pengalaman pengguna.
Melengkapi dashboard dengan berbagai visualisasi data guna menyajikan informasi yang lebih komprehensif.

## 3. Cara Penggunaan

Untuk menjalankan proyek secara lokal, ikuti langkah-langkah berikut:

1. **Masuk ke direktori proyek:**
<pre>cd submission/dashboard/</pre>

2. **Jalankan aplikasi dengan Streamlit:** 
<pre>streamlit run dashboard.py</pre>