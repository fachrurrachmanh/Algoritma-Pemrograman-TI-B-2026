film = [["Danur", 50000 ], 
        ["Inside Out 2", 45000 ],
        ["upin ipin", 30000],
        ["ejen ali", 40000],
        ["cocomelon", 25000]]

number = 1
for x in film:
    print(f"{number}.{x[0]}; harga tiket {x[1]}")
    number+=1

pilihan=int(input("masukkan nomor film: "))

while True:
    if pilihan < 0 or pilihan > 5:
        print("pilihan anda tidak valid")
        pilihan=int(input("masukkan nomor film: "))
    else:
        print(f"anda memilih: {film[pilihan-1]}")
        break



