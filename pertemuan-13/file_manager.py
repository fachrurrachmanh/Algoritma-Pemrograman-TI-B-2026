import os

while True:
    print("\n============================")
    print("     python file manager   ")
    print("============================")
    print("[1] Read file")
    print("[2] Write file")
    print("[3] Delete file")
    print("[0] Exit")

    try:
        pilihan = int(input("Masukkan pilihan: "))
    except ValueError:
        print("Input harus berupa angka!")
        continue

    if pilihan == 1:
        file = [f for f in os.listdir() if f.endswith(".txt")]

        if not file:
            print("belum ada file")
            continue

        print()
        print("daftar file:")
        for i in range(len(file)):
            print(f"{i+1}. {file[i]}")

        nomor = input("pilih nomor file: ").strip()

        if not nomor.isdigit():
            print("harus angka")
            continue

        nomor = int(nomor)

        if nomor < 1 or nomor > len(file):
            print("nomor tidak valid")
            continue

        nama_file = file[nomor - 1]

        try:
            with open(nama_file, "r") as f:
                print()
                print("isi file:")
                print(f.read())
        except:
            print("gagal membaca file.")

    elif pilihan == 2:
        nama_file = input("masukkan nama file anda: ").strip()

        if nama_file == "":
            print("nama file tidak boleh kosong!")
            continue

        if not nama_file.endswith(".txt"):
            nama_file += ".txt"

        isi = input("masukkan isi file:\n")

        try:
            with open(nama_file, "w") as f:
                f.write(isi)
            print("file berhasil disimpan.")
        except:
            print("gagal menyimpan file.")

    elif pilihan == 3:
        file = [f for f in os.listdir() if f.endswith(".txt")]

        if not file:
            print("tidak ada file")
            continue
        
        print()
        print("daftar file:")
        for i in range(len(file)):
            print(f"{i+1}. {file[i]}")

        nomor = input("pilih nomor file yang ingin dihapus: ").strip()

        if not nomor.isdigit():
            print("harus angka")
            continue

        nomor = int(nomor)

        if nomor < 1 or nomor > len(file):
            print("nomor tidak valid")
            continue

        nama_file = file[nomor - 1]

        konfirmasi = input(f"yakin hapus {nama_file}? (y/n): ").lower()

        if konfirmasi == "y":
            try:
                os.remove(nama_file)
                print("file berhasil dihapus")
            except:
                print("gagal menghapus file")
        else:
            print("dibatalkan")

    elif pilihan == 0:
        break

    else:
        print("pilihan tidak tersedia")
