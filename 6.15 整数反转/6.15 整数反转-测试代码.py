from solution import reverse_integer


def test_reverse_integer():
    assert reverse_integer(123) == 321
    assert reverse_integer(-123) == -321
    assert reverse_integer(120) == 21
    assert reverse_integer(0) == 0
    assert reverse_integer(1534236469) == 0  # 超出int范围，返回0
    assert reverse_integer(-1534236469) == 0  # 超出int范围，返回0


# 运行测试
if __name__ == "__main__":
    test_reverse_integer()
    print("All tests passed!")
