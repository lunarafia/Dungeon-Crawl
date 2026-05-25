import pygame
import random
import Entity
import Rooms
from Map import TileKind, Map
from Camera import createScreen, camera

#dice roll
def roll_d20():
    return random.randint(1, 20)

pygame.init()
# screen = pygame.display.set_mode((1280, 720)) #set resolution
screen = createScreen(1280, 720, "Dungeon Crawl")

background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((19, 15, 46)) #background colour

tileKinds = [
    TileKind("floor", "Assets/Tiles/tile010.png", False), #0
    TileKind("wall", "Assets/Tiles/tile016.png", True), #1
    TileKind("boundary", "Assets/Tiles/floor_placeholder.png", True), #2
    TileKind("door", "Assets/Tiles/wall_placeholder.png", False), #3
]

# map = Map("Assets/Maps/Entrance.map", tileKinds, 16)
map = Map("Assets/Maps/Entrance.map", tileKinds, 16)

#Ensures that map is rendered at the centre of game window

game_width = 1280
game_height = 720

map_width = len(map.tiles[0]) * map.tileSize
map_height = len(map.tiles) * map.tileSize

offset_x = (game_width - map_width) // 2
offset_y = 32

class Player:
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)
        self.rect = pygame.Rect(self.x, self.y, 16, 16)
        self.color = (250, 120, 60)
        self.velX = 0
        self.velY = 0
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False
        self.speed = 3

    def drawPlayer(self, win):
        pygame.draw.rect(win, self.color, self.rect)

    def update(self):
        self.velX = 0
        self.velY = 0
        if self.left_pressed and not self.right_pressed:
            self.velX = -self.speed
        if self.right_pressed and not self.left_pressed:
            self.velX = self.speed
        if self.up_pressed and not self.down_pressed:
            self.velY = -self.speed
        if self.down_pressed and not self.up_pressed:
            self.velY = self.speed

        self.x += self.velX
        self.y += self.velY
        
        self.rect = pygame.Rect(self.x, self.y, 16, 16)
        
        camera.x = self.x - camera.width/2
        camera.y = self.y - camera.height/2

#Player
player = Player(game_width/2, game_height/2)

#Button class
class Button:
    def __init__(self, x, y, width, height, text):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text

    def draw(self, screen, font):
        pygame.draw.rect(screen, (200, 200, 200), self.rect)
        label = font.render(self.text, True, (0, 0, 0))
        screen.blit(label, (self.rect.x + 10, self.rect.y + 10))

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)
    
font = pygame.font.SysFont(None, 30)

north_btn = Button(100, 520, 100, 50, "North")
south_btn = Button(100, 620, 100, 50, "South")
west_btn = Button(5, 570, 100, 50, "West")
east_btn = Button(195, 570, 100, 50, "East")
observe_btn = Button(700, 500, 100, 50, "Observe")
bag_btn = Button(850, 500, 50, 50, "B" )

def move(direction):
    global current_room

    if direction in current_room.exits:
        current_room = current_room.exits[direction]
        print("Moved to:", current_room.name)


    else:
        print("Not a valid dirction.")

def observe(current_room): 
    room_desc = font.render(current_room.description, True, (255, 255, 255))
    screen.blit(room_desc, (450, 450))


#text handling
# display_surface = pygame.display.set_mode((X, Y))
# font = pygame.font.Font('Arial.ttf', 20)

clock = pygame.time.Clock()

running = True
current_room = Rooms.Entrance #init room traversal

while running:

    screen.blit(background, (0, 0)) #display background
    dt_ms = clock.tick(60)

    #Ensure consistent player speed   ...does it work? no
    dt = dt_ms / 1000.0
    player.x += player.speed * dt

    # pygame.time.delay(30) #adds 30ms delay between frames, prevents game from running too fast

    map.draw(screen, offset_x, offset_y)

    #room traversal
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
        
        #Room Traversal
        if event.type == pygame.MOUSEBUTTONDOWN: #means event triggers when the key is pressed
            mouse_pos = pygame.mouse.get_pos()

            if north_btn.is_clicked(mouse_pos):
                move("North")
                # print("Player moved North")

            if south_btn.is_clicked(mouse_pos):
                move("South")
                # print("Player moved South")
                
            if west_btn.is_clicked(mouse_pos):
                move("West")
                # print("Player moved West")

            if east_btn.is_clicked(mouse_pos):
                move("East")
                # print("Player moved East")

            if observe_btn.is_clicked(mouse_pos):
                observe(current_room)

        #Character Movement
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                player.left_pressed = True
            if event.key == pygame.K_d:
                player.right_pressed = True
            if event.key == pygame.K_w:
                player.up_pressed = True
            if event.key == pygame.K_s:
                player.down_pressed = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                player.left_pressed = False
            if event.key == pygame.K_d:
                player.right_pressed = False
            if event.key == pygame.K_w:
                player.up_pressed = False
            if event.key == pygame.K_s:
                player.down_pressed = False

        player.drawPlayer(screen)
        player.update()



        
        #UI Rendering
        #Bottom panel
        pygame.draw.rect(screen, (180, 180, 180), (0, 480, 1280, 240))

        #Button rendering
        north_btn.draw(screen, font)
        south_btn.draw(screen, font)
        west_btn.draw(screen, font)
        east_btn.draw(screen, font)
        observe_btn.draw(screen, font)
        bag_btn.draw(screen, font)



        pygame.display.update()


pygame.quit()


