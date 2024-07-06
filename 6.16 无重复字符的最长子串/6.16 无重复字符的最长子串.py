def length_of_longest_substring(s):
    # 如果输入的字符串为空，则返回0
    if not s:
        return 0

    left, max_len, cur_len = 0, 0, 0
    # 使用集合来存储窗口内的字符，以便快速查找
    windows = set()

    # 遍历字符串s
    for i in range(len(s)):
        cur_len += 1
        # 如果当前字符已经在窗口内，则需要移动左指针，并更新当前长度
        while s[i] in windows:
            windows.remove(s[left])
            cur_len -= 1
            left += 1
        # 更新最大长度
        if cur_len > max_len:
            max_len = cur_len
        # 将当前字符加入窗口
        windows.add(s[i])

    # 返回最大长度
    return max_len
