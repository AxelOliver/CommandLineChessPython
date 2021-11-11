from app.pieces.piece import Piece
from colorama import *


class Knight(Piece):
    def __str__(self):
        if self.side == "W":
            return Style.BRIGHT + Fore.LIGHTWHITE_EX + "N" + Fore.RESET + Style.NORMAL
        else:
            return Style.BRIGHT + Fore.LIGHTBLACK_EX + "N" + Fore.RESET + Style.NORMAL

    def validate_move(self, start, end, board):
        # check that is correct L shape
        if (abs(start[0] - end[0]) == 2 and abs(start[1] - end[1]) == 1
                or abs(start[0] - end[0]) == 1 and abs(start[1] - end[1]) == 2):
            if board[end[0]][end[1]] is not None:
                if board[end[0]][end[1]].side != self.side:
                    return True, "Valid"
                else:
                    return False, "Can't take own piece"
            else:
                return True, "Valid"
        else:
            return False, "Incorrect movement for knight, Must be L shape"
