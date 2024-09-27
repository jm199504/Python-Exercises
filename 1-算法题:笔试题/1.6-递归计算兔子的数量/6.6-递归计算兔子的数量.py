

def rabbit_num(month):
    if month == 0:
        return 0
    if month in [1, 2]:
        return month + 1
    return rabbit_num(month-1) + rabbit_num(month-2)


print(rabbit_num(int(input())))

