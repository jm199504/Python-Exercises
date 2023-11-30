import pandas as pd

# 读取CSV文件
df = pd.read_csv('files/030.csv')

# 转换日期格式
df['date'] = pd.to_datetime(df['date'], format='%m/%d/%Y').dt.strftime('%Y年%m月%d日')

# 保存为新的CSV文件
df.to_csv('files/030_new.csv', index=False)