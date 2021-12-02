from .ai import Ai
from .board import Board
from .human import Human
from random import choice as r_choice


class Game:
    valid_moves = {}
    selected_piece = None

    def __init__(self) -> None:
        self.turn = r_choice([0, 1])
        self.board = Board()
        self.human = Human(0)
        self.ai = Ai(1)

        self.start(self.turn)

    def start(self, starting_turn) -> None:
        pass

    def select_piece(self, tile_location):
        row, col = tile_location
        pass

    def place_piece(self, tile_location):
        row, col = tile_location
        pass

    def finished(self) -> int or None:
        if self.board.red_remaining <= 0:
            return 0
        elif self.board.white_remaining <= 0:
            return 1
        else:
            return None
