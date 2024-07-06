# 3.10 仅读前/后几行数据

### 问题描述

某一个csv文件，包含了多个字段，包含用户ID、等级、所使用的编程语言，现需要仅读取前几行数据，或者后几行数据。

### 输入示例

| id | level | language |
| --- | --- | --- |
| 1 | 6 | Java |
| 2 | 4 | Python |
| 3 | 8 | C++ |
| 4 | 7 | python |
| 5 | 1 | Go |
| 6 | 2 | C++ |
| 7 | 2 | Python |

### 输出示例（eg.前三行）

| id | level | language |
| --- | --- | --- |
| 1 | 6 | Java |
| 2 | 4 | Python |
| 3 | 8 | C++ |

### 示例代码

```python
import pandas as pd

# 读取CSV文件
data = pd.read_csv('files/026.csv')

# 读取最前5行（head默认后5行）
print('-'*30)
print(data.head())

# 可以指定最前N行
print('-'*30)
print(data.head(3))

# 读取最后5行（tail默认前5行）
print('-'*30)
print(data.tail())

# 可以指定最后N行
print('-'*30)
print(data.tail(3))

# 不输出CSV默认索引
print('-'*30)
print(data.tail().to_string(index=False))
```

### 输出预览

```python
------------------------------
   id  level language
0   1      6     Java
1   2      4   Python
2   3      8      C++
3   4      7   python
4   5      1       Go
------------------------------
   id  level language
0   1      6     Java
1   2      4   Python
2   3      8      C++
------------------------------
   id  level language
2   3      8      C++
3   4      7   python
4   5      1       Go
5   6      2      C++
6   7      2   Python
------------------------------
   id  level language
4   5      1       Go
5   6      2      C++
6   7      2   Python
------------------------------
 id  level language
  3      8      C++
  4      7   python
  5      1       Go
  6      2      C++
  7      2   Python
```