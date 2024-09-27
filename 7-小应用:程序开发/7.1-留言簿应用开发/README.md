## 7.1-留言簿应用开发

### 问题描述

使用 Python 的 Web 框架，做一个 Web 版本留言簿应用。

### 应用示例效果

### 数据库构建

`macOS`推荐下载`DBeaver`，是一款免费开源的数据库管理工具。对应轻量级的应用开发并且是使用关系型数据库，可以考虑直接使用`SQLite`，具备以下特性：

1. 零配置：SQLite不需要任何繁琐的配置过程。您只需要创建一个数据库文件，并可以立即开始使用它。这使得SQLite成为开发和原型验证的理想选择。
2. 轻量级和高性能：SQLite是一个轻量级的数据库，数据库引擎本身非常小巧且高效。它在处理小型和局部应用程序方面表现出色，并且具有很低的资源占用和快速的响应时间。
3. 广泛支持的平台：SQLite是跨平台的，并且可以在各种操作系统上运行，包括Windows、MacOS、Linux等。这使得SQLite成为跨平台应用程序的理想选择。
4. 完整的标准兼容性：SQLite符合SQL标准，并提供了许多常见的SQL功能，如表、视图、索引、触发器和存储过程等。它支持标准的SQL查询语句和事务处理，以及其他高级功能。
5. 零管理：由于SQLite是一个嵌入式数据库，它不需要独立的数据库服务器进行管理。您只需要处理单个数据库文件，不需要启动、停止或管理数据库服务器进程。
6. 开源和免费：SQLite是开源的，根据公共领域许可证分发。您可以自由地使用、复制和分发SQLite。

### Python Web框架：Flask

Flask是一个轻量级的Python Web框架，它旨在构建简单、易于扩展和灵活的Web应用程序，具备以下特性：

1. 简单易用：Flask采用简洁的设计理念，使用起来非常简单和直观。它具有直观的API和清晰的文档，使得开发人员能够快速入门并构建Web应用。
2. 轻量级：Flask是一个轻量级的框架，它只提供了一些基本的功能和核心组件，而其他更高级的功能可以根据需要通过扩展来添加。这种设计使得Flask灵活且易于定制，可以满足各种不同的项目需求。
3. 路由和视图：Flask使用路由装饰器来定义URL和函数之间的映射关系。您可以使用Flask的路由系统来定义不同URL路径的处理函数，这些处理函数可以渲染网页、处理表单提交、提供API接口等。
4. 模板引擎：Flask集成了Jinja2模板引擎，它提供了灵活而强大的模板系统，使您能够构建动态的网页。您可以在模板中使用模板语法来插入动态内容、循环处理数据、继承和扩展模板等。
5. 数据库集成：Flask与各种数据库系统（如SQLite、MySQL、PostgreSQL等）集成良好。它提供了轻量级的对象关系映射（ORM）库（如SQLAlchemy）的集成支持，使您能够更方便地处理数据库操作。
6. 扩展机制：Flask支持丰富的扩展机制，可以通过安装和配置扩展来添加额外的功能。Flask的扩展库提供了许多常用功能的封装，如身份验证、表单验证、缓存、国际化等，方便快捷地集成到应用程序中。
7. RESTful支持：Flask对构建RESTful API提供了良好的支持。您可以使用Flask来定义和处理API资源和路由，通过HTTP方法（如GET、POST、PUT、DELETE等）对资源进行操作。
8. 社区和生态系统：Flask拥有庞大而活跃的社区，有许多开发人员共享他们的经验、教程和扩展。同时，Flask还有丰富的第三方库和工具，用于处理身份验证、表单处理、数据库操作、测试等。

Flask官方网站：[https://flask.palletsprojects.com/](https://flask.palletsprojects.com/)

### 解答思路

（1）数据库设计：留言簿应当包含用户ID、用户昵称、留言文本、留言时间

![Untitled](022_%E7%95%99%E8%A8%80%E7%B0%BF%E5%BA%94%E7%94%A8%E5%BC%80%E5%8F%91%20a0e2a20484c14a349a68e4822d9c803d/Untitled.png)

（2）应用设计

```python
guestbook/  # 应用目录
-- templates  # 资源文件目录（通常包含html/css/js等）
  -- index.html
-- app.py  # 程序入口（Web后端代码）
-- guestbook.db  # 数据库文件（存储留言簿记录）
```

（3）解答示例Python代码（`app.py`）

```python
import os
import time

# pip3 install flask
# pip3 install flask_sqlalchemy

from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# 定义sqlite的URI地址，若不存在该文件则自动生成guestbook.db数据库文件
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv(
    'DATABASE_URL',
    'sqlite:///' + os.path.join(app.root_path, 'guestbook.db'))

db = SQLAlchemy(app)

# 定义数据库表的字段，并注明其数据类型
class Guestbook(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30))
    content = db.Column(db.String(200))
    time_text = db.Column(db.String(100))

# 首页，'/'则表示127.0.0.1:5000所展示的页面功能（默认端口为5000）
@app.route('/')
def index():
    content_list = Guestbook.query.all()
    return render_template('index.html', contentlist=content_list)

# 新增留言，路径为'/add'，请求方式：POST，接收表单的username和content并insert到数据库表
@app.route('/add', methods=['post'])
def add():
    time_text = str(time.asctime(time.localtime(time.time())))
    new_message = Guestbook(username=request.form['username'], content=request.form['content'], time_text=time_text)
    db.session.add(new_message)
    db.session.commit()
    return redirect(url_for('index'))

# 主函数（程序入口）
if __name__ == '__main__':
    app.run()
```

（4）解答示例HTML代码（`index.py`）

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>GuestBook App</title>
</head>
<body>
    <h1>留言簿</h1>
    <h2>请输入姓名及留言内容</h2>
        <form action="{{ url_for('add') }}" method="post">
            <p>姓名：<input type="text" name="username"></p>
            <p>内容：<input type="text" name="content"></p>
            <p><input type="submit" value="提交留言"></p>
        </form>
    <h2>留言历史信息</h2>

        {% for contents in contentlist %}
            <div style="font-size:12pt;color:gray">
                <p>姓名：{{ contents.username }}</p>
                <p>留言时间：{{ contents.time_text }}</p>
                <p>内容：{{ contents.content }}</p>
            </div>
            <HR align=left width=300 color=black SIZE=1>
        {% endfor %}

</body>
</html>
```