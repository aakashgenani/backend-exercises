# Backend Programming with Python
# Homework 5 - Battleships

import random, math


class SpaceShip:
    def __init__(self, name, hp, armour, damage):
        self.name = name
        self.hp = hp
        self.armour = armour
        self.damage = damage

    def attack(self, other):
        if isinstance(other, SpaceShip):
            damage_dealt = self.damage - other.armour
            if damage_dealt < 0 < self.damage:
                damage_dealt = 1
            other.hp = other.hp - damage_dealt
        print(
            f'Damage dealt to {other.name} = {self.damage} ({self.name} Damage) - {other.armour} ({other.name} Armor) = {damage_dealt}')
        print(f'HP left on {other.name} = {other.hp}')

    def upgrade(self, upgrade_name):
        if upgrade_name == 'Titanium Armour':
            self.armour = self.armour + 3
            self.hp = self.hp + 250
        elif upgrade_name == 'Absorption Shield':
            self.armour = math.floor(self.armour * 1.5)
        elif upgrade_name == 'Proton Torpedos':
            self.damage = self.damage + 25
        elif upgrade_name == 'Flare Engine':
            self.damage = math.floor(self.damage * 1.5)
            self.armour = self.armour + 3
            self.hp = math.floor(self.hp * 1.2)


def main():
    ship1 = SpaceShip('Nostromo', random.randint(1, 100), random.randint(0, 30), random.randint(0, 30))
    ship2 = SpaceShip('Covenant', random.randint(1, 100), random.randint(0, 30), random.randint(0, 30))

    print(f'Stats before upgrades:\n'
          f'Ship 1: Name = {ship1.name}, HP = {ship1.hp}, Armour = {ship1.armour}, Damage = {ship1.damage}\n'
          f'Ship 2: Name = {ship2.name}, HP = {ship2.hp}, Armour = {ship2.armour}, Damage = {ship2.damage}')

    ship1_upgrades = list()
    ship2_upgrades = list()
    while True:
        a = input('Do you want to upgrade a ship? (y/n)  ')
        if a == 'y':
            ship_name = input("Enter ship's name: ")
            upgrade_name = input("Now enter the upgrade's name: ")
            if ship_name == ship1.name and upgrade_name not in ship1_upgrades:
                ship1.upgrade(upgrade_name)
                ship1_upgrades.append(upgrade_name)
            elif ship_name == ship2.name and upgrade_name not in ship2_upgrades:
                ship2.upgrade(upgrade_name)
                ship2_upgrades.append(upgrade_name)
        elif a == 'n':
            break

        print(f'Stats after upgrades:\n'
              f'Ship 1: Name = {ship1.name}, HP = {ship1.hp}, Armour = {ship1.armour}, Damage = {ship1.damage}\n'
              f'Ship 2: Name = {ship2.name}, HP = {ship2.hp}, Armour = {ship2.armour}, Damage = {ship2.damage}')

    print(f'Battle begins between {ship1.name} and {ship2.name}')

    while ship1.hp and ship2.hp > -1:
        if ship1.damage == 0 == ship2.damage:
            print(f'Match is drawn as both ships cannot attack')
            break
        (print(f'{ship1.name} attacks {ship2.name}'), ship1.attack(ship2)) if ship1.damage > 0 \
            else print(f'{ship1.name} cannot attack as it has zero damage')
        if ship2.hp < 1:
            print(f'{ship1.name} defeated {ship2.name}!')
            break
        (print(f'{ship2.name} attacks {ship1.name}'), ship2.attack(ship1)) if ship2.damage > 0 \
            else print(f'{ship2.name} cannot attack as it has zero damage')
        if ship1.hp < 1:
            print(f'{ship2.name} defeated {ship1.name}!')
            break


if __name__ == '__main__':
    main()
