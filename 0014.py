# 第 0014 题： 纯文本文件 student.txt为学生信息, 里面的内容（包括花括号）如下所示：
#
# {
# 	"1":["张三",150,120,100],
# 	"2":["李四",90,99,95],
# 	"3":["王五",60,66,68]
# }
# 请将上述内容写到 student.xls 文件

import xlwt

def txt2xls_1(filename, xlsname):
    try:
        f = open(filename)
        xls = xlwt.Workbook()
        sheet = xls.add_sheet('sheet1', cell_overwrite_ok=True)
        while True:
            line = f.readline()
            if not line:
                break
            if line != '{\n' and line!='}':
                x = int(line.split(':')[0].replace('\"','')) - 1
                items = line.replace('"','').split(':')[1].split(']')[0].split('[')[1].split(',')
                items.insert(0,x+1)
                for y in range(len(items)):
                    item = items[y]
                    sheet.write(x, y, item)  # (x,y)表示单元格(经度,纬度)
        f.close()
        xls.save(xlsname)
    except:
        raise

# filename_1 = "files\\txt2excel.txt"
# xlsname_1 = "files\\txt2excel.xls"
# txt2xls_1(filename_1, xlsname_1)

