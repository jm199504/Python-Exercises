import os
import re


def count_lines(file_path):
    """
    统计 Python 文件的行数、空行数和注释行数。

    :param file_path:   文件路径
    :return:            文件总行数、空行数和注释行数
    """
    total_empty_lines = 0
    total_comment_lines = 0

    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

        # 统计空行和注释行
        for line in lines:
            line = line.strip()
            if line == "":
                total_empty_lines += 1
            elif re.match(r"^\s*#", line):
                total_comment_lines += 1

    return len(lines), total_empty_lines, total_comment_lines


directory = "your_directory_path"  # 替换为你的目录路径
files = [file for file in os.listdir(directory) if file.endswith(".py")]

for file in files:
    file_path = os.path.join(directory, file)
    lines, empty_lines, comment_lines = count_lines(file_path)

    print("文件: ", file)
    print("总行数: ", lines)
    print("空行数: ", empty_lines)
    print("注释行数: ", comment_lines)
    print()
