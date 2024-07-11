from solution import  permute


def test_permute():
    nums = [1, 2, 3]
    expected = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 2, 1], [3, 1, 2]]
    assert permute(nums) == expected
    print("全排列测试用例通过！")


# 运行测试
if __name__ == "__main__":
    test_permute()
    print("All tests passed!")
