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