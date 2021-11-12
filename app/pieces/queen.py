from app.pieces.piece import Piece
from app.pieces.bishop import Bishop
from app.pieces.rook import Rook
from copy import deepcopy
from colorama import *


class Queen(Piece):
    def __str__(self):
        if self.side == "White":
            return Style.BRIGHT + Fore.LIGHTWHITE_EX + "Q" + Fore.RESET + Style.NORMAL
        else:
            return Style.BRIGHT + Fore.LIGHTBLACK_EX + "Q" + Fore.RESET + Style.NORMAL

    def validate_move(self, start, end, board):
        test_board = deepcopy(board)
        test_board.move([start, end])
        if Bishop.validate_move(Bishop(self.side), start, end, board)[0]:
            if (not Rook.validate_move(Rook(self.side), start, end, board)[0]
                    and Rook.validate_move(Rook(self.side), start, end, board)[1] == "Piece in the way"):
                return False, "Piece in the way"
            else:
                if not test_board.check(board.turn)[0]:
                    return True, "Valid"
                else:
                    return False, "That would put you in check"
        elif Rook.validate_move(Rook(self.side), start, end, board)[0]:
            if (not Bishop.validate_move(Bishop(self.side), start, end, board)[0]
                    and Bishop.validate_move(Bishop(self.side), start, end, board)[1] == "Piece in the way"):
                return False, "Piece in the way"
            else:
                if not test_board.check(board.turn)[0]:
                    return True, "Valid"
                else:
                    return False, "That would put you in check"
        else:
            return False, "Can't move there"


if __name__ == '__main__':
    queen = Queen("White")
    queen.validate_move([0, 1], [0, 6], "Board")
