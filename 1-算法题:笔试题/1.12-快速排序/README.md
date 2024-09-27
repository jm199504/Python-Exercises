## 1.12-快速排序

### 问题描述
给你一个整数数组 nums ，使用快速排序对 nums 进行排序。

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
def quicksort(nums):
    """
    对数组进行快速排序

    参数：
    nums: List[int] - 待排序数组

    返回：
    List[int] - 排序后的数组
    """
    # 边界条件：如果数组为空或长度为 1，则直接返回
    if len(nums) <= 1:
        return nums
    
    pivot = nums[len(nums) // 2]  # 选择基准元素
    left = [x for x in nums if x < pivot]  # 小于基准元素的部分
    middle = [x for x in nums if x == pivot]  # 等于基准元素的部分
    right = [x for x in nums if x > pivot]  # 大于基准元素的部分

    # 递归对左边和右边部分进行排序，然后合并
    return quicksort(left) + middle + quicksort(right)

# 示例测试
nums1 = [3, 6, 8, 10, 1, 2, 1]
sorted_nums1 = quicksort(nums1)
print(sorted_nums1)  # 输出: [1, 1, 2, 3, 6, 8, 10]

nums2 = [3, 6, 8, 10, 1, 2, 1, 5]
sorted_nums2 = quicksort(nums2)
print(sorted_nums2)  # 输出: [1, 1, 2, 3, 5, 6, 8, 10]
```

