# 导入所需的库和模块
from pyecharts import options as opts
from pyecharts.charts import Bar, Line
from pyecharts.faker import Faker

# 创建数据
v1 = [2.0, 4.9, 7.0, 23.2, 25.6, 76.7, 135.6, 162.2, 32.6, 20.0, 6.4, 3.3]
v2 = [2.6, 5.9, 9.0, 26.4, 28.7, 70.7, 175.6, 182.2, 48.7, 18.8, 6.0, 2.3]
v3 = [2.0, 2.2, 3.3, 4.5, 6.3, 10.2, 20.3, 23.4, 23.0, 16.5, 12.0, 6.2]

# 创建 Bar 实例，加入数据，设置 X、Y 轴标签，扩展 Y 轴，并关闭 Y 轴数据标签
bar = Bar()
bar.add_xaxis(Faker.months)
bar.add_yaxis("蒸发量", v1)
bar.add_yaxis("降水量", v2)
bar.extend_axis(
        yaxis=opts.AxisOpts(
            axislabel_opts=opts.LabelOpts(formatter="{value} °C"), interval=5
        )
    )
bar.set_series_opts(label_opts=opts.LabelOpts(is_show=False))
bar.set_global_opts(
        title_opts=opts.TitleOpts(title="Overlap-bar+line"),
        yaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(formatter="{value} ml")),
    )

# 创建 Line 实例，加入数据，设置对应轴的标签并指定 Y 轴显示在右侧
line = Line().add_xaxis(Faker.months).add_yaxis("平均温度", v3, yaxis_index=1)

# 调用 Bar 实例中绘制 overlap 图表的方法，将 Line 加入 Bar 实例中
bar.overlap(line)

# 在 notebook 中渲染图表
bar.render_notebook()