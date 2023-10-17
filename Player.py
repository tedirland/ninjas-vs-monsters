import pygame


class Player():
    '''This is the class representing a Player in our game.
    Its constructor takes a screen
    '''

    def __init__(self,screen) -> None:
        self.screen = screen
        #load image to background
        self.image = pygame.image.load("./images/ninja/Idle__000.png")
        # get the coords of the image
        self.rect = self.image.get_rect()
        
    def move_player(self,screen):
        screen.blit(self.image,self.rect)