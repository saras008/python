def rekursif(bil):
    if (bil > 3):
        hasil = bil + rekursif(bil-1)
        print(hasil)
    else:
        hasil=0
    return hasil

rekursif(5)

