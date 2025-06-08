# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding

Jaya Jaya Institut merupakan salah satu institusi pendidikan perguruan yang telah berdiri sejak tahun 2000. Hingga saat ini ia telah mencetak banyak lulusan dengan reputasi yang sangat baik. Akan tetapi, terdapat banyak juga siswa yang tidak menyelesaikan pendidikannya alias drop-out.

### Permasalahan Bisnis

1. Tingginya jumlah siswa yang _drop-out_

   Jumlah siswa yang _drop-out_ perlu dikurangi untuk menjaga reputasi dan daya tarik institusi. Jumlah _drop-out_ yang tinggi dapat mencerminkan ketidakpuasan siswa terhadap kualitas pendidikan atau dukungan yang diberikan. Tingginya angka drop-out dapat mengakibatkan berkurangnya jumlah pendaftar baru, menurunnya kepercayaan orang tua dan calon siswa, serta berpotensi merusak reputasi institusi di mata masyarakat dan pihak pemangku kepentingan lainnya.

2. Tidak adanya sistem yang dapat memonitor situasi dan kondisi siswanya

   Tanpa sistem pemantauan yang efektif, institusi sulit untuk mengidentifikasi siswa yang berpotensi drop-out secara tepat waktu dan memberikan intervensi yang diperlukan. Hal ini membuat upaya pencegahan drop-out menjadi kurang efisien dan tidak terarah. Tanpa sistem monitoring, institusi tidak dapat secara proaktif menangani masalah siswa yang mengalami kesulitan akademik atau personal yang dapat menyebabkan drop-out. Ini dapat mengakibatkan peningkatan jumlah drop-out, yang pada gilirannya akan merugikan institusi dalam jangka panjang, baik dari segi finansial maupun reputasi.

### Cakupan Proyek

Proyek ini mencakup analisis data performa siswa untuk mengidentifikasi pola yang berkontribusi terhadap tingkat drop-out. Selain itu, proyek ini juga akan mencakup pengembangan model prediksi drop-out berbasis machine learning dan perancangan business dashboard interaktif yang akan mempermudah pemantauan performa siswa.

### Persiapan

Sumber data: [Jaya Jaya Institut](https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/data.csv)

Setup environment:
```
Membuat Virtual Environment Python
python -m venv venv / python3 -m venv venv 

Mengaktifkan venv
venv\Scripts\activate

Setup environment yang pertama yaitu menginstall dependensi
pip install -r requirements.txt

Melakukan prediksi menggunakan data baru bisa melalui 
app.py

Langkah langkah melakukan prediksi
1. Buka app.py
2. Lakukan edit pada isi feature di variabel data
3. Jalankan file menggunakan python app.py
4. Hasil prediksi akan muncul di output terminal 
```

## Business Dashboard

https://public.tableau.com/views/StudentPerformanceDashboard_17493664968670/StudentPerformanceDashboard?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link

Business dashboard yang dibuat bertujuan untuk memberikan wawasan mendalam mengenai pola akademik siswa dan faktor-faktor yang berkontribusi terhadap risiko drop-out. Dashboard ini akan membantu pihak akademik dalam memantau performa siswa serta mengambil langkah preventif untuk mengurangi angka drop-out.

### Penjelasan Dashboard

Dashboard ini menyajikan berbagai informasi terkait karakteristik mahasiswa dan faktor-faktor yang dapat berkontribusi terhadap kemungkinan drop-out:

- **Displaced (Mahasiswa Pindahan)**: Menunjukkan jumlah mahasiswa yang merupakan pindahan (1) dibandingkan dengan mahasiswa yang bukan pindahan (0). Mahasiswa pindahan tampaknya memiliki jumlah yang hampir seimbang dengan mahasiswa yang bukan pindahan.
- **Admission Grade**: Grafik ini menunjukkan distribusi nilai masuk mahasiswa, yang mencerminkan bagaimana kualitas akademik awal dapat mempengaruhi retensi mereka di institusi.
- **Class Type**: Memperlihatkan jumlah mahasiswa berdasarkan jenis kelas yang mereka ikuti. Mayoritas mahasiswa berada di kategori kelas tertentu (1), sementara hanya sebagian kecil dalam kategori lain (0).
- **Marital Status (Status Pernikahan)**: Diagram ini menggambarkan jumlah mahasiswa berdasarkan status pernikahan mereka. Sebagian besar mahasiswa memiliki status 1, sementara yang lainnya tersebar di kategori lainnya.
- **Scholarship (Beasiswa)**: Memperlihatkan jumlah mahasiswa yang menerima beasiswa (1) dibandingkan dengan mereka yang tidak menerima beasiswa (0). Beasiswa bisa menjadi faktor yang membantu mahasiswa untuk tetap melanjutkan studinya.
- **Tuition Fees Up to Date (Status Pembayaran Biaya Kuliah)**: Menampilkan jumlah mahasiswa yang telah membayar biaya kuliah tepat waktu (1) dibandingkan dengan yang memiliki tunggakan (0). Mahasiswa dengan tunggakan bisa berisiko lebih tinggi untuk dropout.
- **Total Student**: Menampilkan total jumlah mahasiswa yang dianalisis dalam dataset ini.

Dashboard ini membantu pengambil keputusan di perguruan tinggi dalam memahami faktor-faktor utama yang berkontribusi terhadap tingkat drop-out dan bagaimana intervensi dapat dilakukan untuk meningkatkan retensi mahasiswa.

## Menjalankan Sistem Machine Learning

```
Prototype sistem Machine Learning dapat diakses melalui link berikut :
https://bpds-2-fadhilah-nurrahmayanti-a117xbm150.streamlit.app/

Feature dapat diisi melalui sidebar Streamlit setelah selesai mengisi feature, bisa memencet tombol Predict Student Outcome, setelah itu output hasil prediksi akan muncul serta rekomendasi yang dapat dilakukan.
```

## Kesimpulan

Berdasarkan analisis yang dilakukan, ditemukan beberapa faktor utama yang berkontribusi terhadap tingkat drop-out siswa:

1. **Tingkat akademik dan performa mahasiswa**: Nilai pada mata kuliah tertentu, khususnya **admission grade** dan **curricular unit scores**, memiliki dampak signifikan terhadap kemungkinan drop-out.
2. **Faktor keuangan**: Mahasiswa yang memiliki tunggakan biaya kuliah (*tuition fees up to date*) cenderung memiliki kemungkinan lebih tinggi untuk drop-out.
3. **Latar belakang keluarga**: Pendidikan orang tua dan status pekerjaan mereka juga berkontribusi dalam prediksi dropout mahasiswa.
4. **Faktor sosial dan ekonomi**: Mahasiswa yang menerima beasiswa (*scholarship holder*) memiliki kecenderungan lebih kecil untuk drop-out.
5. **Faktor individu**: Usia saat masuk kuliah (*age at enrollment*) dan status sebagai mahasiswa internasional juga mempengaruhi retensi mahasiswa.

## Rekomendasi Action Items

Untuk membantu perguruan tinggi memahami dan mengidentifikasi pola yang mempengaruhi tingkat drop-out mahasiswa, berikut beberapa langkah strategis yang dapat diambil:

1. **Meningkatkan Dukungan Akademik**: 
   - Mengadakan program remedial untuk mahasiswa dengan nilai rendah di mata kuliah yang memiliki dampak besar terhadap kemungkinan drop-out.
   - Menyediakan bimbingan akademik lebih intensif bagi mahasiswa yang terindikasi berisiko tinggi drop-out.

2. **Menyediakan Bantuan Finansial**:
   - Memberikan fleksibilitas pembayaran biaya kuliah bagi mahasiswa dengan keterbatasan finansial.
   - Meningkatkan jumlah penerima beasiswa untuk mendukung mahasiswa dari latar belakang ekonomi kurang mampu.

3. **Memperhatikan Latar Belakang Mahasiswa**:
   - Memberikan program mentorship bagi mahasiswa yang berasal dari keluarga dengan tingkat pendidikan rendah.
   - Meningkatkan program orientasi dan dukungan bagi mahasiswa internasional agar mereka lebih mudah beradaptasi dengan lingkungan akademik.

4. **Monitoring Berbasis Data**:
   - Memanfaatkan business dashboard untuk melakukan pemantauan performa mahasiswa secara real-time.
   - Menggunakan model prediksi machine learning untuk mengidentifikasi mahasiswa yang memiliki risiko tinggi drop-out sejak dini.

5. **Meningkatkan Engagement Mahasiswa**:
   - Menyediakan kegiatan ekstrakurikuler dan komunitas akademik untuk meningkatkan keterlibatan mahasiswa dalam lingkungan kampus.
   - Mendorong komunikasi aktif antara dosen dan mahasiswa untuk menciptakan lingkungan belajar yang lebih suportif.

Dengan mengimplementasikan langkah-langkah ini, diharapkan tingkat drop-out mahasiswa di Jaya Jaya Institut dapat ditekan, sehingga lebih banyak mahasiswa dapat menyelesaikan studi mereka dengan sukses.
