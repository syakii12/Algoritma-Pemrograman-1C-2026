baris = int(input("Jumlah baris Lampu: "))
Lampu = int(input("Jumlah lampu per baris: "))

for i in range(1,baris + 1):
    print("Baris ke-", i)

    for j in range(1, Lampu + 1):
        if j % 3 == 0:
            print("Lampu mengalami gangguan")
        else:
            print("Lampu berfungsi normal")

print("Periksa sumber listrik utama taman")
