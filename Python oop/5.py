class Dog:
    def sound(self):
        print("Rough Rough🐕‍🦺")

class Cat:
    def sound(self):
        print("Meow Meow🐈")
        
class Crow:
    def sound(self):
        print("Caww Caww🐦‍⬛")

animals=[Dog(),Cat(),Crow()]

for animals in animals:
    animals.sound()

