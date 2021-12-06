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
        self.all_human_available_moves = []
        (
            self.all_human_available_moves,
            self.all_ai_available_moves,
        ) = self.all_valid_moves()

    def take_turn(self, tile_location):
        if not self.selected_piece:
            self.players[self.turn].select_piece(tile_location)
        elif self.selected_piece[0:2] == tile_location:
            self.selected_piece = None
        else:
            valid = self.players[self.turn].place_piece(tile_location)
            if valid:
                (
                    self.all_human_available_moves,
                    self.all_ai_available_moves,
                ) = self.all_valid_moves()

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

            if not piece.king:
                if (piece.type == 0 and row < og_row) or (
                    piece.type == 1 and row > og_row
                ):
                    if (piece.type == 0 and row == 0) or (
                        piece.type == 1 and row == 7
                    ):
                        # format:
                        #   valid move,
                        #   king created,
                        #   move to tile location
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
                # Checks if i and j are within the bounds of the board,
                #   and only count the black squares
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
                    # Checks for friendly token blocks, can't jump over them
                    if (
                        (i == row + 2 and j == col + 2)
                        and self.board.pieces[row + 1][col + 1]
                        and self.board.pieces[row + 1][col + 1].type == piece
                    ):
                        # Friendly token blocking bottom right of token
                        pass
                    elif (
                        (i == row - 2 and j == col + 2)
                        and self.board.pieces[row - 1][col + 1]
                        and self.board.pieces[row - 1][col + 1].type == piece
                    ):
                        # Friendly token blocking top right of token
                        pass
                    elif (
                        (i == row + 2 and j == col - 2)
                        and self.board.pieces[row + 1][col - 1]
                        and self.board.pieces[row + 1][col - 1].type == piece
                    ):
                        # Friendly token blocking bottom left of token
                        pass
                    elif (
                        (i == row - 2 and j == col - 2)
                        and self.board.pieces[row - 1][col - 1]
                        and self.board.pieces[row - 1][col - 1].type == piece
                    ):
                        # Friendly token blocking top left of token
                        pass

                    # Removes jump tiles if no enemy piece is there
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
                        # Validates if the piece can
                        #   actually be moved to that spot
                        (
                            is_valid,
                            made_king,
                            move_location,
                        ) = self.validate_move(
                            piece,
                            (row, col),
                            (i, j),
                        )

                        if is_valid:
                            valid_moves.append(move_location)
                            has_captured, removed_piece = self.captured(
                                move_location
                            )

                            if made_king:
                                king_creation_moves.append(move_location)

                            if has_captured:
                                captures[move_location] = removed_piece

        return valid_moves, king_creation_moves

    def captured(self, move):
        # TODO: check if piece is captured,
        #   if opposite side takes king the token becomes king
        return None, None

    def all_valid_moves(self):
        all_human_available_moves = []
        all_ai_available_moves = []

        for i in range(8):
            for j in range(8):
                piece = self.board.pieces[i][j]
                if piece:
                    moves, king_moves = self.all_valid_moves_for_piece(
                        i, j, self.board.pieces[i][j]
                    )
                    piece.moves = moves
                    piece.king_moves = king_moves

                    if piece.type == self.human.type:
                        all_human_available_moves += moves
                    elif piece.type == self.ai.type:
                        all_ai_available_moves += moves

        return all_human_available_moves, all_ai_available_moves

    def finished(self) -> int or None:
        # if opponent has no legal moves or no remaining pieces they have won,
        # draw if neither side has a legal move
        if self.board.red_remaining <= 0:
            return 0
        elif self.board.white_remaining <= 0:
            return 1
        else:
            return None
