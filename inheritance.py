class orang:
    def __init__(self,fname,lname):
        self.firstname= fname
        self.lastname=lname

    def printname(self):
        print(self.firstname, self.lastname)

p1=orang("Jhon", "Doe")

p1.printname()