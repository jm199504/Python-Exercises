## 9.9-雷达图

### 问题描述

（1）生成数据集

（2）绘制雷达图

### 示例输出

<img src="https://github.com/jm199504/Python-Exercises/blob/master/9-%E7%BB%98%E5%88%B6%E5%9B%BE%E8%A1%A8%EF%BC%88pyecharts%EF%BC%89/9.9-%E9%9B%B7%E8%BE%BE%E5%9B%BE/Figure_1.jpg?raw=true" style="zoom:80%;" />

### 示例代码

```python
# 导入 pyecharts 库中的 Radar 类和 options 模块的 opts 类
from pyecharts import options as opts
from pyecharts.charts import Radar

# 定义两个数据系列 v1 和 v2
v1 = [[4300, 10000, 28000, 35000, 50000, 19000]]
v2 = [[5000, 14000, 28000, 31000, 42000, 21000]]

# 创建 Radar 图表对象
radar = Radar()

# 添加雷达图坐标系信息
radar.add_schema(
    schema=[
        opts.RadarIndicatorItem(name="销售", max_=6500),
        opts.RadarIndicatorItem(name="管理", max_=16000),
        opts.RadarIndicatorItem(name="信息技术", max_=30000),
        opts.RadarIndicatorItem(name="客服", max_=38000),
        opts.RadarIndicatorItem(name="研发", max_=52000),
        opts.RadarIndicatorItem(name="市场", max_=25000)
    ]
)

# 添加预算分配和实际开销两个数据系列
radar.add("预算分配", v1)
radar.add("实际开销", v2)

# 设置系列选项，隐藏标签
radar.set_series_opts(label_opts=opts.LabelOpts(is_show=False))

# 设置全局选项，包括标题和图例等
radar.set_global_opts(
    legend_opts=opts.LegendOpts(selected_mode="single"),
    title_opts=opts.TitleOpts(title="Radar-单例模式")
)

# 在 Jupyter Notebook 中渲染图表
radar.render_notebook()
```