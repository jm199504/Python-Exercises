# 9.7-时间轴

### 问题描述

（1）生成数据集

（2）绘制时间轴

### 示例输出

<img src="https://github.com/jm199504/Python-Exercises/blob/master/9-%E7%BB%98%E5%88%B6%E5%9B%BE%E8%A1%A8%EF%BC%88pyecharts%EF%BC%89/9.7-%E6%97%B6%E9%97%B4%E8%BD%B4/Figure_1.jpg?raw=true" style="zoom:80%;" />

### 示例代码

```python
# 导入需要的模块和库
from pyecharts import options as opts
from pyecharts.charts import Bar, Timeline
from pyecharts.faker import Faker

# 生成假数据
x = Faker.choose()

# 创建一个时间轴图表对象
tl = Timeline()

# 循环创建每年的柱状图
for i in range(2015, 2020):
    # 创建柱状图对象
    bar = Bar()

    # 添加 x 轴数据
    bar.add_xaxis(x)

    # 添加 y 轴数据和标签
    bar.add_yaxis("商家A", Faker.values())
    bar.add_yaxis("商家B", Faker.values())

    # 设置全局配置
    bar.set_global_opts(title_opts=opts.TitleOpts("某商店{}年营业额".format(i)))

    # 将柱状图添加到时间轴中
    tl.add(bar, "{}年".format(i))

# 在 Jupyter Notebook 中显示时间轴图表
tl.render_notebook()
```