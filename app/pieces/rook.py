from app.pieces.piece import Piece
from copy import deepcopy
from colorama import *


class Rook(Piece):
    def __str__(self):
        if self.side == "White":
            return Style.BRIGHT + Fore.LIGHTWHITE_EX + "R" + Fore.RESET + Style.NORMAL
        else:
            return Style.BRIGHT + Fore.LIGHTBLACK_EX + "R" + Fore.RESET + Style.NORMAL

    def validate_move(self, start, end, board):
        test_board = deepcopy(board)
        test_board.move([start, end])
        # check if going left/down/up/right
        counter = 0
        up_down = 0
        left_right = 0
        if start[0] == end[0]:
            up_down = 0
        elif start[0] > end[0]:
            up_down = -1
        else:
            up_down = 1
        if start[1] == end[1]:
            left_right = 0
        elif start[1] < end[1]:
            left_right = 1
        else:
            left_right = -1
        counter = left_right

        # check if is a straight path
        if start[0] == end[0] or start[1] == end[1]:
            if up_down != 0:
                for i in range(start[0] + up_down, end[0], up_down):
                    if board.board[i][start[1]] is not None:
                        return False, "Piece in the way"
            elif left_right == 0:
                return False, "Can't move in place"
            else:
                for i in range(start[1] + left_right, end[1], left_right):
                    if board.board[0][i] is not None:
                        return False, "Piece in the way"
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
            return False, "Rook must move in straight path"
