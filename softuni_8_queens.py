size = 8


board = [["-"] * 8 for _ in range(8)]


def print_board(board: list) -> None:
    for row in board:
        print("".join(row))
    print()


def is_placeable(position: tuple, cols, rows, left_diagonals, right_diagonals) -> bool:
    if position[0] in rows:
        return False
    if position[1] in cols:
        return False
    if position[0] - position[1] in left_diagonals:
        return False
    if position[0] + position[1] in right_diagonals:
        return False
    return True


def put_queen(position: tuple, cols, rows, left_diagonals, right_diagonals) -> None:
    board[position[0]][position[1]] = "*"
    rows.add(position[0])
    cols.add(position[1])
    left_diagonals.add(position[0] - position[1])
    right_diagonals.add(position[0] + position[1])


def remove_queen(position: tuple, cols, rows, left_diagonals, right_diagonals) -> None:
    board[position[0]][position[1]] = "-"
    rows.remove(position[0])
    cols.remove(position[1])
    left_diagonals.remove(position[0] - position[1])
    right_diagonals.remove(position[0] + position[1])


def place_queen(row: int, cols, rows, left_diagonals, right_diagonals):
    if row == size:
        print_board(board)
        return
    for col in range(size):
        if is_placeable((row, col), cols, rows, left_diagonals, right_diagonals):
            put_queen((row, col), cols, rows, left_diagonals, right_diagonals)
            place_queen(row + 1, cols, rows, left_diagonals, right_diagonals)
            remove_queen((row, col), cols, rows, left_diagonals, right_diagonals)


place_queen(0, set(), set(), set(), set())
