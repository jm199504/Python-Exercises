from solution import is_palindrome


# 测试用例
def test_is_palindrome():
    # 正测试用例
    assert is_palindrome(121)  # 121 是回文数
    assert is_palindrome(1001)  # 10 不是回文数

    # 负测试用例
    assert not is_palindrome(10)  # 10 不是回文数
    assert not is_palindrome(123)  # 123 不是回文数
    assert not is_palindrome(-123)  # -123 也不是回文数
    print("所有测试用例通过！")


# 运行测试
if __name__ == "__main__":
    test_is_palindrome()
    print("All tests passed!")
