m = int(input())
n = int(input())
visited = []
solutions = []


def move_down_right(start_row: int, start_col: int, rows: int, cols: int):
    if start_row == rows - 1 and start_col == cols - 1:
        solutions.append(1)
        return
    for options in ((start_row + 1, start_col), (start_row, start_col + 1)):
        if options not in visited and options[0] < rows and options[1] < cols:
            visited.append((start_row, start_col))
            move_down_right(options[0], options[1], rows, cols)
            visited.remove((start_row, start_col))


move_down_right(0, 0, m, n)
print(len(solutions))
