class orang:
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname
    
    def print_me(self):
        print("My fullname is", self.firstname,self.lastname)

p1=orang("Iyus","Simatupang")
p1.print_me()

class siswa(orang):
    pass

murid = siswa("Iyus", "Dedi Putra")
murid.print_me()