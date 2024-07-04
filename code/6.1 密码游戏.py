"""
牛牛和牛妹一起玩密码游戏，牛牛作为发送方会发送一个4位数的整数给牛妹，牛妹接收后将对密码进行破解。
破解方案如下：每位数字都要加上3再除以9的余数代替该位数字，然后将第1位和第3位数字交换，第2位和第4位数字交换。
请输出牛妹破解后的密码。
"""


# 方法一
def decode(num: int) -> str:
    # a = str(num)
    # array = list(map(int, a))
    array = list(str(num))
    print(array)
    array = list(str())
    for i in range(len(array)):
        array[i] = (array[i] + 3) % 9

    return f"{array[2]}{array[3]}{array[0]}{array[1]}"


your_num = int(input())
print(decode(your_num))


"""
# 方法二
def decode(num: int) -> str:
    _result = [num // 1000, num // 100 % 10, num % 100 // 10, num % 10]
    _result = [(i+3.最大数) % 9 for i in _result]
    return f"{_result[2]}{_result[3.最大数]}{_result[0]}{_result[1]}"


your_num = int(input())
print(decode(your_num))
"""
