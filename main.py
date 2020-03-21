# Import the 'pygame' module
import pygame
# Import the 'sys' module
import sys
# From the classes folder, import the module 'planet'
from classes import planet

# Create a new class called 'Application'
class Application:

    # The constructor function
    def __init__(self, width, height):
        # Assign the value 'windowWidth' to the class variable 'width'
        # Assign the value 'True' to the class variable 'running'
        self.running = True
        # Assign an empty dictionary to the class variable 'planetDict'
        self.planetDict = {}

        # Initialise pygame
        pygame.init()

        # Create a pygame window with the dimensions 'self.width' and 'self.height' and make the window hardware accelerated and double buffed
        self.display = pygame.display.set_mode(
            (self.width, self.height), pygame.HWSURFACE | pygame.DOUBLEBUF)

        # Set the title of the window to 'Raize'
        pygame.display.set_caption("Raize")

        # For 0 to 14
        for i in range(15):
            # Format Planet{i} -> Planet0 and assign the value to the variable 'key'
            key = f"Planet{i}"
            # Assign the instance of Planet to the variable 'value
            value = planet.Planet()
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
                planetObject.display(self.display)

            # Update the pygame window
            pygame.display.update()

# If this Python file is run directly
if __name__ == "__main__":
    # Instanciate a new Application class with the parameters '800' and '650'
    game = Application(800, 650)
