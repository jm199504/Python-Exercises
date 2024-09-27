# 8.16-六边形箱图

### 问题描述

（1）生成数据集

（2）绘制六边形箱图

### 示例输出

<img src="https://github.com/jm199504/Python-Exercises/blob/master/8-%E7%BB%98%E5%88%B6%E5%9B%BE%E8%A1%A8%EF%BC%88matplotlib%EF%BC%89/8.16-%E5%85%AD%E8%BE%B9%E5%BD%A2%E7%AE%B1%E5%9B%BE/Figure_1.jpg?raw=true" style="zoom:80%;" />

### 示例代码

```python
import numpy as np
import matplotlib.pyplot as plt

# 生成随机数据
x = np.random.randn(1000)
y = np.random.randn(1000)

# 绘制六边形箱图
plt.hexbin(x, y, gridsize=20)

# 显示图形
plt.show()
```