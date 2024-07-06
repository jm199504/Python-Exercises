def two_sum(nums, target):
    # 创建一个字典来存储已经遍历过的数和它们的索引
    num_dict = {}

    for i, num in enumerate(nums):
        # 计算目标和与当前数的差值
        complement = target - num

        # 检查差值是否已经在字典中
        if complement in num_dict:
            # 如果在，那么返回这两个数的索引
            return [num_dict[complement], i]

            # 如果差值不在字典中，将当前数和它的索引添加到字典中
        num_dict[num] = i

        # 如果没有找到符合条件的两个数，抛出异常
    raise ValueError("No two sum solution")
