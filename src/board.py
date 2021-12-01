from src.piece import Piece


class Board:
    board = []
    pieces = []
    white_remaining = 0
    red_remaining = 0

    def __init__(self) -> None:
        self.setup_board()

    def setup_board(self) -> None:
        for row in range(8):
            self.board.append([])
            self.pieces.append([])

            for col in range(8):
                if (row + 1) % 2 == col % 2:
                    if row < 3:
                        self.pieces[row].append(Piece(0, row, col))
                        self.white_remaining += 1
                    elif row > 4:
                        self.pieces[row].append(Piece(1, row, col))
                        self.red_remaining += 1
                    else:
                        self.pieces[row].append(None)

                    self.board[row].append(1)

                else:
                    self.board[row].append(0)
                    self.pieces[row].append(None)
    
    def get_piece(self, row, col):
        return self.pieces[row][col]

