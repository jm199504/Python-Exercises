# 1.1 统计函数运行时长

### 问题描述

现有一个流程涉及调用多个函数，但最近发现流程整体运行时间慢，现需要对每一个函数统计运行时长，小阳同学知道在函数最开始获取`time.time()`，在函数最后获取`time.time()`，通过相减即可获得函数运行时长，但是每一个函数都要这么写会相当繁琐。

### 解答思路

使用装饰器对每一个函数装饰，装饰器在调用`func()`前后获取`time.time()`，计算各函数的运行时长。

### 装饰器（Decorator）介绍

装饰器用于修改函数或类的行为的设计模式。

装饰器允许您在不修改原始函数或类的情况下，给它们添加新的功能，这使得代码更具可重用性和可扩展性。

简而言之，装饰器就像一个包装，它可以为被装饰的函数或类添加一些额外的功能。

Python示例：

```python
def my_decorator(func):
    def wrapper():
        print("Do something before the function is called.")
        func()
        print("Do something after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello, world!")

say_hello()
```

### 解答示例代码

使用装饰器记录函数的执行时间

```python
import time  # 导入time模块

def timing_decorator(func):  # 定义计时装饰器函数，接受一个函数作为参数
    def wrapper(*args, **kwargs):  # 定义包装器函数，用于包裹被装饰的函数
        start_time = time.time()  # 记录函数开始执行的时间
        result = func(*args, **kwargs)  # 执行被装饰的函数，并获取其返回值
        end_time = time.time()  # 记录函数执行结束的时间
        print(f"{func.__name__} took {end_time - start_time:.2f} seconds to run.")  # 打印函数执行所花费的时间
        return result  # 返回被装饰函数的返回值
    return wrapper  # 返回包装器函数

@timing_decorator  # 使用装饰器语法将slow_function函数应用计时装饰器
def slow_function():  # 定义一个被装饰的函数
    time.sleep(2)  # 在函数内部使用time.sleep函数暂停2秒钟

slow_function()  # 调用被装饰后的slow_function函数，此时会自动计时并输出执行时间
```

### 装饰器的其它常见应用

装饰器还有其它很多常见的应用，例如：

访问控制：使用装饰器实现用户身份验证、权限检查等功能

```python
def admin_required(func):
    def wrapper(user, *args, **kwargs):
        if user.is_admin:
            return func(user, *args, **kwargs)
        else:
            raise PermissionError("Only admins can access this function.")
    return wrapper

@admin_required
def restricted_function(user):
    print("You have access to this restricted function.")

class User:
    def __init__(self, is_admin):
        self.is_admin = is_admin

admin = User(is_admin=True)
non_admin= User(is_admin=False)

try: restricted_function(admin) except PermissionError as e: print(e)

try: restricted_function(non_admin) except PermissionError as e: print(e)
```

日志记录：使用装饰器自动记录函数的调用日志。

```python
import logging

def log_decorator(func):
    def wrapper(*args, **kwargs):
        logging.basicConfig(level=logging.INFO)
        logging.info(f"Function '{func.__name__}' is called with arguments: {args}, {kwargs}")
        result = func(*args, **kwargs)
        logging.info(f"Function '{func.__name__}' has finished.")
        return result
    return wrapper

@log_decorator
def example_function(a, b, c=3):
    print("This is an example function.")
    return a + b + c

example_function(1, 2, c=4)
```