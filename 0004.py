# 任一个英文的纯文本文件，统计其中的单词出现的个数。
import re
from collections import Counter
f = open("files/abc.txt")

letters = re.compile('[a-z]+')

words = list()
line = f.readline()

while line:
    fandp = letters.findall(line)
    words.extend(fandp)
    line = f.readline()
f.close()

print(words)
print(Counter(words))