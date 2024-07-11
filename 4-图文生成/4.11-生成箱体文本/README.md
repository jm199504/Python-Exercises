## 4.11 生成箱体文本

### 问题描述
针对英文文本用箱体包裹的样式，用于标识关键信息。

### 输入示例

```python
config = {
    "Field1": "Value1",
    "LongField2": "Value2",
    "Field3": "Value3"
}
```



### 输出示例

```
╔════════════════════╗
║ Field1:     Value1 ║
║ LongField2: Value2 ║
║ Field3:     Value3 ║
╚════════════════════╝
```



### Python示例代码
```python
def print_config_box(config):
    # 计算配置信息的最大长度
    max_length = max(len(str(key))+len(str(config[key])) for key in config.keys())

    # 打印顶部边框
    top = "╔" + "═" * (max_length + 4) + "╗"
    print(top)

    # 打印配置字段信息
    for key, value in config.items():
        padding = " " * (len(top) - len(str(key)) - len(str(value)) - 6)
        print("║ " + key + ": " + padding + str(value) + " ║")

    # 打印底部边框
    print("╚" + "═" * (max_length + 4) + "╝")


# 示例配置字段
config = {
    "Field1": "Value1",
    "LongField2": "Value2",
    "Field3": "Value3"
}

# 打印输出框
print_config_box(config)

```

