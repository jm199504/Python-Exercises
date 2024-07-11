import xlrd
from xml.dom.minidom import Document

# 打开名为'student.xls'的Excel文件
excel_data = xlrd.open_workbook('files/student.xls')
# 获取名称为'sheet1'的工作表
table = excel_data.sheet_by_name('sheet1')

# 获取Excel表格的行数和列数
nrows = table.nrows
ncols = table.ncols

# 创建一个空字典mydict
mydict = dict()
# 遍历行
for i in range(0, nrows):
    # 将每行的第一个单元格（学生ID）转换成字符串
    idstr = str(table.cell(i, 0).value)
    # 创建一个空列表templist
    templist = list()
    # 遍历列，获取每个单元格的数据
    for j in range(1, ncols):
        data = table.cell(i, j).value
        # 将获取的数据添加到templist列表中
        templist.append(data)
    # 将该学生的信息以键值对的形式加入到mydict字典中
    mydict[idstr] = templist

# 创建一个XML文档对象doc
doc = Document()
# 创建根节点root
root = doc.createElement("root")
# 将根节点添加到XML文档中
doc.appendChild(root)
# 创建一个名为'student'的节点
student = doc.createElement("student")
# 将'student'节点添加到根节点下
root.appendChild(student)

# 创建一个注释节点notes，并添加到'student'节点下
notes = doc.createTextNode("<!--学生信息表\"id\" : [名字, 数学, 语文, 英文]-->")
student.appendChild(notes)

# 将字典mydict转换成字符串，并创建一个文本节点info，添加到'student'节点下
info = doc.createTextNode(str(mydict))
student.appendChild(info)

# 定义XML文件名
filename = "files/student.xml"

# 将XML文档写入文件中
with open(filename, "wb") as outfile:
    # 将XML文档进行美化和编码，并写入文件
    outfile.write(doc.toprettyxml(encoding="utf-8"))
