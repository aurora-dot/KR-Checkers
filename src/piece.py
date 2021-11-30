class Piece:
    king = False

    def __init__(self, type: int, row: int, col: int):
        self.colour = "W" if type == 0 else "R"
        self.row = row
        self.col = col
    
    def make_king(self):
        self.king = True

    def __str__(self) -> str:
        return self.colour
    