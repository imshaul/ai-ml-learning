class Animal:
    def __init__(self,name):
        self.name=name
    def sound(self):
        print(f"{self.name} is making sound")

class Dog(Animal):
    def eat(self):
        print(f"{self.name} is eating")

class Cat(Dog):
    pass

dog=Dog("Lullu")
cat=Cat("Meow")
dog.sound()
dog.eat()
cat.sound()
cat.eat()