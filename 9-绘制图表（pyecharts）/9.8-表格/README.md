# 9.8-表格

### 问题描述

（1）生成数据集

（2）绘制表格

### 示例输出

<img src="?raw=true" style="zoom:80%;" />

### 示例代码

```python
from pyecharts.components import Table        # 导入Table组件
from pyecharts.options import ComponentTitleOpts    # 导入标题选项

table = Table()    # 创建一个表格对象

headers = ["City name", "Area", "Population", "Annual Rainfall"]    # 表格的表头
rows = [
    ["Brisbane", 5905, 1857594, 1146.4],    # 表格的数据行
    ["Adelaide", 1295, 1158259, 600.5],
    ["Darwin", 112, 120900, 1714.7],
    ["Hobart", 1357, 205556, 619.5],
    ["Sydney", 2058, 4336374, 1214.8],
    ["Melbourne", 1566, 3806092, 646.9],
    ["Perth", 5386, 1554769, 869.4],
]

table.add(headers, rows)    # 在表格中添加表头和数据行

table.set_global_opts(
    title_opts=ComponentTitleOpts(title="Table-基本示例", subtitle="我是副标题支持换行哦")    # 设置表格的标题和副标题
)

table.render_notebook()    # 在notebook中渲染并显示表格
```