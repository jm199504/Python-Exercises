## 9.22-散点图

### 问题描述

（1）生成数据集

（2）绘制散点图

### 示例输出

<img src="https://github.com/jm199504/Python-Exercises/blob/master/9-%E7%BB%98%E5%88%B6%E5%9B%BE%E8%A1%A8%EF%BC%88pyecharts%EF%BC%89/9.22-%E6%95%A3%E7%82%B9%E5%9B%BE/Figure_1.jpg?raw=true" style="zoom:80%;" />

### 示例代码

```python
from pyecharts import options as opts
from pyecharts.charts import EffectScatter
from pyecharts.faker import Faker

# 创建 EffectScatter 实例
scatter = EffectScatter()
    
# 设置 x 轴数据
scatter.add_xaxis(Faker.choose())

# 设置 y 轴数据
scatter.add_yaxis("Y轴名称", Faker.values())

# 设置全局选项
scatter.set_global_opts(title_opts=opts.TitleOpts(title="EffectScatter-基本示例"))

# 在notebook中渲染并显示图表
scatter.render_notebook()
```