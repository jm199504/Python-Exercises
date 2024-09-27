# 8.17-箭头图

### 问题描述

（1）生成数据集

（2）绘制箭头图

### 示例输出

<img src="https://github.com/jm199504/Python-Exercises/blob/master/8-%E7%BB%98%E5%88%B6%E5%9B%BE%E8%A1%A8%EF%BC%88matplotlib%EF%BC%89/8.17-%E7%AE%AD%E5%A4%B4%E5%9B%BE/Figure_1.jpg?raw=true" style="zoom:80%;" />

### 示例代码

```python
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
```