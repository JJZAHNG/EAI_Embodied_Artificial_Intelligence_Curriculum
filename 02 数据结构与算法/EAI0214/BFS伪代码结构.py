from collections import deque

def bfs(grid, start, end):
    queue = deque([start])
    visited = set([start])
    parent = {start: None}

    while queue:
        node = queue.popleft()
        if node == end:
            break
        for neighbor in get_neighbors(node, grid):
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = node
                queue.append(neighbor)

    # 路径回溯
    path = []
    curr = end
    while curr:
        path.append(curr)
        curr = parent[curr]
    return path[::-1]

