## 5.4 JSON转字典 & 字典转JSON

## 问题描述

将dict对象和string对象互转；将dict对象存储到JSON文件，从JSON文件读取dict数据

### Python示例代码

有一份dict变量，通过`print()`输出，但是呈现的不够层次清晰

```python
data = {
    'name': 'ACME',
    'shares': 100,
    'price': 542.23
}

print(data)

# {'name': 'ACME', 'shares': 100, 'price': 542.23}
```

可以通过`json.dumps()`将Python对象转换为JSON字符串，通过`indent`参数可以更好地输出层次关系

```python
json_str = json.dumps(data, indent=4)
print(json_str)
print(type(json_str))

"""
{
    "name": "ACME",
    "shares": 100,
    "price": 542.23
}
<class 'str'>
"""
json.loads()`函数则将`JSON格式的字符串`转换为dict`对象
data2 = json.loads(json_str)
print(data2)
print(type(data2))

# {'name': 'ACME', 'shares': 100, 'price': 542.23}
# <class 'dict'>
```

将dict对象存储为JSON文件

```python
with open('data.json', 'w') as f:
    json.dump(data, f)
```

从JSON文件读取数据

```python
with open('data.json', 'r') as f:
    data3 = json.load(f)
```

总结一下

（1）`dict对象` —`json.dumps()`—>`string对象`

（2）`string对象` —`json.loads()`—>`dict对象`

（3）`dict对象`—`json.dump()`—>`JSON文件`

（4）`JSON文件`—`json.load()`—>`dict对象`