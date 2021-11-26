def pangkatAngka(angka,nilai): 
    print("Masukan angka yang ingin di Pangkatkan")
    angka = int(input("Angka : "))
    mod = input("ingin memodifikasi pangkat ?(yes/no): ")
    if mod == "yes":
        nilai = float(input("Masukan nilai pangkat : "))
        pangkat = angka ** nilai
        print("hasil dari", angka,"^", nilai, "=",pangkat)
    elif mod == "no":
        pangkat = angka ** 2
        print("hasil dari", angka,"^ 2 =", pangkat)
def akarBilangan():
    print("Masukan angka yang ingin di Akar")
    angka = float(input("Angka : "))
    mod = input("ingin memodifikasi pangkat ?(yes/no): ")
    if mod == "yes":
        nilai = float(input("Masukan nilai akar : "))
        akar = round(angka ** (1/nilai), 2)
        print("hasil akar pangkat", nilai, "dari", angka, "=", akar)
    elif mod == "no":
        akar = round((angka ** 0.5), 2)
        print("hasil akar pangkat", angka, "dari", angka, "=", akar)
print("Menu Program Yang Tersedia")
print("1. Pangkatkan Angka")
print("2. Akarkan Bilangan")
menu = int(input("masukan pilihan yang diinginkan : "))
if menu == 1:
    print("Masukan angka yang ingin di Pangkatkan")
    angka = float(input("Angka : "))
    mod = input("ingin memodifikasi pangkat ?(yes/no): ")
    if mod == "yes":
        nilai = float(input("Masukan nilai akar : "))
        pangkatAngka(angka,nilai)
    elif mod == "no":
        pangkatAngka(angka,2)
elif menu == 2:
    akarBilangan()