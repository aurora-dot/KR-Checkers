from .player import Player


class Human(Player):
    selected_piece = None

    def __init__(self, side, board, game) -> None:
        super().__init__(side, board, game)

    def select_piece(self, tile_location):
        row, col = tile_location
        print("hit 1")
        if (
            self.board.pieces[row][col]
            and self.board.pieces[row][col].type == 0
        ):
            # check that there are possible valid moves
            #   e.g., all row in line ahead is full
            # Make piece active
            # display possible valid moves for piece
            #

            self.selected_piece = (row, col, self.board.pieces[row][col])
            print(self.selected_piece)
            print("Selected")

    def place_piece(self, tile_location):
        row, col = tile_location
        if self.board.board[row][col] == 1:
            print("Bruh")
            print(self.selected_piece[0:2], (row + 1, col + 1))
            if (
                self.selected_piece[0:2] == (row + 1, col + 1)
                or self.selected_piece[0:2] == (row + 1, col - 1)
                or self.selected_piece[0:2] == (row - 1, col + 1)
                or self.selected_piece[0:2] == (row - 1, col - 1)
            ):

                if (
                    self.board.pieces[row][col]
                    and self.board.pieces[row][col].type == 0
                ):
                    print("bad")
                elif not self.board.pieces[row][col] or (
                    self.board.pieces[row][col]
                    and self.board.pieces[row][col].type != 0
                ):
                    print("okay-ish")
                    if not self.selected_piece[2].king:
                        print("Warmer")
                        if row < self.selected_piece[0]:
                            if row == 0:
                                self.selected_piece[2].king = True
                                print("Made piece king")

                            print("yay! but only forward")
                            self.board.move_piece(
                                self.selected_piece[0:2], (row, col)
                            )
                            self.selected_piece = None
                    else:
                        self.board.move_piece(
                            self.selected_piece[0:2], (row, col)
                        )
                        self.selected_piece = None
                        print("King moved")
                        print("yay!")
