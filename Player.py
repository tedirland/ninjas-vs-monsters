import pygame


class Player():
    '''This is the class representing a Player in our game.
    Its constructor takes a screen
    '''

    def __init__(self,screen) -> None:
        self.screen = screen
        self.x = 200
        self.y = 200
        #load image to background
        self.image = pygame.image.load("./images/ninja/Idle__000.png")
        self.image = pygame.transform.scale_by(self.image, .35)
        # get the coords of the image
        self.rect = self.image.get_rect()
        
    def draw_player(self,screen):
        screen.blit(self.image,(self.x, self.y))