from collections import deque


def dfs(node, graph, visited: set, cycles: set, sorted_nodes: deque):
    if node in cycles:
        raise Exception
    if node in visited:
        return
    visited.add(node)
    cycles.add(node)
    for child in graph[node]:
        dfs(child, graph, visited, cycles, sorted_nodes)

    cycles.remove(node)
    sorted_nodes.appendleft(node)


num_rows = int(input())
graph = {}
sorted_nodes = deque()

for _ in range(num_rows):
    info = input().split("->")
    node = info[0].strip()
    children = info[1].strip().split(", ") if info[1] else []
    graph[node] = children

visited = set()
cycles = set()

for node in graph:
    dfs(node, graph, visited, cycles, sorted_nodes)

print(*sorted_nodes, sep=" ")
