import copy
from time import sleep
from .player import Player
from math import inf


class Ai(Player):
    depth = 3
    level = 3
    not_started = True

    def __init__(self, type, board, game) -> None:
        super().__init__(type, board, game)

    def select_piece(self, tile_location):
        self.not_started = False
        print("og:")
        print(self.board)

        self.new_board = self.minmax(
            1, copy.deepcopy(self.board), self.depth, -inf, inf
        )
        # self.selected_piece = (
        #     self.selected_piece[0],
        #     self.selected_piece[1],
        #     self.selected_piece[2],
        # )

        print("new:")
        print(self.new_board)
        sleep(400)
        return True

    def select_level(self, level):
        if level in [1, 2, 3]:
            if level == 1:
                self.depth = 5
            elif level == 2:
                self.depth = 20
            elif level == 3:
                self.depth = 50
            self.level = level
            return True

        return False

    def minmax(self, turn, board, depth, alpha, beta):
        if depth == 0 or self.game.finished(board) is not None:
            return self.game.calculate_heuristic(board)
        else:

            new_board = copy.deepcopy(board)
            self.game.generate_moves_for_board(new_board)

            # Human turn
            if turn == 0:
                human_moves = [
                    [from_loc, to_loc]
                    for from_loc, data in new_board.human_move_set.items()
                    for to_loc in data["moves"]
                ]

                print("h: ", human_moves)

                max_score = -inf
                for move in human_moves:
                    print("h move: ", move)
                    p_row, p_col = move[0]
                    n_row, n_col = move[1]

                    self.place_piece(
                        (n_row, n_col),
                        new_board,
                        (p_row, p_row, new_board.pieces[p_row][p_col]),
                    )
                    score = self.minmax(1, new_board, depth - 1, alpha, beta)

                    new_board = copy.deepcopy(board)
                    max_score = max(score, max_score)
                    alpha = max(alpha, score)
                    if beta <= alpha:
                        break

                return max_score

            # AI turn
            elif turn == 1:
                ai_moves = [
                    [from_loc, to_loc]
                    for from_loc, data in new_board.ai_move_set.items()
                    for to_loc in data["moves"]
                ]

                print("a: ", ai_moves)

                min_score = inf
                for move in ai_moves:
                    print("a move: ", move)

                    p_row, p_col = move[0]
                    n_row, n_col = move[1]

                    self.place_piece(
                        (n_row, n_col),
                        new_board,
                        (p_row, p_row, new_board.pieces[p_row][p_col]),
                    )
                    score = self.minmax(0, new_board, depth - 1, alpha, beta)

                    new_board = copy.deepcopy(board)
                    max_score = min(score, min_score)
                    beta = min(beta, score)
                    if beta <= alpha:
                        break

                return max_score
