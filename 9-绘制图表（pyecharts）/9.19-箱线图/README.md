## 9.19-箱线图

### 问题描述

（1）生成数据集

（2）绘制箱线图

### 示例输出

<img src="https://github.com/jm199504/Python-Exercises/blob/master/9-%E7%BB%98%E5%88%B6%E5%9B%BE%E8%A1%A8%EF%BC%88pyecharts%EF%BC%89/9.19-%E7%AE%B1%E7%BA%BF%E5%9B%BE/Figure_1.jpg?raw=true" style="zoom:80%;" />

### 示例代码

```python
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
```