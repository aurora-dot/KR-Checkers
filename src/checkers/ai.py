from .player import Player


class Ai(Player):
    def __init__(self, side, board, game) -> None:
        super().__init__(side, board, game)
