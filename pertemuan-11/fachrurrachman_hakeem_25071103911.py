data = [59, 40, 36, 40, 30, 26, 97, 8, 23, 31, 2, 40, 99, 70, 64, 36, 43, 20, 1, 9]

def linear_search(data, target):
    for i in range(len(data)):
        if data[i] == target:
            return i      
    return -1             

def binary_search(data, target):
    sorted_data =sorted(data)  
    kiri, kanan=0, len(sorted_data) - 1
 
    while kiri <= kanan:
        tengah = (kiri + kanan)// 2
        if sorted_data[tengah] == target:
            return tengah                 
        elif sorted_data[tengah] < target:
            kiri= tengah + 1
        else:
            kanan =tengah - 1
    return -1                          
 
print("DATA ARRAY")
print(data)
print(f"jumlah data: {len(data)}")
print(f"jumlah indeks: {len(data)-1}")

while True:
    try:
        target= int(input("masukkan nilai yang dicari: "))
        break
    except ValueError:
        print("input harus berupa bilangan bulat!")
        continue

print()
print("HASIL PENCARIAN")

#untuk linear search
indeks_linear = linear_search(data, target)
print()
print(f"[linear search (data asli)]")
if indeks_linear!=-1:
    print(f"nilai {target} ketemu di index: {indeks_linear}")
else:
    print(f"nilai {target} tidak ketemu, return: -1")
print()

#untuk binary search
indeks_binary = binary_search(data, target)
sorted_data = sorted(data)
print("[binary Search (data terurut)]")
print(f"data terurut: {sorted_data}")
if indeks_binary!=-1:
    print(f"nilai {target} ketemu di index: {indeks_binary}")
else:
    print(f"nilai {target} tidak ketemu, return: -1")

print()
