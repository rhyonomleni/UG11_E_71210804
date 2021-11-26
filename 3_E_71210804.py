#fungsi 1
def hitungKata():
    kalimat = input ("Masukkan sebuah kalimat/kata : ")
    a = input ("Masukkan kata yang ingin dihitung : ")
    b = kalimat.count("{}".format(a))
    print ("Terdapat sebanyak {0} kata {1} di dalam string".format(b,a))
#fungsi 2
def cekkata():
    kalimat = input ("Masukkan sebuah kalimat/kata : ")
    kata = input ("Masukkan kata yang ingin di cek : ")
    if kata in kalimat:
        print ("Kata {0} terdapat di dalam string".format(kata))
        print ("String diubah menjadi : ")
        a = kalimat.replace(kata, kata.upper(),2)
        print (a)
    else :
        print ("Kata {0} tidak terdapat di dalam string".format(kata))
        print ("String diubah menjadi : ")
        print (kalimat, kata)
#fungsi 3
def ubahKata():
    kalimat = input ("Masukkan sebuah kalimat/kata : ")
    kata = input ("Masukkan kata yang ingin di ubah : ")
    ganti = input ("Masukkan kata pengganti : ")
    print ("Anda akan mengubah kata {0} menjadi {1} sebanyak 1x".format(kata, ganti))
    ubah = input("Apakah anda ingin mengubah jumlah total penggantian kata ? (yes/no) : ")
    if ubah == "yes":
        total = int(input ("Masukkan jumlah total penggantian : "))
        print ("String berhasil diubah menjadi : ")
        a = kalimat.replace(kata, ganti, total)
        print (a)
    else:
        print ("String berhasil diubah menjadi : ")
        b = kalimat.replace(kata, ganti, 1)
        print (b)
print("=======Program Manipulasi String=======")
print ("Pilihan Menu")
print ("1. Hitung kata")
print ("2. cek kata")
print ("3. ubah kata")
pilihan = int(input ("Pilihan anda : "))
if pilihan == 1:
    hitungKata()
elif pilihan ==2:
    cekkata()
else :
    ubahKata()