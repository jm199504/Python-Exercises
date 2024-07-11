from solution import length_of_longest_substring


def test_length_of_longest_substring():
    assert length_of_longest_substring("") == 0
    assert length_of_longest_substring("abcabcbb") == 3  # "abc"
    assert length_of_longest_substring("bbbbb") == 1  # "b"
    assert length_of_longest_substring("pwwkew") == 3  # "wke"
    assert length_of_longest_substring("dvdf") == 3  # "ddf"
    assert length_of_longest_substring("abcdd") == 4  # "abc"
    assert length_of_longest_substring("aab") == 2  # "aa"


# 运行测试
if __name__ == "__main__":
    test_length_of_longest_substring()
    print("All tests passed!")
