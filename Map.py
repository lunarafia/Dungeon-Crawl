import pygame

class TileKind:
    def __init__(self, name, image, is_solid):
        self.name = name
        self.image = pygame.image.load(image)
        self.is_solid = is_solid
    
class Map:
    def __init__(self, mapFile, tileKinds, tileSize):
        self.tileKinds = tileKinds
        
        #Load file
        file = open(mapFile, "r")
        data = file.read()
        file.close()

        #Set up tiles from loaded data
        self.tiles = []
        for line in data.split("\n"):
            row = []
            for tileNumber in line:
                row.append(int(tileNumber))

            self.tiles.append(row)


        #Set size
        self.tileSize = tileSize

    def draw(self, screen, offset_x, offset_y):
        for y, row in enumerate(self.tiles):
            for x, tile in enumerate(row):
                    
                location = (
                    x * self.tileSize + offset_x,
                    y * self.tileSize + offset_y
                )

                image = self.tileKinds[tile].image
                screen.blit(image, location)

    # def draw(self, screen):
    #     for y, row in enumerate(self.tiles): 
    #         for x, tile in enumerate(row):
    #             location = (x * self.tileSize, y * self.tileSize)
    #             image = self.tileKinds[tile].image
    #             screen.blit(image, location)

