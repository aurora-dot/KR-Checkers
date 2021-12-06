from .player import Player


class Human(Player):
    def __init__(self, type, board, game) -> None:
        super().__init__(type, board, game)

    def select_piece(self, tile_location):
        row, col = tile_location
        if (
            self.board.pieces[row][col]
            and self.board.pieces[row][col].type == self.type
        ):
            self.game.selected_piece = (row, col, self.board.pieces[row][col])

    def place_piece(self, tile_location):
        if tile_location in self.game.selected_piece[2].moves:
            self.board.move_piece(self.game.selected_piece[0:2], tile_location)
            if tile_location in self.game.selected_piece[2].king_moves:
                self.game.selected_piece[2].king = True

            # Check for jumps here and make them maybe

            self.game.selected_piece = None
            self.game.all_valid_moves()
