from .player import Player


class Human(Player):
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

            self.game.selected_piece = (row, col, self.board.pieces[row][col])
            print(self.game.selected_piece)
            print("Selected")

    def place_piece(self, tile_location):
        row, col = tile_location
        if self.board.board[row][col] == 1:
            print("Bruh")
            print(self.game.selected_piece[0:2], (row + 1, col + 1))
            if (
                self.game.selected_piece[0:2] == (row + 1, col + 1)
                or self.game.selected_piece[0:2] == (row + 1, col - 1)
                or self.game.selected_piece[0:2] == (row - 1, col + 1)
                or self.game.selected_piece[0:2] == (row - 1, col - 1)
            ):

                if (
                    self.board.pieces[row][col]
                    and self.board.pieces[row][col].type
                    == self.game.selected_piece[2].type
                ):
                    print("bad")
                elif not self.board.pieces[row][col] or (
                    self.board.pieces[row][col]
                    and self.board.pieces[row][col].type
                    != self.game.selected_piece[2].type
                ):
                    print("okay-ish")
                    if not self.game.selected_piece[2].king:
                        print("Warmer")
                        if (
                            self.game.selected_piece[2].type == 0
                            and row < self.game.selected_piece[0]
                        ) or (
                            self.game.selected_piece[2].type == 1
                            and row > self.game.selected_piece[0]
                        ):
                            if (
                                self.game.selected_piece[2].type == 0
                                and row == 0
                            ) or (
                                self.game.selected_piece[2].type == 1
                                and row == 7
                            ):
                                self.game.selected_piece[2].king = True
                                print("Made piece king")

                            print("yay! but only forward")
                            self.board.move_piece(
                                self.game.selected_piece[0:2], (row, col)
                            )
                            self.game.selected_piece = None
                    else:
                        self.board.move_piece(
                            self.game.selected_piece[0:2], (row, col)
                        )
                        self.game.selected_piece = None
                        print("King moved")
                        print("yay!")
