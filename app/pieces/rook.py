from app.pieces.piece import Piece
from colorama import *


class Rook(Piece):
    def __str__(self):
        if self.side == "W":
            return Style.BRIGHT + Fore.LIGHTWHITE_EX + "R" + Fore.RESET + Style.NORMAL
        else:
            return Style.BRIGHT + Fore.LIGHTBLACK_EX + "R" + Fore.RESET + Style.NORMAL