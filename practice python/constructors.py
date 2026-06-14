class Car:
    def __init__(self,model,year,color,for_sale):
        self.model=model
        self.year=year
        self.color=color
        self.for_sale=for_sale

car1=Car("Mustang",2024,"black",False)
car2=Car("Impala",1995,"red",True)
print(car1.model)
print(car2.model)
print(car2.year)
print(car2.color)