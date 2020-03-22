import pytmx

class Map:

    def __init__(self, file):
        self.tileData = pytmx.load_pygame(file, pixelalpha=True)
        self.tileWidth = self.tileData.tilewidth
        self.tileHeight = self.tileData.tileheight
        self.width = self.tileData.width * self.tileWidth
        self.height = self.tileData.height * self.tileHeight
        