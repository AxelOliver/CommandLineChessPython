from copy import deepcopy

from app.pieces.pawn import Pawn
from app.pieces.knight import Knight
from app.pieces.bishop import Bishop
from app.pieces.rook import Rook
from app.pieces.queen import Queen
from app.pieces.king import King
from app.pieces.piece import Piece
from colorama import *


class Board:
    def __init__(self):
        self.board = [list([None] * 8) for _ in range(8)]
        self.turn = "White"

    def __str__(self):
        string = "   A  B  C  D  E  F  G  H\n"
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
            string += f" {8 - x}"
            string += "\n"
        string += "   A  B  C  D  E  F  G  H"
        return string

    def set_debug_board(self):
        for x in range(8):
            for y in range(8):
                if x == 0:
                    if y == 1 or y == 6:
                        self.board[x][y] = Knight("Black")
                    elif y == 2 or y == 5:
                        self.board[x][y] = Bishop("Black")
                    elif y == 3:
                        self.board[x][y] = Queen("Black")
                    elif y == 4:
                        self.board[x][y] = King("Black")
                    elif y == 0 or y == 7:
                        self.board[x][y] = Rook("Black")
                elif x == 1:
                    self.board[x][y] = Pawn("Black")
                    if y == 4:
                        self.board[x][y] = None
                        self.board[3][y] = Pawn("Black")
                elif x == 6:
                    self.board[x][y] = Pawn("White")
                    if y == 5:
                        self.board[x][y] = None
                        self.board[5][y] = Pawn("White")
                    if y == 6:
                        self.board[x][y] = None
                        self.board[4][y] = Pawn("White")
                elif x == 7:
                    if y == 3:
                        self.board[x][y] = Queen("White")
                    elif y == 2 or y == 5:
                        self.board[x][y] = Bishop("White")
                    elif y == 4:
                        self.board[x][y] = King("White")
                    elif y == 0 or y == 7:
                        self.board[x][y] = Rook("White")

    def set_board(self):
        for x in range(8):
            for y in range(8):
                if x == 0:
                    if y == 1 or y == 6:
                        self.board[x][y] = Knight("Black")
                    elif y == 2 or y == 5:
                        self.board[x][y] = Bishop("Black")
                    elif y == 3:
                        self.board[x][y] = Queen("Black")
                    elif y == 4:
                        self.board[x][y] = King("Black")
                    elif y == 0 or y == 7:
                        self.board[x][y] = Rook("Black")
                elif x == 1:
                    self.board[x][y] = Pawn("Black")
                elif x == 6:
                    self.board[x][y] = Pawn("White")
                elif x == 7:
                    if y == 1 or y == 6:
                        self.board[x][y] = Knight("White")
                    elif y == 2 or y == 5:
                        self.board[x][y] = Bishop("White")
                    elif y == 3:
                        self.board[x][y] = Queen("White")
                    elif y == 4:
                        self.board[x][y] = King("White")
                    elif y == 0 or y == 7:
                        self.board[x][y] = Rook("White")

    def convert_move(self, validated_move):
        if validated_move == ["o-o"] or validated_move == ["o-o-o"]:
            return validated_move
        converter_dict = {
            '1': 7, 'a': 0,
            '2': 6, 'b': 1,
            '3': 5, 'c': 2,
            '4': 4, 'd': 3,
            '5': 3, 'e': 4,
            '6': 2, 'f': 5,
            '7': 1, 'g': 6,
            '8': 0, 'h': 7
        }
        converted_move = []
        for move in validated_move:
            converted_move.append([converter_dict[move[1]], converter_dict[move[0]]])
        return converted_move

    def validate_notation(self, user_move):
        valid_numbers = "12345678"
        valid_letters = "abcdefgh"
        if user_move == ["o-o"] or user_move == ["o-o-o"]:
            return True
        elif len(user_move) != 2:
            return False
        else:
            if len(user_move[0]) != 2:
                return False
            elif not all(x in valid_letters for x in user_move[0][0]):
                return False
            elif not all(x in valid_numbers for x in user_move[0][1]):
                return False
            elif user_move[0] == user_move[1]:
                return False
            elif len(user_move[1]) != 2:
                return False
            elif not all(x in valid_letters for x in user_move[1][0]):
                return False
            elif not all(x in valid_numbers for x in user_move[1][1]):
                return False
            else:
                return True

    def validate_move(self, move, turn):
        if move == ["o-o"] or move == ["o-o-o"]:
            return self.validate_castle(move)
        else:
            start = self.board[move[0][0]][move[0][1]]
            end = self.board[move[1][0]][move[1][1]]
            if start is None:
                return False, "No Piece Found"
            elif start.side is not turn:
                if turn == "White":
                    return False, "Not Black's turn"
                else:
                    return False, "Not White's turn"
            else:
                return start.validate_move(move[0], move[1], self)

    def move(self, move):
        if move == ["o-o"]:
            if self.turn == "White":
                self.move([[7, 4], [7, 6]])
                self.move([[7, 7], [7, 5]])
            else:
                self.move([[0, 4], [0, 6]])
                self.move([[0, 7], [0, 5]])
        elif move == ["o-o-o"]:
            if self.turn == "White":
                self.move([[7, 4], [7, 2]])
                self.move([[7, 0], [7, 3]])
            else:
                self.move([[0, 4], [0, 2]])
                self.move([[0, 0], [0, 3]])
        else:
            self.board[move[1][0]][move[1][1]] = self.board[move[0][0]][move[0][1]]
            self.board[move[1][0]][move[1][1]].has_moved = True
            self.board[move[0][0]][move[0][1]] = None

    def validate_castle(self, user_move):
        if user_move == ["o-o"]:
            return self.validate_castle_king_side()
        else:
            return self.validate_castle_queen_side()

    def validate_castle_king_side(self):
        if self.turn == "White":
            test_board = deepcopy(self)
            if type(self.board[7][4]) is King:
                if self.board[7][4].has_moved is False:
                    if type(self.board[7][7]) is Rook:
                        if self.board[7][7].has_moved is False:
                            if test_board.validate_move([[7, 4], [7, 5]], self.turn)[0]:
                                test_board.move([[7, 4], [7, 5]])
                                if test_board.validate_move([[7, 5], [7, 6]], self.turn)[0]:
                                    return True, "Valid"
                            return False, "King cannot pass through check or his own piece"
                        else:
                            return False, "King or Rook has already moved"
                    else:
                        return False, "Rook not in position"
                else:
                    return False, "King has already moved"
            else:
                return False, "King not in position"
        else:
            test_board = deepcopy(self)
            if type(self.board[0][4]) is King:
                if self.board[0][4].has_moved is False:
                    if type(self.board[0][7]) is Rook:
                        if self.board[0][7].has_moved is False:
                            if test_board.validate_move([[0, 4], [0, 5]], self.turn)[0]:
                                test_board.move([[0, 4], [0, 5]])
                                if test_board.validate_move([[0, 5], [0, 6]], self.turn)[0]:
                                    return True, "Valid"
                            return False, "King cannot pass through check or his own piece"
                        else:
                            return False, "King or Rook has already moved"
                    else:
                        return False, "Rook not in position"
                else:
                    return False, "King has already moved"
            else:
                return False, "King not in position"

    def validate_castle_queen_side(self):
        if self.turn == "White":
            test_board = deepcopy(self)
            if type(self.board[7][4]) is King:
                if self.board[7][4].has_moved is False:
                    if type(self.board[7][0]) is Rook:
                        if self.board[7][0].has_moved is False:
                            if test_board.validate_move([[7, 4], [7, 3]], self.turn)[0]:
                                test_board.move([[7, 4], [7, 3]])
                                if test_board.validate_move([[7, 3], [7, 2]], self.turn)[0]:
                                    return True, "Valid"
                            return False, "King cannot pass through check or his own piece"
                        else:
                            return False, "King or Rook has already moved"
                    else:
                        return False, "Rook not in position"
                else:
                    return False, "King has already moved"
            else:
                return False, "King not in position"
        else:
            test_board = deepcopy(self)
            if type(self.board[0][4]) is King:
                if self.board[0][4].has_moved is False:
                    if type(self.board[0][7]) is Rook:
                        if self.board[0][7].has_moved is False:
                            if test_board.validate_move([[0, 4], [0, 3]], self.turn)[0]:
                                test_board.move([[0, 4], [0, 3]])
                                if test_board.validate_move([[0, 3], [0, 2]], self.turn)[0]:
                                    return True, "Valid"
                            return False, "King cannot pass through check or his own piece"
                        else:
                            return False, "King or Rook has already moved"
                    else:
                        return False, "Rook not in position"
                else:
                    return False, "King has already moved"
            else:
                return False, "King not in position"

    def check(self, turn):
        white_king = None
        black_king = None
        for j in range(8):
            for i in range(8):
                if type(self.board[j][i]) is King:
                    if self.board[j][i].side == 'White':
                        white_king = [j, i]
                    else:
                        black_king = [j, i]
        if white_king is None or black_king is None:
            return False, "King is none"
        else:
            for j in range(8):
                for i in range(8):
                    if type(self.board[j][i]) is not King and self.board[j][i] is not None:
                        if self.board[j][i].validate_move([j, i], white_king, self)[0]:
                            if turn == "White":
                                return True, False
                            else:
                                return False, True
                        elif self.board[j][i].validate_move([j, i], black_king, self)[0]:
                            if turn == "Black":
                                return True, False
                            else:
                                return False, True
        return False, False

    def checkmate(self, turn):
        if self.turn == "White":
            self.turn = "Black"
        else:
            self.turn = "White"
        for j in range(8):
            for i in range(8):
                if self.board[j][i] is not None and self.board[j][i].side != turn:
                    for x in range(8):
                        for y in range(8):
                            if self.board[j][i].validate_move([j, i], [x, y], self)[0]:
                                if self.turn == "White":
                                    self.turn = "Black"
                                else:
                                    self.turn = "White"
                                return False
        return True


if __name__ == '__main__':
    board = Board()
    board.set_board()
    print(board)
