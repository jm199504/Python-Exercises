# 8.4 饼图

### 问题描述

（1）生成数据集

（2）绘制饼图

### 示例输出

<img src="?raw=true" style="zoom:80%;" />

### 示例代码

```python
import matplotlib.pyplot as plt

# 设置内容列表
slices = [7, 2, 2, 13]
# 设置对应内容名称
activities = ['sleeping', 'eating', 'working', 'playing']
# 设置对应颜色
cols = ['c', 'm', 'r', 'b']
# 绘制饼图
# startangle: 起始绘制角度,默认图是从x轴正方向逆时针画起,如设定=90则从y轴正方向画起
# shadow: 是否设置阴影效果
# explode: 每一块距离中心距离
# autopct: 设置百分号显示格式
plt.pie(slices,
        labels=activities, colors=cols,
        startangle=90, shadow=True,
        explode=(0, 0.12, 0, 0),
        autopct='%1.2f%%')
# 设置标题
plt.title('Interesting Graph Check it out')
plt.show()

```