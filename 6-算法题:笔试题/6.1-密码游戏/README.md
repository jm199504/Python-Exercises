# 6.1 密码游戏

### 问题描述

牛牛和牛妹一起玩密码游戏，牛牛作为发送方会发送一个4位数的整数给牛妹，牛妹接收后将对密码进行破解。

破解方案如下：每位数字都要加上3再除以9的余数代替该位数字，然后将第1位和第3位数字交换，第2位和第4位数字交换。

请输出牛妹破解后的密码。

### **输入描述**

输入一个四位数的整数。

### **输出描述**

输出破解后的密码，以四位数的形式。

### **示例**

输入：`1234`

输出：`6745`

### 备注

`输入不会有前置0，但是输出要保持前置0`

### 解题思路一

（1）将接收的整数转为字符串格式

（2）将字符串转为整型数组

（3）按照题目要求循环处理每一位数字

（4）按照交换要求输出每一位数字

### 解答一示例代码

```python
def decode(num: int) -> str:
    a = str(num)
    array = list(map(int, a))
    for i in range(len(array)):
        array[i] = (array[i] + 3) % 9

    return f"{array[2]}{array[3]}{array[0]}{array[1]}"

your_num = int(input())
print(decode(your_num))
```

### 解题思路二

（1）将接收的整数使用数值运算分别提取每一位的数字

（2）存放至数组中

（3）按照题目要求循环处理每一位数字

（4）按照交换要求输出每一位数字

### 解答二示例代码

```python
def decode(num: int) -> str:
    _result = [num // 1000, num // 100 % 10, num % 100 // 10, num % 10]
    _result = [(i+3) % 9 for i in _result]
    return f"{_result[2]}{_result[3]}{_result[0]}{_result[1]}"

your_num = int(input())
print(decode(your_num))
```

