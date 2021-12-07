from .player import Player


class Human(Player):
    def __init__(self, type, board, game) -> None:
        super().__init__(type, board, game)

    def select_piece(self, tile_location):
        row, col = tile_location
        piece = self.board.pieces[row][col]
        if piece and piece.type == self.type:
            self.selected_piece = (row, col, self.board.pieces[row][col])
