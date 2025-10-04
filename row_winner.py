def row_winner(board):
    # Проверяем строки
    if any([1 for x in board if len(set(x)) == 1 and x[0] != ' ']):
        return True

    # Проверяем столбцы
    if any([1 for i in range(len(board)) if len(set([x[i] for x in board])) == 1]):
        return True

    # Проверяем диагональ
    if len(set([board[i][i] for i in range(len(board))])) == 1 or \
            len(set([board[i][len(board) - i - 1 ] for i in range(len(board))])) == 1:
        return True

    # Возвращаем False если не нашлось победителей
    return False


def assert_equal(data, result):
    if data == result:
        print("OK")
    else:
        print(f"Error: expected: {result}, got: {data}")

# Детектим строку
assert_equal(
    row_winner(
        [
            ['A', 'A', 'A', 'A'],
            [' ', ' ', ' ', ' '],
            ['A', ' ', ' ', 'A'],
            ['B', ' ', 'B', 'A']
        ]
    ),
    True
)
# Детектим столбец
assert_equal(
    row_winner(
        [
            ['X', ' ', 'X'],
            ['O', ' ', 'X'],
            ['O', 'O', 'X']
        ]
    ),
    True
)
# Детектим диагонали
assert_equal(
    row_winner(
        [
            ['A', 'A', ' ', ' '],
            [' ', 'A', ' ', ' '],
            ['A', ' ', 'A', 'A'],
            ['B', ' ', 'B', 'A']
        ]
    ),
    True
)
assert_equal(
    row_winner(
        [
            ['A', 'A', ' ', 'B'],
            [' ', 'A', 'B', ' '],
            ['A', 'B', ' ', 'A'],
            ['B', ' ', 'B', 'A']
        ]
    ),
    True
)
# Нет победителя
assert_equal(
    row_winner(
        [
            [' ', ' ', ' ', ' '],
            [' ', 'A', ' ', ' '],
            ['A', ' ', 'A', 'A'],
            ['B', ' ', 'B', 'A']
        ]
    ),
    False
)