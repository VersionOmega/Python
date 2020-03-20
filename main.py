import pygame
import sys


class Application:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.running = True

        pygame.init()

        self.display = pygame.display.set_mode(
            (self.width, self.height), pygame.HWSURFACE | pygame.DOUBLEBUF)

        pygame.display.set_caption("RPG II")

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                    sys.exit()
                    print("penis2")

            pygame.display.update()


if __name__ == "__main__":
    game = Application(800, 650)
