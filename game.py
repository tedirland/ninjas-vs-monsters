import pygame
from update_screen import update_screen
from Background import Background
from Player import Player

clock = pygame.time.Clock()

pygame.init()

#get the display info. Info is a class...
display_info = pygame.display.Info()
screen_size = (display_info.current_w, display_info.current_h)
screen = pygame.display.set_mode(screen_size)
RUNNING = True # BOOL for game loop
background = Background(screen,screen_size)
player = Player(screen)

# This is the main game loop
while RUNNING:
    # check to see if any events occured since the last time through the game loop
    for event in pygame.event.get():
        # Check to see what event it was
        if event.type == pygame.QUIT:
            RUNNING = False
    clock.tick(60) #integer passed is the FPS
    pygame.display.flip() # DRAW OUR STUFF
    update_screen(screen = screen, player= player,  background=background)
