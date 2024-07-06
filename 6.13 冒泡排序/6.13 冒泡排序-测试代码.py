from solution import bubble_sort


def test_bubble_sort():
    # 测试空数组
    assert bubble_sort([]) == []

    # 测试单元素数组
    assert bubble_sort([5]) == [5]

    # 测试已排序数组
    assert bubble_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

    # 测试逆序数组
    assert bubble_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

    # 测试有重复元素的数组
    assert bubble_sort([3, 6, 8, 10, 1, 2, 1]) == [1, 1, 2, 3, 6, 8, 10]

    # 测试随机数组
    assert bubble_sort([3, 6, 8, 10, 1, 2, 1, 5]) == [1, 1, 2, 3, 5, 6, 8, 10]


# 运行测试
if __name__ == "__main__":
    test_bubble_sort()
    print("All tests passed!")


