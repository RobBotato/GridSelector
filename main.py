import pygame
from settings import *


class Tiles:

    def __init__(self):
        self.pos = pygame.mouse.get_pos()
        self.row = self.pos[1] // size
        self.col = self.pos[0] // size
        self.pixel = pygame.Rect((self.col * size, self.row * size), (size, size))

    def drawTiles(self, WIN):
        for x in range(0, WIDTH, size):
            for y in range(0, HEIGHT, size):
                square = pygame.Rect(x, y, size, size)
                pygame.draw.rect(WIN, LIGHT_GRAY, square, 1)

    def drawSelector(self, WIN):
        WIN.blit(pygame.transform.scale(pygame.image.load('assets/selector.png'),(size, size)), self.pixel)

    def draw(self, WIN):
        pygame.draw.rect(WIN, BLACK, (self.col * size, self.row * size, size, size))
  
    def update(self, WIN):
        self.drawTiles(WIN)
        self.drawSelector(WIN)


class Game:

    def __init__(self):
        pygame.init()
        self.WIN = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Pixels')
        self.clock = pygame.time.Clock()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
    
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.Tiles.draw(self.WIN)
            self.Tiles = Tiles()
            self.WIN.fill(WHITE)
            self.Tiles.update(self.WIN)

            pygame.display.flip()
            self.clock.tick(FPS)


if __name__ == '__main__':
    game = Game()
    game.run()