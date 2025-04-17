# === 环境建模 ===
room = [
    ['S', 0, 0, 1, 'D'],
    [0, 1, 0, 0, 0],
    ['D', 0, 1, 0, 'C'],
    [0, 0, 0, 0, 'D']
]
battery = 10
BATTERY_LIMIT = 3

# === 待实现 ===
def bfs(start, target):
    """使用队列实现BFS算法，返回从start到target的路径列表"""
    # TODO：请同学实现BFS搜索
    pass

def move_and_act(path, mode):
    """沿着路径移动并执行清扫或充电"""
    global battery
    for pos in path:
        battery -= 1
        print(f"移动到 {pos}，剩余电量：{battery}")
        if mode == 'clean':
            # TODO：补充清扫灰尘逻辑
            pass
        elif mode == 'charge':
            # TODO：补充充电逻辑
            pass

def run():
    """主控系统，完成完整清扫逻辑"""
    current = (0, 0)  # TODO: 获取起点位置

    while True:
        # TODO: 如果电量过低，前往充电站
        # TODO: 找灰尘，规划路径并清扫
        # TODO: 判断任务是否完成
        break  # 结束条件

run()
