# 8.3 柱状图

### 问题描述

（1）生成数据集

```python
n = 12
X = np.arange(n)  # [ 0  1  2  3  4  5  6  7  8  9 10 11]

# 均匀分布随机值
Y1 = (1 - X / float(n)) * np.random.uniform(0.5, 1.0, n)
Y2 = (1 - X / float(n)) * np.random.uniform(0.5, 1.0, n)
```

（2）绘制柱状图，设置柱状位置及颜色等



### 示例输出

<img src="https://github.com/jm199504/Python-Exercises/blob/master/8-%E7%BB%98%E5%88%B6%E5%9B%BE%E8%A1%A8%EF%BC%88matplotlib%EF%BC%89/8.3-%E6%9F%B1%E7%8A%B6%E5%9B%BE/Figure_1.png?raw=true" style="zoom:80%;" />

### 示例代码

```python
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

```