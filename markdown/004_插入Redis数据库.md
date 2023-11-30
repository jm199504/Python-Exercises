# 004_插入Redis数据库

### 问题描述

将生成随机码题目生成的 200 个激活码（或者优惠券）保存到 Redis 非关系型数据库中

### 解答思路

1、启动`Redis`服务

2、使用`redis`插入数据

### 使用 Docker 安装 Redis

通过阿里云 Docker 镜像源拉取 Redis 官方镜像：

```
docker pull redis
```

启动 Redis 容器：

```
docker run --name my-redis -d redis
```

其中，`my-redis` 是容器名称，可以根据实际情况修改。

进入 Redis 容器：

```bash
docker exec -it my-redis redis-cli
```

### 解答示例代码

```bash
import random
import string
import redis

def generate_random_str(random_length):
    coupon = random.sample(string.digits + string.ascii_letters, random_length)
    return ''.join(coupon)

coupons = list()
for i in range(10):
    single_result = generate_random_str(20)
    coupons.append(single_result)

# 打开Redis数据库连接
pool = redis.ConnectionPool(host='localhost', port=6379, decode_responses=True)
r = redis.Redis(connection_pool=pool)

nos = list(range(1, len(coupons) + 1))

for i, j in zip(nos, coupons):
    r.set(i, j)

for i in nos:
    print(r.get(str(i)))
```

### 从 Redis 获取Key 1-10

```bash
import redis

# 打开 Redis 数据库连接
r = redis.Redis(host='localhost', port=6379, decode_responses=True)

# 获取 1 到 10 这 10 个键的值
keys = [str(i) for i in range(1, 11)]
values = r.mget(keys)

# 输出结果
for i, value in zip(keys, values):
    print(f"Key: {i}, Value: {value}")
```

### 结果预览

```bash
Key: 1, Value: c5lB7jgGLHy6Yio3WAFI
Key: 2, Value: Mow6lPcgj153YCK72mxd
Key: 3, Value: h1s64vpgoNzrZBVf5bOH
Key: 4, Value: 9k7ihgZCHUBXVmYWIqGt
Key: 5, Value: QB6V4MTFnlOyHXI1Zg9k
Key: 6, Value: zn6tcarxoey2Ilf0CWmY
Key: 7, Value: 3naqXIHtfjm1Nx2TJwU9
Key: 8, Value: jlQeIdrcqVXZ9bHag54u
Key: 9, Value: r07lPnztOoNdshueS2gj
Key: 10, Value: 1fmAU2S6O5spYtRB4v7z
```