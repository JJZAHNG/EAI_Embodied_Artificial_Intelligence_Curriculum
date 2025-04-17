def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]





import numpy as np

data = [10, 12, 11, 98, 13, 14, 11]
mean = np.mean(data)
std = np.std(data)

cleaned = [x for x in data if abs(x - mean) < 2 * std]


bubble_sort(cleaned)
print("清洗排序后：", cleaned)


