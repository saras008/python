class orang:
    def __init__(self,nama,umur):
        self.nama=nama
        self.umur=umur

    def __str__(self):
        return f"{self.nama} berumur {self.umur}"

p1=orang("iyus",33)

print(p1)