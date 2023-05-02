class Kendaraan:
    def __init__(self,merk,model):
        self.merk=merk
        self.model=model
    
class Mobil(Kendaraan):
    def __init__(self, merk, model,tahun):
        super().__init__(merk, model)
        self.tahun=tahun

    def move(self):
        print("Drive")

class Kapal(Kendaraan):
    def __init__(self, merk, model,harga):
        super().__init__(merk, model)
        self.harga=harga
    def move(self):
        print("Berlayar")

class Pesawat(Kendaraan):
    def move(self):
        print("Terbang")

car1=Mobil("Suzuki", "Ertiga", "2023")
boat1=Kapal("Marcopolo", "Perahu layar", "300 Juta")
plane1=Pesawat("Boeing", "737")

for angkutan_umum in (car1,boat1,plane1):
    angkutan_umum.move()
    print(angkutan_umum.merk)

