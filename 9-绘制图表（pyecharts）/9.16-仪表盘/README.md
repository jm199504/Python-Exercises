## 9.16-仪表盘

### 问题描述

（1）生成数据集

（2）绘制仪表盘

### 示例输出

<img src="https://github.com/jm199504/Python-Exercises/blob/master/9-%E7%BB%98%E5%88%B6%E5%9B%BE%E8%A1%A8%EF%BC%88pyecharts%EF%BC%89/9.16-%E4%BB%AA%E8%A1%A8%E7%9B%98/Figure_1.jpg?raw=true" style="zoom:80%;" />

### 示例代码

```python
from pyecharts import options as opts  # 导入 pyecharts 的选项模块
from pyecharts.charts import Gauge  # 导入 Gauge（仪表盘）模块

gauge =  Gauge()  # 创建一个 Gauge 实例
gauge.add("作业完成情况", [("完成率", 66.6)])  # 添加作业完成情况数据到仪表盘中，包括完成率
gauge.set_global_opts(title_opts=opts.TitleOpts(title="Gauge-基本示例"))  # 设置全局选项，包括标题
gauge.render_notebook()  # 在 Jupyter Notebook 中渲染并展示仪表盘
```