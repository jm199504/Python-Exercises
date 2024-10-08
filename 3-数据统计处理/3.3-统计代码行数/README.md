# 3.3-统计代码行数

### 问题描述

有一个代码目录，统计一下写过多少行代码。包括空行和注释，分别列出来。

### 示例代码

```bash
import os
import re

def count_lines(file_path):
    """
    统计 Python 文件的行数、空行数和注释行数。

    :param file_path:   文件路径
    :return:            文件总行数、空行数和注释行数
    """
    total_empty_lines = 0
    total_comment_lines = 0

    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

        # 统计空行和注释行
        for line in lines:
            line = line.strip()
            if line == "":
                total_empty_lines += 1
            elif re.match(r"^\s*#", line):
                total_comment_lines += 1

    return len(lines), total_empty_lines, total_comment_lines

directory = "your_directory_path"  # 替换为你的目录路径
files = [file for file in os.listdir(directory) if file.endswith(".py")]

for file in files:
    file_path = os.path.join(directory, file)
    lines, empty_lines, comment_lines = count_lines(file_path)

    print("文件: ", file)
    print("总行数: ", lines)
    print("空行数: ", empty_lines)
    print("注释行数: ", comment_lines)
    print()
```

### 测试代码文件

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
for i in range(10):
    single_result = generate_random_str(20)
    print(single_result)
    coupons.append(single_result)
```

### 结果输出

```bash
文件:  0001.py
总行数:  17
空行数:  4
注释行数:  3
```

