## 7.10-实现一个随机丢球程序界面

### 问题描述

有一个单独窗体程序，实现点击鼠标即释放一个球，并随机碰撞窗体的边框实现弹起行为。

### 示例代码

```python
import tkinter as tk
import random

class Ball:
    def __init__(self, canvas, x, y, radius):
        self.canvas = canvas
        self.radius = radius
        self.x = x
        self.y = y
        self.dx = random.choice([-2, 2])  # 随机初始水平速度
        self.dy = random.choice([-2, 2])  # 随机初始垂直速度
        self.ball = canvas.create_oval(x - radius, y - radius, 
                                        x + radius, y + radius, 
                                        fill="blue")
    
    def move(self):
        # 移动球
        self.canvas.move(self.ball, self.dx, self.dy)
        # 获取球的当前坐标
        pos = self.canvas.coords(self.ball)
        if pos[0] <= 0 or pos[2] >= self.canvas.winfo_width():  # 碰撞左边或右边
            self.dx = -self.dx  # 水平速度取反
        if pos[1] <= 0 or pos[3] >= self.canvas.winfo_height():  # 碰撞上边或下边
            self.dy = -self.dy  # 垂直速度取反
        
        # 继续移动
        self.canvas.after(20, self.move)  # 每20毫秒继续移动

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("随机丢球程序")
        self.canvas = tk.Canvas(root, width=600, height=400, bg="white")
        self.canvas.pack()

        self.canvas.bind("<Button-1>", self.throw_ball)  # 绑定鼠标左键点击事件
        
    def throw_ball(self, event):
        ball_radius = 15  # 球的半径
        ball = Ball(self.canvas, event.x, event.y, ball_radius)
        ball.move()  # 开始移动

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
```

