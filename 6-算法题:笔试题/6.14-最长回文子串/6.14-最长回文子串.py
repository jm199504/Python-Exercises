def longest_palindromic_substring(s):
    if not s:
        return ""

    n = len(s)
    # 初始化一个二维数组dp，dp[i][j]表示s[i:j+1]是否为回文串
    dp = [[False] * n for _ in range(n)]
    # 初始化单个字符为回文串
    for i in range(n):
        dp[i][i] = True

    start = 0
    max_len = 1

    # 遍历所有子串
    for j in range(1, n):
        for i in range(j):
            # 如果两个字符相等，并且子串长度小于等于3（或者去掉首尾字符的子串是回文串）
            if s[i] == s[j] and (j - i <= 2 or dp[i + 1][j - 1]):
                dp[i][j] = True
                # 更新最长回文子串的起始位置和长度
                if j - i + 1 > max_len:
                    start = i
                    max_len = j - i + 1

                    # 返回最长回文子串
    return s[start:start + max_len]