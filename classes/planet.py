import pygame

class Planet:

    def __init__(self):
        
        self.name = "Planet"
        self.size = "Size"
        self.imagePath = "art/planet.png"
        self.blit = pygame.image.load(self.imagePath)
    
    def display(self, surface):
        surface.blit(self.blit, (0,0))