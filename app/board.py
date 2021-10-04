from app.pieces.pawn import Pawn
from app.pieces.knight import Knight
from app.pieces.bishop import Bishop
from app.pieces.rook import Rook
from app.pieces.queen import Queen
from app.pieces.king import King
from colorama import *


class Board:
    def __init__(self):
        self.board = [list([None] * 8) for _ in range(8)]

    def __str__(self):
        string = ""
        for x in range(8):
            string += f"{8 - x} "
            for y in range(8):
                if x % 2 == 0:
                    if y % 2 == 0:
                        string += Back.GREEN
                    else:
                        string += Back.BLUE
                if x % 2 == 1:
                    if y % 2 == 1:
                        string += Back.GREEN
                    else:
                        string += Back.BLUE
                if self.board[x][y] is None:
                    string += "   "
                else:
                    string += f" {self.board[x][y]} "
            string += Style.RESET_ALL
            string += "\n"
        string += "   A  B  C  D  E  F  G  H"
        return string

    def set_board(self):
        for x in range(8):
            for y in range(8):
                if x == 0:
                    if y == 1 or y == 6:
                        self.board[x][y] = Knight("B")
                    elif y == 2 or y == 5:
                        self.board[x][y] = Bishop("B")
                    elif y == 3:
                        self.board[x][y] = Queen("B")
                    elif y == 4:
                        self.board[x][y] = King("B")
                    elif y == 0 or y == 7:
                        self.board[x][y] = Rook("B")
                elif x == 1:
                    self.board[x][y] = Pawn("B")
                elif x == 6:
                    self.board[x][y] = Pawn("W")
                elif x == 7:
                    if y == 1 or y == 6:
                        self.board[x][y] = Knight("W")
                    elif y == 2 or y == 5:
                        self.board[x][y] = Bishop("W")
                    elif y == 3:
                        self.board[x][y] = Queen("W")
                    elif y == 4:
                        self.board[x][y] = King("W")
                    elif y == 0 or y == 7:
                        self.board[x][y] = Rook("W")




        for i in range(8):
            self.board[6][i] = Pawn("W")



if __name__ == '__main__':
    board = Board()
    board.set_board()
    print(board)
