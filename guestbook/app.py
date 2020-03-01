from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
import os
import time
# 定义sqlite的URI地址，若不存在该文件则自动生成todo.db文件（数据库）
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL','sqlite:///' + os.path.join(app.root_path, 'guestbook.db'))

db = SQLAlchemy(app)
# 定义数据库表的字段：id、text、complete并注明其数据类型
class Guestbook(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(30))
    content = db.Column(db.String(200))
    timetext = db.Column(db.String(100))
# 首页，'/'则表示127.0.0.1:5000所展示的页面功能
# 展示complete字段为False的数据
@app.route('/')
def index():
    contentlist = Guestbook.query.all()
    return render_template('index.html',contentlist=contentlist)

@app.route('/add',methods=['post'])
def add():
    timetext = str(time.asctime(time.localtime(time.time())))
    newmessage = Guestbook(username=request.form['username'],content=request.form['content'],timetext=timetext)
    db.session.add(newmessage)
    db.session.commit()
    return redirect(url_for('index'))
# 主函数
if __name__ == '__main__':
    app.run()
