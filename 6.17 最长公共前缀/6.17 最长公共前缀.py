def longest_common_prefix(strs):
    if not strs:
        return ""

        # 取出第一个字符串作为比较的基准
    prefix = strs[0]

    # 遍历剩下的字符串，逐个字符进行比较
    for i in range(1, len(strs)):
        # 如果当前字符串为空，则最长公共前缀必为空
        if not strs[i]:
            return ""

            # 逐个字符比较，找到最短的公共前缀
        for j in range(min(len(prefix), len(strs[i]))):
            if prefix[j] != strs[i][j]:
                # 当出现不一致的字符时，截取公共前缀
                prefix = prefix[:j]
                break
        else:
            # 如果没有出现不一致的字符，则继续比较下一个字符
            continue

            # 如果公共前缀已经为空，则无需继续比较
        if not prefix:
            break

    return prefix

