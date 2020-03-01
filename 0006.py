# 你有一个目录，放了你一个月的日记，都是 txt，为了避免分词的问题，假设内容都是英文，请统计出你认为每篇日记最重要的词。
import re
import os
from collections import Counter

letters = re.compile('[a-z]+')

def getCommonWord(filepath):
    f = open(filepath)
    words = list()
    line = f.readline()
    while line:
        fandp = letters.findall(line)
        words.extend(fandp)
        line = f.readline()
    f.close()
    print(dict(Counter(words)))
    return max(dict(Counter(words)), key=dict(Counter(words)).get)

files = os.listdir('0006')
commonwords = dict()
for file in files:
    commonwords[file] = getCommonWord("0006\\"+file)

print(commonwords)
