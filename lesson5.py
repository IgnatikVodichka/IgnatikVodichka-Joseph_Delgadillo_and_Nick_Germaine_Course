import random


class Enemy:
    attack_low = 60
    attack_high = 80

    def get_attack(self):
        print(self.attack_low)


skeleton = Enemy()
goblin = Enemy()


# player_hp = 260

# while player_hp > 0:
#     damage = random.randrange()
#     player_hp -= damage

#     if player_hp <= 30:
#         player_hp = 30
#     print(f"Enemy strikes for {damage} points of damage. Current HP is {player_hp}")

#     if player_hp > 30:
#         continue
#     print("You have low health. You've been teleported to the nearest inn.")
#     break
