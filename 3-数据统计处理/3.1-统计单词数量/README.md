# 3.1-统计单词数量

### 问题描述

任一个英文的纯文本文件，统计其中的单词出现的个数

### 解答思路

使用正则的方式统计`[a-zA-Z]+`

### 示例文件（`abc.txt`）

```bash
Hello, this is a sample text file. It was created for testing purposes. 
You can use this file to count the occurrences of each word. 
Have a nice day!
```

### 示例代码

```bash
import re
from collections import Counter

# 打开文件
f = open("files/abc.txt")

# 匹配大小写字母的正则表达式
letters = re.compile('[a-zA-Z]+')

# 初始化存储单词的列表
words = list()

# 逐行读取文件内容
line = f.readline()
while line:
    # 使用正则表达式找到每行中的单词
    found_words = letters.findall(line)

    # 将找到的单词添加到存储单词的列表中
    words.extend(found_words)

    # 读取下一行
    line = f.readline()

# 关闭文件
f.close()

# 使用 Counter 对单词进行计数
word_count = Counter(words)

# 输出每个单词及其出现次数
print(word_count)
```

### 结果输出

```bash
Counter({'this': 2, 'a': 2, 'file': 2, 'Hello': 1, 'is': 1, 'sample': 1, 'text': 1, 'It': 1, 'was': 1, 'created': 1, 'for': 1, 'testing': 1, 'purposes': 1, 'You': 1, 'can': 1, 'use': 1, 'to': 1, 'count': 1, 'the': 1, 'occurrences': 1, 'of': 1, 'each': 1, 'word': 1, 'Have': 1, 'nice': 1, 'day': 1})
```

