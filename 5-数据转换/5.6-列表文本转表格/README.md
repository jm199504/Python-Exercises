# 5.6-列表转表格

### 文本描述

纯文本文件 numbers.txt, 里面的内容（包括方括号）如下所示：

```
[
  [1, 82, 65535],
  [20, 90, 13],
  [26, 809, 1024]
]
```

请将上述内容写到 numbers.xls 文件中。

### 示例代码

```python
import xlwt

def list2xls(filename, xlsname):
    # 打开文本文件
    f = open(filename)
    # 创建一个新的Excel文档对象
    xls = xlwt.Workbook()
    # 添加一个名为'sheet1'的工作表
    sheet = xls.add_sheet('sheet1', cell_overwrite_ok=True)
    # 初始化行号为0
    x = 0
    # 循环读取文本文件的每一行数据
    while True:
        line = f.readline()
        # 判断是否到达文件末尾
        if not line:
            break
        # 判断该行是否为起始或结束标记，如果不是则进行数据处理
        if line != '[\n' and line != ']':
            # 提取出行的数字列表
            numbers = line.split('[')[1].split(']')[0].split(',')
            # 遍历数字列表，并将每个数字写入Excel工作表中的对应位置
            for y in range(len(numbers)):
                item = numbers[y]
                sheet.write(x, y, item)  # (x,y)表示单元格(经度,纬度)
            # 行号加1
            x += 1
    # 关闭文本文件
    f.close()
    # 将Excel文档保存为xlsname文件
    xls.save(xlsname)

# 定义文本文件名和Excel文件名
file_name = "files/numbers.txt"
xls_name = "files/numbers.xls"
# 将文本文件转换为Excel文件
list2xls(file_name, xls_name)
```

### 预览效果