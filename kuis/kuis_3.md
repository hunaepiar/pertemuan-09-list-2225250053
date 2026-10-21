Kuis Formatif - Kuis 3

Pertemuan 09: List dan Pengolahan Data Numerik

1. Mengapa list lebih tepat daripada banyak variabel terpisah untuk menyimpan 30 nilai?

Jawab: Karena list dapat menyimpan banyak nilai dalam satu variabel sehingga lebih mudah diakses, diolah, dan ditelusuri.

2. Berapa indeks elemen pertama pada list Python?

Jawab: Indeks 0.

3. Apa arti indeks -1?

Jawab: Indeks -1 digunakan untuk mengakses elemen terakhir dalam list.

4. Apa hasil "[10, 20, 30, 40][1:3]"?

Jawab: "[20, 30]", karena slicing mengambil elemen dari indeks 1 sampai sebelum indeks 3.

5. Apa perbedaan "append" dan "insert"?

Jawab: "append()" menambahkan elemen di akhir list, sedangkan "insert()" menambahkan elemen pada posisi indeks yang ditentukan.

6. Apa risiko mengakses indeks yang tidak ada?

Jawab: Program dapat menghasilkan "IndexError" karena indeks tersebut berada di luar jangkauan list.

7. Fungsi apa yang digunakan untuk menghitung banyak elemen list?

Jawab: Fungsi "len()".

8. Bagaimana menghitung rata-rata list numerik dengan "sum" dan "len"?

Jawab: Dengan membagi jumlah seluruh elemen menggunakan "sum(data)" dengan banyak elemen menggunakan "len(data)".

Contoh:

nilai = [60, 70, 80]
rata_rata = sum(nilai) / len(nilai)
print(rata_rata)

Hasil: "70.0"

9. Mengapa list kosong perlu diperiksa sebelum pembagian?

Jawab: Karena "len(data)" bernilai 0 jika list kosong, sehingga pembagian dengan 0 akan menyebabkan "ZeroDivisionError".

10. Apa perintah yang digunakan untuk mengirim commit lokal ke GitHub?

Jawab: "git push".