# 8.19-误差棒图

### 问题描述

（1）生成数据集

（2）绘制误差棒图

### 示例输出

<img src="https://github.com/jm199504/Python-Exercises/blob/master/8-%E7%BB%98%E5%88%B6%E5%9B%BE%E8%A1%A8%EF%BC%88matplotlib%EF%BC%89/8.19-%E8%AF%AF%E5%B7%AE%E6%A3%92%E5%9B%BE/Figure_1.jpg?raw=true" style="zoom:80%;" />

### 示例代码

```python
import numpy as np
import matplotlib.pyplot as plt

# 生成随机数据
x = np.arange(1, 6)
y = np.array([2, 4, 5, 3, 6])
error = np.array([0.5, 0.8, 0.3, 0.7, 0.6])

# 绘制误差棒图
plt.errorbar(x, y, yerr=error, fmt='o', capsize=3)

# 显示图形
plt.show()
```