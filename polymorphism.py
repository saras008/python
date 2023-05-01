#module/function/operator with same name that use/executed on object or class


class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    
    def move(self):
        print("Drive")


class Boat:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model

    def move(self):
        print("Sail")

class Plane:
    def __init__(self,brand, model):
        self.brand=brand
        self.model=model
    
    def move(self):
        print("Fly")

car1=Car("Toyota","Avanza")
boat1=Boat("Ibiza","Touring 20")
plane1=Plane("Garuda Indonesia","Airbus")

for x in(car1,boat1,plane1):
    x.move()