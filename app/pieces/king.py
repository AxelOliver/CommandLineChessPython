from app.pieces.piece import Piece
from copy import deepcopy
from colorama import *


class King(Piece):
    def __str__(self):
        if self.side == "White":
            return Style.BRIGHT + Fore.LIGHTWHITE_EX + "K" + Fore.RESET + Style.NORMAL
        else:
            return Style.BRIGHT + Fore.LIGHTBLACK_EX + "K" + Fore.RESET + Style.NORMAL

    def validate_move(self, start, end, board):
        test_board = deepcopy(board)
        test_board.move([start, end])
        if abs(start[0] - end[0]) == 0 and abs(start[1] - end[1]) == 0:
            return False, "Can't move in same spot"
        elif abs(start[0] - end[0]) <= 1 and abs(start[1] - end[1]) <= 1:
            if board.board[end[0]][end[1]] is not None:
                if board.board[end[0]][end[1]].side != self.side:
                    if not test_board.check(board.turn)[0]:
                        return True, "Valid"
                    else:
                        return False, "That would put you in check"
                else:
                    return False, "Can't take own piece"
            else:
                if not test_board.check(board.turn)[0]:
                    return True, "Valid"
                else:
                    return False, "That would put you in check"
        else:
            return False, "King can only move 1 square at a time"
