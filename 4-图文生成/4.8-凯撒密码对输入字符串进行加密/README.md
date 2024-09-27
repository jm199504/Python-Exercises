## 4.8-凯撒密码对输入字符串进行加密

### 问题描述
接受一个字符串和一个移位值作为参数，然后返回加密后的字符串。加密过程是通过将字符串中的每个字母字符按照移位值进行循环移位来实现的，非字母字符保持不变。

### 示例代码
```python
def encrypt_string(input_string, shift):
    """
    使用凯撒密码对输入字符串进行加密。

    参数:
    - input_string (str): 要加密的字符串。
    - shift (int): 字符应该向前移动的数量。

    返回:
    - encrypted_string (str): 加密后的字符串。
    """
    encrypted_string = ""

    for char in input_string:
        if char.isalpha():
            # 确定ASCII基础值（大写字母使用 'A'，小写字母使用 'a'）
            base = ord('A') if char.isupper() else ord('a')

            # 计算移位后的字符
            shifted_char = chr((ord(char) - base + shift) % 26 + base)
            encrypted_string += shifted_char
        else:
            # 非字母字符保持不变
            encrypted_string += char

    return encrypted_string

# 示例用法:
original_string = "Hello, World!"
shift_amount = 3
encrypted = encrypt_string(original_string, shift_amount)

# 打印原始字符串和加密后的字符串
print(f"原始字符串: {original_string}")
print(f"加密后字符串: {encrypted}")
```

