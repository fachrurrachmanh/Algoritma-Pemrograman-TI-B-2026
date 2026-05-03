DAFTAR_ANGKA = [23, 67, 4, 89, 15, 42, 73, 31, 58, 9]

# BAGIAN A 

#fungsi untuk tebakan user
def tebak_angka(angka_rahasia,maks_percobaan):
    percobaan = 0
    
    while percobaan < maks_percobaan:
        tebakan = int(input("masukkan tebakan anda: "))
        if tebakan < angka_rahasia:
            print("terlalu kecil")
        elif tebakan > angka_rahasia:
            print("terlalu besar")
        else:
            print("benar!")
            sisa_percobaan=maks_percobaan-percobaan-1
            return True, sisa_percobaan
        
        percobaan += 1
    return False, 0

#fungsi menghtiung skor game       
def hitung_skor(berhasil, sisa_percobaan):
        if berhasil:
             return sisa_percobaan*10
        else:
             return 0
        
#funsi untuk menjalankan satu ronde game
def main_satu_ronde(nama, nomor_ronde):
    angka_rahasia = DAFTAR_ANGKA[nomor_ronde % len(DAFTAR_ANGKA)]
    maks_percobaan=7

    berhasil, sisa_percobaan = tebak_angka(angka_rahasia, maks_percobaan)
    skor = hitung_skor(berhasil,sisa_percobaan)

    return [nama, skor]

#Bagian B 
def tampilkan_riwayat(riwayat):
    if len(riwayat)==0:
        print("belum ada riwayat")
    print("--riwayat permainan--")
    print("No  |  Nama  |  Skor")
    print("====================")

    for i in range (len(riwayat)):
        print(f'{i+1}  | {riwayat[i][0]} | {riwayat [i][1]}')

#Bagian C 
def selection_sort_riwayat(riwayat):
    data = riwayat.copy()  
    n = len(data)

    for i in range(n):
        max_idx = i
        for j in range(i + 1, n):
            if data[j]["skor"] > data[max_idx]["skor"]:
                max_idx = j

        data[i], data[max_idx] = data[max_idx], data[i]
        
    return data

def tampilkan_leaderboard(riwayat):
    if len(riwayat) == 0:
        print("Belum ada data")
        return
    urutan = selection_sort_riwayat(riwayat)
    print()
    print("===leaderboard===")
    for i in range(len(urutan)):
        nama = urutan[i][0]
        skor =  urutan[i][1]

        if i == 0:
            print(f"{i+1}. {nama} - {skor}*")
        else:
            print(f"{i+1}. {nama} - {skor}")

#Program Utama
riwayat=[]
nomor_ronde=0 

nama=input("masukkan nama pemain: ")

while True:
    print(f"main ronde {nomor_ronde+1}")
    hasil = main_satu_ronde(nama, nomor_ronde)
    riwayat.append(hasil)
    nomor_ronde += 1

    lanjut=input("main lagi? (y/n): ").lower()
    
        
    if lanjut == 'n':
        break

tampilkan_riwayat(riwayat)
tampilkan_leaderboard(riwayat)


        