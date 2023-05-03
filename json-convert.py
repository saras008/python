import json

x ={
    "nama":"Iyus Dedi Putra",
    "alamat":"Jl. Kelapa Hijau",
    "kendaraan":[
        {
            "merk":"yamaha", "type":"xride"
        },
        {
            "merk":"honda", "type":"mobilio"
        }
    ]
}

print(json.dumps(x))