## 1.19-回文数

### 问题描述
判断一个数字是否为回文数，如果从左边和右边读的结果是一样的则是回文数，若为回文数返回True，反之返回False。

### 实验示例 1
```
输入：nums = 121
输出：True
```

### 实验示例 2

```
输入：nums = 10
输出：False
```

### 示例代码

```python
def is_palindrome(x: int) -> bool:
    """
    判断一个数字是否为回文数。

    参数：
    x: int - 输入的整数

    返回：
    bool - 如果是回文数返回 True，否则返回 False
    """
    # 负数和以0结尾但不是0的正数都不是回文数
    if x < 0 or (x % 10 == 0 and x != 0):
        return False
    
    reversed_number = 0
    original = x
    
    while x > 0:
        # 取个位数并添加到反转的数字中
        reversed_number = reversed_number * 10 + x % 10
        x //= 10  # 去掉个位数

    return original == reversed_number

# 示例测试
print(is_palindrome(121))  # 输出: True
print(is_palindrome(10))   # 输出: False
```

