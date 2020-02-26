# 第 0012 题： 敏感词文本文件 filtered_words.txt，里面的内容 和 0011题一样，
# 当用户输入敏感词语，则用 星号 * 替换，例如当用户输入「北京是个好城市」，则变成「**是个好城市」。

filtered_words = open('files\\filtered_words.txt')
filtered_words_list = list()
line = filtered_words.readline()
if '\n' in line:
    line = line.split('\n')[0]
if line != '':
    filtered_words_list.append(line)

while line:
    line = filtered_words.readline()
    if '\n' in line:
        line = line.split('\n')[0]
    if line == '':
        continue
    filtered_words_list.append(line)
# print(filtered_words_list)
filtered_words.close()

import re
inputword = input('请输入：')
for i in filtered_words_list:
    if re.findall(i,inputword):
        inputword = inputword.replace(i,'*'*len(i))
print(inputword)