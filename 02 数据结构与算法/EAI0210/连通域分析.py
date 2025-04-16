from 递归实现DFS import dfs

def find_connected_components(graph):
    visited = set()
    components = []

    for node in graph:
        if node not in visited:
            component = []
            dfs(node, visited, graph)
            components.append(component)

    return components

# 示例图结构
graph = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A", "D"],
    "D": ["B", "C"],
    "E": ["F"],
    "F": ["E"]
}

connected_components = find_connected_components(graph)
print(connected_components)

