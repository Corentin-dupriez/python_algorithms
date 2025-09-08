from collections import defaultdict


def dfs(node: str, graph: dict, visited: list, path: list):
    global has_cycles
    visited.append(node)
    path.append(node)
    for child in graph[node]:
        if child in path:
            has_cycles = True
            break
        dfs(child, graph, visited, path)


graph = defaultdict(list)


while True:
    node = input()
    if node == "End":
        break
    else:
        node, child = node.split("-")
        graph[node].append(child)

visited = []
has_cycles = False

for node in list(graph.keys()):
    if node not in visited:
        dfs(node, graph, visited, [])

print(f"Acyclic: {'Yes' if not has_cycles else 'No'}")
