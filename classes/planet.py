# Import the 'pygame' module
import pygame
# Import the 'random' module
import random
# From the 'os' module, import 'listdir'
from os import listdir
# From the 'os.path' module, import 'isfile' and 'join'
from os.path import isfile, join

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
        # !-- The following was copied from https://stackoverflow.com/questions/3207219/how-do-i-list-all-files-of-a-directory
        # Create a list of all files in the art folder
        planetList = [f for f in listdir("art/planets") if isfile(join("art/planets", f))]
        # !--
        self.name = "Planet"
        self.resize = random.choice([0.25,0.50,0.75,1.00,1.25,1.50,1.75])
        self.size = self.sizeDict[self.resize]
        self.imagePath = "art/planets/"+random.choice(planetList)
        self.displayImage = pygame.image.load(self.imagePath)
        self.imageWidth, self.imageHeight = self.displayImage.get_rect().width, self.displayImage.get_rect().height
        self.widthBorder = game.windowWidth - self.imageWidth
        self.heightBorder = game.windowHeight - self.imageHeight
        self.x = random.randint(0,self.widthBorder)
        self.y = random.randint(0,self.heightBorder)
        self.pos = (random.randint(0,self.widthBorder),random.randint(0,self.heightBorder))

        self.displayImage = pygame.transform.scale(self.displayImage,(int(self.imageWidth*self.resize),int(self.imageHeight*self.resize)))
        self.imageWidth, self.imageHeight = self.displayImage.get_rect().width, self.displayImage.get_rect().height
    
    def blit(self, surface):
        surface.blit(self.displayImage, self.pos)