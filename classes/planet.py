# Import the 'pygame' module
import pygame
# Import the 'random' module
import random

# Create a new class called 'Planet'
class Planet:

    
    # The constructor function
    def __init__(self, game):

        self.sizeDict = {
        0.25:"Extremely small",
        0.50:"Very small",
        0.75:"Small",
        1.00:"Average",
        1.25:"Large",
        1.50:"Very large",
        1.75:"Extremely large"
    }
        
        self.name = "Planet"
        self.resize = random.choice([0.25,0.50,0.75,1.00,1.25,1.50,1.75])
        self.size = self.sizeDict[self.resize]
        print(self.size)
        self.imagePath = "art/PlanetX@1.00.png"
        self.displayImage = pygame.image.load(self.imagePath)
        self.imageWidth, self.imageHeight = self.displayImage.get_rect().width, self.displayImage.get_rect().height
        self.widthBorder = game.windowWidth - self.imageWidth
        self.heightBorder = game.windowHeight - self.imageHeight
        self.pos = (random.randint(0,self.widthBorder),random.randint(0,self.heightBorder))

        self.displayImage = pygame.transform.scale(self.displayImage,(int(self.imageWidth*self.resize),int(self.imageHeight*self.resize)))
        self.imageWidth, self.imageHeight = self.displayImage.get_rect().width, self.displayImage.get_rect().height
    
    def blit(self, surface):
        surface.blit(self.displayImage, self.pos)