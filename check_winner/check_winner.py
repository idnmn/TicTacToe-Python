from row_winner import row_winner
from column_winner import column_winner
from diagonal_winner import diagonal_winner


def check_winner(board):
    return any([row_winner(board), column_winner(board), diagonal_winner(board)])


def assert_equal(data, result):
    if data == result:
        print("OK")
    else:
        print(f"Error: expected: {result}, got: {data}")

# Детектим строку
assert_equal(
    check_winner(
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
    check_winner(
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
    check_winner(
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
    check_winner(
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
    check_winner(
        [
            [' ', ' ', ' ', ' '],
            [' ', 'A', ' ', ' '],
            ['A', ' ', 'A', 'A'],
            ['B', ' ', 'B', 'A']
        ]
    ),
    False
)