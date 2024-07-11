a = [1, 1, 2, 3, 3, 2, 5, 6, 5]

count = a[0]

for i in range(1, len(a)):
    count ^= a[i]

print(count)
