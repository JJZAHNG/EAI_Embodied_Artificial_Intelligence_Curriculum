def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid  # 找到了，返回索引
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1  # 没找到

# 有序坐标（横坐标）
positions = [100.1, 101.3, 102.6, 104.0, 106.2]
target = 102.6
result = binary_search(positions, target)
print("结果：", "找到" if result != -1 else "未找到")

