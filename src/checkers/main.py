import pygame
from sys import exit
from .gui import Gui

fps = 10
res = (1000, 800)
window = pygame.display.set_mode(res)
pygame.display.set_caption("K&R: Checkers!")


def main() -> None:
    play_game()


def play_game():
    pygame.init()

    playing = True
    clock = pygame.time.Clock()
    gui = Gui(window)
    gui.update_window()

    while playing:
        clock.tick(fps)

        f = gui.checkers.finished(
            gui.checkers.board,
            gui.checkers.all_ai_available_moves,
            gui.checkers.all_human_available_moves,
        )
        if f == -1:
            gui.win_screen("Draw", "orange")
        elif f == 0:
            gui.win_screen("Red wins", "R")
        elif f == 1:
            gui.win_screen("White wins", "W")

        if gui.checkers.turn == gui.checkers.players[1].type:
            gui.checkers.take_turn(None)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()

                if f is not None:
                    pygame.quit()
                    exit()
                elif (
                    pos[0] <= 800
                    and gui.checkers.turn == gui.checkers.players[0].type
                ):
                    gui.checkers.take_turn(gui.convert_x_y_to_row_col(pos))
                elif pos[0] > 800:
                    pass

        gui.update_window()


main()
