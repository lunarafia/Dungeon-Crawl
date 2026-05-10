import main
import Entity

class Room:
    def __init__(self, name, description, exits):
        self.name = name
        self.description = description
        self.exits = {}

#Rooms
Entrance = Room("Entrance", "A plain stone room", "North")
Hallway = Room("Hallway", "A dusty stone hallway", "West")
Prison = Room("PrisonCell", "A cramped prison cell", "East")

#Room connections
Entrance.exits["North"] = Hallway

Hallway.exits["West"] = Prison
Hallway.exits["South"] = Entrance
Prison.exits["East"] = Hallway
