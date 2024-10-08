# 1.3-画满天五角星

### 问题描述

老师布置了一个作业要小盆友画五角星，并且需要画很多个，但是小明想偷懒，所以准备用Python来画五角星。

### 效果展示

<img src="?raw=true" style="zoom:80%;" />

### 示例代码

（1）笔绘：需要使用到`turtle`第三方库，安装：`pip3 install turtle`

（2）随机：使用`random`内置库

```python
import turtle
import random

# 创建屏幕对象
screen = turtle.Screen()

# 创建龟对象
t = turtle.Turtle()

# 设置初始位置和朝向
t.penup()  # 抬起画笔，不绘制图形
t.setposition(0, 0)  # 设置初始位置为屏幕中心
t.pendown()  # 放下画笔，准备绘制图形

# 循环画出10个五角星
for _ in range(10):
    # 生成随机位置和角度
    x = random.randint(-200, 200)
    y = random.randint(-200, 200)
    angle = random.randint(0, 360)

    # 移动到随机位置并设置随机角度
    t.penup()  # 抬起画笔，不绘制图形
    t.setposition(x, y)  # 移动到随机位置
    t.setheading(angle)  # 设置随机角度
    t.pendown()  # 放下画笔，准备绘制图形

    # 画五角星
    for _ in range(5):
        t.forward(100)  # 前进100个单位长度
        t.right(144)  # 右转144度，绘制五角星的一个角

# 等待点击屏幕才退出
screen.exitonclick()
```

- 使用 `random.randint(a, b)` 函数生成 `a` 到 `b` 之间的随机整数：控制五角星绘制的位置
- 每次循环都生成一个新的随机位置（`x` 和 `y`）以及一个随机角度（`angle`）
- 使用 `t.setposition(x, y)` 将龟移动到随机位置
- 使用 `t.setheading(angle)` 设置随机角度
- 使用嵌套的循环画出五个边长相等的五角星