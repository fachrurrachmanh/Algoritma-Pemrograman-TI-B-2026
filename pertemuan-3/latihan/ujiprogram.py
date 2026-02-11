import myOOP
#A. INHERITANCE (Pewarisan)
print(myOOP.ProdukElektronik("tv",3000000,"2 tahun").info_produk())
print(myOOP.ProdukMakanan("roti",15000,"12-12-2026").info_produk())
print()

#B. POLYMORPHISM
print(myOOP.NotifikasiEmail("Anda memiliki email baru.").kirim())
print(myOOP.NotifikasiSMS("Anda memiliki SMS baru.").kirim())
print()

#C. Encapsulation
m1 = myOOP.Mahasiswa("hakim", 90)
print(m1.get_nilai())

m1.set_nilai(-1)
print(m1.get_nilai()) 
