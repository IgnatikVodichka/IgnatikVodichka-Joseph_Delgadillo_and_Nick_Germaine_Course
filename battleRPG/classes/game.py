import random


class bcolors:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


class Person:

    def __init__(self, hp, mp, attack, defence, magic):
        self.maxhp = hp
        self.hp = hp
        self.maxmp = mp
        self.mp = mp
        self.attack_low = attack - random.randrange(5, 15)
        self.attack_high = attack + random.randrange(5, 15)
        self.defence = defence
        self.magic = magic
        self.action = ["Attack", "Magic"]

    def generate_phisical_damage(self):
        return random.randrange(self.attack_low, self.attack_high)

    def generate_magical_damage(self, i):
        magic_damage_low = self.magic[i]["damage"] - random.randrange(3, 10)
        magic_damage_high = self.magic[i]["damage"] + random.randrange(3, 10)
        return random.randrange(magic_damage_low, magic_damage_high)

    def take_damage(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0
        return self.hp
