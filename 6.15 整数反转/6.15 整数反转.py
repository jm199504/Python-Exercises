def reverse_integer(n):
    # 初始化反转后的数字为0
    reversed_num = 0

    # 处理负数情况
    is_negative = False
    if n < 0:
        is_negative = True
        n = -n  # 转为正数进行处理

    # 反转数字
    while n > 0:
        reversed_num = reversed_num * 10 + n % 10
        n //= 10

        # 如果反转后的数字超出了int的范围，则返回0
    if reversed_num > 2 ** 31 - 1 or (is_negative and -reversed_num < -2 ** 31):
        return 0

        # 如果原数是负数，则反转后也应该是负数
    if is_negative:
        reversed_num = -reversed_num

    return reversed_num
