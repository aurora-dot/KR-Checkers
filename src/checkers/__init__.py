import pygame
from .game import Game
from sys import exit

FPS = 60
WINDOW = pygame.display.set_mode((800, 800))


def main() -> None:
    playing = True
    clock = pygame.time.Clock()
    game = Game()

    while playing:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
