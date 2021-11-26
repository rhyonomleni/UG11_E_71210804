def hurufTengah(kata):
    l = len(kata)
    if l%2==0 :
        if len(kata) >= 8:
            a = kata[2:6]
            print ("Huruf tengah pada kata {0} adalah".format(kata), a)
        elif len(kata) <=6:
            b = kata[2:4]
            print ("Huruf tengah pada kata {0} adalah".format(kata), b)
    else:
        if len(kata) >= 9:
            c = kata[3:6]
            print ("Huruf tengah pada kata {0} adalah".format(kata), c)
        elif  len(kata) == 7:
            d = kata[2:5]
            print ("Huruf tengah pada kata {0} adalah".format(kata), d)
        elif len(kata) == 3:
            e = kata[1:-1]
            print ("Huruf tengah pada kata {0} adalah".format(kata), e)
        else:
                print ("-")
kata = input("Masukkan kata : ")
hurufTengah(kata)