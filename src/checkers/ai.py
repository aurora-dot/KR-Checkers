import copy
from .player import Player
from math import inf


class Ai(Player):
    depth = 1
    level = 1

    def __init__(self, type, board, game) -> None:
        super().__init__(type, board, game)

    def select_piece(self, tile_location):
        self.started = True

        new_board = copy.deepcopy(self.board)
        new_board.pieces = copy.deepcopy(self.board.pieces)

        self.minmax(1, copy.deepcopy(new_board), self.depth, -inf, inf)

        self.selected_piece = (
            self.move[0][0],
            self.move[0][1],
            self.board.pieces[self.move[0][0]][self.move[0][1]],
        )

        return True

    def select_level(self, level):
        if level in [1, 2, 3]:
            if level == 1:
                self.depth = 1
            elif level == 2:
                self.depth = 3
            elif level == 3:
                self.depth = 6
            self.level = level
            return True

        return False

    def minmax(self, turn, board, depth, alpha, beta):
        if depth == 0 or self.game.finished(board) is not None:
            return self.game.calculate_heuristic(board)
        else:
            self.game.generate_moves_for_board(board)

            # Human turn
            if turn == 0:
                human_moves = [
                    [from_loc, to_loc]
                    for from_loc, data in board.human_move_set.items()
                    for to_loc in data["moves"]
                ]

                max_score = -inf
                for move in human_moves:
                    p_row, p_col = move[0]
                    n_row, n_col = move[1]

                    new_board = copy.deepcopy(self.board)
                    new_board.pieces = copy.deepcopy(self.board.pieces)

                    valid = self.ai_place_piece(
                        (n_row, n_col),
                        new_board,
                        (p_row, p_row, new_board.pieces[p_row][p_col]),
                    )

                    if valid:
                        score = self.minmax(
                            1, new_board, depth - 1, alpha, beta
                        )
                    else:
                        score = -inf

                    max_score = max(score, max_score)
                    alpha = max(alpha, score)
                    if beta <= alpha:
                        break

                return max_score

            # AI turn
            elif turn == 1:
                ai_moves = [
                    [from_loc, to_loc]
                    for from_loc, data in board.ai_move_set.items()
                    for to_loc in data["moves"]
                ]

                min_score = inf
                for move in ai_moves:
                    p_row, p_col = move[0]
                    n_row, n_col = move[1]

                    new_board = copy.deepcopy(self.board)
                    new_board.pieces = copy.deepcopy(self.board.pieces)

                    valid = self.ai_place_piece(
                        (n_row, n_col),
                        new_board,
                        (p_row, p_row, new_board.pieces[p_row][p_col]),
                    )

                    if valid:
                        score = self.minmax(
                            0, new_board, depth - 1, alpha, beta
                        )
                    else:
                        score = inf
                    if score < min_score and self.depth == depth:
                        self.move = move
                    min_score = min(score, min_score)
                    beta = min(beta, score)
                    if beta <= alpha:
                        break

                return min_score

    def ai_place_piece(self, tile_location, board, selected_piece):
        piece = selected_piece[2]
        location = selected_piece[0:2]

        if tile_location in piece.moves:
            board.move_piece(location, tile_location)
            if tile_location in piece.king_moves:
                piece.king = True
            if tile_location in piece.captures:

                captured_location = piece.captures[tile_location]
                board.remove_piece(captured_location)

            self.game.generate_moves_for_board(board)

            return True

        return False
