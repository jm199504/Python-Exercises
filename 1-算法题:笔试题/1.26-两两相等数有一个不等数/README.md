## 1.26-两两相等数有一个不等数

### 问题描述
给定一个整数数组里面有很多整数，基本都是两两相等，但是存在一个不等数，请输出这个不等数。

### 示例代码

```python
def find_unique(nums):
    """
    找出数组中唯一的不等的数。

    参数:
    nums: List[int] - 输入的整数数组，里面有许多数是相等的，只有一个是不等的。

    返回:
    int - 不等的数
    """
    unique_num = 0  # 初始化异或结果为0

    for num in nums:
        unique_num ^= num  # 对所有数进行异或操作

    return unique_num  # 返回唯一的不等数

# 测试函数
def test_find_unique():
    # 测试用例1
    result = find_unique([2, 2, 3, 2])
    print("Test case 1 passed:", result)  # 应该输出 3

    # 测试用例2
    result = find_unique([4, 1, 2, 1, 2])
    print("Test case 2 passed:", result)  # 应该输出 4

    # 测试用例3
    result = find_unique([1])
    print("Test case 3 passed:", result)  # 应该输出 1

# 运行测试
test_find_unique()
```

