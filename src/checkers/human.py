from .player import Player


class Human(Player):
    def __init__(self, side) -> None:
        super().__init__(side)
