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

            to, king_to = self.game.all_valid_moves_for_piece(self.game.selected_piece[0:2])
            self.game.selected_piece[
                2
            ].moves = to
            self.game.selected_piece[
                2
            ].king_moves = king_to

    def place_piece(self, tile_location):
        if tile_location in self.game.selected_piece[2].moves:
            self.board.move_piece(self.game.selected_piece[0:2], tile_location)
            if tile_location in self.game.selected_piece[2].king_moves:
                self.game.selected_piece[2].king = True

            # Check for jumps here maybe

            self.game.selected_piece = None
