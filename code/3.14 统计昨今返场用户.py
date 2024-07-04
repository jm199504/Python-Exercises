from collections import defaultdict  # 导入defaultdict字典
from datetime import datetime  # 导入datetime模块

import pandas as pd  # 导入pandas库

# 读取CSV文件
df = pd.read_csv('files/033.csv')

# 按照日期进行排序
df = df.sort_values(by='date', ascending=True)

# 用户名to打卡日期
user2date = {}  # 定义一个空字典，用于存储用户名到打卡日期的映射关系

# 打卡日期to符合条件的用户
date2users = defaultdict(list)  # 定义一个defaultdict字典，用于按照日期存储符合条件的用户列表

# 遍历DataFrame中的每一行数据
for value in df.values:
    # 解析行数据
    username = value[1]
    date_str = value[2]
    date = datetime.strptime(date_str, '%Y/%m/%d')

    # 判断该用户是否符合条件
    if user2date.get(username) and (date - user2date[username]).days == 1:
        date2users[date_str].append(username)

    # 更新用户名到打卡日期的映射关系
    user2date[username] = date

# 输出符合条件的用户
for date, users in date2users.items():
    print(f"{date}的返场用户:{','.join(users)}")  # 将符合条件的用户列表输出
