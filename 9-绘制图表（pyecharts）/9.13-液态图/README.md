# 9.13-液态图

### 问题描述

（1）生成数据集

（2）绘制液态图

### 示例输出

<img src="https://github.com/jm199504/Python-Exercises/blob/master/9-%E7%BB%98%E5%88%B6%E5%9B%BE%E8%A1%A8%EF%BC%88pyecharts%EF%BC%89/9.13-%E6%B6%B2%E6%80%81%E5%9B%BE/Figure_1.jpg?raw=true" style="zoom:80%;" />

### 示例代码

```python
# 导入所需的库和模块
from pyecharts import options as opts
from pyecharts.charts import Liquid

# 创建一个 Liquid 实例
liquid = Liquid()

# 添加数据以及图例名称
liquid.add("lq", [0.6, 0.8])

# 设置全局参数，包括标题名称
liquid.set_global_opts(title_opts=opts.TitleOpts(title="Liquid-基本示例"))

# 在notebook中渲染图表
liquid.render_notebook()
```