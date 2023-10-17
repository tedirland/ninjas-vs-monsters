import pygame
clock = pygame.time.Clock()

pygame.init()

#get the display info. Info is a class...
display_info = pygame.display.Info()
screen_size = (display_info.current_w, display_info.current_h)
screen = pygame.display.set_mode(screen_size)
RUNNING = True # BOOL for game loop

# This is the main game loop
while RUNNING:
    # check to see if any events occured since the last time through the game loop
    for event in pygame.event.get():
        # Check to see what event it was
        if event.type == pygame.QUIT:
            RUNNING = False
    # get image off of hd and load into pygame. Returns a Surface object
    background_image = pygame.image.load("./images/background4.png")
    # call the get_rect method on the Surface object
    background_rect = background_image.get_rect()
    # debug
    print(background_rect)
    # blit = block image transfer
    # takes 2 args
    # 1. What to draw
    # 2. where to draw it
    screen.blit(background_image, background_rect)
    clock.tick(60) #integer passed is the FPS
    pygame.display.flip() # DRAW OUR STUFF
