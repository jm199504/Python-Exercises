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