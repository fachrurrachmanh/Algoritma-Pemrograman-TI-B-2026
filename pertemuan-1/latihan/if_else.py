usia = 10

if usia >= 18:
    print("kamu sudah cukup umur")
elif usia <= 0:
    print("kamu belum lahir") 
else:
    print("kamu belum cukup umur")

#conditional operator
#sama dengan ternary operator
x = 5
y = 7

print("x is greater than y" if x > y else "y is greater than x") #menentukan kondisi tanpa menyimpan ke sebuah variabel

result = "x" if x < y else "y" #menentukan kondisi dan menyimpannya ke sebuah variabel
print(f"the min number is {result}")

#nested if
skor = 85
absen = 2
tugas = "mengumpulkan"

if absen <= 3:
  if skor >= 70:
    if tugas == "mengumpulkan":
      print("Lulus dengan nilai sempurna")
    else:
      print("Lulus tapi tugas tidak lengkap")
  else:
    print("Lulus dengan nilai rendah")
else:
  print("Tidak lulus karena tidak bisa mengikuti ujian")

#if statement tidak bisa kosong, maka jika ada sebuah if tanpa statement, gunakan pass statement
a = 33
b = 33

if b > a:
  pass

print(a)
