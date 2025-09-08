from collections import defaultdict


def traverse(row, col, matrix, visited, size: int, char: str):
    movements = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    visited.add((row, col))
    for move in movements:
        if (
            0 <= row + move[0] <= n - 1
            and 0 <= col + move[1] <= m - 1
            and (row + move[0], col + move[1]) not in visited
            and matrix[row][col] == matrix[row + move[0]][col + move[1]]
        ):
            size += 1
            traverse(row + move[0], col + move[1], matrix, visited, size, char)


n = int(input())
m = int(input())
matrix = []

for row in range(n):
    matrix.append([x for x in input()])

visited = set()
areas = defaultdict(int)

for row in range(n):
    for col in range(m):
        if (row, col) in visited:
            pass
        else:
            visited.add((row, col))
            traverse(row, col, matrix, visited, 1, matrix[row][col])
            areas[matrix[row][col]] = areas.setdefault(matrix[row][col], 0) + 1

print(f"Areas: {sum(areas.values())}")

for letter in sorted(list(areas.keys()), key=lambda x: x):
    print(f"Letter '{letter}' -> {areas[letter]}")
