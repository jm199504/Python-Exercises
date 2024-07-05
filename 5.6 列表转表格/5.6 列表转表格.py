import xlwt


def list2xls(filename, xlsname):
    f = open(filename)
    xls = xlwt.Workbook()
    sheet = xls.add_sheet('sheet1', cell_overwrite_ok=True)
    x = 0
    while True:
        line = f.readline()
        if not line:
            break
        if line != '[\n' and line != ']':
            numbers = line.split('[')[1].split(']')[0].split(',')
            for y in range(len(numbers)):
                item = numbers[y]
                sheet.write(x, y, item)  # (x,y)表示单元格(经度,纬度)
            x += 1
    f.close()
    xls.save(xlsname)


filename = "files/016.txt"
xlsname = "files/numbers.xls"
list2xls(filename, xlsname)
