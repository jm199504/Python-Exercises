from solution import multiply_string


def test_multiply_string():
    # 正测试用例
    assert multiply_string('abc', 3) == 'abcabcabc'
    assert multiply_string('Hello', 2) == 'HelloHello'
    assert multiply_string('', 5) == ''
    # 负测试用例
    assert multiply_string('abc', 0) == ''
    assert multiply_string('abc', -1) == ''  # 在这个自定义函数中，我们假设负数乘法结果为空字符串


# 运行测试
if __name__ == "__main__":
    test_multiply_string()
    print("All tests passed!")
