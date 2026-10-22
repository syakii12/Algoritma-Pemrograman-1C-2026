jumlah_a = 0
jumlah_b = 0
jumlah_c = 0
jumlah_d = 0
jumlah_e = 0

total_nilai = 0
nilai_tertinggi = -1
nilai_terendah = 101
nama_tertinggi = ""
nama_terendah = ""

print("=== Input Nilai Mahasiswa ===")

for i in range(1, 11):
    print("")
    print("Mahasiswa ke-" + str(i))
    nama = input("Nama        : ")
    tugas = float(input("Nilai tugas : "))
    uts = float(input("Nilai UTS   : "))
    uas = float(input("Nilai UAS   : "))

    # nilai akhir: tugas 30%, UTS 30%, UAS 40%
    nilai_akhir = tugas * 0.3 + uts * 0.3 + uas * 0.4

    # tentukan kategori nilai
    if nilai_akhir >= 85:
        kategori = "A"
        jumlah_a += 1
    elif nilai_akhir >= 75:
        kategori = "B"
        jumlah_b += 1
    elif nilai_akhir >= 65:
        kategori = "C"
        jumlah_c += 1
    elif nilai_akhir >= 50:
        kategori = "D"
        jumlah_d += 1
    else:
        kategori = "E"
        jumlah_e += 1

    # tampilkan hasil mahasiswa ini
    print("--- Hasil ---")
    print("Nama        :", nama)
    print("Nilai tugas :", tugas)
    print("Nilai UTS   :", uts)
    print("Nilai UAS   :", uas)
    print("Nilai akhir :", round(nilai_akhir, 2))
    print("Kategori    :", kategori)

    # perbarui statistik
    total_nilai += nilai_akhir

    if nilai_akhir > nilai_tertinggi:
        nilai_tertinggi = nilai_akhir
        nama_tertinggi = nama

    if nilai_akhir < nilai_terendah:
        nilai_terendah = nilai_akhir
        nama_terendah = nama

# rekap setelah semua data diproses
print("")
print("=== Rekap Kelas ===")
print("Jumlah mahasiswa nilai A :", jumlah_a)
print("Jumlah mahasiswa nilai B :", jumlah_b)
print("Jumlah mahasiswa nilai C :", jumlah_c)
print("Jumlah mahasiswa nilai D :", jumlah_d)
print("Jumlah mahasiswa nilai E :", jumlah_e)
print("Nilai akhir tertinggi    :", round(nilai_tertinggi, 2), "(" + nama_tertinggi + ")")
print("Nilai akhir terendah     :", round(nilai_terendah, 2), "(" + nama_terendah + ")")
print("Rata-rata nilai akhir    :", round(total_nilai / 10, 2))