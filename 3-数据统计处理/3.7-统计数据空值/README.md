# 3.7-数据空值

### 问题描述

如果你想知道某csv数据文件每一列的信息是否都有完整数据。

### 输入示例文件

| A | B | C |
| --- | --- | --- |
| 1 | 1 | 1 |
|  | 1 | 1 |
| 1 |  | 1 |

### 输出示例结果

```
列   是否有空值
A    True
B    True
C    False
```

### 示例代码

```python
import pandas as pd

def check_csv_columns(file_path):
    # 读取CSV文件
    df = pd.read_csv(file_path)

    # 创建一个字典以保存列名和是否有空值的信息
    result = {}

    # 遍历每一列
    for column in df.columns:
        # 判断当前列是否有空值
        has_null = df[column].isnull().any()

        # 将列名和是否有空值的信息添加到结果字典中
        result[column] = has_null

    return result

# 传入CSV文件的路径
file_path = 'files/020.csv'

# 调用函数进行检查
column_check_result = check_csv_columns(file_path)

# 输出结果
print("列名\t是否有空值")
for column, has_null in column_check_result.items():
    print(f"{column}\t{has_null}")
```

### 输出预览