## 1.8-最长连续序列

### 问题描述
给定一个未排序的整数数组 nums ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。
请你设计并实现时间复杂度为 O(n) 的算法解决此问题。

### 实验示例 1

```
输入：nums = [100, 4, 200, 1, 3, 2]
输出：4
```
解释：最长数字连续序列是[1, 2, 3, 4]。它的长度为 4。

### 实验示例 2

```
输入：nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
输出：9
```

### 解答思路

1.去重：使用 `set` 去重，以提高查找效率。
2.遍历集合：对于每个元素，检查它是否是一个连续序列的起点。
3.扩展序列：从每个起点开始，不断检查比当前元素大 1 的元素是否存在，直到序列结束。
4.记录最长序列长度：在每次扩展序列时，记录当前序列的长度，并与已知的最长序列长度进行比较。

### 示例代码

```python
def longest_consecutive(nums):
    """
    找出未排序整数数组中的最长连续序列的长度

    参数：
    nums: List[int] - 未排序的整数数组

    返回：
    int - 最长连续序列的长度
    """
    num_set = set(nums)  # 将数组转换为集合，去重并加速查找
    longest_streak = 0  # 记录最长连续序列的长度

    for num in num_set:
        # 如果 num - 1 不在集合中，说明 num 是一个连续序列的起点
        if num - 1 not in num_set:
            current_num = num
            current_streak = 1

            # 扩展序列，直到找不到下一个连续的数
            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1

            # 更新最长连续序列的长度
            longest_streak = max(longest_streak, current_streak)

    return longest_streak

# 示例测试
print(longest_consecutive([100, 4, 200, 1, 3, 2]))  # 输出: 4
print(longest_consecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))  # 输出: 9
```

