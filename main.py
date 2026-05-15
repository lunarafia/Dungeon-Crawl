import pygame
import random
import Entity
import Rooms

#dice roll
def roll_d20():
    return random.randint(1, 20)

pygame.init()
screen = pygame.display.set_mode((1280, 720)) #set resolution
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((19, 15, 46)) #background colour

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

north_btn = Button(100, 400, 100, 50, "North")
south_btn = Button(100, 500, 100, 50, "South")
west_btn = Button(-10 + 100, 450, 100, 50, "West")
east_btn = Button(210, 450, 100, 50, "East")
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
    screen.blit(room_desc, (400, 100))


#text handling
# display_surface = pygame.display.set_mode((X, Y))
# font = pygame.font.Font('Arial.ttf', 20)

clock = pygame.time.Clock()

running = True
current_room = Rooms.Entrance #init room traversal

while running:

    screen.blit(background, (0, 0)) #display background
    clock.tick(60)

    #room traversal
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
        
        #Movement
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

        #Button rendering
        north_btn.draw(screen, font)
        south_btn.draw(screen, font)
        west_btn.draw(screen, font)
        east_btn.draw(screen, font)
        observe_btn.draw(screen, font)
        bag_btn.draw(screen, font)

        pygame.display.update()


pygame.quit()


