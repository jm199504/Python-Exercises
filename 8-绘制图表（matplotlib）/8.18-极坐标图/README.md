# 8.18-极坐标图

### 问题描述

（1）生成数据集

（2）绘制极坐标图

### 示例输出

<img src="https://github.com/jm199504/Python-Exercises/blob/master/8-%E7%BB%98%E5%88%B6%E5%9B%BE%E8%A1%A8%EF%BC%88matplotlib%EF%BC%89/8.18-%E6%9E%81%E5%9D%90%E6%A0%87%E5%9B%BE/Figure_1.jpg?raw=true" style="zoom:80%;" />

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