# 8.14-3D散点图

### 问题描述

（1）生成数据集

（2）绘制3D散点图

### 示例输出

<img src="https://github.com/jm199504/Python-Exercises/blob/master/8-%E7%BB%98%E5%88%B6%E5%9B%BE%E8%A1%A8%EF%BC%88matplotlib%EF%BC%89/8.14-3D%E6%95%A3%E7%82%B9%E5%9B%BE/Figure_1.jpg?raw=true" style="zoom:80%;" />

### 示例代码

```python
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()

# 创建3D坐标系对象
# add_subplot的`111`:表示一个由1行、1列组成的子图网格
# projection='3d':表示要创建的子图类型是三维坐标系
ax = fig.add_subplot(111, projection='3d')

# 准备数据
x = np.random.randn(100)  # 生成100个符合标准正态分布（均值为0，标准差为1）的随机数
y = np.random.randn(100)
z = np.random.randn(100)
# 约95%的值会落在距离均值不超过两个标准差的范围内，因此范围基本聚焦在[-2, 2]之间

# 绘制图像
ax.scatter(x, y, z)

# 显示图像
plt.show()
```