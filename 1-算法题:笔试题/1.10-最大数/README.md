## 1.10-最大数

### 问题描述
给定一组非负整数 nums，重新排列每个数的顺序（每个数不可拆分）使之组成一个最大的整数。
注意：输出结果可能非常大，所以你需要返回一个字符串而不是整数。

### 实验示例 1

```
输入：nums = [10, 2]
输出："210"
```
### 实验示例 2

```
输入：nums = [3, 30, 34, 5, 9]
输出："9534330"
```

### 示例代码

```python
from functools import cmp_to_key

def custom_compare(x, y):
    """
    自定义比较函数，用于确定两个数字的顺序
    """
    # 比较两个拼接后的结果
    if x + y > y + x:
        return -1  # x 应该排在 y 前面
    elif x + y < y + x:
        return 1  # y 应该排在 x 前面
    else:
        return 0

def largest_number(nums):
    """
    生成组成最大整数的字符串

    参数：
    nums: List[int] - 非负整数数组

    返回：
    str - 组成的最大整数
    """
    # 将所有数字转为字符串
    nums_str = list(map(str, nums))

    # 使用自定义比较函数进行排序
    nums_str.sort(key=cmp_to_key(custom_compare))

    # 将排序后的数字连接成一个字符串
    result = ''.join(nums_str)

    # 如果结果是 '0'，说明数组都是 0
    return result if result[0] != '0' else '0'

# 示例测试
print(largest_number([10, 2]))  # 输出: "210"
print(largest_number([3, 30, 34, 5, 9]))  # 输出: "9534330"
```

