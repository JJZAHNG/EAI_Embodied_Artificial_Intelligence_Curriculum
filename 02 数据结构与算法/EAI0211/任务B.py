def approx_binary_search(arr, target, epsilon=0.2):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        diff = abs(arr[mid] - target)

        if diff <= epsilon:
            return arr[mid]
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return None  # 没找到近似点

# 示例坐标
positions = [100.1, 101.3, 102.6, 104.0, 106.2]
target = 104.1
result = approx_binary_search(positions, target, epsilon=0.2)
print("结果：", f"匹配点为 {result}" if result else "无近似点")

