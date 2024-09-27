## 8.11-联合图

### 问题描述

（1）生成数据集

（2）绘制联合图

### 示例输出

<img src="https://github.com/jm199504/Python-Exercises/blob/master/8-%E7%BB%98%E5%88%B6%E5%9B%BE%E8%A1%A8%EF%BC%88matplotlib%EF%BC%89/8.11-%E8%81%94%E5%90%88%E5%9B%BE/Figure_1.jpg?raw=true" style="zoom:80%;" />

### 示例代码

```python
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 创建一些模拟数据
x = np.random.randn(100)
y = 0.5 * x + np.random.randn(100)

# 创建联合图
sns.jointplot(x=x, y=y, kind='reg', marginal_ticks=False, color='skyblue')

# 显示图
plt.show()
```