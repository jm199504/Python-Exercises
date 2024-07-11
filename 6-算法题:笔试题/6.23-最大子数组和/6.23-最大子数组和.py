def max_sub_array(nums):
    size = len(nums)
    pre = 0
    res = nums[0]
    for i in range(size):
        pre = max(nums[i], pre + nums[i])
        res = max(res, pre)
    return res
