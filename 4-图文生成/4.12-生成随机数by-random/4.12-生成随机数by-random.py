import random

# 生成一个介于 1 和 10 之间的随机整数（包括 1 和 10）
random_int = random.randint(1, 10)
print(random_int)

# 生成一个介于 1.5 和 5.5 之间的随机浮点数
random_float = random.uniform(1.5, 5.5)
print(random_float)

# 从列表中随机选择一个元素
items = ['apple', 'banana', 'cherry']
random_choice = random.choice(items)
print(random_choice)

# 随机打乱列表中的元素
items = [1, 2, 3, 4, 5]
random.shuffle(items)
print(items)

# 生成一个介于 0 和 1 之间的随机浮点数
random_value = random.random()
print(random_value)

# 从列表中随机选择 3 个独立的元素
items = [1, 2, 3, 4, 5, 6]
random_sample = random.sample(items, 3)
print(random_sample)

# 设置随机种子
random.seed(42)

# 生成随机整数
print(random.randint(1, 10))

# 生成一个介于 0 和 10 之间，步长为 2 的随机整数
random_range = random.randrange(0, 10, 2)
print(random_range)