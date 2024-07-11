from solution import quicksort


# 测试用例
def test_quicksort():
    # 测试空数组
    assert quicksort([]) == []

    # 测试单元素数组
    assert quicksort([5]) == [5]

    # 测试已排序数组
    assert quicksort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

    # 测试逆序数组
    assert quicksort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

    # 测试有重复元素的数组
    assert quicksort([3, 6, 8, 10, 1, 2, 1]) == [1, 1, 2, 3, 6, 8, 10]

    # 测试随机数组
    assert quicksort([3, 6, 8, 10, 1, 2, 1, 5]) == [1, 1, 2, 3, 5, 6, 8, 10]


# 运行测试
if __name__ == "__main__":
    test_quicksort()
    print("All tests passed!")
