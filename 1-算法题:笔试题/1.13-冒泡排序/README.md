## 1.13-冒泡排序

### 问题描述
给你一个整数数组 nums ，使用冒泡排序对 nums 进行排序。

### 实验示例 1

```
输入：nums = [3, 6, 8, 10, 1, 2, 1]
输出：[1, 1, 2, 3, 6, 8, 10]
```
### 实验示例 2
```
输入：nums = [3, 6, 8, 10, 1, 2, 1, 5]
输出：[1, 1, 2, 3, 5, 6, 8, 10]
```

### 示例代码

```python
def bubbleSort(nums):
    """
    对数组进行冒泡排序

    参数：
    nums: List[int] - 待排序数组

    返回：
    List[int] - 排序后的数组
    """
    n = len(nums)
    
    # 进行 n-1 次遍历
    for i in range(n):
        # 设置一个标志位，优化检查是否需要继续
        swapped = False

        # 每次遍历最后 i 个元素已经排序好了，无需再检查
        for j in range(0, n - 1 - i):
            if nums[j] > nums[j + 1]:
                # 交换相邻元素
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                swapped = True  # 标记发生交换

        # 如果没有发生交换，则数组已经是有序的，可以提前退出
        if not swapped:
            break

    return nums

# 示例测试
nums1 = [3, 6, 8, 10, 1, 2, 1]
sorted_nums1 = bubbleSort(nums1)
print(sorted_nums1)  # 输出: [1, 1, 2, 3, 6, 8, 10]

nums2 = [3, 6, 8, 10, 1, 2, 1, 5]
sorted_nums2 = bubbleSort(nums2)
print(sorted_nums2)  # 输出: [1, 1, 2, 3, 5, 6, 8, 10]
```

