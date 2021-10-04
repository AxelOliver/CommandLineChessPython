from app.pieces.piece import Piece
from colorama import *


class Pawn(Piece):
    def __str__(self):
        if self.side == "W":
            return Style.BRIGHT + Fore.LIGHTWHITE_EX + "P" + Fore.RESET + Style.NORMAL
        else:
            return Style.BRIGHT + Fore.LIGHTBLACK_EX + "P" + Fore.RESET + Style.NORMAL

