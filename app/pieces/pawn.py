from copy import deepcopy
from app.pieces.piece import Piece
from colorama import *


class Pawn(Piece):
    def __str__(self):
        if self.side == "White":
            return Style.BRIGHT + Fore.LIGHTWHITE_EX + "P" + Fore.RESET + Style.NORMAL
        else:
            return Style.BRIGHT + Fore.LIGHTBLACK_EX + "P" + Fore.RESET + Style.NORMAL

    def validate_move(self, start, end, board):
        test_board = deepcopy(board)
        test_board.move([start, end])
        # check that movement is in right direction
        if self.side == 'White' and start[0] - end[0] > 0 or self.side == 'Black' and start[0] - end[0] < 0:
            # if is straight line
            if start[1] == end[1]:
                # if hasnt moved, can move 2 forward
                if not self.has_moved and abs(start[0] - end[0]) <= 2 or self.has_moved and abs(start[0] - end[0]) == 1:
                    if board.board[end[0]][end[1]] is not None:
                        return False, "Cant move straight onto another piece"
                    else:
                        if not test_board.check(board.turn)[0]:
                            return True, "Valid"
                        else:
                            return False, "That would put you in check"
                else:
                    return False, "Can only move 1 space or 2 if first move"
            # if is moving diagonally
            elif abs(start[1] - end[1]) == 1:
                if abs(start[0] - end[0]) != 1:
                    return False, "Cannot move like that"
                elif board.board[end[0]][end[1]] is not None:
                    if board.board[end[0]][end[1]].side != self.side:
                        if not test_board.check(board.turn)[0]:
                            return True, "Valid"
                        else:
                            return False, "That would put you in check"
                    else:
                        return False, "Cannot take own piece"
                else:
                    return False, "Cannot move diagonally if not taking"
            else:
                return False, "Cannot move sideways"
        else:
            return False, "Cannot move backwards"

