import numpy as np
import matplotlib.pyplot as plt

# 生成随机数据
x = np.arange(1, 6)
y = np.array([2, 4, 5, 3, 6])
error = np.array([0.5, 0.8, 0.3, 0.7, 0.6])

# 绘制误差棒图
plt.errorbar(x, y, yerr=error, fmt='o', capsize=3)

# 显示图形
plt.show()