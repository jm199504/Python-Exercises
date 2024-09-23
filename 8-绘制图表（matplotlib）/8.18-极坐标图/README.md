# 8.18-极坐标图

### 问题描述

（1）生成数据集

（2）绘制极坐标图

### 示例输出

<img src="?raw=true" style="zoom:80%;" />

### 示例代码

```python
import numpy as np
import matplotlib.pyplot as plt

# 生成随机角度和极径数据
theta = np.linspace(0, 2 * np.pi, 100)
r = np.random.rand(100)

# 绘制极坐标图
plt.polar(theta, r)

# 显示图形
plt.show()
```