## 7.8 使用pytest测试

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

