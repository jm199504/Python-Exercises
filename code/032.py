import pandas as pd

# 读取CSV文件
df = pd.read_csv('files/032.csv')

# 将日期列转换为日期类型
df_time = pd.to_datetime(df['time'])

# 指定日期
year = 2023
month = 12
day = 25

# 筛选出2023年12月25日的数据
december_data = df[(df_time.dt.year == year) & (df_time.dt.month == month) & (df_time.dt.day == day)]

print(f"{year}年{month}月{day}日的数据量: {len(december_data)}")
