def dfs(node, visited, graph):
    visited.add(node)
    print(f"访问：{node}")
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(neighbor, visited, graph)

# 示例图结构
graph = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A", "D"],
    "D": ["B", "C"]
}

visited = set()
dfs("A", visited, graph)

