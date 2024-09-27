# 3.9-哪个语言最多人用

### 问题描述

某一个csv文件，包含了多个字段，包含用户ID、等级、所使用的编程语言，请按照编程语言使用人数降序，并输出各个语言的使用人数。

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

### 输出示例

```python
编程语言 python 的使用人数为 3 人。
编程语言 c++ 的使用人数为 2 人。
编程语言 java 的使用人数为 1 人。
编程语言 go 的使用人数为 1 人。
```

### 示例代码

```python
import pandas as pd

# 读取CSV文件
data = pd.read_csv('files/025.csv')

# 将`language`列的所有字符串转换为小写字母
data['language'] = data['language'].str.lower()

# 使用value_counts方法计算每种编程语言的使用人数
language_counts = data['language'].value_counts()

# 按照使用人数降序排序
language_counts_sorted = language_counts.sort_values(ascending=False)

# 输出每种编程语言的使用人数
for language, count in language_counts_sorted.items():
    print(f"编程语言 {language} 的使用人数为 {count} 人。")
```

