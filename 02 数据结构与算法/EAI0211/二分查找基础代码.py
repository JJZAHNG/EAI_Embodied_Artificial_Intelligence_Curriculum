def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2  # 中点

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1  # 往右查找
        else:
            right = mid - 1  # 往左查找

    return -1  # 未找到


