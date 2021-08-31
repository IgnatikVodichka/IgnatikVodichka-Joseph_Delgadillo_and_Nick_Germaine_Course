from classes.game import Person, bcolors


magic = [
    {"name": "Fire", "cost": 10, "damage": 60},
    {"name": "Ice", "cost": 10, "damage": 50},
    {"name": "Earth", "cost": 10, "damage": 45}
]


player = Person(460, 65, 60, 34, magic)
enemy = Person(1200, 55, 45, 25, magic)

running = True

print(f"{bcolors.FAIL}{bcolors.BOLD}AN ENEMY ATTACKING!{bcolors.ENDC}")

while running:
    print()
    print("=======================================")
    player.choose_action()
    print()

    choice = int(input("Choose and action: "))
    index = choice - 1

    if index == 0:
        damage = player.generate_phisical_damage()
        enemy.take_damage(damage)
        print(f"You've dealt {damage} damage points. Enemy HP: {enemy.get_hp()}")

    enemy_choice = 1

    enemy_damage = enemy.generate_phisical_damage()
    player.take_damage(enemy_damage)
    print(f"Enemy dealt {enemy_damage} damage points. Your HP: {player.get_hp()}")
