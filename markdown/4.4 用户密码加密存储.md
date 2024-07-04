# 4.4 用户密码加密存储

### 问题描述

登录某个网站或者 APP，需要使用用户名和密码。密码是如何加密后存储起来的呢？请使用HMAC对密码加密。

### HMAC介绍

HMAC（Hash-based Message Authentication Code）是一种基于哈希函数和密钥进行消息认证的技术，可以用于校验数据完整性、防范篡改等安全场景。

HMAC算法基于哈希函数，通过加入一个密钥对哈希过程进行改进，具有以下特点：

- 具有非常高的安全性。只有通过 HMAC 分配的密钥才能生成正确的散列值，因此即使散列值被截获，攻击者也无法进行有效的信息窃取。
- 具有良好的可扩展性。可以灵活地添加新的哈希算法，并且对密钥的长度和哈希输出的长度等都具有良好的可调性。

下面是一个使用Python实现HMAC加密的示例：

```python
import hmac

# 生成密钥和消息
secret_key = b"my_secret_key"
message = b"Hello, world!"

# 计算HMAC值
hmac_value = hmac.new(secret_key, message, digestmod="SHA256").hexdigest()

# 输出计算结果
print("HMAC值：", hmac_value)
```

使用了Python内置的`hmac`模块来完成HMAC的计算。`hmac.new()`函数接受3个参数：

- `secret_key`：用于加密的密钥，类型是bytes；
- `message`：要加密的消息，类型是bytes；
- `digestmod`：哈希算法的名称，例如"SHA256"、"MD5"等。

在这个示例中，我们选择了SHA-256算法作为哈希算法，并使用`hexdigest()`函数将结果输出为一个16进制字符串。

### 哈希值介绍

哈希值是一个固定长度的数据，通常用作对输入数据进行摘要或者签名的一种方式。哈希函数将任意长度的输入转换为固定长度的输出，这个输出就是哈希值。

哈希函数具有以下特性：

1. 固定长度：无论输入数据有多长，哈希函数都会生成具有固定长度的哈希值。
2. 唯一性：不同的输入数据通常会产生不同的哈希值。即使输入数据仅有微小的变化，其哈希值也会有很大的不同。
3. 不可逆性：哈希函数是单向的，意味着无法从哈希值反推回原始输入数据。这使得哈希值在密码存储和安全校验中很有用。

常见的哈希算法包括MD5、SHA-1、SHA-256等。在密码校验中，将用户输入的密码进行哈希处理，然后将哈希值与存储的哈希值进行比对，以验证密码的准确性。即使攻击者获取到哈希值，也无法直接获取原始密码，增加了密码的安全性。

由于哈希函数是确定性的，相同的输入将始终产生相同的哈希值。为了增加安全性，通常需要对密码进行加盐处理，即在密码中添加一些随机数据（盐），然后再进行哈希。这样即使两个用户使用相同的密码，其哈希值也将不同，增加了密码的破解难度。

### 解答示例代码

假设我们正在开发一个Web应用程序，需要对用户的密码进行加密存储。我们可以使用HMAC对密码进行加密，并在存储到数据库中前，首先对密码进行哈希，然后将哈希值与用户ID拼接后，再进行一次HMAC计算。这样可以保证即使数据库被攻破，攻击者也无法还原出用户的原始密码。

```python
import hmac
import hashlib
import os

def generate_hmac_key():
    """生成随机密钥"""
    return os.urandom(16)

def hash_password(password, user_id, secret_key):
    """对密码进行HMAC加密"""
    # 计算哈希值
    hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
    # 拼接用户ID和哈希值
    message = f"{user_id}:{hashed_password}".encode('utf-8')
    # 使用HMAC计算散列值
    hmac_value = hmac.new(secret_key, message, digestmod=hashlib.sha256).hexdigest()
    # 返回HMAC值
    return hmac_value

def verify_password(password, user_id, secret_key, stored_hmac):
    """校验密码是否正确"""
    # 重新计算密码的HMAC值
    computed_hmac = hash_password(password, user_id, secret_key)
    # 对比计算得到的HMAC值和存储的HMAC值是否一致
    return hmac.compare_digest(computed_hmac, stored_hmac)

# 示例
password = 'mypassword'
user_id = '123456'

# 生成密钥
secret_key = generate_hmac_key()

# 对密码进行加密
hashed_password = hash_password(password, user_id, secret_key)
print('HMAC值:', hashed_password)

# 校验密码是否正确
is_password_valid = verify_password(password, user_id, secret_key, hashed_password)
print('密码校验结果:', is_password_valid)
```

### 结论

根据上述的代码可知，网站数据库除了存储`用户ID`和`账号密码`外，还需要额外存储`用户密钥`，校验密码时通过上述的`verify_password`来验证。