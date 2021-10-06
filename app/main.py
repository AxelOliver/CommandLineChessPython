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
        validated = False
        while not board.validate_notation(user_move):
            print("Invalid notation. Use chess notation (a2 a4)")
            user_move = input("Enter your move: ").lower().split()

        # board.convert_move(user_move)
        # check if your own piece is on move
        # check if there is opposing colour is present on move
        # move validation
        # check if it puts you in check
        # make move if valid, send error if not
        if turn == "White":
            turn = "Black"
        else:
            turn = "White"
        print(board)
