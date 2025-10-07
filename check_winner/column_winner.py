def column_winner(board):
    if any([1 for i in range(len(board)) if
            len(set([x[i] for x in board])) == 1 and set([x[i] for x in board]) != set(' ')]):
        return True
    return False