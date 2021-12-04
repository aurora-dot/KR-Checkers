from .game import Game
import pygame
from pygame import gfxdraw
import os


class Gui:
    colours = {
        "R": (255, 85, 85),
        "W": (248, 248, 242),
        "black": (40, 42, 54),
        "red": (255, 85, 85),
        "pink": (255, 121, 198),
        "orange": (255, 184, 108),
    }

    def __init__(self, window) -> None:
        self.window = window
        self.checkers = Game()

    def update_window(self) -> None:
        self.draw_board()
        self.draw_pieces()
        self.draw_valid_moves()
        self.draw_side_bar()
        pygame.display.update()

    def draw_board(self) -> None:
        self.window.fill(self.colours["black"])

        for row in range(8):
            for col in range(row % 2, 8, 2):
                rectangle_dimensions = (row * 100, col * 100, 100, 100)
                pygame.draw.rect(
                    self.window, self.colours["red"], rectangle_dimensions
                )

    def draw_pieces(self) -> None:
        for row in range(8):
            for col in range(8):
                piece = self.checkers.board.pieces[row][col]
                if piece:
                    # Piece radius
                    radius = (100 // 2) - 14

                    # Piece position
                    piece_x = (100 * col) + (100 // 2)
                    piece_y = (100 * row) + (100 // 2)

                    if (
                        not self.checkers.selected_piece
                        or (row, col) != self.checkers.selected_piece[0:2]
                    ):
                        # Pink circle outline
                        self.draw_circle(
                            self.window,
                            piece_x,
                            piece_y,
                            radius + 4,
                            self.colours["pink"],
                        )
                    elif (row, col) == self.checkers.selected_piece[0:2]:
                        # Pink circle outline
                        self.draw_circle(
                            self.window,
                            piece_x,
                            piece_y,
                            radius + 4,
                            self.colours["orange"],
                        )

                    # Piece center colour
                    self.draw_circle(
                        self.window,
                        piece_x,
                        piece_y,
                        radius,
                        self.colours[piece.colour],
                    )

                    if piece.king:
                        # Piece center colour
                        self.draw_circle(
                            self.window,
                            piece_x,
                            piece_y,
                            radius - 17,
                            self.colours["black"],
                        )

                        f = pygame.font.Font(
                            os.path.dirname(__file__) + "/resources/font.ttf",
                            32,
                        )
                        self.window.blit(
                            f.render("K", True, self.colours["orange"]),
                            (piece_x - 10, piece_y - 20),
                        )

    def draw_valid_moves(self) -> None:
        pass

    def draw_side_bar(self) -> None:
        # Make side bar white
        rectangle_dimensions = (800, 0, 200, 800)
        pygame.draw.rect(self.window, self.colours["W"], rectangle_dimensions)

        # Create button to show help menu

        # Log text of what happens maybe?

    @staticmethod
    def convert_x_y_to_row_col(pos):
        x, y = pos
        return (y // 100, x // 100)

    @staticmethod
    def draw_circle(surface, x, y, radius, colour):
        gfxdraw.aacircle(surface, x, y, radius, colour)
        gfxdraw.filled_circle(surface, x, y, radius, colour)
