def diagonal_winner(board):
    if (len(set([board[i][i] for i in range(len(board))])) == 1 and
        set([board[i][i] for i in range(len(board))]) != set(' ')) or \
            (len(set([board[i][len(board) - i - 1] for i in range(len(board))])) == 1 and
             set([board[i][len(board) - i - 1] for i in range(len(board))]) != set(' ')):
        return True
    return False