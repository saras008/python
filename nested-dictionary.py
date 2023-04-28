keluarga ={
    "pertama": {
    "nama": "satu",
    "usia" : "tiga tahun"
    },
    "kedua":{
    "nama" : "dua",
    "usia" : "dua tahun"
    },
    "ketiga":{
    "nama" : "tiga",
    "usia" : "satu tahun"
    }
}

for x,y in keluarga.items():
    print(x,y)

#printing setiap key yg ada pada dictionary keluarga
for x in keluarga:
    print(keluarga[x].values())