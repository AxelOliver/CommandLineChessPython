from app.pieces.piece import Piece
from colorama import *


class Bishop(Piece):
    def __str__(self):
        if self.side == "W":
            return Style.BRIGHT + Fore.LIGHTWHITE_EX + "B" + Fore.RESET + Style.NORMAL
        else:
            return Style.BRIGHT + Fore.LIGHTBLACK_EX + "B" + Fore.RESET + Style.NORMAL

    def validate_move(self, start, end, board):
        # check if going left/down/up/right
        counter = 0
        up_down = 0
        left_right = 0
        if start[0] < end[0]:
            up_down = 1
        else:
            up_down = -1
        if start[1] < end[1]:
            left_right = 1
        else:
            left_right = -1
        counter = left_right

        # check if is a diagonal path
        if abs(start[0] - end[0]) == abs(start[1] - end[1]):
            # check if piece is in path
            for i in range(start[0] + up_down, end[0], up_down):
                if board[i][start[1] + counter] is not None:
                    return False, "Piece in the way"
                counter += left_right
            # if moving on to a piece
            if board[end[0]][end[1]] is not None:
                if board[end[0]][end[1]].side != self.side:
                    return True, "Valid"
                else:
                    return False, "Can't take own piece"
            else:
                return True, "Valid"
        else:
            return False, "Bishop must move in diagonal path"
