## 1.18-三数之和

### 问题描述
给你一个整数数组 nums ，判断是否存在三元组 [nums[i], nums[j], nums[k]] 满足 i != j、i != k 且 j != k ，
同时还满足 nums[i] + nums[j] + nums[k] == 0 。请你返回所有和为 0 且不重复的三元组。
注意：答案中不可以包含重复的三元组。

### 实验示例 1

```
输入：nums = [-1, 0, 1, 2, -1, -4]
输出：[[-1, -1, 2], [-1, 0, 1]]
```

### 示例代码

```python
def three_sum(nums):
    """
    查找数组中所有和为零的不重复三元组。

    参数：
    nums: List[int] - 输入的整数数组

    返回：
    List[List[int]] - 和为零的三元组列表
    """
    nums.sort()  # 首先对数组进行排序
    res = []

    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue  # 跳过重复元素

        left, right = i + 1, len(nums) - 1  # 设置双指针
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total < 0:
                left += 1  # 总和小于0，移动左指针向右
            elif total > 0:
                right -= 1  # 总和大于0，移动右指针向左
            else:
                # 找到了一个三元组
                res.append([nums[i], nums[left], nums[right]])
                # 跳过重复的元素
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
    
    return res

# 示例测试
print(three_sum([-1, 0, 1, 2, -1, -4]))  # 输出: [[-1, -1, 2], [-1, 0, 1]]
```

