import Inventory
import pygame
import random

class Item:
    def __init__(self, name, consumable=False):
        self.name = name
        self.consumable = consumable

#Subclass of Item class, contains Weapons
class Weapon(Item):
    def __init__(self, name, dice):
        super().__init__(name, False)
        self.dice = dice

Dagger = Weapon("Dagger", 4)
Hammer = Weapon("Hammer", 4)
Spear = Weapon("Spear", 6)
ShortSword = Weapon("Shortsword", 6)
LongSword = Weapon("Longsword", 8) #1d8
MorningStar = Weapon("Morning Star", 8)

#Lists
WeaponList = [Dagger, Hammer, Spear, ShortSword, LongSword, MorningStar]

# Dictionaries
# iterate through weapon list, find all weapons where dice = 4 and add them to dictionary
d4Weapon = {}
for i in WeaponList:
    if i.dice == 4:
        d4Weapon[i.name] = i

d6Weapon = {}
for i in WeaponList:
    if i.dice == 6:
        d6Weapon[i.name] == i

d8Weapon = {}
for i in WeaponList:
    if i.dice == 8:
        d8Weapon[i.name] == i

# EnemyList = []
# for i in range(20):
#     EnemyList.append(WeaponList(i))

# #Error checking
# print(f"EnemyList: {EnemyList}")
print(f"WeaponList: {WeaponList}")

#Armor class
class Armor(Item):
    pass

#Subclass of Item class, contains potions and their associated functions
class Potion(Item):
    def __init__ (self, name, healPoints):
        super().__init__(name, True) #init parent class
        self.healPoints = healPoints

def basicHeal():
    random.randint(2, 6)

def averageHeal():
    random.randint(4, 10)

def improvedHeal():
    random.randint(6, 14)

basicPotion = Potion("Basic Health Potion", basicHeal)
averagePotion = Potion("Average Health Potion", averageHeal)
improvedPotion = Potion("Improved Health Potion", improvedHeal)

#Create potions that temporarily modify player stats
