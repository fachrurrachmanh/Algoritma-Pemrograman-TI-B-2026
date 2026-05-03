import soal2
import soal3

rekap = []
hari = input("masukkan hari: ")

for x in range(1, hari+1):
    baris_baru=[]
    for y in range(1, x):
        film = input(f"masukkan jumlah film di hari {x}")
        baris_baru.append(y)