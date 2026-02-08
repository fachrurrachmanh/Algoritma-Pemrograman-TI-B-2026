def rata_rata(nilai):
    total = sum(nilai)
    if total == False:
        print("data kosong")
    else:
        rata = total/len(nilai)
        return rata
    
list = [80, 75, 90, 60, 85]
print(rata_rata(list))
