
while True:
    n = int(input("Masukkan tinggi setengah menara n (2-15): "))
    if n >= 2 and n <= 15:
        break
    print("n harus 2 sampai 15, ulangi")

print("")

for i in range(1, n + 1):
    for s in range(n - i):
        print("  ", end="")
    for k in range(1, i + 1):
        print(k % 10, end=" ")
    for k in range(i - 1, 0, -1):
        print(k % 10, end=" ")
    print()
for i in range(n - 1, 0, -1):
    for s in range(n - i):
        print("  ", end="")
    for k in range(1, i + 1):
        print(k % 10, end=" ")
    for k in range(i - 1, 0, -1):
        print(k % 10, end=" ")
    print()