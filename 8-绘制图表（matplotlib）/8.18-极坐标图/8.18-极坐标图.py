import numpy as np
import matplotlib.pyplot as plt

# 生成随机角度和极径数据
theta = np.linspace(0, 2 * np.pi, 100)
r = np.random.rand(100)

# 绘制极坐标图
plt.polar(theta, r)

# 显示图形
plt.show()