from mako.template import Template

# 定义HTML模板
mytemplate = Template("""
<html>
<head>
    <title>${title}</title>
</head>
<body>
    <h1>${heading}</h1>
    % for item in items:
        <p>${item}</p>
    % endfor
</body>
</html>
""")

# 定义变量
title = "My Page"
heading = "Welcome to My Page"
items = ["Item 1", "Item 2", "Item 3 MaxNum"]

# 使用变量生成HTML
html = mytemplate.render(title=title, heading=heading, items=items)

# 输出生成的HTML
print(html)


# 输出生成的HTML
with open('output.html', 'w') as f:
    f.write(html)
