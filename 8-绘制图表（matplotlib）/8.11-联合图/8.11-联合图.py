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