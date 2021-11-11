from app.pieces.piece import Piece
from colorama import *


class Pawn(Piece):
    def __str__(self):
        if self.side == "W":
            return Style.BRIGHT + Fore.LIGHTWHITE_EX + "P" + Fore.RESET + Style.NORMAL
        else:
            return Style.BRIGHT + Fore.LIGHTBLACK_EX + "P" + Fore.RESET + Style.NORMAL

    def validate_move(self, start, end, board):
        # check that movement is in right direction
        if self.side == 'W' and start[0] - end[0] > 0 or self.side == 'B' and start[0] - end[0] < 0:
            # if is straight line
            if start[1] == end[1]:
                # if hasnt moved, can move 2 forward
                if not self.has_moved and abs(start[0] - end[0]) <= 2 or self.has_moved and abs(start[0] - end[0]) == 1:
                    if board[end[0]][end[1]] is not None:
                        return False, "Cant move straight onto another piece"
                    else:
                        return True, "Valid"
                else:
                    return False, "Can only move 1 space or 2 if first move"
            # if is moving diagonally
            elif abs(start[1] - end[1]) == 1:
                if abs(start[0] - end[0]) != 1:
                    return False, "Cannot move like that"
                elif board[end[0]][end[1]] is not None:
                    if board[end[0]][end[1]].side != self.side:
                        return True, "Valid"
                    else:
                        return False, "Cannot take own piece"
                else:
                    return False, "Cannot move diagonally if not taking"
            else:
                return False, "Cannot move sideways"
        else:
            return False, "Cannot move backwards"

