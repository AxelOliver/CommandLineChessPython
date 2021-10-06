from app.pieces.piece import Piece
from colorama import *


class Pawn(Piece):
    def __str__(self):
        if self.side == "W":
            return Style.BRIGHT + Fore.LIGHTWHITE_EX + "P" + Fore.RESET + Style.NORMAL
        else:
            return Style.BRIGHT + Fore.LIGHTBLACK_EX + "P" + Fore.RESET + Style.NORMAL

    def validate_move(self, current_pos, new_pos, is_taking):
        if not is_taking:
            if not self.has_moved:
                if abs(new_pos[1] - current_pos[1]) == 1 or abs(new_pos[1] - current_pos[1]) == 2:
                    return True
                else:
                    return False
            if self.has_moved:
                if abs(new_pos[1] - current_pos[1]) == 1:
                    return True
                else:
                    return False
        else:
            if abs(new_pos[1] - current_pos[1]) == 1 and abs(new_pos[2] - current_pos[2] == 1):
                return True
            else:
                return False
