from .player import Player


class Ai(Player):
    def __init__(self, side, board) -> None:
        super().__init__(side, board)
