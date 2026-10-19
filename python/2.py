class Character:
    def __init__(self, name, health, attack_power, level, defense):
        self.name = name
        self._health = health
        self.attack_power = attack_power
        self.level = level
        self.defense = defense
    def display_stats(self):
        print(self.name)
        print(self.health)
        print(self.attack_power)
        print(self.level)
    # def attack(self, enemy):
    #     Damage = enemy.defense - self.attack_power 
    #     print(f"Remaining Health : {enemy.health-Damage}")

    def take_damage(self,damage):
        health = self._health-damage
        print(f"Health is {health}")
        if health<=0:
            health=0
        else:
            pass

    def heal(enemy, amount):
        is_user = int(input("Do you wanna heal :"))
        if is_user <= 1:
            Healing = enemy.health + amount
            print(f"Health Restored = {Healing}")
        else:
            pass
hero1 = Character("Dante",500,70,5,100)
hero2 = Character("Vergil",500,75,5,100)
# print(Character.attack(hero1,hero2))
print(Character.heal(hero2,50))
print(Character.take_damage(enemy,attack_power))