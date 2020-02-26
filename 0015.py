# 第 0015 题： 纯文本文件 city.txt为城市信息, 里面的内容（包括花括号）如下所示：
#
# {
#     "1" : "上海",
#     "2" : "北京",
#     "3" : "成都"
# }
# 请将上述内容写到 city.xls 文件中

import xlwt

def txt2xls_2(filename, xlsname):
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
                city = line.replace('"','').split(':')[1]
                if ',' in city:
                    city = city.replace(',','')
                items = [x+1,city]
                for y in range(len(items)):
                    item = items[y]
                    sheet.write(x, y, item)  # (x,y)表示单元格(经度,纬度)
        f.close()
        xls.save(xlsname)
    except:
        raise

filename_2 = "files\\city.txt"
xlsname_2 = "files\\city.xls"
txt2xls_2(filename_2, xlsname_2)