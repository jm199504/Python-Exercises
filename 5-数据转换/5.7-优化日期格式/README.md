# 5.7-优化日期格式

### 问题描述

有一份CSV文件，其中的日期格式统一为mm/dd/yyyy，但是这种看起来并不清晰，小领导期望将日期格式统一转为YYYY年mm月dd日。

### 示例原始CSV文件

| id | username | date |
| --- | --- | --- |
| 1 | Alice | 01/31/2022 |
| 2 | Bob | 02/15/2022 |
| 3 | Charlie | 03/07/2022 |

### 示例输出CSV文件

| id | username | date |
| --- | --- | --- |
| 1 | Alice | 2022年01月31日 |
| 2 | Bob | 2022年02月15日 |
| 3 | Charlie | 2022年03月07日 |

### 示例代码

```python
import pandas as pd

# 读取CSV文件
df = pd.read_csv('files/030.csv')

# 转换日期格式
df['date'] = pd.to_datetime(df['date'], format='%m/%d/%Y').dt.strftime('%Y年%m月%d日')

# 保存为新的CSV文件
df.to_csv('files/030_new.csv', index=False)
```

-