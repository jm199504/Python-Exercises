# 使用字典解包操作符 `*` 来合并字典
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
merged_dict = {**dict1, **dict2}

# 使用 `update()` 方法合并字典
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
dict1.update(dict2)
print(dict1)

# 使用 `collections` 模块中的 `ChainMap` 类合并字典
from collections import ChainMap

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
merged_dict = dict(ChainMap(dict1, dict2))
print(merged_dict)