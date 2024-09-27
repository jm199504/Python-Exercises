# 9.10-极坐标图

### 问题描述

（1）生成数据集

（2）绘制极坐标图

### 示例输出

<img src="https://github.com/jm199504/Python-Exercises/blob/master/9-%E7%BB%98%E5%88%B6%E5%9B%BE%E8%A1%A8%EF%BC%88pyecharts%EF%BC%89/9.10-%E6%9E%81%E5%9D%90%E6%A0%87%E5%9B%BE/Figure_1.jpg?raw=true" style="zoom:80%;" />

### 示例代码

```python
# 导入所需的包和模块
from pyecharts import options as opts
from pyecharts.charts import Polar
from pyecharts.faker import Faker

# 创建一个 Polar 实例
polar = Polar()

# 设置角度坐标轴的选项，使用 Faker.week 作为类别数据
polar.add_schema(angleaxis_opts=opts.AngleAxisOpts(data=Faker.week, type_="category"))

# 添加数据系列 A，设置数据为 [1, 2, 3, 4, 3, 5, 1]，图表类型为柱状图，与 stack0 进行堆叠
polar.add("A", [1, 2, 3, 4, 3, 5, 1], type_="bar", stack="stack0")

# 添加数据系列 B，设置数据为 [2, 4, 6, 1, 2, 3, 1]，图表类型为柱状图，与 stack0 进行堆叠
polar.add("B", [2, 4, 6, 1, 2, 3, 1], type_="bar", stack="stack0")

# 添加数据系列 C，设置数据为 [1, 2, 3, 4, 1, 2, 5]，图表类型为柱状图，与 stack0 进行堆叠
polar.add("C", [1, 2, 3, 4, 1, 2, 5], type_="bar", stack="stack0")

# 设置全局选项，包括标题选项，将图表标题设置为 "Polar-AngleAxis"
polar.set_global_opts(title_opts=opts.TitleOpts(title="Polar-AngleAxis"))

# 在 Jupyter Notebook 中渲染图表
polar.render_notebook()
```