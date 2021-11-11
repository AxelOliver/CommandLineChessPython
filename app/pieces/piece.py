class Piece:
    def __init__(self, side, has_moved=False):
        self.side = side
        self.has_moved = has_moved

    def validate_move(self, start, end, board):
        pass
