# 第 0019 题： 将 第 0016 题中的 numbers.xls 文件中的内容写到 numbers.xml 文件中，如下
#
# 所示：
#
# <?xml version="1.0" encoding="UTF-8"?>
# <root>
# <numbers>
# <!--
# 	数字信息
# -->
#
# [
# 	[1, 82, 65535],
# 	[20, 90, 13],
# 	[26, 809, 1024]
# ]
#
# </numbers>
# </root>

import xlrd

exceldata = xlrd.open_workbook('files\\numbers.xls')

table = exceldata.sheet_by_name('sheet1')   #通过表名获取

nrows = table.nrows  #行数
ncols = table.ncols  #列数

mylist = list()
for i in range(0, nrows):
    templist = list()
    for j in range(0, ncols):
        templist.append(int(table.cell(i, j).value))
    mylist.append(templist)

from xml.dom.minidom import Document

doc = Document()
root = doc.createElement("root")
doc.appendChild(root)
student = doc.createElement("numbers")
root.appendChild(student)

notes = doc.createTextNode("<!--数字信息-->")
student.appendChild(notes)
info = doc.createTextNode(str(mylist))
student.appendChild(info)
filename = "files\\numbers.xml"

with open(filename, "wb") as outfile:
    outfile.write(doc.toprettyxml(encoding="utf-8"))