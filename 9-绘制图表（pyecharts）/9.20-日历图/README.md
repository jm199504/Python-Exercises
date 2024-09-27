## 9.20-日历图

### 问题描述

（1）生成数据集

（2）绘制日历图

### 示例输出

<img src="https://github.com/jm199504/Python-Exercises/blob/master/9-%E7%BB%98%E5%88%B6%E5%9B%BE%E8%A1%A8%EF%BC%88pyecharts%EF%BC%89/9.20-%E6%97%A5%E5%8E%86%E5%9B%BE/Figure_1.jpg?raw=true" style="zoom:80%;" />

### 示例代码

```python
# 导入 datetime 模块，用于处理日期和时间
import datetime

# 导入 random 模块，用于生成随机数
import random

# 导入 pyecharts 的 options 和 Calendar 模块
from pyecharts import options as opts
from pyecharts.charts import Calendar

# 设置开始日期和结束日期
begin = datetime.date(2017, 1, 1)
end = datetime.date(2017, 12, 31)

# 生成数据，包括日期和随机步数
data = [
    [str(begin + datetime.timedelta(days=i)), random.randint(1000, 25000)]
    for i in range((end - begin).days + 1)
]

# 创建 Calendar 实例
c = Calendar()

# 添加数据到图表
c.add("", data, calendar_opts=opts.CalendarOpts(range_="2017"))

# 设置全局选项，包括标题和可视化映射
c.set_global_opts(
    # 设置图表标题
    title_opts=opts.TitleOpts(title="Calendar-2017年微信步数情况"),
    # 设置可视化映射的最大值和最小值
    visualmap_opts=opts.VisualMapOpts(
        max_=20000,
        min_=500,
        orient="horizontal",
        is_piecewise=True,
        pos_top="230px",
        pos_left="100px",
    )
)

# 在 Jupyter notebook 上渲染图表
c.render_notebook()
```