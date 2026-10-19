def attack(*enemy):
    for e in range(1):
        print(f"enemy attacked : {enemy}")
attack("goblin","magneto","hulk","Dr doom")

def create_player(**stats):
    for key,value in stats.items():
        print(key,":",value)
create_player(
    name="sahil",
    health=300,
    damage=60,
    level=5
)
