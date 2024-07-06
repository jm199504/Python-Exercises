def rotate(nums, k):
    k %= len(nums)  # 需要考虑nums长度小于k的情况
    nums[:] = nums[-k:] + nums[:-k]  # 将倒数k个元素挪至数组开头与剩余元素拼接
    return nums
