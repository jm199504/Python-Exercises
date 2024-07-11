import pandas as pd


def check_csv_columns(file_path):
    # 读取CSV文件
    df = pd.read_csv(file_path)

    # 创建一个字典以保存列名和是否有空值的信息
    result = {}

    # 遍历每一列
    for column in df.columns:
        # 判断当前列是否有空值
        has_null = df[column].isnull().any()

        # 将列名和是否有空值的信息添加到结果字典中
        result[column] = has_null

    return result


# 传入CSV文件的路径
file_path = 'files/020.csv'

# 调用函数进行检查
column_check_result = check_csv_columns(file_path)

# 输出结果
print("列名\t是否有空值")
for column, has_null in column_check_result.items():
    print(f"{column}\t{has_null}")