def bilangan_prima(n):
    hasil = []

    for i in range(2, n + 1):
        jumlah_pembagi = 0

        for j in range(1, i + 1):
            if i % j == 0:
                jumlah_pembagi += 1

        if jumlah_pembagi == 2:
            hasil.append(i)

    return hasil

print(f"bilangan prima hingga n = 50 ialah {bilangan_prima(50)}")
