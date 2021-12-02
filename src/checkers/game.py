import pygame
from .board import Board
from random import choice as r_choice


class Game:
    def __init__(self, window) -> None:
        self.window = window
        self.board = Board()
        self.turn = r_choice(["R", "W"])

    def update_window(self):
        self.draw_board()
        self.draw_pieces()
        self.draw_valid_moves()
        pygame.display.update()

    def draw_board(self):
        pass

    def draw_pieces(self):
        pass

    def draw_valid_moves(self):
        pass
