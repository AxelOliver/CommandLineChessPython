from app.board import Board

if __name__ == '__main__':
    board = Board()
    board.set_board()
    print(board)

    checkmate = False
    stalemate = False
    turn = "White"
    valid_numbers = "12345678"
    valid_letters = "abcdefgh"
    while not checkmate or not stalemate:
        print(f"{turn} to move")
        user_move = input("Enter your move: ").lower().split()

        # make sure correct format for converting, then convert
        while not board.validate_notation(user_move):
            print("Invalid move. Use chess notation (a2 a4)")
            user_move = input("Enter your move: ").lower().split()

        user_move = board.convert_move(user_move)

        valid_move = board.validate_move(user_move, turn)
        if not valid_move[0]:
            print(valid_move[1])
            continue
        board.move(user_move)
        if turn == "White":
            turn = "Black"
        else:
            turn = "White"
        # check if it puts you in check
        # will have a safe board to revert to and a board with move made, then check if any piece can take the king
        # on the updated board
        print(board)
