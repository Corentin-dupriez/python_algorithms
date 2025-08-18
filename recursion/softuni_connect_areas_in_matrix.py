class Area:
    def __init__(self, row, col, size) -> None:
        self.row = row
        self.col = col
        self.size = size

    def __str__(self) -> str:
        return f"({self.row}, {self.col}), size: {self.size}"


def find_connected_areas(row: int, col: int):
    if not 0 <= row < rows or not 0 <= col < cols or not matrix[row][col] == "-":
        return 0
    matrix[row][col] = "v"
    result = 1
    result += find_connected_areas(row - 1, col)
    result += find_connected_areas(row + 1, col)
    result += find_connected_areas(row, col - 1)
    result += find_connected_areas(row, col + 1)
    return result


rows = int(input())
cols = int(input())

matrix = []
visited = []
areas = []

for _ in range(rows):
    matrix.append([x for x in input()])


for row in range(rows):
    for col in range(cols):
        area = find_connected_areas(row, col)
        if area > 0:
            areas.append(Area(row, col, area))

print(f"Total areas found: {len(areas)}")

for idx, area in enumerate(sorted(areas, key=lambda x: (-x.size, x.row, x.col))):
    print(f"Area #{idx + 1} at {area.__str__()}")
