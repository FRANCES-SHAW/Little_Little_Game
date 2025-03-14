import pygame
import sys
from settings import *
from level import Level

class Valley_Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1024, 640))
        pygame.display.set_caption("Sprout land")
        self.clock = pygame.time.Clock()
        self.level = Level()
        # self.running = True
        # self.load_data()
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            dt = self.clock.tick() / 1000
            self.level.run(dt)
            pygame.display.update()

if __name__ == "__main__":
    game = Valley_Game()
    game.run()