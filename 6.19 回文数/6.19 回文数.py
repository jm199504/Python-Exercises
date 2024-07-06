

def is_palindrome(n):
    # 将整数转换为字符串
    str_n = str(n)
    # 检查字符串是否与其反转字符串相等
    return str_n == str_n[::-1]