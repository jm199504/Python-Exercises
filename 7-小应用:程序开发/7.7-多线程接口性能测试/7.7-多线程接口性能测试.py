from flask import Flask, jsonify

app = Flask(__name__)


# 模拟一个简单的接口，返回 Hello World
@app.route('/hello')
def hello():
    return jsonify(message='Hello, World!')


if __name__ == "__main__":
    app.run()
