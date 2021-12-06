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
        self.all_valid_moves()

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
        og_row, og_col = piece_location
        row, col = tile_location

        # Checks if board tile is black,
        #   that the piece is not counted as an option
        #   and that you cannot land on pieces
        if (
            row < 8
            and row >= 0
            and col < 8
            and col >= 0
            and self.board.board[row][col] == 1
            and self.board.pieces[row][col]
            != self.board.pieces[og_row][og_col]
            and (not self.board.pieces[row][col])
        ):

            # For white as example
            # if blank square above you can move but only one above
            #   or black square past token diagonally
            #       above you can move and take piece, two above
            #   can't jump over your own piece (done)
            # if king, do above but can move backwards or forward
            # if opposite side takes king the token becomes king
            # if reached other side, token become king

            if not piece.king:
                if (piece.type == 0 and row < og_row) or (
                    piece.type == 1 and row > og_row
                ):
                    if (piece.type == 0 and row == 0) or (
                        piece.type == 1 and row == 7
                    ):
                        return True, True, (row, col)
                    else:
                        return True, False, (row, col)
                else:
                    return False, False, (row, col)
            else:
                return True, False, (row, col)

        else:
            return False, False, None

    def all_valid_moves_for_piece(self, row, col, piece):
        valid_moves = []
        king_creation_moves = []
        captures = {}

        for i in range(row - 2, row + 3, 1):
            for j in range(col - 2, col + 3, 1):
                if (
                    (i + 1) % 2 == j % 2
                    and i != row
                    and j != col
                    and i < 8
                    and i >= 0
                    and j < 8
                    and i >= 0
                ):

                    # Move filters
                    if (
                        (i == row + 2 and j == col + 2)
                        and self.board.pieces[row + 1][col + 1]
                        and self.board.pieces[row + 1][col + 1].type == piece
                    ):
                        # Bottom right, same side piece blocking
                        pass
                    elif (
                        (i == row - 2 and j == col + 2)
                        and self.board.pieces[row - 1][col + 1]
                        and self.board.pieces[row - 1][col + 1].type == piece
                    ):
                        # Top right, same side piece blocking
                        pass
                    elif (
                        (i == row + 2 and j == col - 2)
                        and self.board.pieces[row + 1][col - 1]
                        and self.board.pieces[row + 1][col - 1].type == piece
                    ):
                        # Bottom left, same side piece blocking
                        pass
                    elif (
                        (i == row - 2 and j == col - 2)
                        and self.board.pieces[row - 1][col - 1]
                        and self.board.pieces[row - 1][col - 1].type == piece
                    ):
                        # Top left, same side piece blocking
                        pass
                    elif (
                        i == row + 2 and j == col + 2
                    ) and not self.board.pieces[row + 1][col + 1]:
                        pass
                    elif (
                        i == row + 2 and j == col - 2
                    ) and not self.board.pieces[row + 1][col - 1]:
                        pass
                    elif (
                        i == row - 2 and j == col + 2
                    ) and not self.board.pieces[row - 1][col + 1]:
                        pass
                    elif (
                        i == row - 2 and j == col - 2
                    ) and not self.board.pieces[row - 1][col - 1]:
                        pass
                    else:
                        is_valid, made_king, to = self.validate_move(
                            piece,
                            (row, col),
                            (i, j),
                        )

                        if is_valid:
                            valid_moves.append(to)
                            has_captured, removed_piece = self.captured(to)

                            if made_king:
                                king_creation_moves.append(to)

                            if has_captured:
                                captures[to] = removed_piece

        return valid_moves, king_creation_moves

    def captured(self, move):
        return None, None

    def all_valid_moves(self):
        for i in range(8):
            for j in range(8):
                piece = self.board.pieces[i][j]
                if piece:
                    to, king_to = self.all_valid_moves_for_piece(
                        i, j, self.board.pieces[i][j]
                    )
                    piece.moves = to
                    piece.king_moves = king_to

    def finished(self) -> int or None:
        # if opponent has no legal moves or no remaining pieces they have won,
        # draw if neither side has a legal move
        if self.board.red_remaining <= 0:
            return 0
        elif self.board.white_remaining <= 0:
            return 1
        else:
            return None
