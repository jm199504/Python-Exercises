import re   # 导入正则表达式模块
import os   # 导入操作系统模块
from collections import Counter  # 导入计数器模块

letters = re.compile('[a-zA-Z]+')   # 定义正则表达式模式，只匹配字母


def get_common_word(file_path):
    """
    获取文件中出现次数最多的单词
    :param file_path: 文件路径
    :return: 出现次数最多的单词
    """
    f = open(file_path)   # 打开文件
    words = list()   # 存储所有单词的列表
    line = f.readline()   # 逐行读取文件内容
    while line:   # 只要还有内容可读
        found_words = letters.findall(line)   # 使用正则表达式模式查找所有单词
        words.extend(found_words)   # 添加到单词列表中
        line = f.readline()   # 继续读取下一行
    f.close()   # 关闭文件
    # 使用计数器对单词出现次数进行统计，并返回出现次数最多的单词
    return max(dict(Counter(words)), key=dict(Counter(words)).get)


files = os.listdir('007')   # 获取目录下所有文件名
common_words = dict()   # 存储每个文件中出现次数最多的单词的字典
for file in files:
    common_words[file] = get_common_word("007/" + file)   # 获取每个文件中出现次数最多的单词，并添加到字典中

print(common_words)   # 输出所有文件中出现次数最多的单词字典到控制台
