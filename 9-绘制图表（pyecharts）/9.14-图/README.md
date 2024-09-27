## 9.14-图

### 问题描述

（1）生成数据集

（2）绘制图

### 示例输出

<img src="https://github.com/jm199504/Python-Exercises/blob/master/9-%E7%BB%98%E5%88%B6%E5%9B%BE%E8%A1%A8%EF%BC%88pyecharts%EF%BC%89/9.14-%E5%9B%BE/Figure_1.jpg?raw=true" style="zoom:80%;" />

### 示例代码

```python
# 导入需要使用的模块和类
from pyecharts import options as opts
from pyecharts.charts import Graph

# 定义节点
nodes = [
    {"name": "结点1", "symbolSize": 10},
    {"name": "结点2", "symbolSize": 20},
    {"name": "结点3", "symbolSize": 30},
    {"name": "结点4", "symbolSize": 40},
    {"name": "结点5", "symbolSize": 50},
    {"name": "结点6", "symbolSize": 40},
    {"name": "结点7", "symbolSize": 30},
    {"name": "结点8", "symbolSize": 20},
]

# 定义节点之间的关系
links = []
for i in nodes:
    for j in nodes:
        links.append({"source": i.get("name"), "target": j.get("name")})

# 创建 Graph 实例
graph = Graph()

# 向实例中添加节点和节点之间的关系，并设置图形的斥力
graph.add("关注度", nodes, links, repulsion=8000)

# 设置全局参数，如标题等
graph.set_global_opts(title_opts=opts.TitleOpts(title="Graph-基本示例"))

# 在 Jupyter Notebook 上渲染图形
graph.render_notebook()
```