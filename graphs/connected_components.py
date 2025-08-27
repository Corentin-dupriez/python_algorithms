def dfs(node, graph, visited, connected: list):
    if node in visited:
        return
    visited.append(node)
    for child in graph[node]:
        dfs(child, graph, visited, connected)

    connected.append(node)


num_rows = int(input())
graph = []
for _ in range(num_rows):
    graph.append([int(x) for x in input().split()])
visited = []


for node in range(len(graph)):
    if node in visited:
        continue
    connected = []
    dfs(node, graph, visited, connected)
    print(f"Connected component: {' '.join(str(x) for x in connected)}")
