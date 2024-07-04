# 3.11 统计Python高阶玩家

### 问题描述

某一个csv文件，包含了多个字段，包含用户ID、等级、所使用的编程语言，现需要输出编程语言（language）使用Python并且等级（level）≥4的用户信息。

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

| id | level | language |
| --- | --- | --- |
| 2 | 4 | Python |
| 4 | 7 | python |

### 示例代码

可以通过`df[(df[列A] == “XX”) & df[列B] ≥ Y]`进行解决

```python
import pandas as pd

def get_python_coder(file_path):
    # 读取CSV文件
    df = pd.read_csv(file_path)

    # 将编程语言转换为小写，方便比较
    df['language'] = df['language'].str.lower()

    # 筛选出使用Python编程语言的数据
    python_high_users = df[(df['language'] == 'python') & (df['level'] >= 4)]

    print(python_high_users)

# 传入CSV文件的路径
file_path = 'files/024.csv'

# 调用函数进行检查
get_python_coder(file_path)
```