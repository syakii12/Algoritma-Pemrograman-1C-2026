total_belanja = int(input("Masukkan total belanja: Rp"))

if total_belanja % 100000 == 0:
    bayar = 0
elif total_belanja % 50000 == 0:
    bayar = total_belanja * 50 / 100
elif total_belanja % 10000 == 0:
    bayar = total_belanja * 80 / 100
elif total_belanja >= 200000:
    bayar = total_belanja * 90 / 100
else:
    bayar = total_belanja

print("Total belanja awal : Rp", total_belanja)
print("Total yang dibayar : Rp", bayar)

poin = "Poin Bertambah" if bayar > 0 else "Tidak Ada Poin"
print("Status poin        :", poin)
