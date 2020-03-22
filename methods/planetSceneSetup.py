# Import the 'pygame' module
import pygame
# Import the 'random' module
import random
# From the classes folder, import the module 'planet'
from classes import planet

def init(game):
    # Load the background image
    game.backgroundImage = pygame.image.load("art/background.png")
    # Change the background image's dimensions to match the size of the window
    game.backgroundImage = pygame.transform.scale(game.backgroundImage, (game.windowWidth, game.windowHeight))

    # Loop 2 to 20 times
    for i in range(random.randint(2,20)):
        # Format Planet{i} -> Planet0 and assign the value to the variable 'key'
        key = f"Planet{i}"
        # Assign the instance of Planet to the variable 'value
        value = planet.Planet(game)
        # Add the variable 'value' to the dictionary 'game.planetDict' with the key 'key'
        game.planetDict[key] = value