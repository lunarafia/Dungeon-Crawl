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

#text handling
# display_surface = pygame.display.set_mode((X, Y))
# font = pygame.font.Font('Arial.ttf', 20)

clock = pygame.time.Clock()

running = True
# current_room = Entrance #init room traversal

while running:

    #display background
    screen.blit(background, (0, 0)) 
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #room traversal
    for event in pygame.event.get():
        if event.type == pygame.K_DOWN: #K_DOWN means event triggers when the key is press K_UP means event triggers when its released hence event.type
            if event.key == pygame.K_UP:
                print("Player moved North")

            if event.key == pygame.K_DOWN:
                print("Player moved South")

            if event.key == pygame.K_LEFT:
                print("Player moved west")

            if event.key == pygame.K_RIGHT:
                print("Player moved East") 

pygame.quit()


