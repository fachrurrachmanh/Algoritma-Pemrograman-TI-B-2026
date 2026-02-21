try:
    # Input data
    nama_barang = input("Masukkan nama barang: ")
    harga = float(input("Masukkan harga barang: "))
    jumlah = int(input("Masukkan jumlah barang: "))

    # Validasi jumlah
    if jumlah <= 0:
        raise ValueError("Jumlah barang harus lebih dari 0")

    # Hitung total
    total = harga * jumlah

except ValueError:
    print("Terjadi kesalahan")

else:
    print("\n=== STRUK BELANJA ===")
    print("Barang :", nama_barang)
    print("Total  : Rp", total)

finally:
    print("\nTerima kasih telah berbelanja.")