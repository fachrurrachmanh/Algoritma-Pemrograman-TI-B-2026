#match syntax
'''
match expression:
  case x:
    code block
  case y:
    code block
  case z:
    code block
'''

hari = 4
match hari:
  case 6:
    print("hari ini libur")
  case 7:
    print("hari ini libur")
  case _: #default case, harus diletak diakhir
    print("hari ini masuk")

#combine case
hari = 4
match hari:
  case 1 | 2 | 3 | 4 | 5:
    print("hari ini hari kerja")
  case 6 | 7:
    print("hari ini hari libur")
  case _:
    print("No match")

#case dengan if
bulan = 5
hari = 4
match hari:
  case 1 | 2 | 3 | 4 | 5 if bulan == 1:
    print("hari kerja di januari")
  case 1 | 2 | 3 | 4 | 5 if bulan == 2:
    print("hari kerja di februari")
  case 1 | 2 | 3 | 4 | 5 if bulan == 3:
    print("hari kerja di maret")
  case 1 | 2 | 3 | 4 | 5 if bulan == 4:
    print("hari kerja di april")
  case 1 | 2 | 3 | 4 | 5 if bulan == 5:
    print("hari kerja di Mei")
  case 1 | 2 | 3 | 4 | 5 if bulan == 6:
    print("hari kerja di juni")
  case 1 | 2 | 3 | 4 | 5 if bulan == 7:
    print("hari kerja di juli")
  case 1 | 2 | 3 | 4 | 5 if bulan == 8:
    print("hari kerja di agustus")
  case 1 | 2 | 3 | 4 | 5 if bulan == 9:
    print("hari kerja di september")
  case 1 | 2 | 3 | 4 | 5 if bulan == 10:
    print("hari kerja di oktober")
  case 1 | 2 | 3 | 4 | 5 if bulan == 11:
    print("hari kerja di november")
  case 1 | 2 | 3 | 4 | 5 if bulan == 12:
    print("hari kerja di desember")
  case _:
    print("No match")



