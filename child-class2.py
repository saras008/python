class mobil:
    def __init__(self,merk,tipe):
        self.merk=merk
        self.tipe=tipe

    def printme(self):
        print("Mobil terlaris 2022 adalah", self.merk,self.tipe)

class EvCar(mobil):
    def __init__(self, merk, tipe,harga):
        super().__init__(merk, tipe)
        self.harga=harga

mobil_listrik=EvCar("Wuling","AirEv","300")
mobil_listrik.printme()