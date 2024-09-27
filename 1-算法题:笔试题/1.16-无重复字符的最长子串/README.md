## 1.16-无重复字符的最长子串

### 问题描述
给定一个字符串 s ，请你找出其中不含有重复字符的最长子串的长度。

### 实验示例 1

```
输入：s = "abcabcbb"
输出：3
```
### 实验示例 2

```
输入：s = "bbbbb"
输出：1
```

### 实验示例 3

```
输入：s = "abcdd"
输出：4
```

### 示例代码

```python
def length_of_longest_substring(s: str) -> int:
    """
    查找给定字符串中不含有重复字符的最长子串的长度。

    参数：
    s: str - 输入字符串

    返回：
    int - 不含重复字符的最长子串的长度
    """
    char_index = {}  # 用于存储字符最后一次出现的位置
    left = 0  # 左指针
    max_length = 0  # 记录最大长度

    for right in range(len(s)):
        # 如果字符已经在字典中，并且在左指针之后，更新左指针的位置
        if s[right] in char_index and char_index[s[right]] >= left:
            left = char_index[s[right]] + 1
        
        # 更新字符的最新位置
        char_index[s[right]] = right
        
        # 计算当前窗口的长度，并更新最大长度
        max_length = max(max_length, right - left + 1)

    return max_length

# 示例测试
print(length_of_longest_substring("abcabcbb"))  # 输出: 3
print(length_of_longest_substring("bbbbb"))     # 输出: 1
print(length_of_longest_substring("abcdd"))     # 输出: 4
```

