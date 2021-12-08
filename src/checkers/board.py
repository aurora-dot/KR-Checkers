from .piece import Piece


class Board:
    board = []
    pieces = []
    white_remaining = 0
    red_remaining = 0

    human_move_set = {}
    ai_move_set = {}

    all_human_moves = []
    all_ai_moves = []

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

    def remove_piece(self, captured_location):
        piece_row, piece_col = captured_location
        piece_type = self.pieces[piece_row][piece_col].type
        self.pieces[piece_row][piece_col] = None

        if piece_type == 0:
            self.white_remaining -= 1
        elif piece_type == 1:
            self.red_remaining -= 1

    def __str__(self) -> str:
        out = ""
        for row in range(len(self.board)):
            for col in range(len(self.board[0])):
                if self.pieces[row][col]:
                    out += str(self.pieces[row][col]) + " "
                else:
                    out += str(self.board[row][col]) + " "
            out += "\n"

        return out
