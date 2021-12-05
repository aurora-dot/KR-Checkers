from .player import Player


class Human(Player):
    def __init__(self, side, board, game) -> None:
        super().__init__(side, board, game)

    def select_piece(self, tile_location):
        row, col = tile_location
        if (
            self.board.pieces[row][col]
            and self.board.pieces[row][col].type == 0
        ):
            # check that there are possible valid moves
            #   e.g., all row in line ahead is full
            # Make piece active
            # display possible valid moves for piece
            #

            self.game.selected_piece = (row, col, self.board.pieces[row][col])

    def place_piece(self, tile_location):
        if self.game.validate_move(tile_location):
            self.board.move_piece(self.game.selected_piece[0:2], tile_location)
            self.game.selected_piece = None
