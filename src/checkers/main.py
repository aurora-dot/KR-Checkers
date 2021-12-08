import pygame
from sys import exit
from .gui import Gui
from .instructions import instructions_thread


fps = 30
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

    thread = instructions_thread()

    while playing:
        clock.tick(fps)

        f = gui.checkers.finished(
            gui.checkers.board,
        )
        if f == -1:
            gui.win_screen("Draw", "orange")
        elif f == 0:
            gui.win_screen("Red wins", "R")
        elif f == 1:
            gui.win_screen("White wins", "W")

        if (
            gui.checkers.turn == gui.checkers.players[1].type
            and gui.checkers.players[1].started
            and gui.checkers.players[1].move
            and f is None
        ):
            gui.checkers.take_turn(gui.checkers.players[1].move[1])
        elif (
            gui.checkers.turn == gui.checkers.players[1].type
            and not gui.checkers.players[1].started
            and f is None
        ):
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
                    # Sidebar

                    if pos[0] >= 805 and pos[0] <= 995:
                        # Instructions

                        if pos[1] >= 7 and pos[1] <= 80:
                            thread.start()

                        # Easy
                        if pos[1] >= 95 and pos[1] <= 170:
                            gui.checkers.ai.select_level(1)

                        # Medium
                        if pos[1] >= 185 and pos[1] <= 260:
                            gui.checkers.ai.select_level(2)

                        # Hard
                        if pos[1] >= 275 and pos[1] <= 350:
                            gui.checkers.ai.select_level(3)

                        # Help
                        if pos[1] >= 365 and pos[1] <= 440:
                            gui.checkers.show_valid_moves = (
                                not gui.checkers.show_valid_moves
                            )

        gui.update_window()


main()
