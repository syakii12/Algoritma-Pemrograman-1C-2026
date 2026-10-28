n = int(input("Masukkan jumlah baris: "))

if n > 0:
    for i in range(1, n ):

        for j in range(1, i + 1):
            print(j, end=" ")

        for k in range(n - i):
            print("    ", end="")

        for j in range(i, 0, -1):
            print(j, end=" ")

        print()
else:
    print("Masukkan bilangan positif")
