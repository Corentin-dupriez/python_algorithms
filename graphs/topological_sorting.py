def find_dependencies(graph: dict) -> dict:
    dependencies = {}
    for node, children in graph.items():
        dependencies[node] = dependencies.setdefault(node, 0)
        for child in children:
            if child != "":
                dependencies[child] = dependencies.setdefault(child, 0) + 1
    return dependencies


def find_node_without_dependencies(dependency_by_node):
    for node, dependencies in dependency_by_node.items():
        if dependencies == 0:
            return node
    return None


num_rows = int(input())

graph = {}

for _ in range(num_rows):
    info = input().split("->")
    node = info[0].strip()
    children = info[1].strip().split(", ") if info[1] else []
    graph[node] = children

dependency_by_node = find_dependencies(graph)
has_cycles = False
sorted_nodes = []

while dependency_by_node:
    node_to_remove = find_node_without_dependencies(dependency_by_node)

    if node_to_remove is None:
        has_cycles = True
        break

    dependency_by_node.pop(node_to_remove)
    sorted_nodes.append(node_to_remove)

    for child in graph[node_to_remove]:
        dependency_by_node[child] -= 1

if has_cycles:
    print("Invalid topological sorting")
else:
    print(f"Topological sorting: {', '.join(sorted_nodes)}")
