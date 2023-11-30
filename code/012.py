"""
KiKi学习了循环，BoBo老师给他出了一系列打印图案的练习，该任务是打印用“*”组成的菱形图案。
"""


# 方法一
def print_diamond(num):
    for i in range(1, num + 1):  # 输出上半部分三角形
        print(" " * (num + 1 - i) + "* " * i)
    for j in range(num + 1, 0, -1):  # 输出下半部分三角形
        print(" " * (num + 1 - j) + "* " * j)


size = int(input())
print_diamond(size)


"""
# 方法二
def print_diamond(num):
    # 上半部分三角形（包含最长的一行）
    # “*” 数量由 1 -> num + 1（注意Python的for左闭右开）
    for i in range(1, num + 2):
        # 每一行字符串总长度（包含“*”和“ ”）：num + 行号(i)
        print(('* ' * i).rstrip().rjust(i + num))
    # 下半部分三角形
    # “*” 数量由 num 至 1
    count = 0  # 空格的数量
    # 每一行字符串总长度：2倍"*"的数量 + 空格（由1开始递增）
    for j in range(num, 0, -1):
        print(('* ' * j).rstrip().rjust(2 * j + count))
        count += 1


size = int(input())
print_diamond(size)
"""
