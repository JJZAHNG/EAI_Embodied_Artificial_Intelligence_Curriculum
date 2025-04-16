def binary_search_rec(arr, target, left, right):
    if left > right:
        return -1
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_rec(arr, target, mid + 1, right)
    else:
        return binary_search_rec(arr, target, left, mid - 1)

