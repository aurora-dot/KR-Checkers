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
            # check that there are possible valid moves
            #   e.g., all row in line ahead is full
            # Make piece active
            # display possible valid moves for piece
            #

            self.game.selected_piece = (row, col, self.board.pieces[row][col])

    def place_piece(self, tile_location):
        is_valid, made_king = self.game.validate_move(
            self.game.selected_piece[2],
            self.game.selected_piece[0:2],
            tile_location,
        )
        if is_valid:
            self.board.move_piece(self.game.selected_piece[0:2], tile_location)
            if made_king:
                self.game.selected_piece[2].king = True

            # Check for jumps here

            self.game.selected_piece = None
