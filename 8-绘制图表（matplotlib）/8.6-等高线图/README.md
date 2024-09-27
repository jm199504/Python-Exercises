## 8.6-等高线图

### 问题描述

（1）生成数据集

（2）绘制等高线图

### 示例输出

<img src="https://github.com/jm199504/Python-Exercises/blob/master/8-%E7%BB%98%E5%88%B6%E5%9B%BE%E8%A1%A8%EF%BC%88matplotlib%EF%BC%89/8.6-%E7%AD%89%E9%AB%98%E7%BA%BF%E5%9B%BE/Figure_1.jpg?raw=true" style="zoom:80%;" />

### 示例代码

```python
import matplotlib.pyplot as plt
import numpy as np


# 绘制等高线函数
def f(x, y):
    return (1 - x / 2 + x ** 5 + y ** 3) * np.exp(-x ** 2 - y ** 2)


n = 256
x = np.linspace(-3, 3, n)
y = np.linspace(-3, 3, n)
# 互相影响其输出形状的函数
X, Y = np.meshgrid(x, y)

# 其中第三个参数表示分为10个部分，默认为0表示最少分层两部分
plt.contourf(X, Y, f(X, Y), 8, alpha=0.8, cmap=plt.cm.hot)

# 绘制黑白类型的等高线
C = plt.contour(X, Y, f(X, Y), 8, alpha=0.8, colors='black')
# 将其添加标签，使用内置显示和设置字体大小
plt.clabel(C, inline=True, fontsize=10)

plt.xticks(())
plt.yticks(())

plt.show()

```