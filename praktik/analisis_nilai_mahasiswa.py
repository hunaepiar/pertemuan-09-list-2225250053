def rata_rata(data):
    if len(data) == 0:
        return 0
    return sum(data) / len(data)


def nilai_lulus(data, batas=60):
    lulus = []

    for x in data:
        if x >= batas:
            lulus.append(x)

    return lulus


nilai = [78, 55, 90, 67, 60, 82, 45, 71, 88, 59]

lulus = nilai_lulus(nilai)
belum_lulus = len(nilai) - len(lulus)

print("Data nilai:", nilai)
print("Banyak data:", len(nilai))
print("Total nilai:", sum(nilai))
print(f"Rata-rata: {rata_rata(nilai):.2f}")
print("Nilai minimum:", min(nilai))
print("Nilai maksimum:", max(nilai))
print("Nilai lulus:", lulus)
print("Jumlah lulus:", len(lulus))
print("Jumlah belum lulus:", belum_lulus)