from solution import  longest_common_prefix


def test_longest_common_prefix():
    assert longest_common_prefix(["flower", "flow", "flight"]) == "fl"
    assert longest_common_prefix(["dog", "racecar", "car"]) == ""
    assert longest_common_prefix([]) == ""
    assert longest_common_prefix(["a"]) == "a"
    assert longest_common_prefix(["ab", "abc"]) == "ab"
    assert longest_common_prefix(["abc", "abcd", "abcde"]) == "abc"


# 运行测试
if __name__ == "__main__":
    test_longest_common_prefix()
    print("All tests passed!")
