## 1.4-排列组合

### 问题描述

提供三个字符，比如：a、b、c，需要输出所有组合情况，组合里可重复字符。

### 示例输入

```text
a,b,c
```

### 示例输出（可重复）

```text
a,a,a
a,a,b
a,a,c
a,b,a
a,b,b
a,b,c
a,c,a
a,c,b
a,c,c
b,a,a
b,a,b
b,a,c
b,b,a
b,b,b
b,b,c
b,c,a
b,c,b
b,c,c
c,a,a
c,a,b
c,a,c
c,b,a
c,b,b
c,b,c
c,c,a
c,c,b
c,c,c
```

### 示例代码（itertools库）

`itertools`模块提供了一些函数来生成排列、组合和笛卡尔积等操作。

```python
from itertools import permutations

def get_all_permutations(elements, length):
    all_permutations = []
    for p in permutations(elements, length):
        all_permutations.append(''.join(p))
    return all_permutations

# 测试代码
elements = 'abc'
length = 3

permutations = get_all_permutations(elements, length)

for permutation in permutations:
    print(permutation)
```

### 示例代码（递归）

递归是一种通过将问题分解为更小的子问题来解决复杂问题的方法。

`find_combinations` 函数是实现递归的主要函数。它接受四个参数：

- `elements`：表示待组合的元素集合。
- `length`：表示期望的组合长度。
- `current_combination`：当前正在形成的组合。
- `all_combinations`：用于存储所有找到的组合的列表。

递归的边界条件是 `length` 为 0，当 `length` 为 0 时，将当前组合添加到 `all_combinations` 列表中。

在主函数 `get_all_combinations` 中，它初始化了空的 `all_combinations` 列表，并调用 `find_combinations` 函数来找到所有组合。

```python
def find_combinations(elements, length, current_combination, all_combinations):
    if length == 0:
        all_combinations.append(','.join(current_combination))
        return

    for element in elements:
        current_combination.append(element)
        find_combinations(elements, length - 1, current_combination, all_combinations)
        current_combination.pop()

def get_all_combinations(elements, length):
    all_combinations = []
    find_combinations(elements, length, [], all_combinations)
    return all_combinations

# 测试代码
elements = 'abc'
length = 3

combinations = get_all_combinations(elements, length)

for combination in combinations:
    print(combination)
```