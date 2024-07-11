from flask import Flask, request, session, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3

app = Flask(__name__)
app.secret_key = "123456"  # 设置 Flask 应用的密钥，用于 session 加密


def create_db():
    """
    创建数据库表格，如果表格不存在的话
    """
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT)")
    conn.commit()
    conn.close()


def register_user(username, password):
    """
    注册用户并将加密后的密码存储到数据库中
    """
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    hashed_password = generate_password_hash(password)  # 加密密码
    c.execute("INSERT INTO users VALUES (?, ?)", (username, hashed_password))
    conn.commit()
    conn.close()


def authenticate_user(username, password):
    """
    验证用户输入的密码是否与数据库中存储的密码匹配
    """
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    c.execute("SELECT password FROM users WHERE username=?", (username,))
    result = c.fetchone()
    conn.close()

    if result and check_password_hash(result[0], password):  # 验证密码
        return True
    else:
        return False


@app.route("/register", methods=["GET", "POST"])
def register():
    """
    提供用户注册页面，并处理用户提交的注册信息
    """
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        register_user(username, password)
        return redirect(url_for("login"))
    return '''
        <form method="post" action="/register">
            <p>用户名：<input type="text" name="username"></p>
            <p>密码：<input type="password" name="password"></p>
            <p><input type="submit" value="注册"></p>
        </form>
    '''


@app.route("/login", methods=["GET", "POST"])
def login():
    """
    提供用户登录页面，并处理用户提交的登录信息
    """
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if authenticate_user(username, password):
            session["username"] = username  # 将用户名保存到 session 中
            return redirect(url_for("profile"))
        else:
            return "Wrong username or password"
    return '''
        <form method="post" action="/login">
            <p>用户名：<input type="text" name="username"></p>
            <p>密码：<input type="password" name="password"></p>
            <p><input type="submit" value="登录"></p>
        </form>
    '''


@app.route("/profile")
def profile():
    """
    显示用户个人资料页面，需要用户登录后才能访问
    """
    if "username" not in session:
        return redirect(url_for("login"))
    return f"Welcome {session['username']}"


if __name__ == "__main__":
    create_db()
    app.run()