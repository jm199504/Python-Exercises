# 1.5-菱形图案

打印用“*”组成的菱形图案。

### **输入描述**

```
多组输入，一个整数（2~20）。
```

### **输出描述**

```
针对每行输入，输出用“*”组成的菱形，每个“*”后面有一个空格。
```

### 输入`2`，输出

```python
  * 
 * * 
* * * 
 * * 
  *
```

### 输入`3`，输出

```python
   * 
  * * 
 * * * 
* * * * 
 * * * 
  * * 
   *
```

### 输入`4`，输出

```python
    * 
   * * 
  * * * 
 * * * * 
* * * * * 
 * * * * 
  * * * 
   * * 
    *
```

### 解题思路1

通过分析示例数据之后，明确分上下两个三角形进行输出

（1）针对上半部分，我们假设输入的数字为`num`：

- 每一行的`“*”数量` ⇒ `行号`（注意：`行号`记作`i`，计数从`1`开始）
- 每一行的`开头“ ”数量` ⇒ `num + 1 - 第几行` = `num + 1 - i`

示例代码：

```python
for i in range(1, num + 1):  # 输出上半部分三角形
    print(" " * (num + 1 - i) + "* " * i)
```

输入：

```python
2
```

输出：

```python
  * 
 * *
```

（2）针对下半部分

- 每一行的`”*”数量` ⇒ `行号`（注意：行号记作`j`，计数从`num+1`开始，因为上半部分的三角形已经绘画行号至`num`，因此下一行即为`num+1`，注意`python`中的`for循环`是左必右开）
- 每一行的开头“ ”数量 ⇒ num + 1 - 第几行 = num + 1 - j

示例代码：

```python
for j in range(num + 1, 0, -1):  # 输出下半部分三角形
    print(" " * (num + 1 - j) + "* " * j)
```

输入：

```python
2
```

输出：

```python
* * * 
 * * 
  *
```

### 示例代码1

```python
def print_diamond(num):
    for i in range(1, num + 1):  # 输出上半部分三角形
        print(" " * (num + 1 - i) + "* " * i)
    for j in range(num + 1, 0, -1):  # 输出下半部分三角形
        print(" " * (num + 1 - j) + "* " * j)

size = int(input())  # 用户输入数字，即num
print_diamond(size)
```

### 解答思路2

（1）明确每一行号即为“*”的数量，该解题思路不变

（2）由于Python有丰富的字符串处理库，考虑利用内置字符串处理库将空格填充

需要提前介绍两个内置string的处理函数：

< 1 > `rstrip()` 是 Python 中的一个字符串方法，用于去除字符串末尾的字符，默认情况下去除末尾的空白字符。

该方法不会改变原字符串，而是返回一个新的字符串，可以用于删除字符串末尾指定的字符或字符串，语法：

```python
str.rstrip([chars])
```

参数 `chars` 是可选的，表示指定要删除的字符集合，如果没有指定，则默认删除空白字符，包括空格、换行符、回车符等，示例：

```python
str = "  你好  "
print(str.rstrip()) # 输出："  你好"（删除了末尾的空格）

str = "hello world!!!"
print(str.rstrip("world!")) # 输出："hello "（删除了末尾的 "world!!!"）

```

使用 `rstrip()` 可以帮助我们处理一些字符串尾部有多余空白字符或特定字符的情况，增加字符串处理的灵活性。

---

< 2 > `rjust()` 是 Python 中的一个字符串方法，用于将字符串靠右对齐，并在左侧填充指定的字符（通常是空格）来达到指定的宽度。

该方法不会改变原始字符串，而是返回一个新的字符串，语法：

```python
str.rjust(width, [fillchar])

```

参数 `width` 是必需的，表示最终字符串的宽度，包括原始字符串的长度和填充字符的数量。如果原始字符串长度大于或等于指定的宽度，则返回原始字符串。

参数 `fillchar` 是可选的，表示用于填充的字符。如果未指定，默认使用空格字符，示例：

```python
str = "Hello"
print(str.rjust(10)) # 输出："     Hello"（在左侧填充 5 个空格，总宽度为 10）

str = "Hello"
print(str.rjust(10, "-")) # 输出："-----Hello"（在左侧填充 5 个连字符，总宽度为 10）

str = "Hello"
print(str.rjust(5)) # 输出："Hello"（原始字符串长度大于指定宽度，不需要填充）

```

`rjust()` 可以在字符串格式化、输出对齐等场景中很有用，能够使字符串更整齐地显示在指定宽度的位置。

### 示例代码2

（1）上半部分三角形：明确每一行的“*”的数量，通过`rstrip()`删除字符串最右侧的空格，了解每一行的总字符串长度之后，使用`rjust()`进行空格填充

（2）下半部分三角形：除了参考上半部分三角形的构建方法外，还需要注意每一行的前置空格逐行递增的规律，因此新增一个`count`变量来表示前置空格数量

```python
def print_diamond(num):
    # 上半部分三角形（包含最长的一行）
    # “*” 数量由 1 -> num + 1（注意Python的for左闭右开）
    for i in range(1, num + 2):
        # 每一行字符串总长度（包含“*”和“ ”）：num + 行号(i)
        print(('* ' * i).rstrip().rjust(i + num))
    # 下半部分三角形
    # “*” 数量由 num 至 1
    count = 0  # 空格的数量
    # 每一行字符串总长度：2倍"*"的数量 + 空格（由1开始递增）
    for j in range(num, 0, -1):
        print(('* ' * j).rstrip().rjust(2 * j + count))
        count += 1

size = int(input())
print_diamond(size)
```

### 输入为20时的效果展示

```
                    *
                   * *
                  * * *
                 * * * *
                * * * * *
               * * * * * *
              * * * * * * *
             * * * * * * * *
            * * * * * * * * *
           * * * * * * * * * *
          * * * * * * * * * * *
         * * * * * * * * * * * *
        * * * * * * * * * * * * *
       * * * * * * * * * * * * * *
      * * * * * * * * * * * * * * *
     * * * * * * * * * * * * * * * *
    * * * * * * * * * * * * * * * * *
   * * * * * * * * * * * * * * * * * *
  * * * * * * * * * * * * * * * * * * *
 * * * * * * * * * * * * * * * * * * * *
* * * * * * * * * * * * * * * * * * * * *
 * * * * * * * * * * * * * * * * * * * *
  * * * * * * * * * * * * * * * * * * *
   * * * * * * * * * * * * * * * * * *
    * * * * * * * * * * * * * * * * *
     * * * * * * * * * * * * * * * *
      * * * * * * * * * * * * * * *
       * * * * * * * * * * * * * *
        * * * * * * * * * * * * *
         * * * * * * * * * * * *
          * * * * * * * * * * *
           * * * * * * * * * *
            * * * * * * * * *
             * * * * * * * *
              * * * * * * *
               * * * * * *
                * * * * *
                 * * * *
                  * * *
                   * *
                    *

```