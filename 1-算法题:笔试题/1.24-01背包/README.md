## 1.24-01背包

### 问题描述
输入两个整数*n,m ,n表示你拥有的积分，m表示有多少礼品，接下来有m行，每行a和b，a表示物品所需要消耗的积分，b表示这个物品大家的喜爱值，a和b取值范围是[1,100]，装入最多的喜爱值。

### 输入示例

```
68 3
69 10
60 1
8 2
```

### 输出示例

```
3
```

### 示例代码

```python
def knapsack(n, m, items):
    """
    解决01背包问题，计算在给定积分下能够获得的最大喜爱值。

    参数:
    n: int - 可用的积分
    m: int - 物品的数量
    items: List[Tuple[int, int]] - 每个物品的 (消耗积分, 喜爱值)

    返回:
    int - 能获得的最大喜爱值
    """
    # 创建一个数组用于存储当前最大喜爱值
    dp = [0] * (n + 1)

    for a, b in items:
        # 从后往前更新，以避免重复使用同一个物品
        for j in range(n, a - 1, -1):
            dp[j] = max(dp[j], dp[j - a] + b)
    
    return dp[n]  # 返回可以获得的最大喜爱值

# 测试函数
def test_knapsack():
    # 测试用例
    n = 68
    m = 3
    items = [(69, 10), (60, 1), (8, 2)]  # (消耗积分, 喜爱值)
    result = knapsack(n, m, items)
    print("Max happiness value:", result)  # 应该输出 3

# 运行测试
test_knapsack()
```

