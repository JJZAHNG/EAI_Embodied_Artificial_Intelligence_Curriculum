from collections import deque
import time
import random

# ========= 环境建模 =========
# 0: 空地，1: 障碍，'S': 起点，'C': 充电站，'D': 灰尘点
room = [
    ['S', 0, 0, 1, 'D'],
    [0, 1, 0, 0, 0],
    ['D', 0, 1, 0, 'C'],
    [0, 0, 0, 0, 'D']
]

ROWS, COLS = len(room), len(room[0])
battery = 10
BATTERY_LIMIT = 3

# ========= BFS 路径规划 =========
def bfs(start, target):
    queue = deque([start])
    visited = set([start])
    parent = {start: None}

    while queue:
        x, y = queue.popleft()
        if (x, y) == target:
            break
        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < ROWS and 0 <= ny < COLS and room[nx][ny] != 1:
                if (nx, ny) not in visited:
                    visited.add((nx, ny))
                    parent[(nx, ny)] = (x, y)
                    queue.append((nx, ny))

    # 回溯路径
    path = []
    curr = target
    while curr in parent:
        path.append(curr)
        curr = parent[curr]
    path.reverse()
    return path

# ========= 行为控制 =========
def move_and_act(path, mode):
    global battery
    for pos in path:
        battery -= 1
        print(f"移动到 {pos}，剩余电量：{battery}")
        if mode == 'clean' and room[pos[0]][pos[1]] == 'D':
            print("清扫灰尘 ✔️")
            room[pos[0]][pos[1]] = 0
        elif mode == 'charge' and room[pos[0]][pos[1]] == 'C':
            print("开始充电... ⚡")
            battery = 10
        time.sleep(0.3)

# ========= 状态机主流程 =========
def find_all(target):
    result = []
    for i in range(ROWS):
        for j in range(COLS):
            if room[i][j] == target:
                result.append((i, j))
    return result

def run():
    global battery
    current = find_all('S')[0]

    while True:
        dusts = find_all('D')
        if not dusts:
            print("✅ 房间已清洁完毕！")
            break

        # 优先处理电量不足情况
        if battery <= BATTERY_LIMIT:
            charger = find_all('C')[0]
            path = bfs(current, charger)
            print("⚠️ 电量低，前往充电站...")
            move_and_act(path, 'charge')
            current = charger
            continue

        # 找最近灰尘点
        target = dusts[0]
        path = bfs(current, target)
        print("🧹 前往灰尘点...")
        move_and_act(path, 'clean')
        current = target

run()
