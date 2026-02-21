#typecasting adalah mengubah tipe data dari sebuah variabel
gpa = 3.5 #float gpa
print(gpa)
print(type(gpa)) #untuk mengetahui tipe data dari variabel
gpa = int(gpa) #mengubah float gpa menjadi int gpa
print(gpa)
print(type(gpa)) #mengetahui tipe data yang telah diubah sebelumnya

nama = "hakim" #string
print(type(nama))
nama = bool (nama) #string nama diubah ke bool nama
print(type(nama))
print(nama) #menghasilkan nilai True karena string nama memiliki panjang lebih atau sama dengan 1
#jika string nama memilki panjang 0 maka bool nama menghasilkan False