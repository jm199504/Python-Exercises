## 7.6-基于flask的用户登录和注册系统

### 问题描述
基于flask框架实现用户登录和注册系统，具体功能包含：
（1）注册新用户：用户可以通过提供用户名和密码进行注册，注册成功后将用户信息保存到数据库中。
（2）用户登录：注册成功后，用户可以使用注册时的用户名和密码进行登录。
（3）密码加密：用户的密码在保存到数据库中时需要进行加密处理，以提高安全性。
（4）单元测试：编写单元测试来验证注册和登录功能的正确性和健壮性。

### 相关需求
1、用户注册界面：http://localhost:5000/register

```
用户名：[输入框]
密码：[输入框]
[注册按钮]
```

2、用户注册成功后直接跳转至登录页面

3、用户登录界面：http://localhost:5000/login
```
用户名：[输入框]
密码：[输入框]
[注册按钮]
```

4、用户登录成功界面：http://localhost:5000/login
```
欢迎 「用户名」 登录
```

5、用户登录失败界面：http://localhost:5000/login
```
Wrong username or password
```

### 前期准备

```
pip install Flask Flask-SQLAlchemy Flask-WTF
```

### 示例代码（app.py）

```python
# app.py
import os
from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = os.urandom(24)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# 用户模型
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)

# 初始化数据库
@app.before_first_request
def create_tables():
    db.create_all()

# 路由：注册
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if User.query.filter_by(username=username).first():
            flash('Username already exists!', 'danger')
        else:
            hashed_password = generate_password_hash(password, method='sha256')
            new_user = User(username=username, password=hashed_password)
            db.session.add(new_user)
            db.session.commit()
            flash('Registration successful! Please log in.', 'success')
            return redirect(url_for('login'))
    return render_template('register.html')

# 路由：登录
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            session['username'] = username
            return render_template('welcome.html', username=username)
        else:
            flash('Wrong username or password', 'danger')
    return render_template('login.html')

# 路由：注销
@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
```

### 示例代码（templates/register.html）

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Register</title>
</head>
<body>
    <h2>注册</h2>
    <form method="POST">
        <label>用户名:</label>
        <input type="text" name="username" required>
        <br>
        <label>密码:</label>
        <input type="password" name="password" required>
        <br>
        <button type="submit">注册</button>
    </form>
    <p>已经注册？<a href="{{ url_for('login') }}">登录</a></p>
</body>
</html>
```



