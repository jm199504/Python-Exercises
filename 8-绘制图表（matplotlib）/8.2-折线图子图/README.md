# 8.2-折线子图

### 问题描述

（1）生成数据集

```python
x = np.linspace(0, 2*np.pi, 400)
y1 = np.sin(x)
y2 = np.cos(x)
```

（2）绘制折线四个图

- sin函数（搭配蓝色实线）
- cos函数（搭配红色实线）
- sin函数+cos函数（搭配蓝色实线和红色虚线）
- sin函数（搭配绿色实线）

### 示例输出

<img src="https://github.com/jm199504/Python-Exercises/blob/master/8-%E7%BB%98%E5%88%B6%E5%9B%BE%E8%A1%A8%EF%BC%88matplotlib%EF%BC%89/8.2-%E6%8A%98%E7%BA%BF%E5%9B%BE%E5%AD%90%E5%9B%BE/Figure_1.png?raw=true" style="zoom:80%;" />

### 示例代码

```python
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

```