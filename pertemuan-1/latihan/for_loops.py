#for loops akan mencetak dengan akhiran newline, jika akhiran ingin diubah maka gunakan end=""
#for number in numbers artinya untuk setiap number di numbers
for x in range(1, 6): #mencetak halo sebanyak 5 kali
    print("halo")
print()

for x in range(5): #mencetak halo sebanyak 5 kali
    print("halo")

angka = "1367501-"
for x in angka: #untuk setiap x di angka, artinya jika dicetak maka akan tercetak x sebagai 1, x sebagai 3, dst
    print(x, end="")

for x in reversed(angka):
    print(x)