import pandas as pd

# 读取CSV文件
data = pd.read_csv('files/025.csv')

# 将`language`列的所有字符串转换为小写字母
data['language'] = data['language'].str.lower()

# 使用value_counts方法计算每种编程语言的使用人数
language_counts = data['language'].value_counts()

# 按照使用人数降序排序
language_counts_sorted = language_counts.sort_values(ascending=False)

# 输出每种编程语言的使用人数
for language, count in language_counts_sorted.items():
    print(f"编程语言 {language} 的使用人数为 {count} 人。")
