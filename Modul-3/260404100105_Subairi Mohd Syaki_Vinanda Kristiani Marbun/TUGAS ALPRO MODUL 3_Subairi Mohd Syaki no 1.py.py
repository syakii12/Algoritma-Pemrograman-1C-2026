jumlah_penumpang = 0
total_pendapatan = 0
total_jarak = 0
jarak_terjauh = 0

print("=== Kasir Terminal Bus Sidoarjo ===")
print("Masukkan jarak penumpang (km), ketik 0 untuk selesai")

while True:
    jarak = float(input("Jarak penumpang (km): "))

    # break: hentikan perulangan jika kasir memasukkan 0
    if jarak == 0:
        break

    if jarak < 0:
        print("Jarak negatif tidak valid, ulangi")
        continue

    jumlah_penumpang += 1

    if jarak <= 5:
        tarif = 3000
    elif jarak <= 15:
        tarif = 3000 + 1000 * (jarak - 5)
    else:
        tarif = 13000 + 500 * (jarak - 15)

    if jumlah_penumpang % 5 == 0:
        tarif = tarif * 0.5
        print("Penumpang ke-" + str(jumlah_penumpang) + " mendapat diskon 50%")

    print("Tarif penumpang ke-" + str(jumlah_penumpang) + ": Rp" + str(round(tarif)))

    total_pendapatan += tarif
    total_jarak += jarak

    if jarak > jarak_terjauh:
        jarak_terjauh = jarak

print("")
print("=== Rekap ===")
print("Jumlah penumpang :", jumlah_penumpang)
print("Total pendapatan : Rp" + str(round(total_pendapatan)))

if jumlah_penumpang > 0:
    print("Jarak terjauh    :", jarak_terjauh, "km")
    print("Rata-rata jarak  :", round(total_jarak / jumlah_penumpang, 2), "km")
else:
    print("Belum ada penumpang yang dihitung")