from pyecharts.charts import Bar
from pyecharts import options as opts
bar = (
    Bar()
    .add_xaxis(["黄河水利职业技术学院", "重庆工商职业学院", "青岛职业技术学院", "石家庄铁路职业技术学院", "陕西工业职业技术学院", "江苏建筑职业技术学院"])
    .add_yaxis("资源使用情况", [161, 91, 58, 54, 48, 48])
    .reversal_axis()
)
bar.set_global_opts(title_opts=opts.TitleOpts(title="主标题", subtitle="副标题"))
bar.render_notebook()