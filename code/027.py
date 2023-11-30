import pandas as pd


def get_python_coder(file_path):
    # 读取CSV文件
    df = pd.read_csv(file_path)

    # 将编程语言转换为小写，方便比较
    df['language'] = df['language'].str.lower()

    # 筛选出使用Python编程语言的数据
    python_high_users = df[(df['language'] == 'python') & (df['level'] >= 4)]

    print(python_high_users)


# 传入CSV文件的路径
file_path = 'files/027.csv'

# 调用函数进行检查
get_python_coder(file_path)
