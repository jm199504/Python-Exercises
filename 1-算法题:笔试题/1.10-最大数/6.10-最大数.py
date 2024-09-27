def largest_number(nums):
    n = len(nums)
    nums = list(map(str, nums))  # 转换为字符串列表
    for i in range(n):
        for j in range(i + 1, n):
            # 若拼接后的字符串结果更小，则交换位置
            if nums[i] + nums[j] < nums[j] + nums[i]:
                nums[i], nums[j] = nums[j], nums[i]

    return str(int("".join(nums)))
