from .player import Player


class Ai(Player):
    piece_new_location = None
    level = 2

    def __init__(self, type, board, game) -> None:
        super().__init__(type, board, game)

    def select_piece(self, tile_location):
        selected_piece, self.piece_new_location = self.minmax(1, 0, 0)
        self.game.selected_piece = (
            selected_piece[0],
            selected_piece[1],
            selected_piece[2],
        )
        return True

    def place_piece(self, tile_location):
        print(2)
        return True
