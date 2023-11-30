import turtle
import random

# 创建屏幕对象
screen = turtle.Screen()

# 创建龟对象
t = turtle.Turtle()

# 设置初始位置和朝向
t.penup()
t.setposition(0, 0)
t.pendown()

# 循环画出5个五角星
for _ in range(5):
    # 生成随机位置和角度
    x = random.randint(-200, 200)
    y = random.randint(-200, 200)
    angle = random.randint(0, 360)

    # 移动到随机位置并设置随机角度
    t.penup()
    t.setposition(x, y)
    t.setheading(angle)
    t.pendown()

    # 画五角星
    for _ in range(5):
        t.forward(100)
        t.right(144)

# 等待点击屏幕才退出
screen.exitonclick()