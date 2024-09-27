# 9.15-地理图

### 问题描述

（1）生成数据集

（2）绘制地理图

### 示例输出

<img src="https://github.com/jm199504/Python-Exercises/blob/master/9-%E7%BB%98%E5%88%B6%E5%9B%BE%E8%A1%A8%EF%BC%88pyecharts%EF%BC%89/9.15-%E5%9C%B0%E7%90%86%E5%9B%BE/Figure_1.jpg?raw=true" style="zoom:80%;" />

### 示例代码

```python
# 导入 pyecharts 的相关包
from pyecharts import options as opts
from pyecharts.charts import Geo
from pyecharts.faker import Faker

# 打印虚假数据
print([list(z) for z in zip(Faker.provinces, Faker.values())])

# 创建一个地理图表对象
geo = Geo()

# 配置地图类型为中国地图
geo.add_schema(maptype="china")

# 给地图增加数据并命名
geo.add("geo", [list(z) for z in zip(Faker.provinces, Faker.values())])

# 配置系列选项的标签设置为不显式展示
geo.set_series_opts(label_opts=opts.LabelOpts(is_show=False))

# 配置全局参数
geo.set_global_opts(
    visualmap_opts=opts.VisualMapOpts(),
    title_opts=opts.TitleOpts(title="Geo-基本示例")
)

# 使用 Jupyter Notebook 渲染地理图表
geo.render_notebook()
```