# 009_区分HTML内容

### 问题描述

一个HTML文件，找出里面的标题、内容、链接、正文内容

### 解答示例代码

```bash
from bs4 import BeautifulSoup

html_doc = open("test.html", 'r', encoding='utf-8')

html_handle = html_doc.read()

# 使用beautifulsoup解析功能，解析器使用lxml
soup = BeautifulSoup(html_handle, 'html.parser')
# 输出标题
print('标题：', soup.title)
# 输出p标签的内容
print('内容：', soup.p)
# 输出a链接
print('链接：', soup.find_all('a'))
# 输出body正文
print('正文：', soup.find_all('body'))
# 输出整个html文件
print('整个html文件：', soup.get_text)
```

### 测试HTML

```html
#! /usr/bin/env python
#coding=utf-8
from bs4 import BeautifulSoup as BS

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
soup = BS(html_doc, 'lxml')    
print soup.get_text()
```

### 结果输出

```bash
标题： <title>The Dormouse's story</title>
内容： <p class="title"><b>The Dormouse's story</b></p>
链接： [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>, <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>, <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]
正文： [<body>
<p class="title"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a> and
<a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""
soup = BS(html_doc, 'lxml')    
print soup.get_text()</body>]
整个html文件： <bound method PageElement.get_text of #! /usr/bin/env python
#coding=utf-8
from bs4 import BeautifulSoup as BS

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a> and
<a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""
soup = BS(html_doc, 'lxml')    
print soup.get_text()</body></html>>
```

