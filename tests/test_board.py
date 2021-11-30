import unittest
from src.board import Board


class MyTestCase(unittest.TestCase):
    def test_something(self):
        board = Board()
        for row in range(len(board.board)):
            for col in range(len(board.board[0])):
                print(board.board[row][col], end=' ')
            print()
   

if __name__ == '__main__':
    unittest.main()
