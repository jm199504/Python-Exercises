import numpy as np  # 导入numpy库，用于处理数组和数学运算
import seaborn as sns  # 导入seaborn库，用于绘制统计图
import matplotlib.pyplot as plt  # 导入matplotlib库中的pyplot模块，用于绘图

np.random.seed(0)  # 设置随机种子，以确保生成的随机数是可重复的
sns.set()  # 设置seaborn的默认图形样式

# 生成一个10x12的二维数组，其中包含随机生成的均匀分布的浮点数（0到1之间）
uniform_data = np.random.rand(10, 12)

# 创建一个图形对象，设置图形的大小为10x8英寸
plt.figure(figsize=(10, 8))

# 使用seaborn绘制热图
# uniform_data：要绘制的数据矩阵
# vmin=0：热图中的数据最小值显示为0
# vmax=1：热图中的数据最大值显示为1
ax = sns.heatmap(uniform_data, vmin=0, vmax=1)

# 显示图形
plt.show()