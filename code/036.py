# 方法一
def count_3(num):
    count = 0
    # 循环遍历1-100之间的所有数字
    for i in range(1, num):
        # 将数字转换成字符串，以便使用字符串中的方法，统计当前数字中3的个数，并加到计数器中
        count += str(i).count('3')
    return count


# 方法二
# def count_3():
#     count = 0
#     for i in range(1, 101):
#         hundred = i // 100
#         tens = (i - 100 * hundred) // 10
#         single_digit = i - 100 * hundred - 10 * tens
#         for num in [hundred, tens, single_digit]:
#             if int(num) == 3:
#                 count += 1
#     return count


print(count_3())
