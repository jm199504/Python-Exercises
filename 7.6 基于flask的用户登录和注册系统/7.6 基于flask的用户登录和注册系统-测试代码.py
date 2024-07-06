import unittest  # 导入unittest模块用于编写单元测试

from solution import app, create_db, register_user, authenticate_user  # 导入解决方案中的app和函数


# 定义一个测试类，继承自unittest.TestCase
class FlaskAppTests(unittest.TestCase):

    def setUp(self):
        app.testing = True  # 设置程序处于测试模式
        self.app = app.test_client()  # 创建一个测试客户端
        create_db()  # 创建测试数据库

    # 测试注册用户功能
    def test_register_user(self):
        register_user("test_user", "test_password")
        self.assertTrue(authenticate_user("test_user", "test_password"))

    # 测试使用错误密码登录用户
    def test_login_user_with_wrong_password(self):
        register_user("test_user", "test_password")
        response = self.app.post('/login', data=dict(
            username='test_user',
            password='test_password123'
        ), follow_redirects=True)
        self.assertIn(b"Wrong username or password", response.data)

    # 测试正常登录用户
    def test_login_user(self):
        response = self.app.post('/login', data=dict(
            username='test_user',
            password='test_password'
        ), follow_redirects=True)
        self.assertIn(b"Welcome test_user", response.data)


# 如果该脚本单独运行，执行单元测试
if __name__ == '__main__':
    unittest.main()
