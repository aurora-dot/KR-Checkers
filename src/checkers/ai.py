from .player import Player
from math import inf


class Ai(Player):
    depth = 10
    level = 1

    def __init__(self, type, board, game) -> None:
        super().__init__(type, board, game)

    def select_piece(self, tile_location):
        self.selected_piece, self.next_location = self.minmax(
            self.game.turn, self.board, self.depth, -inf, inf
        )
        self.selected_piece = (
            self.selected_piece[0],
            self.selected_piece[1],
            self.selected_piece[2],
        )
        return True

    def select_level(self, level):
        if level == 1:
            self.level = level
            self.depth = 10
            return True
        elif level == 2:
            self.level = level
            self.depth = 25
            return True
        elif level == 3:
            self.level = level
            self.depth = 50
            return True
        return False

    def minmax(self, turn, board, depth, alpha, beta):
        pass
