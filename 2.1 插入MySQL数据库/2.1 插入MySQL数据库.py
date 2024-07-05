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
