from classes.game import Person, bcolors


magic = [
    {"name": "fire", "cost": 10, "damage": 60},
    {"name": "ice", "cost": 10, "damage": 50},
    {"name": "earth", "cost": 10, "damage": 45}
]


player = Person(460, 65, 60, 34, magic)


print(player.generate_phisical_damage())
print(player.generate_magical_damage(1))
