Pertemuan 09 - List dan Pengolahan Data Numerik

Nama: [khunaepi]
NIM: [2225250053]
Kelas: [3B]

1. Tujuan

Mempelajari penggunaan list dalam Python untuk menyimpan, mengakses, mengubah, dan mengolah kumpulan data numerik. Materi juga mencakup penggunaan indeks, slicing, perulangan, seleksi, fungsi statistik, serta pengumpulan tugas menggunakan Git dan GitHub.

2. Struktur Folder

pertemuan-09-list-NIM/
├── README.md
├── .gitignore
├── latihan/
│   ├── 01_buat_list.py
│   ├── 02_indeks_slicing.py
│   ├── 03_manipulasi_list.py
│   ├── 04_agregasi_nilai.py
│   ├── 05_filter_kelulusan.py
│   └── 06_fungsi_statistik.py
├── praktik/
│   └── analisis_nilai_mahasiswa.py
└── kuis/
    ├── kuis_3.md
    └── exit_ticket.md

3. Daftar Latihan

1. 01_buat_list.py — Membuat list dan menghitung banyak data menggunakan "len()".
2. 02_indeks_slicing.py — Mengakses elemen list menggunakan indeks dan slicing.
3. 03_manipulasi_list.py — Mengubah, menambahkan, dan menghapus elemen list.
4. 04_agregasi_nilai.py — Menghitung total, rata-rata, nilai minimum, dan maksimum.
5. 05_filter_kelulusan.py — Memilih nilai yang memenuhi batas kelulusan menggunakan perulangan dan seleksi.
6. 06_fungsi_statistik.py — Menghitung rata-rata menggunakan fungsi buatan sendiri.

4. Program Praktik

File: "praktik/analisis_nilai_mahasiswa.py"

Program ini digunakan untuk mengolah data nilai mahasiswa. Fitur yang diterapkan meliputi:

- Menampilkan seluruh data nilai.
- Menghitung banyak data dan total nilai.
- Menghitung rata-rata nilai.
- Menentukan nilai minimum dan maksimum.
- Menampilkan daftar nilai lulus dengan batas nilai minimal 60.
- Menghitung jumlah mahasiswa yang lulus dan belum lulus.
- Menggunakan fungsi untuk menghitung rata-rata dan menyaring nilai lulus.

5. Cara Menjalankan Program

Pastikan Python sudah terpasang dan folder proyek telah dibuka di VS Code.

Jalankan program praktik utama melalui terminal dari folder utama proyek:

python praktik/analisis_nilai_mahasiswa.py

Jika perintah "python" tidak dikenali pada Windows, coba:

py praktik/analisis_nilai_mahasiswa.py

Untuk menjalankan salah satu latihan, gunakan contoh berikut:

python latihan/01_buat_list.py

Nama file dapat diganti sesuai latihan yang ingin dijalankan.

6. Test Case Program Praktik

Data masukan:

nilai = [78, 55, 90, 67, 60, 82, 45, 71, 88, 59]

Hasil yang diharapkan:

Keterangan| Hasil
Banyak data| 10
Total nilai| 695
Rata-rata| 69.50
Nilai minimum| 45
Nilai maksimum| 90
Daftar nilai lulus| [78, 90, 67, 60, 82, 71, 88]
Jumlah lulus| 7
Jumlah belum lulus| 3

Hasil aktual: Sesuai dengan hasil yang diharapkan setelah program dijalankan.

Status: Berhasil, apabila hasil aktual pada komputer sesuai dengan hasil yang diharapkan.

7. Kuis dan Exit Ticket

Folder "kuis" berisi dua file dokumentasi:

- "kuis_3.md" — Berisi 10 pertanyaan kuis formatif mengenai list, indeks, slicing, manipulasi data, fungsi, dan GitHub beserta jawabannya.
- "exit_ticket.md" — Berisi empat pertanyaan refleksi mengenai pemahaman materi Pertemuan 09 dan persiapan untuk materi string pada Pertemuan 10.

8. Git dan GitHub

Proyek ini dikelola menggunakan Git untuk mencatat perubahan kode dan GitHub untuk menyimpan repositori secara daring.

Perintah dasar untuk memperbarui repositori setelah perubahan:

git add .
git commit -m "docs: memperbarui dokumentasi tugas"
git push

9. Refleksi

Melalui kegiatan ini, saya mempelajari cara menyimpan banyak data menggunakan list, mengakses elemen dengan indeks dan slicing, serta memanipulasi data menggunakan "append()", "insert()", dan "remove()". Saya juga memahami penggunaan perulangan, seleksi, dan fungsi untuk menghitung statistik nilai mahasiswa serta menentukan kelulusan. Selain itu, saya belajar menyusun struktur proyek dan mendokumentasikan hasil pekerjaan menggunakan README, Git, dan GitHub.

10. Sumber

Bahan ajar Pertemuan 09 — List dan Pengolahan Data Numerik: Praktik di VS Code dan Pengumpulan melalui GitHub.
