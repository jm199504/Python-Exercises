# 5.3-JSON转表格

### 问题描述

小张有一个JSON数据，为了拿给客户看，需要转为Excel格式。

### 示例JSON

```python
[
	{"name": "Alice", "age": 25, "city": "New York"},
	{"name": "Bob", "age": 30, "city": "San Francisco"},
	{"name": "Charlie", "age": 35, "city": "London"}
]
```

### 示例Excel

| name | age |
| --- | --- |
| Alice | 25 |
| Bob | 30 |
| Charlie | 35 |

### 示例代码

需先安装第三方库：`pip install openpyxl`

```python
import json
from openpyxl import Workbook

# 读取 JSON 数据
json_data = '''
[
    {"name": "Alice", "age": 25, "city": "New York"},
    {"name": "Bob", "age": 30, "city": "San Francisco"},
    {"name": "Charlie", "age": 35, "city": "London"}
]
'''

# 解析 JSON 数据
data = json.loads(json_data)

# 创建工作簿和工作表
wb = Workbook()
ws = wb.active

# 将 JSON 数据写入工作表
for row in data:
    ws.append(row.values())

# 保存工作簿到文件
wb.save('data.xlsx')
```

-