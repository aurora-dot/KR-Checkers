from .piece import Piece


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
                        self.pieces[row].append(Piece(1))
                        # self.pieces[row][-1].king = True
                        self.white_remaining += 1
                    elif row > 4:
                        self.pieces[row].append(Piece(0))
                        self.red_remaining += 1
                    else:
                        self.pieces[row].append(None)

                    self.board[row].append(1)

                else:
                    self.board[row].append(0)
                    self.pieces[row].append(None)

    def move_piece(self, piece_location, destination_location):
        piece_row, piece_col = piece_location
        destination_row, destination_col = destination_location

        piece = self.pieces[piece_row][piece_col]
        self.pieces[destination_row][destination_col] = piece
        self.pieces[piece_row][piece_col] = None
