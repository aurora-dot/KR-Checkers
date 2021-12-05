from cmath import pi
from .ai import Ai
from .board import Board
from .human import Human


class Game:
    def __init__(self) -> None:
        self.start_new_game()

    def start_new_game(self):
        self.selected_piece = None
        self.turn = 0
        self.board = Board()
        self.human = Human(0, self.board, self)
        self.ai = Ai(1, self.board, self)
        self.players = [self.human, self.ai]

    def take_turn(self, tile_location):
        if not self.selected_piece:
            self.players[self.turn].select_piece(tile_location)
        elif self.selected_piece[0:2] == tile_location:
            self.selected_piece = None
        else:
            self.players[self.turn].place_piece(tile_location)
            # self.turn = 1 if self.turn == 0 else 0

    def calculate_heuristic(self):
        total, human, ai = (0, 0, 0)
        print(total, human, ai)

    def validate_move(self, piece, piece_location, tile_location):
        row, col = tile_location

        if row < 8 and col < 8 and self.board.board[row][col] == 1:
            if (
                piece_location == (row + 1, col + 1)
                or piece_location == (row + 1, col - 1)
                or piece_location == (row - 1, col + 1)
                or piece_location == (row - 1, col - 1)
            ):
                if not self.board.pieces[row][col] or (
                    self.board.pieces[row][col]
                    and self.board.pieces[row][col].type != piece.type
                ):
                    if not piece.king:
                        if (
                            piece.type == 0 and row < self.selected_piece[0]
                        ) or (
                            piece.type == 1 and row > self.selected_piece[0]
                        ):
                            if (piece.type == 0 and row == 0) or (
                                piece.type == 1 and row == 7
                            ):
                                return True, True

                            return True, False
                    else:
                        return True, False

        return False, False

    def validate_move(self, piece, piece_location, tile_location):
        og_row, og_col = piece_location
        row, col = tile_location

        # Checks if board tile is black, 
        #   that the piece is not counted as an option 
        #   and that you cannot land on pieces
        if (
            row < 8
            and col < 8
            and self.board.board[row][col] == 1
            and self.board.pieces[row][col]
            != self.board.pieces[og_row][og_col]
            and (not self.board.pieces[row][col])
        ):
            print("yes")

            # For white as example
            # if blank square above you can move but only one above
            #   or black square past token diagonally above you can move and take piece, two above
            #   can't jump over your own piece
            # if king, do above but can move backwards or forward
            # if opposite side takes king the token becomes king
            # if reached other side, token become king

            return True, False, (row, col)
        else:
            print("no")
            return False, False, None

    def all_valid_moves_for_piece(self, piece_location):
        valid_moves = []
        row, col = piece_location
        for i in range(row - 2, row + 3, 1):
            for j in range(col - 2, col + 3, 1):

                # when in corner of bounding box check if red is next to it to see if it should be counted
                # can't jump to ''i == row - 2 & j == col - 2'' if  ''i == row - 1 & j == col - 1''
                # i == row - 2 & j == col + 2
                # i == row + 2 & j == col - 2
                # i == row + 2 & j == col + 2

                # find all possibilities, 

                print(i, j)
                is_valid, made_king, to = self.validate_move(
                    self.selected_piece[2], self.selected_piece[0:2], (i, j)
                )
                if is_valid:
                    print("h : ", to)
                    valid_moves.append(to)

        return valid_moves

    def finished(self) -> int or None:
        # if opponent has no legal moves or no remaining pieces they have won,
        # draw if neither side has a legal move
        if self.board.red_remaining <= 0:
            return 0
        elif self.board.white_remaining <= 0:
            return 1
        else:
            return None
