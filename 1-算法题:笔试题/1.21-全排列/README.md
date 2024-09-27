## 1.21-全排列

### 问题描述
给定一个不含重复数字的数组 nums ，返回其所有可能的全排列 。你可以按任意顺序返回答案。

### 实验示例 1
```
输入：[1, 2, 3]
输出：[[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 2, 1], [3, 1, 2]]
```

### 示例代码

```python
def permute(nums):
    """
    返回给定数组的所有可能全排列。

    参数：
    nums: List[int] - 输入的整数数组（不含重复数字）

    返回：
    List[List[int]] - 所有可能的全排列
    """
    result = []  # 存储结果
    used = [False] * len(nums)  # 用来标记数字是否被使用

    def backtrack(current_permutation):
        # 如果当前排列的长度等于 nums 的长度，表示已生成一个完整的排列
        if len(current_permutation) == len(nums):
            result.append(current_permutation[:])  # 添加复制的当前排列
            return
        
        for i in range(len(nums)):
            if used[i]:  # 如果 nums[i] 已被使用，跳过
                continue
            
            # 选择 nums[i]
            current_permutation.append(nums[i])
            used[i] = True  # 将 nums[i] 标记为已使用

            # 继续递归
            backtrack(current_permutation)

            # 回溯，撤销选择
            current_permutation.pop()  # 移除最后一个元素
            used[i] = False  # 标记为未使用，允许再次选择

    # 从空的当前排列开始
    backtrack([])
    
    return result

# 示例测试
print(permute([1, 2, 3]))  # 输出: [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
```

