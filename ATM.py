print("==============================================")
print(           "Selamat Datang di ATM BRI          ")
print("==============================================")
print(                  "Pilih Option :              ")
print("==============================================")
print(                  "1. Cek Uang                 ")
print(                  "2. Ambil Uang               ")
print(                  "3. Tabung Uang              ")
print("==============================================")
option=int(input("Silahkan Pilih Option :"))
if option==1:
    print("Uang kamu berjumlah Rp. 200.000")
elif option==2:
    print("Uang kamu berjumlah Rp. 200.000, mau ambil berapa?")
    print("1. 100.000")
    print("2. 200.000")
    uang_kamu=200000
    option2=int(input("Pilih Option :"))
    if option2==1:
        hasil=uang_kamu-200000
        print("Uang kamu sekarang berjumlah Rp. :", hasil)
    elif option2==2:
        hasil2=uang_kamu-200000
        print("Uang kamu sekarang berjumlah Rp. :", hasil2)
    else:
        print("Keyword anda salah!")
elif option==3:
    uang_kamu==200000
    print("Uang berjumlah Rp. 200.000, mau nabung berapa?")
    option3=int(input("Masukkan jumlah uang :"))
    hasil3=uang_kamu+option3
    print("Jumlah uang kamu sekarang adalah Rp. :", hasil3)
else:
    print("Keyword anda salah, silahkan masukkan lagi :")
