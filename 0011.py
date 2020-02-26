# 第 0011 题： 敏感词文本文件 filtered_words.txt，里面的内容为以下内容，
# 当用户输入敏感词语时，则打印出 Freedom，否则打印出 Human Rights。

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

inputword = input('请输入：')
if inputword in filtered_words_list:
    print('Freedom')
else:
    print('Human Rights')