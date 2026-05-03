import soal2
total=int(input("masukkan total pembelian anda: "))
bayar=int(input("masukkan jumlah yang kamu bayar: "))

if total == soal2.total:
    while True:
        if bayar < total:
            print("uang bayar kamu kurang")
            bayar=input("masukkan jumlah yang kamu bayar: ")
        else:
            kembalian = bayar - total
            if kembalian == 0:
                print("uang pas, ngga ada kembalian")
            else:
                print(f"kembalian anda: {kembalian}")
            break
else:
    print("total yang anda masukkan tidak valid")

print(f"total pembelian anda: {total}")
print(f"jumlah yang anda bayar: {bayar}")
print(f"total kembalian anda: {kembalian}")



