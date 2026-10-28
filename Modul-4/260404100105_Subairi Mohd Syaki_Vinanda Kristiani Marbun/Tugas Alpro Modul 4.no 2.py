total = 0

for h in range(1, 8):
    print("Hari ke-", h)
    gaji = 100000

    while True:
        lembur = int(input("Masukkan jam lembur: "))

        if lembur < 0 or lembur in [5, 7]:
            print("Jam lembur tidak sesuai ketentuan!")
        else:
            break

    if lembur == 1:
        gaji += 25000
    elif lembur == 2:
        gaji += 50000
    elif lembur == 3:
        gaji += 75000
    elif lembur == 4:
        gaji += 100000
    elif lembur == 6:
        gaji += 200000
    elif lembur == 8:
        gaji += 300000
    elif lembur > 8:
        print("Jam lembur melebihi batas")

    shift = input("Bekerja shift malam? (ya/tidak): ")

    if shift == "ya":
        gaji += 50000

    total += gaji
    print("Gaji harian: Rp", gaji)

print("Total gaji mingguan: Rp", total)