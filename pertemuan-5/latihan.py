A = [[5, 3, 1],  
    [2, 8, 4],  
    [6, 0, 7]]
  
B = [[1, 2, 3],  
    [4, 5, 6],  
    [7, 8, 9]]  

# a. Menjumlahkan matriks A dan B, simpan hasilnya dalam variabel C_tambah          
baris, kolom = len(A), len(A[0]) 
C_tambah = [[A[i][j] + B[i][j] for j in range(kolom)] for i in range(baris)]

# b. Mengurangkan matriks A dikurangi B, simpan dalam variabel C_kurang
baris, kolom = len(A), len(A[0]) 
C_kurang= [[A[i][j] - B[i][j] for j in range(kolom)] for i in range(baris)] 

# c. Mengalikan setiap elemen matriks A dengan skalar k = 4 , simpan dalam C_skalar
baris_A, kolom_A = len(A), len(A[0]) 
baris_B, kolom_B = len(B), len(B[0]) 

C_skalar = [[0]*kolom_B for _ in range(baris_A)] 
for i in range(baris_A): 
    for j in range(kolom_B): 
        for k in range(kolom_A): 
            C_skalar[i][j] += A[i][k] * B[k][j]


# d. Menampilkan ketiga hasil dengan format rapi baris per baris 
print("hasil tambah ialah:")
for x in C_tambah:
    print(x)
print()

print("hasil kurang ialah:")
for x in C_kurang:
    print(x)
print()

print("hasil kali ialah:")
for x in C_skalar:
    print(x)
