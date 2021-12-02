class Piece:
    king = False

    def __init__(self, type: int) -> None:
        self.type = type
        self.colour = "W" if type == 0 else "R"

    def make_king(self) -> None:
        self.king = True

    def __str__(self) -> str:
        return self.colour
