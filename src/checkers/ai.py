import copy
from time import sleep
from .player import Player
from math import inf


class Ai(Player):
    depth = 50
    level = 3

    def __init__(self, type, board, game) -> None:
        super().__init__(type, board, game)

    def select_piece(self, tile_location):
        print("og:")
        print(self.board)

        self.new_board = self.minmax(
            self.game.turn, self.board, self.depth, -inf, inf
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
            print("--- Reached max depth or finished ---")
            print(depth)
            print(self.game.finished(board))
            print(self.game.calculate_heuristic(board))
            return self.game.calculate_heuristic(board)
        else:

            # Human turn
            if turn == 0:
                self.game.generate_moves_for_board(board)
                human_moves = [
                    [from_loc, to_loc]
                    for from_loc, data in board.human_move_set.items()
                    for to_loc in data["moves"]
                ]
                print(human_moves)

                max_eval = -inf
                for move in human_moves:
                    p_row, p_col = move[0]
                    n_row, n_col = move[1]

                    new_board = copy.deepcopy(board)
                    print("\n--- h turn ---")
                    print(new_board)
                    print(
                        (n_row, n_col),
                        (p_row, p_col, new_board.pieces[p_row][p_col]),
                    )
                    self.game.generate_moves_for_board(new_board)
                    if not new_board.pieces[p_row][p_col]:
                        print(human_moves)
                    self.place_piece(
                        (n_row, n_col),
                        new_board,
                        (p_row, p_col, new_board.pieces[p_row][p_col]),
                    )

                    self.game.generate_moves_for_board(new_board)
                    minmax_eval = self.minmax(
                        1, new_board, depth - 1, alpha, beta
                    )
                    print("yuh")
                    max_minmax_eval = max(max_eval, minmax_eval)
                    alpha = max(alpha, minmax_eval)
                    if beta <= alpha:
                        break

                return max_minmax_eval

            # AI turn
            elif turn == 1:
                self.game.generate_moves_for_board(board)
                ai_moves = [
                    [from_loc, to_loc]
                    for from_loc, data in board.ai_move_set.items()
                    for to_loc in data["moves"]
                ]
                print(ai_moves)

                min_eval = -inf
                for move in ai_moves:
                    p_row, p_col = move[0]
                    n_row, n_col = move[1]

                    new_board = copy.deepcopy(board)
                    print("\n --- a turn ---")
                    print(new_board)
                    print(
                        (n_row, n_col),
                        (p_row, p_col, new_board.pieces[p_row][p_col]),
                    )
                    self.game.generate_moves_for_board(new_board)
                    if not new_board.pieces[p_row][p_col]:
                        print(ai_moves)
                    self.place_piece(
                        (n_row, n_col),
                        new_board,
                        (p_row, p_col, new_board.pieces[p_row][p_col]),
                    )
                    self.game.generate_moves_for_board(new_board)
                    minmax_eval = self.minmax(
                        0, new_board, depth - 1, alpha, beta
                    )
                    print("bruh")
                    min_minmax_eval = min(min_eval, minmax_eval)
                    alpha = min(beta, minmax_eval)
                    if beta <= alpha:
                        break

                return min_minmax_eval
