import pygame
from update_screen import update_screen
from check_events import check_events
from Background import Background
from Player import Player

clock = pygame.time.Clock()

pygame.init()

#get the display info. Info is a class...
display_info = pygame.display.Info()
screen_size = (display_info.current_w, display_info.current_h)
screen = pygame.display.set_mode(screen_size)
game_on = True # BOOL for game loop
background = Background(screen,screen_size)
player = Player(screen)

# This is the main game loop
while game_on:
    # run checl_events where we have moved all our event logic
    #check_events returns a dictionary with a "game_on" key
    event_data = check_events(player)
    game_on = event_data["game_on"]

    # run update_screen which is where we draw and update stuff 
    update_screen(screen = screen, player= player,  background=background)
    clock.tick(60) #integer passed is the FPS
    pygame.display.flip() # DRAW OUR STUFF
