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

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()

                if pos[0] <= 800:
                    row, col = gui.get_mouse_row_col(pos)
                    print(row, col)

                    if not gui.checkers.selected_piece:
                        gui.checkers.select_piece(row, col)
                    else:
                        gui.checkers.place_piece(row, col)

                elif pos[0] > 800:
                    print("Side menu")

        gui.update_window()


main()
