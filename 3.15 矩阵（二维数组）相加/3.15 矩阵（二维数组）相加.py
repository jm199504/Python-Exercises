# 使用+

# 相加的两个矩阵
matrix_A = [
    [1, 2, 3],
    [4, 5, 6],
]

matrix_B = [
    [7, 8, 9],
    [10, 11, 12],
]

# 定义一个函数计算矩阵相加
def matrix_add(matrix1, matrix2):
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[i])):
            row.append(matrix1[i][j] + matrix2[i][j])
        result.append(row)
    return result

# 调用函数计算两个矩阵相加
result = matrix_add(matrix_A, matrix_B)

# 输出结果
for row in result:
    print(row)



# 使用numpy

import numpy as np

# 相加的两个矩阵
matrix_A = np.array([
    [1, 2, 3],
    [4, 5, 6],
])

matrix_B = np.array([
    [7, 8, 9],
    [10, 11, 12],
])

# 计算矩阵相加
result = matrix_A + matrix_B

# 输出结果
print(result)