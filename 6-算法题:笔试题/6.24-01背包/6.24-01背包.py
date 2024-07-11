"""
输入两个整数 n,m ,n表示你拥有的积分，m表示有多少礼品
接下来有m行，每行a和b，a表示物品所需要消耗的积分，b表示这个物品大家的喜爱值
a和b取值范围是[1,100]，装入最多的喜爱值。
Input:
68 3
69 10
60 1
8 2
Output:
    3
"""
n_m = input().split(' ')
n = int(n_m[0])
m = int(n_m[1])
items = []
for i in range(m):
    r = input().split(' ')
    items.append([int(r[0]), int(r[1])])
# items[0] 重量； items[1] 价值
s = [0 for i in range(0, n + 1)]

for i in range(0, m):# 物品个数
    for j in range(n, items[i][0]-1, -1):# 背包承重<-单物重量
        s[j] = max(s[j], s[j - items[i][0]] + items[i][1])# max(s[i],s[i-该重量]+该价值)
print(s[n])
