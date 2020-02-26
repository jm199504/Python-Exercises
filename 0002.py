# 第 0002 题: 将 0001 题生成的 200 个激活码（或者优惠券）保存到 MySQL 关系型数据库中。

# 调用第0001题
import random,string

def generate_random_str(randomLength):
    # random.sample() : 提取出N个不同元素的样本用来做进一步的操作
    # string.digits : 0123456789
    # string.ascii_letters : abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
    coupon = random.sample(string.digits+string.ascii_letters,randomLength)
    # random.sample返回的是list类型而转成string
    stringList = ''.join(coupon)
    return stringList

coupons = list()
for i in range(200):
    coupons.append(generate_random_str(20))

print(coupons)

# 第0002题
import pymysql

# 打开数据库连接
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='jimdb', charset='utf8mb4')

cursor = conn.cursor()

nos = list(range(1,len(coupons)+1))

for i,j in zip(nos,coupons):
    cursor.executemany("INSERT INTO couponList (num,coupon)VALUES(%s,%s)",[(i,j)])
    conn.commit()