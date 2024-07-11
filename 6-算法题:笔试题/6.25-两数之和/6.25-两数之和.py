def two_sum(nums, target):
    d = {}
    for i in range(len(nums)):
        a = target - nums[i]
        if nums[i] in d:
            return d[nums[i]], i
        else:
            d[a] = i
