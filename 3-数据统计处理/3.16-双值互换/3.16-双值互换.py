# 借助第三变量
a = 1
b = 2
temp = a
a = b
b = temp
print(a, b)  # 输出: 2, 1


# 加减法
a = 1
b = 2
a = a + b
b = a - b
a = a - b
print(a, b)  # 输出: 2, 1

# 使用异或操作
a = 1
b = 2
a = a ^ b
b = a ^ b
a = a ^ b
print(a, b)  # 输出: 2, 1

# 元组解包交换
a = 1
b = 2
a, b = b, a
print(a, b)  # 输出: 2, 1