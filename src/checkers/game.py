from .ai import Ai
from .board import Board
from .human import Human

# from random import choice as r_choice


class Game:
    def __init__(self) -> None:
        self.start_new_game()

    def start_new_game(self):
        self.valid_moves = {}
        self.selected_piece = None
        self.turn = 0  # r_choice([0, 1])
        self.board = Board()
        self.human = Human(0, self.board, self)
        self.ai = Ai(1, self.board, self)

    def start(self, starting_turn) -> None:
        pass

    def take_turn(self, tile_location):
        if self.turn == 0:
            if not self.selected_piece:
                self.human.select_piece(tile_location)
            elif self.selected_piece[0:2] == tile_location:
                self.selected_piece = None
            else:
                self.human.place_piece(tile_location)

    def validate_move(self, move):
        print("bruh sound #2")

        ################################################
        # Validate move flow                           #
        ################################################
        # Human class stores the valid moves and piece #
        # Person clicks piece,                         #
        #   Human class checks if the selected piece   #
        #   has valid moves                            #
        # Person clicks tile                           #
        #   Human class moves the piece to the tile    #
        ################################################

    def all_valid_moves(self):
        print("bruh sound #3")

    def finished(self) -> int or None:
        if self.board.red_remaining <= 0:
            return 0
        elif self.board.white_remaining <= 0:
            return 1
        else:
            return None
