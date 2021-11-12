from app.board import Board
from copy import deepcopy

if __name__ == '__main__':
    board = Board()
    board.set_board()
    print(board)

    check = False
    checkmate = False
    stalemate = False
    while not checkmate or not stalemate:
        previous_state = deepcopy(board)
        print(f"{board.turn} to move")
        user_move = input("Enter your move: ").lower().split()

        while not board.validate_notation(user_move):
            print("Invalid move. Use chess notation (a2 a4)")
            user_move = input("Enter your move: ").lower().split()

        user_move = board.convert_move(user_move)

        valid_move = board.validate_move(user_move, board.turn)
        if not valid_move[0]:
            print(valid_move[1])
            continue
        board.move(user_move)
        if board.check(board.turn)[1]:
            # check all king moves from here incase it's checkmate
            if board.checkmate(board.turn):
                print(board)
                print("CHECKMATE!")
                break
            else:
                print(board)
                print("CHECK!")
                if board.turn == "White":
                    board.turn = "Black"
                else:
                    board.turn = "White"
                continue
        elif board.check(board.turn)[0]:
            board = previous_state
            print(board)
            print("Get out of check first!")
            continue
        if board.turn == "White":
            board.turn = "Black"
        else:
            board.turn = "White"
        # check if it puts you in check
        # will have a safe board to revert to and a board with move made, then check if any piece can take the king
        # on the updated board
        print(board)
