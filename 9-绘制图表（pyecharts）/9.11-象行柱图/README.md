# 9.11-象行柱图

### 问题描述

（1）生成数据集

（2）绘制象行柱图

### 示例输出

<img src="?raw=true" style="zoom:80%;" />

### 示例代码

```python
from pyecharts import options as opts
from pyecharts.charts import PictorialBar
from pyecharts.globals import SymbolType

# 设置数据
location = ["山西", "四川", "西藏", "北京", "上海", "内蒙古", "云南", "黑龙江", "广东", "福建"]
values = [13, 42, 67, 81, 86, 94, 166, 220, 249, 262]

# 创建 PictorialBar 实例
pictorial_bar = PictorialBar()

# 添加 x 轴和 y 轴数据
pictorial_bar.add_xaxis(location)
pictorial_bar.add_yaxis(
        "",  # 系列名称，这里为空即可
        values,  # y 轴数据
        label_opts=opts.LabelOpts(is_show=False),  # 不显示标签
        symbol_size=18,  # 符号大小
        symbol_repeat="fixed",  # 符号是否按照固定数量重复
        symbol_offset=[0, 0],  # 符号的偏移量
        is_symbol_clip=True,  # 是否裁剪超出坐标系的符号部分
        symbol=SymbolType.ROUND_RECT,  # 符号类型
    )

# 翻转 x 轴和 y 轴
pictorial_bar.reversal_axis()

# 设置全局选项
pictorial_bar.set_global_opts(
        title_opts=opts.TitleOpts(title="PictorialBar-各省份人口数量（虚假数据）"),  # 设置标题
        xaxis_opts=opts.AxisOpts(is_show=False),  # 不显示 x 轴
        yaxis_opts=opts.AxisOpts(
            axistick_opts=opts.AxisTickOpts(is_show=False),  # 不显示 y 轴刻度
            axisline_opts=opts.AxisLineOpts(
                linestyle_opts=opts.LineStyleOpts(opacity=0)  # 不显示 y 轴线条
            ),
        ),
    )

# 在 Jupyter Notebook 中渲染图表
pictorial_bar.render_notebook()
```