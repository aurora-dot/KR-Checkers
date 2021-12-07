class Piece:
    king = False
    moves = []
    king_moves = []
    captures = []
    jumps = []

    def __init__(self, type: int) -> None:
        self.type = type
        self.colour = "R" if type == 0 else "W"

    def make_king(self) -> None:
        self.king = True

    def __str__(self) -> str:
        return self.colour
