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

        # Dictionary to convert the numerical size of the planet (by what scale factor it's image is scaled by) to an alphabetical size (to use for displaying)
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
        # Create a list of all files in the art/planets folder
        planetList = [f for f in listdir("art/planets") if isfile(join("art/planets", f))]
        # !--

        self.name = "Planet"
        # Random choice for the scale factor that the planet image will be scaled by
        self.resize = random.choice([0.25,0.50,0.75,1.00,1.25,1.50,1.75])
        # Convert that scale factor into a text size
        self.size = self.sizeDict[self.resize]
        # Choose a random item in the list planetList and create a path to that file
        self.imagePath = "art/planets/"+random.choice(planetList)
        # Load that path using pygame
        self.displayImage = pygame.image.load(self.imagePath)
        # Scale the image by the scale factor previously determined
        self.displayImage = pygame.transform.scale(self.displayImage,(int(self.imageWidth*self.resize),int(self.imageHeight*self.resize)))
        # Get the width and height of the image file used 
        self.imageWidth, self.imageHeight = self.displayImage.get_rect().width, self.displayImage.get_rect().height
        # Get the maximum X coordinate that the image could be displayed at
        self.widthBorder = game.windowWidth - self.imageWidth
        # Get the maximum Y coordinate that the image could be displayed at
        self.heightBorder = game.windowHeight - self.imageHeight
        # Set the X co ordinate of the image to be a random number between 0 and the maximum X value
        self.x = random.randint(0,self.widthBorder)
        # Set the Y co ordinate of the image to be a random number between 0 and the maximum Y value
        self.y = random.randint(0,self.heightBorder)
        # Get the pygame rect object of the image
        self.rect = self.displayImage.get_rect()
    
    # Class method 'blit'
    def blit(self, surface):
        # Display the pygame object 'self.displayImage' onto the surface 'surface' at X position 'self.x' and Y position 'self.y'
        surface.blit(self.displayImage, (self.x, self.y))