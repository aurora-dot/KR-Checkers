import abc


class Player:
    selected_piece = None
    started = False
    move = None

    def __init__(self, type, board, game) -> None:
        self.type = type
        self.board = board
        self.game = game

    @abc.abstractmethod
    def select_piece(self, tile_location):
        """Select piece from board"""

    def place_piece(self, tile_location, board, selected_piece):
        self.started = False
        piece = selected_piece[2]
        location = selected_piece[0:2]

        # print(piece)
        # print(piece.moves)
        # print(piece.king_moves)
        # print(piece.captures)

        if tile_location in piece.moves:
            board.move_piece(location, tile_location)
            if tile_location in piece.king_moves:
                piece.king = True
            # if tile_location in piece.captures:
            #     captured_location = piece.captures[tile_location]
            #     board.remove_piece(captured_location)

            # Check for jumps here and make them maybe

            self.selected_piece = None
            self.game.generate_moves_for_board(board)

            print(board)

            return True

        return False
