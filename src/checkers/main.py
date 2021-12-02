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
    gui.update_window()

    while playing:
        clock.tick(fps)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()

                if pos[0] <= 800:
                    tile_location = gui.get_mouse_row_col(pos)
                    print(tile_location)

                    if not gui.checkers.selected_piece:
                        gui.checkers.select_piece(tile_location)

                        # Hover thingy to show where
                        # location of piece will be moved to

                        # Show valid moves only for the selected piece

                    else:
                        gui.checkers.place_piece(tile_location)

                    gui.update_window()

                elif pos[0] > 800:
                    print("Side menu")
                    gui.update_window()


main()
