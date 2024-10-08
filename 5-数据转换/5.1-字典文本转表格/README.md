# 5.1-文本转表格

### 问题描述

纯文本文件 student.txt为学生信息，里面的内容（包括花括号）如下所示：

```
{
  "1":["张三",150,120,100],
  "2":["李四",90,99,95],
  "3":["王五",60,66,68]
}
```

请将上述内容写到 student.xls 文件中。

### 示例代码

安装第三方库：`pip3 install xlwt`

```python
import xlwt

def txt2xls(filename, xlsname):
    # 打开文本文件
    f = open(filename)
    # 创建一个新的Excel文档对象
    xls = xlwt.Workbook()
    # 添加一个名为'sheet1'的工作表
    sheet = xls.add_sheet('sheet1', cell_overwrite_ok=True)
    # 循环读取文本文件的每一行数据
    while True:
        line = f.readline()
        # 判断是否到达文件末尾
        if not line:
            break
        # 判断该行是否为起始或结束标记，如果不是则进行数据处理
        if line != '{\n' and line != '}':
            # 提取出行号（x）和数据项（items）
            x = int(line.split(':')[0].replace('\"', '')) - 1
            items = line.replace('"', '').split(':')[1].split(']')[0].split('[')[1].split(',')
            # 在数据项列表的头部插入行号
            items.insert(0, x + 1)
            # 遍历数据项列表，并将每个数据项写入Excel工作表中的对应位置
            for y in range(len(items)):
                item = items[y]
                sheet.write(x, y, item)  # (x,y)表示单元格(经度,纬度)
    # 关闭文本文件
    f.close()
    # 将Excel文档保存为xlsname文件
    xls.save(xlsname)

file_name = "files/txt2excel.txt"
xls_name = "files/txt2excel.xls"
txt2xls(file_name, xls_name)
```

### 输出示例