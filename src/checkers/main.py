import pygame
from sys import exit
from .game import Game

FPS = 60
WINDOW = pygame.display.set_mode((800, 800))


def main() -> None:
    playing = True
    clock = pygame.time.Clock()
    checkers = Game(WINDOW)

    while playing:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        checkers.update_window()


main()
