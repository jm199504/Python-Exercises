import random
import string


def generate_random_str(random_length):
    # random.sample() : 提取出N个不同元素的样本用来做进一步的操作
    # string.digits : 0123456789
    # string.ascii_letters : abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
    coupon = random.sample(string.digits + string.ascii_letters, random_length)
    return ''.join(coupon)  # random.sample返回的是list类型而转成string


coupons = list()
for i in range(10):
    single_result = generate_random_str(20)
    print(single_result)
    coupons.append(single_result)
