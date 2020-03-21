# Import the 'pygame' module
import pygame
# Import the 'sys' module
import sys
# Import the 'random' module
import random
# From the classes folder, import the module 'planet'
from classes import planet

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

        # For 0 to 14
        for i in range(random.randint(2,20)):
            # Format Planet{i} -> Planet0 and assign the value to the variable 'key'
            key = f"Planet{i}"
            # Assign the instance of Planet to the variable 'value
            value = planet.Planet(self)
            # Add the variable 'value' to the dictionary 'self.planetDict' with the key 'key'
            self.planetDict[key] = value

        # While 'self.running' is True
        while self.running:
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

            # Loop through the key:value pairs in 'self.planetDict'
            for planetName, planetObject in self.planetDict.items():
                # Blit the planet on the window 'self.display'
                planetObject.blit(self.display)

            # Update the pygame window
            pygame.display.update()

# If this Python file is run directly
if __name__ == "__main__":
    # Instanciate a new Application class with the parameters '800' and '650'
    game = Application(1080, 960)
