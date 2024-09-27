# 3.13-统计指定日期数量

### 问题描述

现有一份数据包含time字段，包含了年/月/日 小时:分钟，但是客户更关心指定日期的数据量，不在意具体的时间点，现需要对以下csv文件进行处理。

### 输入csv示例

| id | username | time |
| --- | --- | --- |
| 1 | Alice | 2023/12/23 8:28 |
| 2 | Bob | 2023/12/23 19:01 |
| 3 | Charlie | 2023/12/24 7:01 |
| 4 | David | 2023/12/25 12:19 |
| 5 | Eve | 2023/12/25 13:01 |
| 6 | Fank | 2023/12/26 1:33 |

### 输出示例

```python
2023年12月25日的数据量: 2
```

### 解答代码

```python
import pandas as pd

# 读取CSV文件
df = pd.read_csv('files/032.csv')

# 将日期列转换为日期类型
df_time = pd.to_datetime(df['time'])

# 指定日期
year = 2023
month = 12
day = 25

# 筛选出2023年12月25日的数据
december_data = df[(df_time.dt.year == year) & (df_time.dt.month == month) & (df_time.dt.day == day)]

print(f"{year}年{month}月{day}日的数据量: {len(december_data)}")
```