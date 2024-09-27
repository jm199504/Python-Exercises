## 1.14-最长回文子串

### 问题描述
给定一个字符串 s，输出 s 中最长的回文子串，其中回文子串指该子串倒序与正序相同。

### 实验示例 1

```
输入：s = "abccba"
输出："abccba"
```
### 实验示例 2

```
输入：s = "babad"
输出："bab"
```

### 示例代码
```python
def longestPalindrome(s: str) -> str:
    """
    找到给定字符串中的最长回文子串。

    参数：
    s: str - 输入字符串

    返回：
    str - 最长的回文子串
    """
    def expand_from_center(left: int, right: int) -> str:
        # 从中心扩展，返回回文子串
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        # 返回扩展后的回文子串
        return s[left + 1:right]

    longest = ""
    
    for i in range(len(s)):
        # 对于奇数长度的回文（以单个字符为中心）
        odd_palindrome = expand_from_center(i, i)
        # 对于偶数长度的回文（以两个字符为中心）
        even_palindrome = expand_from_center(i, i + 1)
        
        # 更新最长回文子串
        longest = max(longest, odd_palindrome, even_palindrome, key=len)

    return longest

# 示例测试
s1 = "abccba"
result1 = longestPalindrome(s1)
print(result1)  # 输出: "abccba"

s2 = "babad"
result2 = longestPalindrome(s2)
print(result2)  # 输出: "bab" 或 "aba"
