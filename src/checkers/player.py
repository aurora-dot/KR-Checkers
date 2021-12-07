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

    def place_piece(self, tile_location):
        piece = self.game.selected_piece[2]
        location = self.game.selected_piece[0:2]

        if tile_location in piece.moves:
            self.board.move_piece(location, tile_location)
            if tile_location in piece.king_moves:
                piece.king = True
            if tile_location in piece.captures:
                captured_location = piece.captures[tile_location]
                self.board.remove_piece(captured_location)

            # Check for jumps here and make them maybe

            self.game.selected_piece = None
            self.game.all_valid_moves(self.board)

            return True

        return False
