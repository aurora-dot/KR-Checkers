from .ai import Ai
from .board import Board
from .human import Human
from random import choice as r_choice


class Game:
    valid_moves = {}

    def __init__(self) -> None:
        self.turn = r_choice([0, 1])

        self.board = Board()
        self.human = Human(0)
        self.ai = Ai(1)

        self.start(self.turn)

    def start(self, starting_turn) -> None:
        pass
