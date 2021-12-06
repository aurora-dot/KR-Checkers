from .player import Player


class Ai(Player):
    def __init__(self, type, board, game) -> None:
        super().__init__(type, board, game)
        # Should be three levels of difficulty, 1, 2, 3
        self.level = 1

    def select_piece(self, tile_location):
        pass

    def place_piece(self, tile_location):
        pass
