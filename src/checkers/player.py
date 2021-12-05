import abc


class Player:
    def __init__(self, type, board, game) -> None:
        self.type = type
        self.board = board
        self.game = game

    def minmax(self, turn, alpha, beta):
        pass

    @abc.abstractmethod
    def select_piece(self, tile_location):
        """Select piece from board"""

    @abc.abstractmethod
    def place_piece(self, tile_location):
        """Place selected piece on board"""
