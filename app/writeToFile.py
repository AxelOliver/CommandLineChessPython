def write_to_file(board, turn):
    string = ""
    empty_count = 0
    for y in board:
        for x in y:
            if x is None:
                empty_count += 1
            else:
                if x.side[0] == "W":
                    if empty_count > 0:
                        string += str(empty_count)
                        empty_count = 0
                    if type(x).__name__ == "Knight":
                        string += 'N'
                    else:
                        string += type(x).__name__[0]
                else:
                    if empty_count > 0:
                        string += str(empty_count)
                        empty_count = 0
                    if type(x).__name__ == "Knight":
                        string += 'n'
                    else:
                        string += type(x).__name__[0].lower()
        if empty_count != 0:
            string += str(empty_count)
            empty_count = 0

        string += "/"
    string = string[:-1]
    string += " z "
    if (board[7][4] is not None and board[7][4].has_moved is False
            and board[7][7] is not None and board[7][7].has_moved is False):
        string += "K"
        if board[7][0] is not None and board[7][0].has_moved is False:
            string += "Q"
    if board[7][4] is not None and board[7][4].has_moved:
        string += "-"
    if (board[0][4] is not None and board[0][4].has_moved is False
            and board[0][7] is not None and board[0][7].has_moved is False):
        string += "k"
        if board[0][0].has_moved is False:
            string += "q"
    if board[0][4] is None or board[0][4].has_moved:
        string += "-"
    string += " "
    with open('FEN.txt', 'w') as f:
        f.write(string)
        f.close()

    counter = 0
    for char in string:
        if char != 'z':
            counter += 1
        else:
            break
    with open("FEN.txt", "r+") as f:
        f.seek(counter)
        if turn[0] == "W":
            f.write("w")
        else:
            f.write("b")
        f.close()
