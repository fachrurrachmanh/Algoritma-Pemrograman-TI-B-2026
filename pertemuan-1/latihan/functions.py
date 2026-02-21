#fungsi menggunakan kata kunci def lalu diikuti dengan nama fungsi
def fungsi_tambah(a, b):
    tambah = a+b
    return tambah

hasil = fungsi_tambah(5, 7)
print(hasil)

#default parameter 
def sapaan (nama= "hakim"):
    print(f"halo {nama}")

sapaan("agus")
sapaan("budi")
sapaan()

#posisional argumen
def my_function(kampus, jurusan):
  print("saya berkuliah di ", kampus)
  print("jurusan saya di", kampus + "adalah", jurusan)

my_function("unri", "teknik elektro")
'''unri akan di passing ke parameter kampus 
dan teknik elektro di passing ke parameter jurusan''' 

#keyword argumen
def my_function(kampus, jurusan):
   print("saya berkuliah di ", kampus)
   print("jurusan saya di", kampus + "adalah", jurusan)

my_function(kampus="unri", jurusan="teknik elektro")
my_function(jurusan="teknik elektro", kampus="unri")

#mixing positional dan keyword argumen
#posisional argumen harus berada diawal terlebih dahulu
def my_function(nama, jk, usia):
   print("halo nama saya ", nama +", saya seorang ", jk +" berusia ", usia)

my_function("hakim", "pria", usia = 18)

#Arbitrary Arguments - *args (parameter yang menampung beberapa argumen)
def my_function(*konco):
  for teman in konco:
     print(teman)
  print("teman yang paling muda adalah " + konco[2])

my_function("faris", "eng", "faras")

#Arbitrary Arguments - *args dengan argumen biasa