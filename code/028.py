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
