# Import the 'pygame' module
import pygame
# Import the 'sys' module
import sys
# Import the 'random' module
import random
# From the classes folder, import the module 'planet'
from classes import planet
# From the scenes folder, import the module 'planetScene'
from scenes import planetScene
# From the methods folder, import the module 'loadingSceneSetup'
from methods import loadingSceneSetup, planetSceneSetup

# Create a new class called 'Application'
class Application:

    # The constructor function
    def __init__(self, width, height):
        # Assign the value 'windowWidth' to the class variable 'width'
        self.windowWidth = width
        # Assign the value 'windowHeight' to the class variable 'height'
        self.windowHeight = height
        # Assign the value 'True' to the class variable 'running'
        self.running = True
        # Assign an empty dictionary to the class variable 'planetDict'
        self.planetDict = {}

        # Initialise pygame
        pygame.init()

        # Create a pygame window with the dimensions 'self.windowWidth' and 'self.windowHeight' and make the window hardware accelerated and double buffed
        self.display = pygame.display.set_mode(
            (self.windowWidth, self.windowHeight), pygame.HWSURFACE | pygame.DOUBLEBUF)

        # Set the title of the window to 'Raize'
        pygame.display.set_caption("Raize")

        self.scene = planetScene

        planetSceneSetup.init(self)

        # While 'self.running' is True
        while self.running:
            self.display.blit(self.backgroundImage, (0,0))
            # For each event in the list 'pygame.event.get()'
            for event in pygame.event.get():
                # If the close button is pressed in the window
                if event.type == pygame.QUIT:
                    # Set 'self.running' to False
                    self.running = False
                    # Quit the pygame window
                    pygame.quit()
                    # Exit the python script
                    sys.exit()

            
            self.scene.play(self)
            

            # Update the pygame window
            pygame.display.update()

# If this Python file is run directly
if __name__ == "__main__":
    # Instanciate a new Application class with the parameters '800' and '650'
    game = Application(1080, 960)
