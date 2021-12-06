from .player import Player


class Human(Player):
    def __init__(self, type, board, game) -> None:
        super().__init__(type, board, game)

    def select_piece(self, tile_location):
        row, col = tile_location
        piece = self.board.pieces[row][col]
        if piece and piece.type == self.type:
            self.game.selected_piece = (row, col, self.board.pieces[row][col])

    def place_piece(self, tile_location):
        piece = self.game.selected_piece[2]
        location = self.game.selected_piece[0:2]

        if tile_location in piece.moves:
            self.board.move_piece(location, tile_location)
            if tile_location in piece.king_moves:
                piece.king = True

            # Check for jumps here and make them maybe

            self.game.selected_piece = None
            self.game.all_valid_moves()

            return True

        return False
