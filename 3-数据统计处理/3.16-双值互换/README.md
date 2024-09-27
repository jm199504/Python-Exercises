## 3.16-双值互换

提供多种方法实现a和b变量值互换

### 问题描述

将两个变量的值进行互换

### 示例输入

```python
a = 1
b = 2
```

### 示例输出

```python
a = 2
b = 1
```

### 示例代码（借助第三变量）

```python
a = 1
b = 2
temp = a
a = b
b = temp
print(a, b)  # 输出: 2, 1
```

### 示例代码（加减法）

注意该方法仅限于integer类型变量

```python
a = 1
b = 2
a = a + b
b = a - b
a = a - b
print(a, b)  # 输出: 2, 1
```

### 示例代码（使用异或操作）

```python
a = 1
b = 2
a = a ^ b
b = a ^ b
a = a ^ b
print(a, b)  # 输出: 2, 1
```

### 示例代码（元组解包交换）

```python
a = 1
b = 2
a, b = b, a
print(a, b)  # 输出: 2, 1
```