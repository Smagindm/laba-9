def tic_tac_toe(board):
    lines = board + list (zip(*board)) + [
        [board[i][i] for i in range(3)],
        [board[i][2-i] for i in range (3)]
    ]
    for line in lines:
        if line [0] !=0 and line.count(line[0]) == 3:
            return line [0]

    if any (0 in row for row in board):
        return -1

    return 0