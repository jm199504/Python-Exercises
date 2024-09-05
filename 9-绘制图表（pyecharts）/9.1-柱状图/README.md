# 9.1-柱状图

### 问题描述

（1）生成数据集

（2）绘制柱状图

### 示例输出

<img src="?raw=true" style="zoom:80%;" />

### 示例代码

```python
from pyecharts.charts import Bar

bar = Bar()
bar.add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
bar.add_yaxis("商家A", [5, 20, 36, 10, 75, 90])
# render 会生成本地 HTML 文件，默认会在当前目录生成 render.html 文件
# 也可以传入路径参数，如 bar.render("mycharts.html")
# bar.render()
bar.render_notebook()

```