import pygame
from sys import exit
from .gui import Gui


def main() -> None:
    fps = 60
    res = (1000, 800)
    window = pygame.display.set_mode(res)
    pygame.display.set_caption("K&R: Checkers!")

    playing = True
    clock = pygame.time.Clock()
    gui = Gui(window)

    while playing:
        clock.tick(fps)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        gui.update_window()


main()
