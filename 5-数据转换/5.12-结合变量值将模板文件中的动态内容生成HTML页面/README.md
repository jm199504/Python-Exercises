## 5.12-结合变量值将模板文件中的动态内容生成HTML页面

### 问题描述

结合变量值将模板文件中的动态内容生成HTML页面，实现生成新的HTML页面。

### 输入html示例

```html
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


```

### 输入python示例

```python
title = "My Page"
heading = "Welcome to My Page"
items = ["Item 1", "Item 2", "Item 3 MaxNum"]
```

### 输出HTML示例

```html

<html>
<head>
    <title>My Page</title>
</head>
<body>
    <h1>Welcome to My Page</h1>
        <p>Item 1</p>
        <p>Item 2</p>
        <p>Item 3 MaxNum</p>
</body>
</html>

```

### 示例代码

```python
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

```

