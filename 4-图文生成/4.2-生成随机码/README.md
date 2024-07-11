# 4.2 生成随机码

### 问题描述

作为 Store App 独立开发者，你需要为你的应用生成随机码，使用 Python 如何生成 200 个随机码？

### 解答思路

1、明确随机码通常由数字（0-9）和字母（a-z，A-Z）组成

2、需要通过随机的方式生成长度为N的字符串，且需要200个

### 解答示例代码

```bash
import random
import string

def generate_random_str(random_length):
    # random.sample() : 提取出N个不同元素的样本用来做进一步的操作
    # string.digits : 0123456789
    # string.ascii_letters : abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
    coupon = random.sample(string.digits + string.ascii_letters, random_length)
    return ''.join(coupon)  # random.sample返回的是list类型而转成string

coupons = list()
for i in range(10):  # 生成10条激活码
    single_result = generate_random_str(20)  # 假设激活码长度为20
    print(single_result)
    coupons.append(single_result)
```

### 结果预览

```bash
Z7iEYPnRUsF5wOIVjmdM
qQ2zO6wUbZpmkrP3oigK
RbVs6WvC57Sf3EoijDXO
YG6tiqO7rJTRFShCdMNV
urXAHb5DTC1EP3GycJMg
t8wDedk4WzqCXNSvGToy
z1MROFPYmKigXpWLjSlG
JBrCv6AtI42f9gxi8Vkl
bO71oNqfGUFeHVrzh2x9
MeRsrhQZLgipoOt5vVj7
```

