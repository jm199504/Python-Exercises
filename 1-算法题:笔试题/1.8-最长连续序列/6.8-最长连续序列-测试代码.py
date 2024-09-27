from solution import longest_consecutive


def test_longest_consecutive():
    example_1 = {
        "input": [100, 4, 200, 1, 3, 2],
        "output": 4
    }

    example_2 = {
        "input": [0, 3, 7, 2, 5, 8, 4, 6, 0, 1],
        "output": 9
    }

    assert longest_consecutive(example_1["input"]) == example_1["output"]
    assert longest_consecutive(example_2["input"]) == example_2["output"]


# 运行测试
if __name__ == "__main__":
    test_longest_consecutive()
    print("All tests passed!")
