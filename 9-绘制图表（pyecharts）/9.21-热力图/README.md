# 9.21 热力图

### 问题描述

（1）生成数据集

（2）绘制热力图

### 示例输出

<img src="?raw=true" style="zoom:80%;" />

### 示例代码

```python
# 导入随机数生成模块
import random

# 导入必要模块
from pyecharts import options as opts
from pyecharts.charts import HeatMap
from pyecharts.faker import Faker

# 生成数据
value = [[i, j, random.randint(0, 50)] for i in range(24) for j in range(7)]

# 创建一个 HeatMap 实例
heatmap = HeatMap()

# 设置 x 轴数据
heatmap.add_xaxis(Faker.clock)

# 设置 y 轴数据
heatmap.add_yaxis(
        "series0", Faker.week, value, label_opts=opts.LabelOpts(position="middle")
    )

# 设置全局选项
heatmap.set_global_opts(
        title_opts=opts.TitleOpts(title="HeatMap-基本示例"),
        visualmap_opts=opts.VisualMapOpts(),
    )

# 在notebook中渲染并显示图表
heatmap.render_notebook()
```