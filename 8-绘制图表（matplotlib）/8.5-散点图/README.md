# 8.5-散点图

### 问题描述

（1）生成数据集

（2）绘制散点图

### 示例输出

<img src="https://github.com/jm199504/Python-Exercises/blob/master/8-%E7%BB%98%E5%88%B6%E5%9B%BE%E8%A1%A8%EF%BC%88matplotlib%EF%BC%89/8.5-%E6%95%A3%E7%82%B9%E5%9B%BE/Figure_1.jpg?raw=true" style="zoom:80%;" />

### 示例代码

```python
import matplotlib.pyplot as plt
import numpy as np

# mean: 0 ; std: 1 ; num: n
n = 1024
X = np.random.normal(0, 1, n)
Y = np.random.normal(0, 1, n)
# 设置散点的颜色
T = np.arctan2(Y, X)

# 绘制散点图(s表示size，c表示color，alpha表示不透明度)
plt.scatter(X, Y, s=30, c=T, alpha=0.5)

# 限制坐标轴范围
plt.xlim((-1.5, 1.5))
plt.ylim((-1.5, 1.5))

# 不显示坐标轴
plt.xticks(())
plt.yticks(())

plt.show()

```