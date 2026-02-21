#string bisa ditulis dengan "" dan ''
nama = "hakim" #hakim adalah string yang disimpan ke variabel nama

#multiline string (diapit dengan tiga quotation)
buah = """
apel,
mangga,
semangka,
anggur
"""
print(buah)

#slicing string [start:end]
sapa = "hello, world"
print(sapa [:5])#print dari awal hingga indeks ke 5

#modify string (membuat string baru dari sebuah string yang diubah)
nama = "faris"
print(nama.replace("f", "p"))
#return = paris merupakan string baru

#string combine
a = "oke"
b = "class"
print(a+" "+b)

#f-string
usia = 18
text = f"dia berusia {usia} tahun"
print(text)
#atau
print(f'dia berusia {usia} tahun')
print(f'dia berusia {usia*10} tahun')

#escape character
'''
\"  Double quote
\'	Single Quote	
\\	Backslash	
\n	New Line	
\r	Carriage Return	
\t	Tab	
\b	Backspace
'''

#string method (mengembalikan string baru, dan tidak mengubah string original)
name ="hakim"
print(name.capitalize())
print(name.isalpha())
#dll