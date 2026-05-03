def inputan():
    while True:
        n = input("Masukkan jumlah elemen: ")
        if n.isdigit():  # cek apakah angka
            n = int(n)
            break
        else:
            print("Input harus berupa angka non-negatif!")

    data = []
    for i in range(n):
        while True:
            x = input(f"Elemen ke-{i+1}: ")
            if x.isdigit():  # cek angka non-negatif
                data.append(int(x))
                break
            else:
                print("Input harus berupa angka non-negatif!")

    return data

def radix_sort(arr):
    mylist = arr.copy()
    maxVal = max(mylist) if mylist else 0
    exp = 1

    while maxVal // exp > 0:
        radixArray = [[], [], [], [], [], [], [], [], [], []]

        # Masukkan ke bucket
        while len(mylist) > 0:
            val = mylist.pop()
            index = (val // exp) % 10
            radixArray[index].append(val)

        # Ambil lagi dari bucket
        for bucket in radixArray:
            while len(bucket) > 0:
                mylist.append(bucket.pop())

        exp *= 10

    return mylist

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    kiri = merge_sort(arr[:mid])
    kanan = merge_sort(arr[mid:])

    hasil = []
    i = j = 0

    while i < len(kiri) and j < len(kanan):
        if kiri[i] < kanan[j]:
            hasil.append(kiri[i])
            i += 1
        else:
            hasil.append(kanan[j])
            j += 1

    hasil.extend(kiri[i:])
    hasil.extend(kanan[j:])

    return hasil

data = inputan()

print("\nData awal:", data)

print("\nRADIX SORT: ", end="")
print(radix_sort(data.copy()))

print("\nMERGE SORT: ",end="")
print(merge_sort(data.copy()))

