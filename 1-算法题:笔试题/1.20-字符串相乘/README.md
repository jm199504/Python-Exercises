## 6.20 字符串相乘

### 问题描述
传入一个字符串和一个数值，输出的结果是将字符串重复数值的次数。

### 实验示例 1

```
输入："abc", 3
输出："abcabcabc"
```

### 实验示例 2

```
输入："", 5
输出：""
```

### 示例代码

```python
def repeat_string(s: str, n: int) -> str:
    """
    将字符串重复指定次数。

    参数：
    s: str - 输入的字符串
    n: int - 重复的次数

    返回：
    str - 重复后的字符串
    """
    return s * n  # 使用字符串乘法操作

# 示例测试
print(repeat_string("abc", 3))  # 输出: "abcabcabc"
print(repeat_string("", 5))     # 输出: ""
```

