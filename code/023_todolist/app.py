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