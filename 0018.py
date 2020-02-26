# 第 0018 题： 将 第 0015 题中的 city.xls 文件中的内容写到 city.xml 文件中，如下 所示：
#
#     <?xmlversion="1.0" encoding="UTF-8"?>
#     <root>
#     <cities>
#     <!--
#     	城市信息
#     -->
#     {
#     	"1" : "上海",
#     	"2" : "北京",
#     	"3" : "成都"
#     }
#     </cities>
#     </root>

import xlrd

exceldata = xlrd.open_workbook('files\\city.xls')

table = exceldata.sheet_by_name('sheet1')   #通过表名获取

nrows = table.nrows  #行数
ncols = table.ncols  #列数

mydict = dict()
for i in range(0, nrows):
    idstr = str(int(table.cell(i, 0).value))
    city = str(table.cell(i, 1).value)

    mydict[idstr] = city

from xml.dom.minidom import Document

doc = Document()
root = doc.createElement("root")
doc.appendChild(root)
student = doc.createElement("cities")
root.appendChild(student)

notes = doc.createTextNode("<!--城市信息-->")
student.appendChild(notes)
info = doc.createTextNode(str(mydict))
student.appendChild(info)
filename = "files\\city.xml"

with open(filename, "wb") as outfile:
    outfile.write(doc.toprettyxml(encoding="utf-8"))