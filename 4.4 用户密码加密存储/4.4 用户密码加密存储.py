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
