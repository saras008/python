class orang:
    def __init__(self,nama,umur):
        self.nama = nama
        self.umur = umur

    def method_gw(self):
        print("Nama saya adalah", self.nama)

#method adalah function yg ada di dalam class
p1=orang("Iyus", 33)
p1.method_gw()