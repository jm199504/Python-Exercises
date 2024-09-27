## 1.15-整数反转

### 问题描述
给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转，有效数值范围为 [(−2)^31, 2^31 − 1]，若超出有效数值范围则输出 0。

### 实验示例 1

```
输入：num = 123
输出：321
```
### 实验示例 2

```
输入：num = -123
输出：-321
```

### 实验示例 3
```
输入：num = 1534236469
输出：0
```

### 示例代码

```python
def reverse_integer(num: int) -> int:
    """
    反转一个 32 位有符号整数。

    参数：
    num: int - 待反转整数

    返回：
    int - 反转后的整数，如果超出 32 位范围则返回 0
    """
    # 定义 32 位整数的范围
    INT_MIN, INT_MAX = -2**31, 2**31 - 1
    
    # 记录数字的符号
    sign = -1 if num < 0 else 1
    num *= sign  # 转为正数处理

    # 反转数字
    reversed_num = 0
    while num > 0:
        digit = num % 10  # 获取最后一位数字
        num //= 10  # 去掉最后一位数字
        
        # 检查是否会溢出
        if (reversed_num > (INT_MAX - digit) // 10):
            return 0
        
        reversed_num = reversed_num * 10 + digit  # 添加反转后的数字
        
    return sign * reversed_num  # 恢复符号

# 示例测试
print(reverse_integer(123))          # 输出: 321
print(reverse_integer(-123))         # 输出: -321
print(reverse_integer(1534236469))   # 输出: 0
```

