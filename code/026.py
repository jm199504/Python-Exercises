import pandas as pd

# 读取CSV文件
data = pd.read_csv('files/026.csv')

# 读取最前5行（head默认后5行）
print('-'*30)
print(data.head())

# 可以指定最前N行
print('-'*30)
print(data.head(3))

# 读取最后5行（tail默认前5行）
print('-'*30)
print(data.tail())

# 可以指定最后N行
print('-'*30)
print(data.tail(3))

# 不输出CSV默认索引
print('-'*30)
print(data.tail().to_string(index=False))

