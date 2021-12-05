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
            self.game.selected_piece[
                2
            ].moves = self.game.all_valid_moves_for_piece(
                self.game.selected_piece[0:2]
            )

    def place_piece(self, tile_location):
        if tile_location in self.game.selected_piece[2].moves:
            self.board.move_piece(self.game.selected_piece[0:2], tile_location)
            # if made_king:
            #     self.game.selected_piece[2].king = True

            # Check for jumps here

            self.game.selected_piece = None
