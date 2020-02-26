# 第 0001 题： 做为 Apple Store App 独立开发者，你要搞限时促销，
# 为你的应用生成激活码（或者优惠券），使用 Python 如何生成 200 个激活码（或者优惠券）？
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
for i in range(10):
    coupons.append(generate_random_str(20))

print(coupons)