import pandas as pd

# 读取 JSON 数据
json_data = '''
[
    {"name": "Alice", "age": 25, "city": "New York"},
    {"name": "Bob", "age": 30, "city": "San Francisco"},
    {"name": "Charlie", "age": 35, "city": "London"}
]
'''

# 解析 JSON 数据
df = pd.read_json(json_data)

# 将数据保存为 Excel 文件
df.to_excel('data.xlsx', index=False)
