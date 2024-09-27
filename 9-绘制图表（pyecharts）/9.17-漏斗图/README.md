# 9.17-漏斗图

### 问题描述

（1）生成数据集

（2）绘制漏斗图

### 示例输出

<img src="https://github.com/jm199504/Python-Exercises/blob/master/9-%E7%BB%98%E5%88%B6%E5%9B%BE%E8%A1%A8%EF%BC%88pyecharts%EF%BC%89/9.17-%E6%BC%8F%E6%96%97%E5%9B%BE/Figure_1.jpg?raw=true" style="zoom:80%;" />

### 示例代码

```python
# 导入所需模块
import pyecharts.options as opts 
from pyecharts.charts import Funnel

# 定义漏斗图数据
x_data = ["展现", "点击", "访问", "咨询", "订单"]
y_data = [100, 80, 60, 40, 20]
data = [[x_data[i], y_data[i]] for i in range(len(x_data))]

# 创建漏斗图对象
funnel = Funnel()

# 添加漏斗图数据
funnel.add(
    series_name="", # 系列名称，这里为空
    data_pair=data, # 数据
    gap=2, # 数据图形间的间隔距离
    tooltip_opts=opts.TooltipOpts(trigger="item", formatter="{a} <br/>{b} : {c}%"), # 提示框选项，用于控制提示框的格式和展示方式
    label_opts=opts.LabelOpts(is_show=True, position="inside"), # 标签选项，用于控制数据标签的显示位置和样式
    itemstyle_opts=opts.ItemStyleOpts(border_color="#fff", border_width=1), # 图形样式选项，用于控制数据图形的颜色、边框、阴影等效果
)

# 设置漏斗图配置选项
funnel.set_global_opts(title_opts=opts.TitleOpts(title="漏斗图", subtitle="纯属虚构")) # 主题样式、标题、副标题等配置

# 显示漏斗图（在Notebook中进行显示）
funnel.render_notebook()
```