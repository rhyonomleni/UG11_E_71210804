import random
def generate(level):
    operasi = ['+','-','/','*']
    r = random.choice(operasi)
    if level == 1:
        a = random.randint(20,50)
        b = random.randint(20,50)
        r = random.choice(operasi)
        #hasil
        hasil = eval(str(a) + r + str(b))
        print("Berapakah hasil dari {0}{1}{2}".format(a,r,b))
        #jawaban
        jawab = int(input ("Masukkan Jawaban Anda : "))
        if jawab == hasil:
            return print("Jawaban Anda Benar !")
        else:
            print("Jawaban Anda Masih Salah !")
            print("Hasil dari",a,r,b, "=", hasil )
    elif level == 2:
        a = random.randint(20,70)
        b = random.randint(20,70)
        c = random.randint(20,70)
        r = random.choice(operasi)
        var2 = random.choice(operasi)
        #hasil
        hasil = eval(str(a) + r + str(b) + var2 + str(c))
        print("Berapakah hasil dari {0}{1}{2}{3}{4}".format(a,r,b,var2,c))
        #jawab
        jawab = int(input("Masukkam Jawaban Anda : "))
        if jawab == hasil:
            return print ("Jawaban Anda Benar ! ")
        else:
            print("Jawaban Anda Masih Salah !")
            print ("Hasil dari", a,r,b,r,c, "=", hasil)
    elif level == 3:
        a = random.randint(20,100)
        b = random.randint(20,100)
        c = random.randint(20,100)
        d = random.randint(20,100)
        r = random.choice(operasi)
        var2 = random.choice(operasi)
        var3 = random.choice(operasi)
        #hasil
        hasil = eval(str(a) + r + str(b) + var2 + str(c) + var3 + str(d))
        print("Berapakah hasil dari {0}{1}{2}{3}{4}{5}{6}".format(a,r,b,var2,c,var3,d))
        #jawab
        jawab = int(input("Masukkam Jawaban Anda : "))
        if jawab == hasil:
            return print ("Jawaban Anda Benar ! ")
        else :
            print("Jawaban Anda Masih Salah !")
            print("Hasil dari", a,r,b,r,c,r,d, "=", hasil)
print("===Program test artimatika dasar===")
print("Pilihan level yang tersedia : ")
print("1. Easy")
print("2. Medium")
print("3. Hard")
level = int(input("Masukkan tingkatan yang ingin anda coba : "))
generate(level)