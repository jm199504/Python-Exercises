## 8.7 堆叠图

### 问题描述

（1）生成数据集

（2）绘制堆叠图

### 示例输出

<img src="https://github.com/jm199504/Python-Exercises/blob/master/8-%E7%BB%98%E5%88%B6%E5%9B%BE%E8%A1%A8%EF%BC%88matplotlib%EF%BC%89/8.7-%E5%A0%86%E5%8F%A0%E5%9B%BE/Figure_1.jpg?raw=true" style="zoom:80%;" />

### 示例代码

```python
import matplotlib.pyplot as plt

# 堆叠图
# 堆叠图用于表示部分相对整体而言随时间的关系。堆叠图基本上类似于饼图，只是随时间而变化。
# eg:我们一天有 24 小时，想看看每天如何花费时间，现将日常活动分为：睡觉，吃饭，工作和玩耍。

# 创建数据集
# 假设在一天当中记录五次
days = [1, 2, 3, 4, 5]
sleeping = [7, 8, 6, 11, 7]
eating = [2, 3, 4, 3, 2]
working = [7, 8, 7, 2, 2]
playing = [8, 5, 7, 8, 13]

# 绘制堆叠图
plt.stackplot(days, sleeping, eating, working, playing, colors=['m', 'c', 'r', 'k'])

# 设置坐标轴名称
plt.xlabel('Time')
plt.ylabel('Cost Time')
plt.title('Stacked Graph')
plt.show()

```