# 003_插入MySQL数据库

### 问题描述

将生成促随机码题目生成的 200 个激活码（或者优惠券）保存到 MySQL 关系型数据库中。

### 解答思路

1、启动MySQL服务，并建立好数据库和表

2、使用`pymysql`插入数据

### **使用 Docker 安装 MySQL**

（1）确保已经安装 Docker 客户端和服务器。

（2）在终端中执行以下命令拉取 MySQL 镜像：

```
docker pull mysql
```

（3）通过以下命令创建一个名为“mysql_container”的容器，并将容器中的3306端口映射到宿主机上的3306端口：

```
docker run -it -d -e MYSQL_ROOT_PASSWORD=123456 -p 3306:3306 --name mysql_container mysql
```

- “-it”指定终端交互模式
- “-d”指定容器在后台运行
- “-e MYSQL_ROOT_PASSWORD=123456”设置MYSQL_ROOT用户的密码为123456
- “-p 3306:3306”指定宿主机端口3306与容器中的3306端口映射
- “--name mysql_container”指定容器名称为mysql_container
- “mysql”表示使用mysql镜像。

（4）启动容器：

```
docker start mysql_container
```

（5）进入容器：

```
docker exec -it mysql_container bash
```

（6）登录mysql：

```
mysql -u root -p
```

（7）输入密码

```
123456
```

（8）新建数据库

```
CREATE DATABASE jimdb;
```

（9）使用指定数据库

```bash
USE jimdb;
```

（10）新建数据库表

```bash
CREATE TABLE couponList (
    id INT PRIMARY KEY AUTO_INCREMENT,
    code VARCHAR(255) NOT NULL,
    description VARCHAR(255)
);
```

### 解答示例代码

```bash
import random
import string
import pymysql

def generate_random_str(random_length):
    coupon = random.sample(string.digits + string.ascii_letters, random_length)
    return ''.join(coupon)

coupons = list()
for i in range(10):
    single_result = generate_random_str(20)
    coupons.append(single_result)

# 打开数据库连接
conn = pymysql.connect(
    host='127.0.0.1',  # 数据库主机地址
    port=3306,  # 数据库端口号
    user='root',  # 数据库用户名
    passwd='123456',  # 数据库密码
    db='jimdb',  # 要连接的数据库名
    charset='utf8mb4'  # 字符编码
)

cursor = conn.cursor()

nos = list(range(1, len(coupons) + 1))  # 设置编号

for i, j in zip(nos, coupons):
    cursor.executemany("INSERT INTO couponList (id, code) VALUES (%s,%s)", [(i, j)])
    conn.commit()  # 提交事务，保存插入的数据到数据库中
```

### 结果预览

```bash
mysql> use jimdb;
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

Database changed
mysql> select * from couponList;
+----+----------------------+-------------+
| id | code                 | description |
+----+----------------------+-------------+
|  1 | rlfyqGDVSzeYb8hOTw4J | NULL        |
|  2 | 4MHhlvyIBzcjYapo6nwE | NULL        |
|  3 | TXVa9qltK4GvYoQjzMcI | NULL        |
|  4 | UqhFGElXSJL9o7kKPe3B | NULL        |
|  5 | Axot6kBzZd43aKVP5iTe | NULL        |
|  6 | u6wLKEMnijYPrexWXmyt | NULL        |
|  7 | vZV5LA64lNzGDyCjOnps | NULL        |
|  8 | SoBc4qk8h2DQtdOWV9Kr | NULL        |
|  9 | jzqDIBpyK4un3t8Rog7d | NULL        |
| 10 | aJzH4sXjVPt7E8GMl6oQ | NULL        |
+----+----------------------+-------------+
10 rows in set (0.00 sec)
```

---

### 可能存在问题

【问题】出现“RuntimeError: 'cryptography' package is required for sha256_password or caching_sha2_password auth methods”问题

【解决】指出缺少名为 “cryptography” 的包，这是用于支持 “sha256_password” 或 “caching_sha2_password” 身份验证方法的包。

```bash
pip3 install cryptography
```

但是存在网络超时的情况，使用清华大学的镜像站点进行安装：

```bash
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple cryptography
```

