def longest_consecutive(nums):
    res = 0  # 最长连续序列的长度
    num_set = set(nums)  # 记录nums中的所有数值
    for num in num_set:
        # 若当前数是一个连续序列的起点（最小值），则统计这个连续序列的长度
        if (num - 1) not in num_set:
            seq_len = 1     # 连续序列的长度初始长度等于1
            while (num + 1) in num_set:  # 若该连续序列存在则持续追加，直至连续序列中断
                seq_len += 1
                num += 1
            res = max(res, seq_len)  # 更新最长连续序列长度
    return res
