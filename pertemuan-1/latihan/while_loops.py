usn = input("masukkan nama username anda: ")
usn_confirm = input("konfirmasi username anda: ")

while not usn == usn_confirm:
    print("username yang anda konfirmasi tidak sesuai")
    usn_confirm = input("konfirmasi username anda: ")

print("selamat datang")
