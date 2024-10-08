## 7.4-待办事项应用开发

### 问题描述

使用 Python 的 Web 框架，做一个 Web 版本 TodoList 应用。

### 解答思路和示例代码

（1）数据库表设计：事项ID、事项内容、是否完成

（2）应用设计

```html
todolist/  # 应用目录
-- templates  # 资源文件目录（通常包含html/css/js等）
  -- index.html
-- app.py  # 程序入口（Web后端代码）
-- guestbook.db  # 数据库文件（存储留言簿记录）
```

（3）解答示例Python代码（`app.py`）

```python
import os

from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv(
    'DATABASE_URL', 'sqlite:///' + os.path.join(app.root_path, 'todo.db'))

db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(200))
    complete = db.Column(db.Boolean)

@app.route('/')
def index():
    incomplete = Todo.query.filter_by(complete=False).all()  # 从数据库中查询未完成的任务
    complete = Todo.query.filter_by(complete=True).all()  # 从数据库中查询已完成的任务
    return render_template('index.html', incomplete=incomplete, complete=complete)

@app.route('/add', methods=['POST'])
def add():
    todo = Todo(text=request.form['todoitem'], complete=False)  # 从表单中获取待办事项的文本
    db.session.add(todo)  # 将待办事项对象添加到数据库会话中
    db.session.commit()  # 提交会话，将待办事项保存到数据库
    return redirect(url_for('index'))  # 重定向到主页

@app.route('/complete/<id>')
def complete(id):
    todo = Todo.query.filter_by(id=int(id)).first()  # 根据id从数据库中查询待办事项
    todo.complete = True  # 将待办事项的状态标记为已完成
    db.session.commit()  # 提交会话，更新数据库中的待办事项
    return redirect(url_for('index'))  # 重定向到主页

@app.route('/incomplete/<id>')
def incomplete(id):
    todo = Todo.query.filter_by(id=int(id)).first() # 根据id从数据库中查询待办事项
    todo.complete = False  # 将待办事项的状态标记为未完成
    db.session.commit()  # 提交会话，更新数据库中的待办事项
    return redirect(url_for('index'))  # 重定向到主页

if __name__ == '__main__':
    app.run()
```

（4）解答示例HTML代码（`index.html`）

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>TodoList App</title>
</head>
<body>
    <h1>Todo List</h1>
    <h2>添加新的任务</h2>
        <form action="{{ url_for('add') }}" method="post">
            <input type="text" name="todoitem">
            <input type="submit" value="添加任务">
        </form>

    <h2>待完成任务</h2>
        <ul>
        {% for todo in incomplete %}
            <li style="font-size:12pt;color:gray"><input name='{{ todo.id }}' type="hidden">{{ todo.text }}
                <a href="{{ url_for('complete',id=todo.id) }}" style="font-size:10pt">标记已完成</a>
            </li>
        {% endfor %}
        </ul>
    <h2>已完成任务</h2>
    <ul>
        {% for todo in complete %}
            <li style="font-size:12pt;color:green;"><input name='{{ todo.id }}' type="hidden">{{ todo.text }}
                <a href="{{ url_for('incomplete',id=todo.id) }}" style="font-size:10pt">标记未完成</a>
            </li>
        {% endfor %}
        </ul>

</body>
</html>
```

（5）预览入口：

```html
127.0.0.1:5000
```