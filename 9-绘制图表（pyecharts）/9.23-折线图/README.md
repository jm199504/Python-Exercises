# 9.23-折线图

### 问题描述

（1）生成数据集

（2）绘制地理图

### 示例输出

<img src="?raw=true" style="zoom:80%;" />

### 示例代码

```python
from pyecharts.charts import Line  # 导入 Line 类来创建折线图
from pyecharts import options as opts  # 导入 options 模块以使用图表的配置选项

x_data = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]  # x 轴的数据
y_data = [820, 932, 901, 934, 1290, 1330, 1320]  # y 轴的数据

line = Line()  # 创建折线图实例
line.set_global_opts(
    tooltip_opts=opts.TooltipOpts(is_show=False),  # 配置工具提示，不显示
    xaxis_opts=opts.AxisOpts(type_="category"),  # 配置 x 轴类型为类别型
    yaxis_opts=opts.AxisOpts(
        type_="value",
        axistick_opts=opts.AxisTickOpts(is_show=True),
        splitline_opts=opts.SplitLineOpts(is_show=True),
    ),  # 配置 y 轴类型为数值型，显示轴标记和分割线
)
line.add_xaxis(xaxis_data=x_data)  # 添加 x 轴数据
line.add_yaxis(
    series_name="销售数量",  # 设置系列的名称
    y_axis=y_data,  # 添加 y 轴数据
    symbol="emptyCircle",  # 设置数据点的样式为空心圆
    is_symbol_show=True,  # 显示数据点的样式
    label_opts=opts.LabelOpts(is_show=False),  # 配置标签，不显示
)
line.set_global_opts(title_opts=opts.TitleOpts(title="主标题", subtitle="副标题"))  # 设置图表的标题和副标题
line.render_notebook()  # 在 Jupyter Notebook 中渲染折线图并显示
```