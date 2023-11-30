# 导入math模块中的pi常量（即π）
from math import pi


# 定义一个函数，用于计算球体的表面积
def area(radius):
    # 计算球体的表面积公式为：4πr²，这里用 pi 表示 π 的近似值
    v = 4 * pi * radius ** 2
    return v


# 创建一个包含一些半径值的列表
list_a = [1, 2, 4, 9, 10, 13]

# 使用for循环遍历list_a列表中的每个元素，并进行计算并打印其结果（保留两位小数）
for i in list_a:
    # 调用area函数进行计算，同时使用round函数将结果保留两位小数
    print(round(area(i), 2))
