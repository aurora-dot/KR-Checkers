import unittest
from src.checkers.board import Board


class MyTestCase(unittest.TestCase):
    def test_something(self):
        board = Board()

        for row in range(len(board.board)):
            for col in range(len(board.board[0])):
                if board.pieces[row][col]:
                    print(board.pieces[row][col], end=" ")
                else:
                    print(board.board[row][col], end=" ")
            print()

        self.assertEqual(
            board.board,
            [
                [0, 1, 0, 1, 0, 1, 0, 1],
                [1, 0, 1, 0, 1, 0, 1, 0],
                [0, 1, 0, 1, 0, 1, 0, 1],
                [1, 0, 1, 0, 1, 0, 1, 0],
                [0, 1, 0, 1, 0, 1, 0, 1],
                [1, 0, 1, 0, 1, 0, 1, 0],
                [0, 1, 0, 1, 0, 1, 0, 1],
                [1, 0, 1, 0, 1, 0, 1, 0],
            ],
        )


if __name__ == "__main__":
    unittest.main()
