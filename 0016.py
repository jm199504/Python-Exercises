# 第 0016 题： 纯文本文件 numbers.txt, 里面的内容（包括方括号）如下所示：
#
# [
# 	[1, 82, 65535],
# 	[20, 90, 13],
# 	[26, 809, 1024]
# ]
# 请将上述内容写到 numbers.xls 文件中

import xlwt

def txt2xls_3(filename, xlsname):
    try:
        f = open(filename)
        xls = xlwt.Workbook()
        sheet = xls.add_sheet('sheet1', cell_overwrite_ok=True)
        x = 0
        while True:
            line = f.readline()
            if not line:
                break
            if line != '[\n' and line!=']':
                numbers = line.split('[')[1].split(']')[0].split(',')
                for y in range(len(numbers)):
                    item = numbers[y]
                    sheet.write(x, y, item)  # (x,y)表示单元格(经度,纬度)
                x+=1
        f.close()
        xls.save(xlsname)
    except:
        raise

filename_3 = "files\\numbers.txt"
xlsname_3 = "files\\numbers.xls"
txt2xls_3(filename_3, xlsname_3)