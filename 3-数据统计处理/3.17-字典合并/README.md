## 3.17-字典合并

### 问题描述

Python合并字典

### 示例输入

注：相同key时以使用第二个字典进行覆盖

```text
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
```

### 示例输出

```text
{'a': 1, 'b': 3, 'c': 4}
```

### 示例代码

- 使用字典解包操作符 `*` 来合并字典：

```python
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
merged_dict = {**dict1, **dict2}

print(merged_dict)  
# 输出: {'a': 1, 'b': 3, 'c': 4}
```

- 使用 `update()` 方法合并字典：

```python
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
dict1.update(dict2)
print(dict1)

# 若需要使用新对象存储可考虑copy()方法
dict3 = dict1.copy()
dict3.update(dict2)
```

- 使用 `collections` 模块中的 `ChainMap` 类合并字典：

```python
from collections import ChainMap

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
merged_dict = dict(ChainMap(dict1, dict2))
print(merged_dict)
```

`ChainMap` 是 Python 的 `collections` 模块提供的一种数据结构，用于将多个字典或映射类型组合成一个单独的映射。它可以将多个字典链接在一起，形成一个逻辑上的“链”，当进行键查找时，它会按照链的顺序依次在每个字典中查找，直到找到键为止。

`ChainMap` 的一些特点包括：

1. **支持嵌套**: 可以在 `ChainMap` 中嵌套其他 `ChainMap` 或普通字典。
2. **动态更新**: 如果原始字典发生变化，`ChainMap` 会反映这些变化。
3. **性能高效**: 使用 `ChainMap` 进行键查找的时间复杂度与字典的数量无关，因为它只是在逻辑上将多个字典链接在一起，并不会实际复制字典中的内容。