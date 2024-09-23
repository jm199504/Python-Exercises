# 8.16-六边形箱图

### 问题描述

（1）生成数据集

（2）绘制六边形箱图

### 示例输出

<img src="?raw=true" style="zoom:80%;" />

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