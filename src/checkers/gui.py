from .game import Game
import pygame


class Gui:
    colours = {
        "R": (220, 50, 50),
        "W": (248, 248, 242),
        "black": (40, 42, 54),
        "red": (255, 85, 85),
        "pink": (255, 121, 198),
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
        for row in self.checkers.board.pieces:
            for piece in row:
                if piece:
                    # Piece radius
                    radius = (100 // 2) - 15

                    # Piece position
                    piece_x = (100 * piece.col) + (100 // 2)
                    piece_y = (100 * piece.row) + (100 // 2)

                    # Pink circle outline
                    pygame.draw.circle(
                        self.window,
                        self.colours["pink"],
                        (piece_x, piece_y),
                        radius + 2,
                    )

                    # Piece center colour
                    pygame.draw.circle(
                        self.window,
                        self.colours[piece.colour],
                        (piece_x, piece_y),
                        radius,
                    )

                    if piece.king:
                        print("TODO: Add king logo in center")

    def draw_valid_moves(self) -> None:
        pass

    def draw_side_bar(self) -> None:
        # Make side bar white
        rectangle_dimensions = (800, 0, 200, 800)
        pygame.draw.rect(self.window, self.colours["W"], rectangle_dimensions)

        # Create button to show help menu

        # Log text of what happens maybe?
