import matplotlib.pyplot as plt
import numpy as np

# 生成数据集
x = np.linspace(-3, 3, 50)  # 创建一个包含等间距数值的数组
y1 = 2 * x + 1
y2 = x ** 2

# 设置画布
plt.figure()

# 绘制折线图
l1, = plt.plot(x, y2)

# color表示线图颜色，linewidth表示线图粗细，linestyle表示线图样式（可选：'-.' ':'）
l2, = plt.plot(x, y1, color='red', linewidth=1.0, linestyle='--')

# 设置图例说明
plt.legend(handles=[l1, l2, ], labels=['aaa', 'bbb'], loc='upper left')

# 限制坐标轴的范围
plt.xlim((-1, 2))
plt.ylim((-2, 3))

# 为坐标轴重命名
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# 避免负号显示为方块
plt.rcParams['axes.unicode_minus'] = False

# 设置图表标题
plt.title('Plot')

# 设置新的坐标轴显示
new_ticks = np.linspace(-1, 2, 5)
plt.xticks(new_ticks)

# 设置坐标轴显示时使用r字体更好看，\ 表空格
plt.yticks([-2, -1.8, -1, 1.22, 3],
           [r'$very\ bad$',
            '$bad$',
            '$normal$',
            '$good$',
            r'$very\ good$'])

# 获取画布的坐标轴
ax = plt.gca()

# 设置右侧/顶部边框为空
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

# 设置“原点”坐标
ax.spines['bottom'].set_position(('data', 0))
ax.spines['left'].set_position(('data', 0))

# 显示图表
plt.show()
