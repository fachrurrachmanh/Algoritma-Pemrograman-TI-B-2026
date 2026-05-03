film = [["Danur", 50000 ], 
        ["Inside Out 2", 45000 ],
        ["upin ipin", 30000],
        ["ejen ali", 40000],
        ["cocomelon", 25000]]

number = 1
for x in film:
    print(f"{number}.{x[0]}; harga tiket {x[1]}")
    number+=1

print("tekan 0 untuk keluar")
list_pilihan=[]
pilihan=int(input("masukkan nomor film: "))

while not pilihan == 0:
    if pilihan < 0 or pilihan > 5:
        print("pilihan anda tidak valid")
        pilihan=int(input("masukkan nomor film: "))
    else:
        print(f"anda memilih: {film[pilihan-1]}")
        list_pilihan.append(film[pilihan-1])
        while True:
            pilih_lagi=input("pilih lagi? (Y/N): ").lower()
            if pilih_lagi == "y":
                pilihan=int(input("masukkan nomor film: "))
                print(f"anda memilih: {film[pilihan-1]}")
                list_pilihan.append(film[pilihan-1])
            else:
                break
        print(f"anda memilih:")
        for x in list_pilihan:
            print(x)
        break

print(list_pilihan)
harga=[]
indeks=0
for x in list_pilihan:
    harga.append(list_pilihan[indeks][1])
    indeks += 1

total=sum(harga)

print(f"total harga tiket kamu: {total}")

    





