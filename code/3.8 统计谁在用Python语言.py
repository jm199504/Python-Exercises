import pandas as pd


def get_python_coder(file_path):
    # 读取CSV文件
    df = pd.read_csv(file_path)

    # 将编程语言转换为小写，方便比较
    df['language'] = df['language'].str.lower()

    # 筛选出使用Python编程语言的数据
    python_users = df[df['language'] == 'python']

    # 按等级降序排序
    python_users_sorted = python_users.sort_values(['level', 'id'], ascending=[False, True])

    # 输出结果
    print(python_users_sorted.to_string(index=False))
    # python_users_sorted.to_csv('python_users_sorted.csv', index=False)


# 传入CSV文件的路径
file_path = 'files/024.csv'

# 调用函数进行检查
get_python_coder(file_path)
