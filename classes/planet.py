# Import the 'pygame' module
import pygame
# Import the 'random' module
import random

# Create a new class called 'Planet'
class Planet:

    # The constructor function
    def __init__(self, game):
        
        self.name = "Planet"
        self.size = "Size"
        self.imagePath = "art/planet.png"
        self.displayImage = pygame.image.load(self.imagePath)
        self.imageWidth, self.imageHeight = self.displayImage.get_rect().width, self.displayImage.get_rect().height
        self.widthBorder = game.windowWidth - self.imageWidth
        self.heightBorder = game.windowHeight - self.imageHeight
        self.pos = (random.randint(0,self.widthBorder),random.randint(0,self.heightBorder))
    
    def blit(self, surface):
        surface.blit(self.displayImage, self.pos)