## 1.25-两数之和

### 问题描述
给定一个整数数组nums和一个目标值target，请你在该数组中找出和为目标值的那两个整数，并返回他们的数组下标。

### 示例代码

```python
def two_sum(nums, target):
    """
    找出数组中两个数的下标，使它们的和等于目标值。

    参数:
    nums: List[int] - 输入的整数数组
    target: int - 目标值

    返回:
    List[int] - 两个数的下标，如果没有找到则抛出 ValueError。
    """
    num_to_index = {}  # 创建一个字典来存储数字及其索引

    for index, num in enumerate(nums):
        complement = target - num  # 计算目标值所需的补数
        if complement in num_to_index:
            return [num_to_index[complement], index]  # 找到补数，返回其索引
        num_to_index[num] = index  # 存储数字及其索引

    raise ValueError("No two sum solution found")  # 如果没有找到，抛出异常

# 测试函数
def test_two_sum():
    # 测试用例1
    try:
        result = two_sum([2, 7, 11, 15], 9)
        print("Test case 1 passed:", result)  # 应该输出 [0, 1]
    except ValueError as e:
        print("Test case 1 failed:", e)

    # 测试用例2
    try:
        result = two_sum([3, 2, 4], 6)
        print("Test case 2 passed:", result)  # 应该输出 [1, 2]
    except ValueError as e:
        print("Test case 2 failed:", e)

    # 测试用例3
    try:
        result = two_sum([3, 3], 6)
        print("Test case 3 passed:", result)  # 应该输出 [0, 1]
    except ValueError as e:
        print("Test case 3 failed:", e)

# 运行测试
test_two_sum()
```

