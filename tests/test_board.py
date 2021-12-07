import unittest
from src.checkers.board import Board


class MyTestCase(unittest.TestCase):
    def test_board_setup(self):
        # Init board
        board = Board()

        # Prints board
        print(board)

        # Tests board
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

        # Tests pieces
        for row in range(8):
            for col in range(8):
                if row < 3:
                    if board.board[row][col] == 1:
                        c = board.pieces[row][col].colour
                        self.assertEqual(c, "W")
                    else:
                        self.assertEqual(board.pieces[row][col], None)
                if row > 4:
                    if board.board[row][col] == 1:
                        c = board.pieces[row][col].colour
                        self.assertEqual(c, "R")
                    else:
                        self.assertEqual(board.pieces[row][col], None)

        # Tests remaining
        self.assertEqual(board.white_remaining, 12)
        self.assertEqual(board.red_remaining, 12)


if __name__ == "__main__":
    unittest.main()
