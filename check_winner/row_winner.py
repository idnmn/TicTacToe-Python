def row_winner(board):
    # Проверяем строки
    if any([1 for x in board if len(set(x)) == 1 and x[0] != ' ']):
        return True
    return False
