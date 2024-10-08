# 5.2-表格转XML

### 问题描述

将 student.xls 文件中的内容写到 student.xml 文件中，如下所示：

```xml
<?xml version="1.0" encoding="UTF-8"?>
<root>
<students>
<!--
  学生信息表
  "id" : [名字, 数学, 语文, 英文]
-->
{
  "1" : ["张三", 150, 120, 100],
  "2" : ["李四", 90, 99, 95],
  "3" : ["王五", 60, 66, 68]
}
</students>
</root>
```

### XML介绍

XML（可扩展标记语言）是一种常用的结构化数据表示语言，用于存储和传输数据。它使用自定义的标记来描述数据的结构和内容，并且可以自由地根据需要定义新的标记。XML文件由标签、元素、属性和文本数据组成，这些元素可以按照树形结构进行层次化组织。

XML的主要特点包括：

1. 可扩展性：XML允许用户自定义标记，因此可以根据需要定义新的标记和数据结构。
2. 兼容性：XML格式与各种平台和系统都兼容，不受具体编程语言或硬件架构的限制。
3. 可读性：XML采用文本格式，易于阅读和编写。标签和结构化的元素使得数据的含义更加清晰明了。
4. 比较独立：XML文件中的数据和标记之间是独立的，可以通过解析和处理来获取和操作数据，而不需要依赖特定的应用程序。
5. 数据存储和交换：XML可以用于将结构化数据存储在文件中，并用于在不同系统之间传输和交换数据。
6. 标准化：XML是W3C（万维网联盟）的推荐标准，因此得到广泛的支持和应用。

XML文件通常由开始标签和结束标签组成，标签可以嵌套和包含属性。标签中可以包含文本数据，也可以包含子元素。下面是一个简单的XML示例：

```xml
<book>
  <title>XML Basics</title>
  <author>John Doe</author>
  <year>2023</year>
</book>
```

在这个例子中，`<book>`是根元素，它包含了三个子元素`<title>`、`<author>`和`<year>`，每个子元素都包含了文本数据。

通过解析XML文件，程序可以轻松地读取和处理文件中的数据，XML提供了一种结构化的方式来组织和表示信息。

XML在各个领域中被广泛应用，例如配置文件、数据交换和Web服务等。

### 示例代码

```python
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
```