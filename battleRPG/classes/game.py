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
        self.max_hp = hp
        self.hp = hp
        self.max_mp = mp
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

    def reduce_mp(self, mp_cost):
        self.mp -= mp_cost

    def get_hp(self):
        return self.hp

    def get_max_hp(self):
        return self.max_hp

    def get_mp(self):
        return self.mp

    def get_max_mp(self):
        return self.max_mp

    def get_spell_name(self, i):
        return self.magic[i]["name"]

    def get_spell_mp_cost(self, i):
        return self.magic[i]["cost"]

    def choose_action(self):
        i = 1
        print(f"{bcolors.OKBLUE}{bcolors.BOLD}Actions: {bcolors.ENDC}")
        for item in self.action:
            print(f"{str(i)}: {item} ")
            i += 1

    def choose_spell(self):
        i = 1
        print(f"{bcolors.OKBLUE}{bcolors.BOLD}Magic Spells: {bcolors.ENDC}")
        for spell in self.magic:
            print(f"{str(i)}: {spell['name']} MP cost: {spell['cost']}")
            i += 1
