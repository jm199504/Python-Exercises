## 7.8-使用pytest测试

### 问题描述

测试一个简单的用户管理系统，包括用户创建、用户验证和用户信息更新的功能。


### 测试示例
在这个测试文件中，我们定义了几个测试用例来测试UserManager类的不同方法：
`test_create_user`：测试用户创建功能，并验证新用户是否成功创建。
`test_create_existing_user`：测试尝试创建已存在用户的情况，并验证是否引发ValueError。
`test_authenticate_user`：测试用户验证功能，确保正确和错误的密码分别返回True和False，并且不存在的用户返回False。
`test_update_user_email`：测试更新用户邮箱功能，并验证更新后的邮箱是否正确。
`test_update_nonexistent_user_email`：测试尝试更新不存在的用户的邮箱，并验证是否引发ValueError。
`test_get_user_email`：测试获取用户邮箱功能，并验证返回的邮箱地址是否正确。
`test_get_nonexistent_user_email`：测试尝试获取不存在的用户的邮箱，并验证是否引发ValueError。

### 示例代码（user_manager.py）

```python
class User:
    def __init__(self, username, password, email):
        self.username = username
        self.password = password  # 注意：实际中应加密存储
        self.email = email

class UserManager:
    def __init__(self):
        self.users = {}

    def create_user(self, username, password, email):
        if username in self.users:
            raise ValueError("User already exists")
        self.users[username] = User(username, password, email)

    def authenticate_user(self, username, password):
        user = self.users.get(username)
        if user and user.password == password:
            return True
        return False

    def update_user_email(self, username, new_email):
        if username not in self.users:
            raise ValueError("User does not exist")
        self.users[username].email = new_email

    def get_user_email(self, username):
        if username not in self.users:
            raise ValueError("User does not exist")
        return self.users[username].email
```

### 示例代码（test_user_manager.py）

```python
import pytest
from user_manager import UserManager  # 假设上面的用户管理系统类保存在user_manager.py中

@pytest.fixture
def user_manager():
    return UserManager()

def test_create_user(user_manager):
    user_manager.create_user("test_user", "password", "test@example.com")
    assert user_manager.get_user_email("test_user") == "test@example.com"

def test_create_existing_user(user_manager):
    user_manager.create_user("test_user", "password", "test@example.com")
    with pytest.raises(ValueError, match="User already exists"):
        user_manager.create_user("test_user", "password", "test@example.com")

def test_authenticate_user(user_manager):
    user_manager.create_user("test_user", "password", "test@example.com")
    assert user_manager.authenticate_user("test_user", "password") is True
    assert user_manager.authenticate_user("test_user", "wrong_password") is False
    assert user_manager.authenticate_user("nonexistent_user", "password") is False

def test_update_user_email(user_manager):
    user_manager.create_user("test_user", "password", "test@example.com")
    user_manager.update_user_email("test_user", "new_email@example.com")
    assert user_manager.get_user_email("test_user") == "new_email@example.com"

def test_update_nonexistent_user_email(user_manager):
    with pytest.raises(ValueError, match="User does not exist"):
        user_manager.update_user_email("nonexistent_user", "new_email@example.com")

def test_get_user_email(user_manager):
    user_manager.create_user("test_user", "password", "test@example.com")
    assert user_manager.get_user_email("test_user") == "test@example.com"

def test_get_nonexistent_user_email(user_manager):
    with pytest.raises(ValueError, match="User does not exist"):
        user_manager.get_user_email("nonexistent_user")
```

### 测试命令

```
pytest test_user_manager.py
```

