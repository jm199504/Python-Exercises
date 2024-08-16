# 8.5 散点图

### 问题描述

（1）生成数据集

（2）绘制散点图

### 示例输出

<img src="?raw=true" style="zoom:80%;" />

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