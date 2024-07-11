from solution import max_sub_array


def test_max_sub_array():
    example_1 = {
        "input": [-2, 1, -3, 4, -1, 2, 1, -5, 4],
        "output": 6
    }

    example_2 = {
        "input": [1],
        "output": 1
    }

    example_3 = {
        "input": [5, 4, -1, 7, 8],
        "output": 23
    }

    assert max_sub_array(example_1["input"]) == example_1["output"]
    assert max_sub_array(example_2["input"]) == example_2["output"]
    assert max_sub_array(example_3["input"]) == example_3["output"]


# 运行测试
if __name__ == "__main__":
    test_max_sub_array()
    print("All tests passed!")
