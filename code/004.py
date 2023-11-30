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


# -------------------------------
"""
从redis读取指定字段

import redis

# 打开 Redis 数据库连接
r = redis.Redis(host='localhost', port=6379, decode_responses=True)

# 获取 1 到 10 这 10 个键的值
keys = [str(i) for i in range(1, 11)]
values = r.mget(keys)

# 输出结果
for i, value in zip(keys, values):
    print(f"Key: {i}, Value: {value}")

"""