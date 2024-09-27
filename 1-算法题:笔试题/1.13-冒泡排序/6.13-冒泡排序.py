def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # 标记，表示这一趟是否有交换，优化冒泡排序性能
        swapped = False
        for j in range(0, n - i - 1):
            # 如果当前元素大于下一个元素，则交换它们
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                # 发生了交换，则标记为True
                swapped = True
                # 如果这一趟没有发生交换，说明已经有序，直接退出循环
        if not swapped:
            break
    return arr
