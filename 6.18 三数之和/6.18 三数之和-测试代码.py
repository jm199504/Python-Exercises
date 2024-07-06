from solution import three_sum


def test_three_sum():
    nums = [-1, 0, 1, 2, -1, -4]
    expected = [[-1, -1, 2], [-1, 0, 1]]
    assert three_sum(nums) == expected


# 运行测试
if __name__ == "__main__":
    test_three_sum()
    print("All tests passed!")


