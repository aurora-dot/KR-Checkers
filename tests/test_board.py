import unittest
from src.board import Board
from src.piece import Piece


class MyTestCase(unittest.TestCase):
    def test_something(self):
        board = Board()
        for row in range(len(board.board)):
            for col in range(len(board.board[0])):
                if board.pieces[row][col]:
                    print(board.pieces[row][col], end=' ')
                else:
                    print(board.board[row][col], end=' ')
            print()
   

if __name__ == '__main__':
    unittest.main()
