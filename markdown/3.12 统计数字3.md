# 3.12 统计数字3

### 问题描述

编写一个count(3)函数统计1-100以内有几个数字3

### 解答一思路

（1）将数字传递进来后，使用`str()`强制转换为string类型

（2）使用`count(’3’)`获取3的个数

### 解答一示例代码

```python
def count_3():
    count = 0
    # 循环遍历1-100之间的所有数字
    for i in range(1, 101):
        # 将数字转换成字符串，以便使用字符串中的方法，统计当前数字中3的个数，并加到计数器中
        count += str(i).count('3')
    return count

print(count_3())
```

### 解答二思路

（1）可以通过分别获取百、十、个位的数字

（2）判断是否为3，累加即可

### 解答二示例代码

```python
def count_3():
    count = 0
    for i in range(1, 101):
        hundred = i // 100
        tens = (i - 100 * hundred) // 10
        single_digit = i - 100 * hundred - 10 * tens
        for num in [hundred, tens, single_digit]:
            if int(num) == 3:
                count += 1
    return count

print(count_3())
```

-