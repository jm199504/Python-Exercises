from solution import largest_number


def test_largest_number():
    example_1 = {
        "input": [10, 2],
        "output": "210"
    }

    example_2 = {
        "input": [3, 30, 34, 5, 9],
        "output": "9534330"
    }

    assert largest_number(example_1["input"]) == example_1["output"]
    assert largest_number(example_2["input"]) == example_2["output"]


# 运行测试
if __name__ == "__main__":
    test_largest_number()
    print("All tests passed!")
