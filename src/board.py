from src.piece import Piece

class Board:
    board = []
    pieces = []
    white_remaining = 12
    red_remaining = 12

    def __init__(self) -> None:
        self.setup_board()
        pass

    def setup_board(self):
        for row in range(8):
            self.board.append([])
            self.pieces.append([])
            for col in range(8):
                if (row + 1) % 2 == col % 2:
                    if row < 3:
                        self.pieces[row].append(Piece(0, row, col))
                    elif row > 4:
                        self.pieces[row].append(Piece(1, row, col))
                    else:
                        self.pieces[row].append(None)
                    
                    self.board[row].append(1)
                else:
                    self.board[row].append(0)
                    self.pieces[row].append(None)
