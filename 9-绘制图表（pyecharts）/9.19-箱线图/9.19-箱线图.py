# 导入所需的库和模块
from pyecharts import options as opts
from pyecharts.charts import Boxplot

# 设置数据
v1 = [[850, 740, 900, 1070, 930, 850, 950, 980, 980, 880, 1000, 980],
      [960, 940, 960, 940, 880, 800, 850, 880, 900, 840, 830, 790]]
v2 = [[890, 810, 810, 820, 800, 770, 760, 740, 750, 760, 910, 920],
      [890, 840, 780, 810, 760, 810, 790, 810, 820, 850, 870, 870]]

# 创建 Boxplot 对象
boxplot = Boxplot()

# 加载数据
boxplot.add_xaxis(["expr1", "expr2"])
boxplot.add_yaxis("A", boxplot.prepare_data(v1))
boxplot.add_yaxis("B", boxplot.prepare_data(v2))

# 设置全局选项
boxplot.set_global_opts(title_opts=opts.TitleOpts(title="BoxPlot-基本示例"))

# 在 Jupyter Notebook 中显示图表
boxplot.render_notebook()