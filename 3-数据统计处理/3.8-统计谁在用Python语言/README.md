# 3.8-统计谁在用Python

### 问题描述

某一个csv文件，包含了多个字段，包含用户ID、等级、所使用的编程语言，现输出有谁在用Python这一门语言，并且希望按照等级降序输出显示，若等级相同时，请按照用户ID升序，注意大小写忽略。

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
| 4 | 7 | python |
| 2 | 4 | Python |
| 7 | 2 | Python |

### 示例代码

（1）读取CSV文件

（2）将language这一列的字符串统一转为小写

（3）过滤出language这一列的字符串为`python`

（4）按照等级降序、ID升序排序

（5）打印过滤结果

```python
import pandas as pd

def get_python_coder(file_path):
    # 读取CSV文件
    df = pd.read_csv(file_path)

    # 将编程语言转换为小写，方便比较
    df['language'] = df['language'].str.lower()

    # 筛选出使用Python编程语言的数据
    python_users = df[df['language'] == 'python']

    # 按等级降序、ID升序排序
    python_users_sorted = python_users.sort_values(['level', 'id'], ascending=[False, True])

    # 输出结果
    print(python_users_sorted)

# 传入CSV文件的路径
file_path = 'files/024.csv'

# 调用函数进行检查
get_python_coder(file_path)
```

注意执行上述代码后，输出效果如下：

```python
id  level language
3   4      7   python
1   2      4   python
6   7      2   python
```

问题：为什么会多一列数字？

解答：因为在输出结果时默认会显示DataFrame的索引列，导致多出了一个`id`列

（6）优化输出：将输出结果转string并将索引隐藏

```python
print(python_users_sorted.to_string(index=False))
```

（7）若希望将输出结果转为CSV文件输出，使用下行代码替换`print()`

```python
python_users_sorted.to_csv('python_users_sorted.csv', index=False)
```

### 效果预览

![Untitled](024_%E7%BB%9F%E8%AE%A1%E8%B0%81%E5%9C%A8%E7%94%A8Python%207d9bc34a6b3847b6869d040b659379a8/Untitled.png)