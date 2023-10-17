import pygame

class Background():
    def __init__(self,screen, screen_size):
         # get image off of hd and load into pygame
    # Returns a Surface object
        self.background_image = pygame.image.load("./images/background4.png")
        # scale takes 2 args 
        # 1. what to scale 
        # 2. tuple of new coords
        self.background_image = pygame.transform.scale(self.background_image, screen_size)
        self.background_rect = self.background_image.get_rect()

        # change size of the image
        # scale method
        # blit = block image transfer
        # takes 2 args
        # 1. What to draw
        # 2. where to draw it
        screen.blit(self.background_image, self.background_rect)