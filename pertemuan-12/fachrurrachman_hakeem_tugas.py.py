struktur = {
    "Skripsi_Aqil": {
        "Bab_1": {
            "pendahuluan.docx": 45,
            "latar_belakang.docx": 62
        },
        "Bab_2": {
            "landasan_teori.docx": 118,
            "referensi": {
                "paper_A.pdf": 340,
                "paper_B.pdf": 210
            }
        },
        "Bab_3": {
            "metodologi.docx": 89,
            "diagram": {
                "flowchart.png": 512,
                "erd.png": 278,
                "arsitektur": {
                    "sistem.png": 430
                }
            }
        },
        "sidang": {
            "presentasi.pptx": 2048,
            "catatan_revisi.txt": 15
        },
        "README.txt": 8
    }
}

#tugas A
def total_ukuran(folder):
    total = 0
    for isi in folder.values():
        if isinstance(isi, dict): 
            total+= total_ukuran(isi)
        else: 
            total+= isi
    return total


#tugas B
def hitung_file(folder):
    jumlah=0
    for isi in folder.values():
        if isinstance(isi, dict):
            jumlah+= hitung_file(isi)
        else:
            jumlah+= 1
    return jumlah


#tugas C
def cari_terbesar(folder):
    nama_terbesar=""
    ukuran_terbesar=0
    for nama, isi in folder.items():
        if isinstance(isi,dict):
            nama2, ukuran2=cari_terbesar(isi)

            if ukuran2 >ukuran_terbesar:
                nama_terbesar= nama2
                ukuran_terbesar=ukuran2
        else:
            if isi > ukuran_terbesar:
                nama_terbesar=nama
                ukuran_terbesar=isi
    return nama_terbesar, ukuran_terbesar


#tugas D
def tampilkan_tree(folder,level=0):
    for nama, isi in folder.items():
        if isinstance(isi, dict):
            print("  " * level + "📁 " + nama)
        else:
            print("  " * level + f"📃 {nama} ({isi} KB)")
        if isinstance(isi, dict):
            tampilkan_tree(isi, level + 1)


#output
print("=== LAPORAN SKRIPSI ===")
print()

print("total ukuran:", total_ukuran(struktur), "KB")
print("jumlah file:", hitung_file(struktur))
nama, ukuran = cari_terbesar(struktur)
print("file terbesar:",nama, f"({ukuran} KB)")
print()

print("folder: ")
tampilkan_tree(struktur)