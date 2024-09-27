# 9.2-柱状图-XY轴互换

### 问题描述

（1）生成数据集

（2）绘制柱状图

### 示例输出

<img src="https://github.com/jm199504/Python-Exercises/blob/master/9-%E7%BB%98%E5%88%B6%E5%9B%BE%E8%A1%A8%EF%BC%88pyecharts%EF%BC%89/9.2-%E6%9F%B1%E7%8A%B6%E5%9B%BE-XY%E8%BD%B4%E4%BA%92%E6%8D%A2/Figure_1.jpg?raw=true" style="zoom:80%;" />

### 示例代码

```python
from pyecharts.charts import Bar
from pyecharts import options as opts
bar = (
    Bar()
    .add_xaxis(["黄河水利职业技术学院", "重庆工商职业学院", "青岛职业技术学院", "石家庄铁路职业技术学院", "陕西工业职业技术学院", "江苏建筑职业技术学院"])
    .add_yaxis("资源使用情况", [161, 91, 58, 54, 48, 48])
    .reversal_axis()
)
bar.set_global_opts(title_opts=opts.TitleOpts(title="主标题", subtitle="副标题"))
bar.render_notebook()
```