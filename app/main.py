from app.board import Board
from app.writeToFile import write_to_file
from copy import deepcopy

if __name__ == '__main__':
    board = Board()
    board.set_board()
    print(board)

    check = False
    checkmate = False
    stalemate = False
    while not checkmate or not stalemate:
        write_to_file(board.board, board.turn)
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
        print(board)
