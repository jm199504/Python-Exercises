import matplotlib.pyplot as plt

# 设置箭头的起点和终点坐标（由[0, 0]->[1, 1]）
x = [0, 1]
y = [0, 1]

# 设置箭头的起始方向和长度
dx = [1]
dy = [1]

# 绘制箭头图
plt.arrow(x[0], y[0], dx[0], dy[0],
          head_width=0.1, head_length=0.1,
          fc='blue', ec='blue')

# 设置坐标轴范围
plt.xlim(-1, 2)
plt.ylim(-1, 2)

# 显示图形
plt.show()