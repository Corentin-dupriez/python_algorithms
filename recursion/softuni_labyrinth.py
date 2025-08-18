m = int(input())
n = int(input())
lab = []

start_pos = (0, 0)

moves = {"U": (-1, 0), "D": (1, 0), "R": (0, 1), "L": (0, -1)}

visited = []
for _ in range(n):
    lab.append(list(input()))


directions = []


def solve_labyrinth(position: tuple):
    if lab[position[0]][position[1]] == "e":
        print(*directions, sep=" ")
        return
    for direction, move in moves.items():
        visited.append(position)
        new_pos = (position[0] + move[0], position[1] + move[1])
        if (
            not new_pos[0] < 0
            and not new_pos[0] > m - 1
            and not new_pos[1] < 0
            and not new_pos[1] > n - 1
            and new_pos not in visited
            and not lab[new_pos[0]][new_pos[1]] == "*"
        ):
            directions.append(direction)
            solve_labyrinth(new_pos)
            visited.pop()
            directions.pop()


solve_labyrinth(start_pos)
