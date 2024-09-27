## 1.22-两数之和

### 问题描述
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那两个整数，并返回它们的数组下标。
你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。

### 输入/输出示例
two_sum 函数接收一个整数列表 nums 和一个目标值 target，并返回两个索引，这两个索引对应的数相加等于目标值。

如果找不到这样的两个数，则抛出一个 ValueError 异常。

### 测试函数

test_two_sum 提供了两个测试用例来验证 two_sum 函数的正确性。

### 示例代码

```python
def two_sum(nums, target):
    """
    找到数组中两个数字的索引，使它们的和等于目标值.

    参数:
    nums: List[int] - 输入的整数数组
    target: int - 目标值

    返回:
    List[int] - 两个数字的索引

    抛出:
    ValueError - 如果没有找到符合条件的两个数字
    """
    num_to_index = {}  # 创建一个字典来保存数字及其对应的索引

    for index, num in enumerate(nums):
        complement = target - num  # 计算需要的补数
        if complement in num_to_index:
            return [num_to_index[complement], index]  # 返回补数的索引和当前索引
        num_to_index[num] = index  # 将当前数字及其索引存入字典

    raise ValueError("No two sum solution found")  # 如果没有找到满足条件的数字，抛出异常

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

    # 测试用例3（异常情况）
    try:
        result = two_sum([3, 3], 6)
        print("Test case 3 passed:", result)  # 应该输出 [0, 1]
    except ValueError as e:
        print("Test case 3 failed:", e)

# 运行测试
test_two_sum()
```

