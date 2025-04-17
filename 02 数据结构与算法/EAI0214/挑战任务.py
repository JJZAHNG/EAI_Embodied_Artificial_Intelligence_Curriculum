from collections import deque
import pygame
import time

# 地图定义
maze = [
    ['0', '0', '1', '0', '0', '0', '0'],
    ['1', '0', '1', '0', '1', '1', '0'],
    ['0', '0', '0', '0', '0', '1', '0'],
    ['0', '1', '1', '1', '0', '1', '0'],
    ['0', '0', 'K', '1', '0', 'D', '0'],
    ['0', '1', '0', '0', '0', '0', '0'],
    ['0', '0', '0', '1', '1', '1', '0'],
]

ROWS, COLS = len(maze), len(maze[0])
TILE_SIZE = 60
WIDTH, HEIGHT = COLS * TILE_SIZE, ROWS * TILE_SIZE

start = (0, 0)
end = (6, 6)

colors = {
    '0': (255, 255, 255),
    '1': (0, 0, 0),
    'K': (255, 255, 0),
    'D': (200, 0, 0),
    'start': (144, 238, 144),
    'end': (34, 139, 34),
    'visited': (173, 216, 230),
    'path': (100, 149, 237),
}

def get_neighbors(x, y):
    for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < ROWS and 0 <= ny < COLS:
            yield (nx, ny)

def draw_maze(screen, maze, visited=set(), path=[], has_key=False):
    screen.fill((255, 255, 255))
    font = pygame.font.SysFont(None, 24)

    for i in range(ROWS):
        for j in range(COLS):
            cell = maze[i][j]
            color = colors.get(cell, (255, 255, 255))
            rect = pygame.Rect(j * TILE_SIZE, i * TILE_SIZE, TILE_SIZE, TILE_SIZE)

            if (i, j) in path:
                color = colors['path']
            elif (i, j) in visited:
                color = colors['visited']
            elif (i, j) == start:
                color = colors['start']
            elif (i, j) == end:
                color = colors['end']

            pygame.draw.rect(screen, color, rect)
            pygame.draw.rect(screen, (0, 0, 0), rect, 1)

            if cell in ['K', 'D']:
                text = font.render(cell, True, (0, 0, 0))
                screen.blit(text, (j * TILE_SIZE + 20, i * TILE_SIZE + 20))

    pygame.display.flip()

def bfs_visual(screen, maze, start, end):
    queue = deque()
    queue.append((start[0], start[1], False))
    visited = set()
    visited.add((start[0], start[1], False))
    parent = {}

    while queue:
        x, y, has_key = queue.popleft()
        cell = maze[x][y]

        if cell == 'K':
            has_key = True

        draw_maze(screen, maze, {(vx, vy) for vx, vy, _ in visited}, [], has_key)
        time.sleep(0.05)

        if (x, y) == end:
            break

        for nx, ny in get_neighbors(x, y):
            ncell = maze[nx][ny]
            if ncell == '1':
                continue
            if ncell == 'D' and not has_key:
                continue
            if (nx, ny, has_key) not in visited:
                visited.add((nx, ny, has_key))
                parent[(nx, ny, has_key)] = (x, y, has_key)
                queue.append((nx, ny, has_key))

    # 回溯路径
    path = []
    node = None
    for k in [(end[0], end[1], True), (end[0], end[1], False)]:
        if k in parent:
            node = k
            break

    while node in parent:
        path.append((node[0], node[1]))
        node = parent[node]
    path.append(start)
    path.reverse()

    # 动态绘制路径
    for i in range(len(path)):
        draw_maze(screen, maze, visited={(vx, vy) for vx, vy, _ in visited}, path=path[:i+1])
        time.sleep(0.1)

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("BFS 动态迷宫导航（含钥匙/门）")
    draw_maze(screen, maze)

    running = True
    started = False

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if not started:
            bfs_visual(screen, maze, start, end)
            started = True

    pygame.quit()

main()
