# 导入需要的模块和库
from pyecharts import options as opts
from pyecharts.charts import Tree

# 定义树状图的数据
data = [
    {
        "children": [
            {"name": "B"},  # 子节点 B
            {
                "children": [
                    {"children": [{"name": "I"}], "name": "E"},  # 子节点 E
                    {"name": "F"},  # 子节点 F
                ],
                "name": "C",  # 子节点 C
            },
            {
                "children": [
                    {"children": [{"name": "J"}, {"name": "K"}], "name": "G"},  # 子节点 G
                    {"name": "H"},  # 子节点 H
                ],
                "name": "D",  # 子节点 D
            },
        ],
        "name": "A",  # 根节点 A
    }
]

# 创建一个树状图对象
tree = Tree()

# 添加数据到树状图中
tree.add("", data)

# 设置全局配置
tree.set_global_opts(title_opts=opts.TitleOpts(title="Tree-基本示例"))

# 在 Jupyter Notebook 中显示树状图
tree.render_notebook()