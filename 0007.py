# 第 0007 题： 有个目录，里面是你自己写过的程序，统计一下你写过多少行代码。包括空行和注释，但是要分别列出来。

# import os
#
# files = os.listdir('pyfiles')
#
# for file in files:
#     f = open('pyfiles\\'+file,encoding='utf_8', errors='ignore')
#     line = f.readline()
#     while line:
#         line = f.readline()
#         print(line)


import os, re

file_path = 'pyfiles'

def analyzeCode(codefilesource):
    total_line = 0
    comment_line = 0
    blank_line = 0
    with open(codefilesource,encoding='utf_8', errors='ignore') as f:
        lines = f.readlines()
        total_line = len(lines)
        line_index = 0
        # 遍历每一行
        while line_index < total_line:
            line = lines[line_index]
            # 检查是否为注释
            if line.startswith("#"):# 单行注释
                comment_line += 1
            elif re.match("\s*'''", line) is not None:# 多行注释开头
                #\s	匹配任意空白字符，等价于 [\t\n\r\f].
                # * 匹配0个或多个的表达式
                comment_line += 1
                while re.match(".*'''$", line) is None:# 多行注释结尾
                    line = lines[line_index]
                    comment_line += 1
                    line_index += 1
            # 检查是否为空行
            elif line == "\n":
                blank_line += 1
            line_index += 1
    print ("在%s中：" % codefilesource)
    print ("代码行数：", total_line)
    print ("注释行数：", comment_line, "占%0.2f%%" % (comment_line*100.0/total_line))
    print ("空行数：  ", blank_line, "占%0.2f%%" % (blank_line*100.0/total_line))
    return [total_line, comment_line, blank_line]

def runMain(file_path):
    # 切换到code所在目录
    os.chdir(file_path)
    # 遍历该目录下的py文件
    total_lines = 0
    total_comment_lines = 0
    total_blank_lines = 0
    for i in os.listdir(os.getcwd()):
        if os.path.splitext(i)[1] == '.py':
            line = analyzeCode(i)
            total_lines, total_comment_lines, total_blank_lines = total_lines + line[0], total_comment_lines + line[1], total_blank_lines + line[2]
    print ("总代码行数：", total_lines)
    print ("总注释行数：", total_comment_lines, "占%0.2f%%" % (total_comment_lines*100.0/total_lines))
    print ("总空行数：  ", total_blank_lines, "占%0.2f%%" % (total_blank_lines*100.0/total_lines))

if __name__ == '__main__':
    runMain(file_path)
