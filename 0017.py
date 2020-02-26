# 第 0017 题： 将 第 0014 题中的 student.xls 文件中的内容写到 student.xml 文件中，如
#
# 下所示：
#
# <?xml version="1.0" encoding="UTF-8"?>
# <root>
# <students>
# <!--
# 	学生信息表
# 	"id" : [名字, 数学, 语文, 英文]
# -->
# {
# 	"1" : ["张三", 150, 120, 100],
# 	"2" : ["李四", 90, 99, 95],
# 	"3" : ["王五", 60, 66, 68]
# }
# </students>
# </root>
import xlrd

exceldata = xlrd.open_workbook('files\\student.xls')

table = exceldata.sheet_by_name('sheet1')   #通过表名获取

nrows = table.nrows  #行数
ncols = table.ncols  #列数

mydict = dict()
for i in range(0, nrows):
    idstr = str(table.cell(i, 0).value)
    templist = list()
    for j in range(1, ncols):
        data = table.cell(i, j).value
        templist.append(data)
    mydict[idstr] = templist

from xml.dom.minidom import Document

doc = Document()
root = doc.createElement("root")
doc.appendChild(root)
student = doc.createElement("student")
root.appendChild(student)

notes = doc.createTextNode("<!--学生信息表\"id\" : [名字, 数学, 语文, 英文]-->")
student.appendChild(notes)
info = doc.createTextNode(str(mydict))
student.appendChild(info)
filename = "files\\student.xml"

with open(filename, "wb") as outfile:
    outfile.write(doc.toprettyxml(encoding="utf-8"))

# 其他相关方法

# table = exceldata.sheets()[0]            #通过索引获取
# table = exceldata.sheet_by_index(0)      #通过索引获取
# data = table.cell(1,1).value #得到表格数据