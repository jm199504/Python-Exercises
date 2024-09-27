## 1.23-最大子数组和

### 问题描述
给你一个整数数组 nums ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和，子数组是数组中的一个连续部分。

### 实验示例 1

```
输入：nums = [-2,1,-3,4,-1,2,1,-5,4]
输出：6
解释：连续子数组 [4,-1,2,1] 的和最大，为 6 。
```

### 实验示例 2

```
输入：nums = [1]
输出：1
```

### 实验示例 3

```
输入：nums = [5,4,-1,7,8]
输出：23
```

### 示例代码

```python
def max_sub_array(nums):
    """
    找到给定整数数组的最大子数组和。

    参数:
    nums: List[int] - 输入的整数数组

    返回:
    int - 最大子数组和
    """
    if not nums:
        return 0  # 如果数组为空，返回0

    current_sum = nums[0]  # 当前子数组的和
    max_sum = nums[0]      # 最大子数组的和

    for num in nums[1:]:
        current_sum = max(num, current_sum + num)  # 更新当前子数组的和
        max_sum = max(max_sum, current_sum)         # 更新最大子数组的和

    return max_sum

# 测试函数
def test_max_sub_array():
    # 测试用例1
    result = max_sub_array([-2, 1, -3, 4, -1, 2, 1, -5, 4])
    print("Test case 1 passed:", result)  # 应该输出 6

    # 测试用例2
    result = max_sub_array([1])
    print("Test case 2 passed:", result)  # 应该输出 1

    # 测试用例3
    result = max_sub_array([5, 4, -1, 7, 8])
    print("Test case 3 passed:", result)  # 应该输出 23

# 运行测试
test_max_sub_array()
```

