class Animal:
    def __init__(self,name):
        self.name=name

    def eat(self):
        print(f"{self.name} is eating")

class Dog(Animal):
    pass
class Cat(Animal):
    pass

dog=Dog("Crunchy")
cat=Cat("Meow")
print(dog.name)
print(cat.name)