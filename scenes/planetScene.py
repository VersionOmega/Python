def play(game):
    # Loop through the key:value pairs in 'self.planetDict'
    for planetName, planetObject in game.planetDict.items():
        # Blit the planet on the window 'self.display'
        planetObject.blit(game.display)