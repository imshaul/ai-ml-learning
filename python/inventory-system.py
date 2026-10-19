potion = 5

class Player:
    def __init__(self,name):
        self.name = name
        self.health = 500
        self.potion = 5



class Item:
    def __init__(self,name,quantity,price):
        self.name = name
        self._quantity = quantity
        self.price = price
        self.health = 500
        self.potion = 5

    def buy(self, amount):
            self._quantity += amount           
            print(f"""Item : {self.name}
    Quantity : {self._quantity}
    Price : {self.price}""")

    def sell(self, amount):
            if amount>self._quantity:
                    print(f"Not enough in inventory")
            else:
                self._quantity -= amount  

           
    def __str__(self):
        return f"""Item : {self.name}
Price : {self.price}"""
    def __len__(self):
        return self._quantity
    def __add__(self,amount):
        return self._quantity +=amount
class Weapon(Item):
    damage = 25
    def upgrade(self):
        self.damage+=30
        print(f"Damage is now {self.damage}")

class Potion(Item):
    def __init__(self):
        self.heal_amount = 100
    def drink(self,player):
        player.health+=self.heal_amount
        player.potion-=1
        print(f"Health Restored\n Potion left : {player.potion}")

player = Player("Sahil")
i = Item("Sword",20,25.0)
w = Weapon("Sword",20,25.0)
p = Potion()
# user = input("Do you wanna buy or sell a item? : ")
# if user.lower()=="buy":
#     i.buy(100)
# else :
#     i.sell(10)

# print("Do you wanna upgrade your weapon?")
# upd = input("send Yes to upgrade it will cost 50 cronos : ")
# if upd.lower()=="yes":
#     w.upgrade()
# else:
#     pass

# med = input("do you wannna heal : ")
# if med.lower()=="yes":
#     p.drink(player)
# else:
#     pass

print(i)
print(len(i))