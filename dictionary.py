kamus = {
    "merk" : "ford",
    "tipe" : "mustang",
    "tahun" : 1990
}

print(kamus.get("merk"))

for x in kamus:
    print(kamus[x])



kamus["harga"]= "190 Juta"

print(kamus.items())

for x,y in kamus.items():
    print (x,y)
