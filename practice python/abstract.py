from abc import ABC,abstractclassmethod
class Vehicle:
    def __init__(self,model,year,color,for_sale):
        self.model=model
        self.year=year
        self.color=color
        self.for_sale=for_sale
    def start(self):
        print("Vromm Vromm!!!")   
    @abstractclassmethod
    def fuel_type(self):
        pass
class Car(Vehicle):
    def fuel_type(self):
        print("Petrol")
class EV(Vehicle):
    def fuel_type(self):
        print("Battery")
car=Car("Impala",1994,"Black",True)
print(car.model)
print(car.year)
car.start()
car.fuel_type()
ev=EV("Tesla model y",2026,"White",True)
print(ev.model)
print(ev.year)
ev.start()
ev.fuel_type()
