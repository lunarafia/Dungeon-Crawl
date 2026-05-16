import Entity

class Room:
    def __init__(self, name, description, exits):
        self.name = name
        self.description = description
        self.exits = {}

#Rooms
Entrance = Room("Entrance", "Plain stone room.", "North" "West" "East")
MiniBoss = Room("Mini Boss", "A room idk", "South")
WardensHallway = Room("Warden's Hallway", "A dusty unlit hallway.", "North")
EntranceHallway = Room("Entrance Hallway", "A hallway.", "North" "West" "South")
WardensOffice = Room("Warden's Office", "Abandoned office.", "South")
MainHallway = Room("Main Hallway","A hallway.","North" "South" "West")
SecondaryHallway = Room("Second Hallway", "Another hallway", "")

PrisonHallway = Room("Prison Hallway", "A hallway lined with prison cells", "South" "West" "East")
# PrisonCell1 = Room()
# PrisonCell2 = Room()
# PrisonCell3 = Room()
# PrisonCell4 = Room()
# PrisonCell5 = Room()
# PrisonCell6 = Room()

LootRm1 = Room("Loot 1", "Boring stone room, contains a chest", "South")
# LootRm2 = Room()
# LootRm3 = Room()

# Barracks = Room()
# Kitchen = Room()

#Connections
Entrance.exits["West"] = MiniBoss
Entrance.exits["East"] = WardensHallway 
Entrance.exits["North"] = EntranceHallway

WardensHallway.exits ["North"] = WardensOffice
WardensHallway.exits["South"] = Entrance
WardensOffice.exits["South"] = WardensHallway

EntranceHallway.exits["North"] = MainHallway
EntranceHallway.exits["West"] = LootRm1
EntranceHallway.exits["South"] = Entrance

LootRm1.exits["South"] = EntranceHallway

MainHallway.exits["South"] = EntranceHallway
MainHallway.exits["West"] = SecondaryHallway
MainHallway.exits["North"] = PrisonHallway

PrisonHallway.exits["South"] = MainHallway

# #Rooms
# Entrance = Room("Entrance", "A plain stone room", "North")
# Hallway = Room("Hallway", "A dusty stone hallway", "West")
# Prison = Room("PrisonCell", "A cramped prison cell", "East")

# #Room connections
# Entrance.exits["North"] = Hallway

# Hallway.exits["West"] = Prison
# Hallway.exits["South"] = Entrance
# Prison.exits["East"] = Hallway
