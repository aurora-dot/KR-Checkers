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
            self.selected_piece = (row, col, self.board.pieces[row][col])
            print(self.selected_piece)
            print("Selected")

    def place_piece(self, tile_location):
        # Need to do proximity check etc
        row, col = tile_location
        print("hit 2")
        if self.board.board[row][col] == 1:
            if self.board.pieces[row][col]:
                if self.board.pieces[row][col].type == 0:
                    print("bad, not places")

                elif self.board.pieces[row][col] != 0:
                    print("good, placed")
                    self.board.move_piece(self.selected_piece[0:2], (row, col))
                    self.selected_piece = None

            else:
                print("placed, rahh")
                self.board.move_piece(self.selected_piece[0:2], (row, col))
                self.selected_piece = None
