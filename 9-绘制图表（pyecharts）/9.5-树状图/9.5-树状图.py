# 导入 pyecharts 中的相应模块和库
from pyecharts import options as opts
from pyecharts.charts import TreeMap

# 定义树状图中所需的数据
data = [
    {"value": 40, "name": "我是A"}, # 根节点 A
    {
        "value": 180,
        "name": "我是B", # 子节点 B
        "children": [
            {
                "value": 76,
                "name": "我是B.children", # 子节点 B.children
                "children": [
                    {"value": 12, "name": "我是B.children.a"}, # 子节点 B.children.a
                    {"value": 28, "name": "我是B.children.b"}, # 子节点 B.children.b
                    {"value": 20, "name": "我是B.children.c"}, # 子节点 B.children.c
                    {"value": 16, "name": "我是B.children.d"}, # 子节点 B.children.d
                ],
            }
        ],
    },
]

# 创建一个树状图对象
treemap = TreeMap()

# 在树状图中添加数据
treemap.add("演示数据", data)

# 设置全局配置，包括标题等选项
treemap.set_global_opts(title_opts=opts.TitleOpts(title="TreeMap-基本示例"))

# 在 Jupyter Notebook 中渲染并显示树状图
treemap.render_notebook()