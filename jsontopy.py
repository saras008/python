import json

x = '{"nama":"iyus", "alamat":"tanah merah", "umur":"34 tahun"}'

y=json.loads(x)
print(y["nama"])
print(y["umur"])
print(y)