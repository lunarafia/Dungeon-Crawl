import pygame
import main

class Enemy:
    def __init__(self, name, health, damage, speed):
        self.name = name
        self.health = health
        self.damage = damage
        self.speed = speed

class Weapon:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

class Player:
    def __init__(self, name, health, damage, speed):
        self.name = name
        self.health = health
        self.damage = damage
        self.speed = speed

class Item:
    def __init__(self, name):
        self.name = name

class Potion(Item):
    pass

Goblin = Enemy("Goblin", 15, 5, 3)
Slime = Enemy("Slime", 7, 5, 6)
Skeleton = Enemy("Skeleton", 13, 6, 4) 

Sword = Weapon("Sword", 6)
Axe = Weapon("Axe", 5)
Staff = Weapon("Staff", 5)