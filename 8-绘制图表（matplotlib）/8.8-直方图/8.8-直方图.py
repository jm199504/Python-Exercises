import matplotlib.pyplot as plt

# 直方图
# 直方图非常像条形图，倾向于通过将区段组合在一起来显示分布。 这个例子可能是年龄的分组，或测试的分数。
# 我们并不是显示每一组的年龄，而是按照 20 ~ 25，25 ~ 30... 等等来显示年龄。
# population_ages = [22,55,62,45,21,22,34,42,42,4,99,102,110,120,121,122,130,111,115,112,80,75,65,54,44,43,42,48]
import numpy as np

# 生成数据集
population_ages = np.random.rand(50) * 50
bins = np.arange(len(population_ages))
# 绘制直方图
# histtype可选： {‘bar’, ‘barstacked’, ‘step’, ‘stepfilled’}
plt.hist(population_ages, bins, histtype='stepfilled', rwidth=0.8)
# 设置坐标轴名称
plt.xlabel('x')
plt.ylabel('y')
plt.title('Hist Graph')
# 生成备注
plt.legend()
plt.show()
