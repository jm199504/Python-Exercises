import json

data = {
    'name': 'ACME',
    'shares': 100,
    'price': 542.23
}
print(data)

# 将Python对象转换为JSON字符串
json_str = json.dumps(data, indent=4)
print(json_str)
print(type(json_str))

# 将JSON格式的字符串转换为dict对象
data2 = json.loads(json_str)
print(data2)
print(type(data2))

# 将dict对象存储为JSON文件
with open('data.json', 'w') as f:
    json.dump(data, f)

# 从JSON文件读取数据
with open('data.json', 'r') as f:
    data3 = json.load(f)