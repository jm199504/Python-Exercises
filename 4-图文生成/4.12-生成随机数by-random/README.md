## 4.12-生成随机数by-random

### 1. 生成随机整数

- **方法**: `random.randint(a, b)`
- **功能**: 生成一个在 `[a, b]` 范围内的随机整数。

```python
import random

# 生成一个介于 1 和 10 之间的随机整数（包括 1 和 10）
random_int = random.randint(1, 10)
print(random_int)
```

### 2. 生成随机浮点数

- **方法**: `random.uniform(a, b)`
- **功能**: 生成一个在 `[a, b]` 范围内的随机浮点数。

```python
import random

# 生成一个介于 1.5 和 5.5 之间的随机浮点数
random_float = random.uniform(1.5, 5.5)
print(random_float)
```

### 3. 从序列中随机选择一个元素

- **方法**: `random.choice(seq)`
- **功能**: 从序列 `seq` 中随机选择一个元素。

```python
import random

# 从列表中随机选择一个元素
items = ['apple', 'banana', 'cherry']
random_choice = random.choice(items)
print(random_choice)
```

### 4. 随机打乱序列中的元素

- **方法**: `random.shuffle(seq)`
- **功能**: 打乱序列 `seq` 中的元素顺序，修改原序列。

```python
import random

# 随机打乱列表中的元素
items = [1, 2, 3, 4, 5]
random.shuffle(items)
print(items)
```

### 5. 生成指定范围内的随机浮点数（区间为半开区间）

- **方法**: `random.random()`
- **功能**: 生成一个在 `[0.0, 1.0)` 范围内的随机浮点数。

```python
import random

# 生成一个介于 0 和 1 之间的随机浮点数
random_value = random.random()
print(random_value)
```

### 6. 生成随机数序列

- **方法**: `random.sample(population, k)`
- **功能**: 从 `population` 中随机选择 `k` 个独立的元素。

```python
import random

# 从列表中随机选择 3 个独立的元素
items = [1, 2, 3, 4, 5, 6]
random_sample = random.sample(items, 3)
print(random_sample)
```

### 7. 生成随机种子

- **方法**: `random.seed(a=None)`
- **功能**: 设置随机数生成器的种子，使得后续生成的随机数序列可预测。

```python
import random

# 设置随机种子
random.seed(42)

# 生成随机整数
print(random.randint(1, 10))
```

通过设置相同的种子，后续生成的随机数序列将会相同，这在调试时非常有用。

### 8. 生成范围内的随机数（指定步长）

- **方法**: `random.randrange(start, stop[, step])`
- **功能**: 从指定范围 `[start, stop)` 内生成一个随机整数，可以指定步长 `step`。

```python
import random

# 生成一个介于 0 和 10 之间，步长为 2 的随机整数
random_range = random.randrange(0, 10, 2)
print(random_range)
```

这些是 `random` 模块的一些常见用法。根据具体的需求，你可以选择合适的方法来生成所需的随机数或随机化数据。
