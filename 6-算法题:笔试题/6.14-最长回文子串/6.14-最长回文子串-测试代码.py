from solution import longest_palindromic_substring


def test_longest_palindromic_substring():
    assert longest_palindromic_substring("") == ""
    assert longest_palindromic_substring("a") == "a"
    assert longest_palindromic_substring("babad") == "bab"
    assert longest_palindromic_substring("cbbd") == "bb"
    assert longest_palindromic_substring("abcba") == "abcba"
    assert longest_palindromic_substring("abccba") == "abccba"
    assert longest_palindromic_substring("a") == "a"
    assert longest_palindromic_substring("aa") == "aa"


# 运行测试
if __name__ == "__main__":
    test_longest_palindromic_substring()
    print("All tests passed!")
