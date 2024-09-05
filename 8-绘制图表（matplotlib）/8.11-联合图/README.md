# 8.11-联合图

### 问题描述

（1）生成数据集

（2）绘制联合图

### 示例输出

<img src="?raw=true" style="zoom:80%;" />

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