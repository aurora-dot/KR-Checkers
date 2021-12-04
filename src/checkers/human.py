from .player import Player


class Human(Player):
    selected_piece = None

    def __init__(self, side, board) -> None:
        super().__init__(side, board)

    def select_piece(self, tile_location):
        row, col = tile_location
        print("hit 1")
        if (
            self.board.pieces[row][col]
            and self.board.pieces[row][col].type == 0
        ):
            # check that there are possible valid moves
            #   e.g., all row in line ahead is full
            # display possible valid moves
            self.selected_piece = (row, col, self.board.pieces[row][col])
            print(self.selected_piece)
            print("Selected")

    def place_piece(self, tile_location):
        row, col = tile_location
        if self.board.board[row][col] == 1:
            if (
                self.board.pieces[row][col]
                and self.board.pieces[row][col].type == 0
            ):
                print("bad")
            if not self.board.pieces[row][col] or (
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
                    self.board.move_piece(self.selected_piece[0:2], (row, col))
                    self.selected_piece = None
                    print("King moved")
                    print("yay!")

    # def place_piece(self, tile_location):
    #     # Need to do proximity check etc
    #     row, col = tile_location
    #     print("hit 2")
    #     if self.board.board[row][col] == 1:
    #         if self.board.pieces[row][col]:
    #             if self.board.pieces[row][col].type == 0:
    #                 print("bad, not places")

    #             elif self.board.pieces[row][col] != 0:
    #                 print(row, self.selected_piece[0])
    #                 if (
    #                     not self.selected_piece[2].king
    #                     and row == self.selected_piece[0] - 1
    #                 ):
    #                     self.board.move_piece(
    #                         self.selected_piece[0:2], (row, col)
    #                     )
    #                     print("good, placed")
    #                     if row == 0:
    #                         self.selected_piece[2].king = True
    #                         print("Made piece king")
    #                     self.selected_piece = None
    #                 else:
    #                     self.board.move_piece(
    #                         self.selected_piece[0:2], (row, col)
    #                     )
    #                     print("King moved")
    #                     self.selected_piece = None

    #         # Can only move bottom up as a rule (top down for ai).
    #         # # TODO Above, fix this cos it broke
    #         # When reaches the top they will turn into a king
    #         #   so they can move back and forth.

    #         else:
    #             print(row, self.selected_piece[0])
    #             if (
    #                 not self.selected_piece[2].king
    #                 and row == self.selected_piece[0] - 1
    #             ):
    #                 self.board.move_piece
    #                   (self.selected_piece[0:2], (row, col))
    #                 print("rah, placed")
    #                 if row == 0:
    #                     self.selected_piece[2].king = True
    #                     print("Made piece king")
    #                 self.selected_piece = None
    #             else:
    #                 self.board.move_piece
    #                   (self.selected_piece[0:2], (row, col))
    #                 self.selected_piece = None
    #                 print("King moved")
