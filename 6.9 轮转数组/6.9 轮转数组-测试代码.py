from solution import rotate


def test_rotate():
    example_1 = {
        "input": {
            "nums": [1, 2, 3, 4, 5, 6, 7],
            "k": 3
        },
        "output": [5, 6, 7, 1, 2, 3, 4]
    }

    example_2 = {
        "input": {
            "nums": [-1, -100, 3, 99],
            "k": 2
        },
        "output": [3, 99, -1, -100, 3]
    }

    example_1_result = rotate(example_1["input"]["nums"], example_1["input"]["k"])
    example_1_expect = example_1["output"]

    for i, j in zip(example_1_result, example_1_expect):
        assert i == j

    example_2_result = rotate(example_2["input"]["nums"], example_2["input"]["k"])
    example_2_expect = example_2["output"]

    for i, j in zip(example_2_result, example_2_expect):
        assert i == j


# 运行测试
if __name__ == "__main__":
    test_rotate()
    print("All tests passed!")
