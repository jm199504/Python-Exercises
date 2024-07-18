import matplotlib.pyplot as plt
import numpy as np

# 创建X轴数据
n = 12
X = np.arange(n)  # [ 0  1  2  3  4  5  6  7  8  9 10 11]

# uniform: 均匀分布随机值（左闭右开）
Y1 = (1 - X / float(n)) * np.random.uniform(0.5, 1.0, n)
Y2 = (1 - X / float(n)) * np.random.uniform(0.5, 1.0, n)

# 绘制条形条，face-color: 表面颜色, edge-color: 边缘颜色
plt.bar(X, +Y1, facecolor='#9999ff', edgecolor='white')
plt.bar(X, -Y2, facecolor='#ff9999', edgecolor='white')

# 设置文字(数字)且确定位置
for x, y in zip(X, Y1):
    # ha: horizontal alignment: 水平对齐
    plt.text(x, y + 0.15, '%.2f' % y, ha='center')
for x, y in zip(X, Y2):
    plt.text(x, -y - 0.15, '-%.2f' % y, ha='center')

# 设置标题
plt.title("Bar")
plt.xlim(-.5, n)
plt.xticks(())
plt.ylim(-1.25, 1.25)
plt.yticks(())

# 显示图表
plt.show()
