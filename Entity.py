import pygame
import random
from collections import defaultdict

#Dice rolls
def rolld4():
    random.randint(1, 4)

def rolld6():
    random.randint(1, 6)

def rolld8():
    random.randint(1, 8)

class Enemy:
    def __init__(self, name, health, armor, strength, dexterity):
        self.name = name
        self.health = health
        self.armor = armor
        self.strength = strength
        self.dexterity = dexterity
        # self.weapon = weapon

Goblin = Enemy("Goblin", 15, 10, 8, 12)
Skeleton = Enemy("Skeleton", 13, 13, 10, 11) 
Slime = Enemy("Slime", 10, 8, 10, 15 ) #Slimes should be easy to hit but fast

#Want to add weapon attribute to enemy class, should allow null values. Will allow enemies to select a random weapon from a specified dictionary before battle
class Weapon:
    def __init__(self, name, dice):
        self.name = name
        self.dice = dice

Dagger = Weapon("Dagger", 4)
Hammer = Weapon("Hammer", 4)
Spear = Weapon("Spear", 6)
ShortSword = Weapon("Shortsword", 6)
LongSword = Weapon("Longsword", 8) #1d8
MorningStar = Weapon("Morning Star", 8)

class Item:
    def __init__(self, name):
        self.name = name

class Potion(Item):
    pass



class Player:
    def __init__(self, name, health, maxHealth, armor, strength, dexterity, weapon, meleeLow, meleeUp):
        self.name = name
        self.health = health
        self.maxHealth = maxHealth #so potions know how much char max health is
        self.armor = armor #determines if player is hit by attack
        self.strength = strength #melee damage modifier
        self.dexterity = dexterity #determines attack order
        self.weapon = weapon #melee damage mod, determines dice roll
        self.meleeLow = meleeLow 
        self.meleeUp = meleeUp

    #Total damage = Weapon damage dice + Ability modifier + bonus modifier
    # def meleeAttack(self, target):
    #     if self.strength > 0:
    #         if Weapon.dice == 4:
    #             meleeDamage = rolld4 + (self.strength/2)
    #         elif Weapon.dice == 6:
    #             meleeDamage = rolld6 + (self.strength/2)
    #         elif Weapon.dice == 8:
    #             meleeDamage = rolld8 + (self.strength/2)
             
    #     else:
    #         print(f"{self.name} has no strength points.")

#Lists
WeaponList = [Dagger, Hammer, Spear, ShortSword, LongSword, MorningStar]


#Dictionaries
#iterate through weapon list, find all weapons where dice = 4 and add them to dictionary
# d4Weapon = {}
# for i in Weapon:
#     if Weapon.dice == 4:
#         d4Weapon.update(i)

# d6Weapon = {}
# for i in Weapon:
#     if Weapon.dice == 6:
#         d6Weapon.update(i)

# d8Weapon = {}
# for i in Weapon:
#     if Weapon.dice == 8:
#         d8Weapon.update(i)

# EnemyList = []
# for i in range(20):
#     EnemyList.append(WeaponList(i))

# print(f"EnemyList: {EnemyList}")
# print(f"WeaponList: {WeaponList}")