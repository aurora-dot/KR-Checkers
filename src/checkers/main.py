import pygame
from sys import exit
from .gui import Gui


def main() -> None:
    pygame.init()

    fps = 10
    res = (1000, 800)
    window = pygame.display.set_mode(res)
    pygame.display.set_caption("K&R: Checkers!")

    playing = True
    clock = pygame.time.Clock()
    gui = Gui(window)
    gui.update_window()

    while playing:
        clock.tick(fps)

        if (
            gui.checkers.turn == gui.checkers.players[1].type
            and not gui.checkers.finished()
        ):
            gui.checkers.take_turn(None)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()

                if (
                    pos[0] <= 800
                    and gui.checkers.turn == gui.checkers.players[0].type
                    and not gui.checkers.finished()
                ):
                    gui.checkers.take_turn(gui.convert_x_y_to_row_col(pos))
                elif pos[0] > 800:
                    pass

        gui.update_window()


main()
