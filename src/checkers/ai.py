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
        new_board = copy.deepcopy(board)
        (
            all_human_available_moves,
            all_ai_available_moves,
        ) = self.game.all_valid_moves(new_board)

        if depth == 0 or self.game.finished(
            new_board, all_human_available_moves, all_ai_available_moves
        ):
            return self.game.calculate_heuristic(new_board)

        # Human turn
        if turn == 0:
            max_eval = -inf
            print(max_eval)

        elif turn == 1:
            min_eval = -inf
            print(min_eval)
