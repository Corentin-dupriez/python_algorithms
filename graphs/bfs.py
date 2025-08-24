from collections import deque


def bfs(node, graph, visited):
    if node in visited:
        return

    queue = deque([node])
    visited.append(node)

    while queue:
        current_node = queue.popleft()
        print(current_node)
        for child in graph[current_node]:
            if child not in visited:
                queue.append(child)
                visited.append(child)


graph = {
    7: [19, 21, 14],
    19: [1, 12, 31, 21],
    21: [14],
    14: [23, 6],
    1: [7],
    12: [],
    31: [21],
    23: [21],
    6: [],
}

visited = []

bfs(list(graph.keys())[0], graph, visited)
