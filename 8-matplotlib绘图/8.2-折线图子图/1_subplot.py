import matplotlib.pyplot as plt
import numpy as np

# 创建数据
x = np.linspace(0, 2*np.pi, 400)
y1 = np.sin(x)
y2 = np.cos(x)

# 创建一个 2x2 的子图布局，并选择第一个子图
plt.subplot(2, 2, 1)
plt.plot(x, y1, 'b-')  # 绘制正弦函数，蓝色实线
plt.title('Sine Function')  # 添加子图标题
plt.xlabel('x')  # 添加 x 轴标签
plt.ylabel('sin(x)')  # 添加 y 轴标签

# 选择第二个子图
plt.subplot(2, 2, 2)
plt.plot(x, y2, 'r-')  # 绘制余弦函数，红色实线
plt.title('Cosine Function')
plt.xlabel('x')
plt.ylabel('cos(x)')

# 选择第三个子图
plt.subplot(2, 2, 3)
plt.plot(x, y1, 'b-')  # 正弦函数
plt.plot(x, y2, 'r--')  # 余弦函数，红色虚线
plt.title('Sine and Cosine')
plt.xlabel('x')
plt.ylabel('y')

# 选择第四个子图
plt.subplot(2, 2, 4)
plt.plot(x, y1, 'g-')  # 绘制正弦函数，绿色实线
plt.title('Another Sine Function')
plt.xlabel('x')
plt.ylabel('sin(x)')

# 调整子图布局，避免重叠
plt.tight_layout()

# 展示图形
plt.show()
