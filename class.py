class orang:
    def __init__(self,name,age):
        self.name=name
        self.age=age

user = orang("iyus",33)

print(user.name + " umur " + str(user.age))