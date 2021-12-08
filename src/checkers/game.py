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
        self.generate_moves_for_board(self.board)

        # print("h: ", self.human_move_set)
        # print("a: ", self.ai_move_set)
        # print(self.calculate_heuristic(self.board))
        # print("---")

    def take_turn(self, tile_location):
        player = self.players[self.turn]

        if not player.selected_piece:
            player.select_piece(tile_location)
        elif player.selected_piece[0:2] == tile_location:
            player.selected_piece = None
        else:
            print(player.selected_piece, tile_location)
            valid = player.place_piece(
                tile_location, self.board, player.selected_piece
            )
            if valid:
                print("yay")
                self.turn = 0 if self.turn == 1 else 1

                # print("h: ", self.human_move_set)
                # print("a: ", self.ai_move_set)
                # print(self.calculate_heuristic(self.board))
                # print("---")

    def generate_moves_for_board(self, board: Board):
        (
            board.human_move_set,
            board.ai_move_set,
        ) = self.all_valid_moves(board)

        board.all_human_moves = self.move_set_to_all_move_array(
            board.human_move_set
        )
        board.all_ai_moves = self.move_set_to_all_move_array(board.ai_move_set)

    def move_set_to_all_move_array(self, move_set):
        return [
            move for key in move_set.keys() for move in move_set[key]["moves"]
        ]

    def calculate_heuristic(self, board: Board):
        scores = [0, 0]

        for row in range(8):
            for col in range(8):
                piece = board.pieces[row][col]

                if piece:
                    # Pieces
                    scores[piece.type] += 200

                    # King
                    if piece.king:
                        scores[piece.type] += 300
                        scores[1 if piece.type == 0 else 0] -= 300

                    # Backrow
                    if (piece.type == 0 and row == 7) or (
                        piece.type == 1 and row == 0
                    ):
                        scores[piece.type] += 50

        human_score, ai_score = scores
        return human_score - ai_score

    def validate_move(self, piece, piece_location, tile_location, board):
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
            and board.board[row][col] == 1
            and board.pieces[row][col] != board.pieces[og_row][og_col]
            and (not board.pieces[row][col])
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

    def all_valid_moves_for_piece(self, row, col, piece, board):
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
                    passed = True

                    # Move filters
                    # Checks for friendly token blocks, can't jump over them

                    if (
                        (i == row + 2 and j == col + 2)
                        and board.pieces[row + 1][col + 1]
                        and board.pieces[row + 1][col + 1].type == piece.type
                    ):
                        # Friendly token blocking bottom right of token
                        passed = False
                    if (
                        (i == row - 2 and j == col + 2)
                        and board.pieces[row - 1][col + 1]
                        and board.pieces[row - 1][col + 1].type == piece.type
                    ):
                        # Friendly token blocking top right of token
                        passed = False
                    if (
                        (i == row + 2 and j == col - 2)
                        and board.pieces[row + 1][col - 1]
                        and board.pieces[row + 1][col - 1].type == piece.type
                    ):
                        # Friendly token blocking bottom left of token
                        passed = False
                    if (
                        (i == row - 2 and j == col - 2)
                        and board.pieces[row - 1][col - 1]
                        and board.pieces[row - 1][col - 1].type == piece.type
                    ):
                        # Friendly token blocking top left of token
                        passed = False

                    # Removes jump tiles if no enemy piece is there
                    if (i == row + 2 and j == col + 2) and not board.pieces[
                        row + 1
                    ][col + 1]:
                        passed = False
                    if (i == row + 2 and j == col - 2) and not board.pieces[
                        row + 1
                    ][col - 1]:
                        passed = False
                    if (i == row - 2 and j == col + 2) and not board.pieces[
                        row - 1
                    ][col + 1]:
                        passed = False
                    if (i == row - 2 and j == col - 2) and not board.pieces[
                        row - 1
                    ][col - 1]:
                        passed = False

                    if passed:
                        # Validates if the piece can
                        #   actually be moved to that spot
                        (
                            is_valid,
                            made_king,
                            move_location,
                        ) = self.validate_move(
                            piece, (row, col), (i, j), board
                        )

                        if is_valid:
                            valid_moves.append(move_location)
                            has_captured, removed_piece = self.captured(
                                (row, col), move_location
                            )

                            if made_king:
                                king_creation_moves.append(move_location)

                            if has_captured:
                                captures[move_location] = removed_piece

        return valid_moves, king_creation_moves, captures

    def captured(self, piece_location, tile_location):
        # TODO: check if piece is captured,
        #   if opposite side takes king the token becomes king
        p_row, p_col = piece_location
        t_row, t_col = tile_location

        if p_row + 2 == t_row and p_col + 2 == t_col:
            return True, (p_row + 1, p_col + 1)
        elif p_row + 2 == t_row and p_col - 2 == t_col:
            return True, (p_row + 1, p_col - 1)
        elif p_row - 2 == t_row and p_col + 2 == t_col:
            return True, (p_row - 1, p_col + 1)
        elif p_row - 2 == t_row and p_col - 2 == t_col:
            return True, (p_row - 1, p_col - 1)
        else:
            return False, False

    def all_valid_moves(self, board):
        human_move_set = {}
        ai_move_set = {}

        for i in range(8):
            for j in range(8):
                piece = board.pieces[i][j]
                if piece:
                    (
                        moves,
                        king_moves,
                        captures,
                    ) = self.all_valid_moves_for_piece(
                        i, j, board.pieces[i][j], board
                    )
                    piece.moves = moves
                    piece.king_moves = king_moves
                    piece.captures = captures

                    if piece.type == self.human.type:
                        human_move_set[(i, j)] = {
                            "moves": moves,
                            "king_moves": king_moves,
                            "captures": captures,
                        }
                    elif piece.type == self.ai.type:
                        ai_move_set[(i, j)] = {
                            "moves": moves,
                            "king_moves": king_moves,
                            "captures": captures,
                        }

        return human_move_set, ai_move_set

    def finished(self, board) -> int or None:
        if board.all_ai_moves == [] and board.all_human_moves == []:
            return -1
        elif board.red_remaining <= 0 or board.all_ai_moves == []:
            return 0
        elif board.white_remaining <= 0 or board.all_human_moves == []:
            return 1
        else:
            return None
