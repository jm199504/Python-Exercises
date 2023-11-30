import os
import time

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
