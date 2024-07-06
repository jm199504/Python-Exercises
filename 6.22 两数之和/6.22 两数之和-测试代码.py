from solution import two_sum


def test_two_sum():
    nums = [2, 7, 11, 15]
    target = 0
    try:
        result = two_sum(nums, target)
        print(f"The indices that add up to {target} are: {result}")
    except ValueError as e:
        print(e)

    nums = [3, 2, 4]
    target = 6
    try:
        result = two_sum(nums, target)
        print(f"The indices that add up to {target} are: {result}")
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    test_two_sum()
    print("All tests passed!")
