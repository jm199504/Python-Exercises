from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

# 创建一个虚拟的FTP用户
authorizer = DummyAuthorizer()
authorizer.add_user("username", "password", "/Users/junmingguo/PycharmProjects/pythonProject/Python-Exercises-master", perm="elradfmwMT")

# 创建FTP处理程序
handler = FTPHandler
handler.authorizer = authorizer

# 创建FTP服务器实例，并指定IP地址和端口
server = FTPServer(("0.0.0.0", 21), handler)

# 启动服务器
server.serve_forever()