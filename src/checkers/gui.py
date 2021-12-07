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
        "green": (80, 250, 123),
    }

    def __init__(self, window) -> None:
        self.window = window
        self.checkers = Game()

    def update_window(self) -> None:
        if (
            self.checkers.finished(
                self.checkers.board,
                self.checkers.board.all_human_available_moves,
                self.checkers.board.all_ai_available_moves,
            )
            is None
        ):
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
                        not self.checkers.human.selected_piece
                        or (row, col)
                        != self.checkers.human.selected_piece[0:2]
                    ):
                        # Pink circle outline
                        self.draw_circle(
                            self.window,
                            piece_x,
                            piece_y,
                            radius + 4,
                            self.colours["pink"],
                        )
                    elif (row, col) == self.checkers.human.selected_piece[0:2]:
                        # Orange circle outline
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
        if self.checkers.turn == 0:
            if self.checkers.human.selected_piece:
                moves = self.checkers.human.selected_piece[2].moves
            else:
                available_moves = self.checkers.board.all_human_available_moves
                moves = [
                    move
                    for key in available_moves.keys()
                    for move in available_moves[key]["moves"]
                ]

            radius = (100 // 2) - 14
            for move in moves:
                row, col = move

                piece_x = (100 * col) + (100 // 2)
                piece_y = (100 * row) + (100 // 2)

                self.draw_circle(
                    self.window,
                    piece_x,
                    piece_y,
                    radius + 4,
                    self.colours["green"],
                )

                self.draw_circle(
                    self.window,
                    piece_x,
                    piece_y,
                    radius,
                    self.colours[self.checkers.board.pieces[row][col].colour]
                    if self.checkers.board.pieces[row][col]
                    else self.colours["black"],
                )

    def win_screen(self, text, colour_str):
        self.window.fill(self.colours["black"])
        bf = pygame.font.Font(
            os.path.dirname(__file__) + "/resources/font.ttf",
            32,
        )

        sf = pygame.font.Font(
            os.path.dirname(__file__) + "/resources/font.ttf",
            10,
        )

        bf_render = bf.render(text, True, self.colours[colour_str])
        sf_render = sf.render("Click to exit", True, self.colours["green"])

        self.window.blit(
            bf_render,
            bf_render.get_rect(center=self.window.get_rect().center),
        )

        center_sf_render = sf_render.get_rect(
            center=self.window.get_rect().center
        )

        self.window.blit(
            sf_render,
            (center_sf_render[0], center_sf_render[1] + 35),
        )

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
