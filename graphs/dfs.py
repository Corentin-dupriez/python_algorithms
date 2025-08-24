def dfs(node, graph, visited):
    visited.append(node)
    for child in graph[node]:
        if child not in visited:
            dfs(child, graph, visited)

    print(node)


graph = {
    1: [19, 21, 14],
    19: [7, 12, 31, 21],
    21: [14],
    14: [23, 6],
    7: [1],
    12: [],
    31: [21],
    23: [21],
    6: [],
}

visited = []

dfs(list(graph.keys())[0], graph, visited)
