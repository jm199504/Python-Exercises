## 1.17-最长公共前缀

### 问题描述
编写一个函数来查找字符串数组中的最长公共前缀。 如果不存在公共前缀，返回空字符串 ""。

### 实验示例 1

```
输入：s = ["flower","flow","flight"]
输出："fl"
```
### 实验示例 2
```
输入：s = ["dog", "racecar", "car"]
输出：""
```

### 示例代码

```python
def longest_common_prefix(strs):
    """
    查找字符串数组中的最长公共前缀。

    参数：
    strs: List[str] - 输入的字符串数组

    返回：
    str - 最长公共前缀
    """
    if not strs:
        return ""

    # 取第一个字符串作为基准
    prefix = strs[0]

    # 遍历字符串数组
    for string in strs[1:]:
        # 尝试更新公共前缀
        while string[:len(prefix)] != prefix and prefix:
            prefix = prefix[:-1]  # 缩短 prefix
        if not prefix:  # 如果 prefix 为空，提前返回
            return ""

    return prefix

# 示例测试
print(longest_common_prefix(["flower", "flow", "flight"]))  # 输出: "fl"
print(longest_common_prefix(["dog", "racecar", "car"]))     # 输出: ""
```

