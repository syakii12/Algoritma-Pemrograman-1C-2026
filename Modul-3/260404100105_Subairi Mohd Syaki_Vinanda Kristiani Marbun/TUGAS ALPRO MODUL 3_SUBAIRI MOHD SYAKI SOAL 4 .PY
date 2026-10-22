beasiswa_penuh = 0

print("=== Seleksi Awal Penerima Beasiswa ===")

for i in range(1, 11):
    print("")
    print("Mahasiswa ke-" + str(i))
    nama = input("Nama                  : ")
    ipk = float(input("IPK                   : "))
    penghasilan = int(input("Penghasilan orang tua : Rp"))
    if ipk < 3.00:
        print("Hasil:", nama, "tidak memenuhi syarat (IPK kurang dari 3,00)")
        continue
    if penghasilan <= 3000000:
        beasiswa_penuh += 1
        print("Hasil:", nama, "mendapatkan beasiswa PENUH")
    elif penghasilan <= 5000000:
        print("Hasil:", nama, "mendapatkan beasiswa SEBAGIAN")
    else:
        print("Hasil:", nama, "tidak mendapatkan beasiswa")
    if beasiswa_penuh == 3:
        print("")
        print("Kuota beasiswa penuh (3 mahasiswa) sudah terpenuhi")
        print("Proses seleksi dihentikan")
        break

print("")
print("Jumlah penerima beasiswa penuh:", beasiswa_penuh)