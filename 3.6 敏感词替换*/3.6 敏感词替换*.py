import re


def replace_word_in_file(input_word, file_path):
    filtered_words = open(file_path)
    filtered_words_list = list()

    # 读取过滤词文件的每一行
    line = filtered_words.readline()

    # 处理第一行，去除行末的换行符
    if '\n' in line:
        line = line.split('\n')[0]

    # 如果第一行不为空，则将其添加到过滤词列表中
    if line != '':
        filtered_words_list.append(line)

    # 继续读取后续行，处理换行符及空行，并将非空行添加到过滤词列表中
    while line:
        line = filtered_words.readline()

        # 处理行末的换行符
        if '\n' in line:
            line = line.split('\n')[0]

        # 如果行为空，则跳过当前循环
        if line == '':
            continue

        # 将非空行添加到过滤词列表中
        filtered_words_list.append(line)

    # 遍历过滤词列表，使用正则表达式查找输入词中的匹配项，并替换为相应数量的星号
    for i in filtered_words_list:
        if re.findall(i, input_word):
            input_word = input_word.replace(i, '*' * len(i))

    filtered_words.close()

    print(input_word)


replace_word_in_file(input('请输入：'), 'files/013.txt')
