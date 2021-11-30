

class Board:
    board = []
    board_size = 8
    white_remaining = 12
    red_remaining = 12

    def __init__(self) -> None:
        self.setup_board()
        pass

    def setup_board(self):
        for row in range(self.board_size):
            self.board.append([])
            for col in range(self.board_size):
                self.board[row].append(0)
                if row < 3:
                    print()
                if row > 4:
                    print()
        

