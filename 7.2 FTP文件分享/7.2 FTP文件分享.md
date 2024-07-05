# 7.2 FTP文件分享

### 问题描述

小明和小新在一个教室里，在共同创建一个课件，前期他们两个需要共同收集资料，使用IM（通讯工具）传输很麻烦，不仅需要发送还要另存为，小明在思考能不能搭建FTP服务器，可以直接通过拖拽的方式放入指定文件夹。

### 解答示例代码

需要使用到`pyftpdlib`第三方库，通过`pip3 install pyftpdlib`安装，整体流程：

1. 创建用户
2. 创建FTP服务器实例
3. 启动FTP服务器

```python
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
```

参数说明：

- `add_user`中的`”username”`：用户名，在访问FTP服务器时需要填写（鉴权）
- `add_user`中的`“password”`：用户密码，在访问FTP服务器时需要填写（鉴权）
- `add_user`中的`“/Users/…”`：指定文件夹路径
- `FTPServer`中的`“0.0.0.0”`：允许同一局域网访问
- `add_user`中的`perm` 是指文件或目录的权限，用于控制用户对其进行的操作。具体来说，`elradfmwMT` 是一些权限标识符的组合，表示不同的权限。
    - `e`：允许用户进入（enter）目录。
    - `l`：允许用户列出（list）目录的内容。
    - `r`：允许用户读取（read）文件或目录的内容。
    - `a`：允许用户添加（append）数据到文件末尾，可用于往文件中写入内容。
    - `d`：允许用户删除（delete）文件或目录。
    - `f`：允许用户重命名（rename）文件或目录。
    - `m`：允许用户修改（modify）文件或目录的权限。
    - `w`：允许用户写入（write）文件或目录，可用于创建、编辑或覆盖现有文件。
    - `M`：允许用户获得文件的消息摘要（message-digest）。

这些标识符可以以不同的组合形式出现，以指定不同的权限集合。

例如，`elradfmwMT` 表示用户具有完全权限，即可以进入目录、列出目录内容、读取文件内容、添加数据到文件末尾、删除文件或目录、重命名文件或目录、修改文件或目录的权限、写入文件或目录，以及获取文件的消息摘要。

### 可能存在的问题

问题：可能在运行python文件的时候会出现该问题`OSError: [Errno 13] Permission denied`

解决：可以通过`sudo python3 main.py`来解决，注意`main.py`是上述解答示例代码的py文件名称

问题：在macOS下通常不能直接像Windows系统访问FTP

解决：可以使用Cyberduck免费版本

### Cyberduck的截图效果

![Untitled](029_FTP%E6%96%87%E4%BB%B6%E5%88%86%E4%BA%AB%20424d59edb83d4323935b4490836af41d/Untitled.png)