## 5.10-字典转PDF

### 问题描述

有一份python的字典（dict）对象，需要转为PDF格式。

### 输入示例

```python
report_data = [{
    "Package": "com.baidu.ernie.car",
    "测试区间": "2023-06-08 22:00 - 2023-06-09 10:00",
    "测试时长": "X 小时 Y 分钟",
    "Crash数量": 0,
    "ANR数量": 0,
    "Bug单链接": "-",
    "测试结论": "PASS"
},
    {
        "Package": "com.baidu.ernie.car",
        "测试区间": "2023-06-08 22:00 - 2023-06-09 10:00",
        "测试时长": "X 小时 Y 分钟",
        "Crash数量": 0,
        "ANR数量": 0,
        "Bug单链接": "-",
        "测试结论": "PASS"
    }
]

```

### 示例代码

```python
from datetime import datetime

from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle, Spacer
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont


def generate_monkey_test_report(report_data, output_file):
    # 注册中文字体
    pdfmetrics.registerFont(TTFont('MiSans-Thin', 'MiSans-Thin.ttf'))

    # 创建PDF文档
    doc = SimpleDocTemplate(output_file, pagesize=letter)

    # 定义样式
    styles = getSampleStyleSheet()
    title_style = ParagraphStyle('Title', parent=styles['Title'], fontName='MiSans-Thin')
    body_style = ParagraphStyle('BodyText', parent=styles['BodyText'], fontName='MiSans-Thin')
    table_style = TableStyle([
        ('ALIGN', (0, 0), (-1, 0), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'MiSans-Thin'),
        ('FONTSIZE', (0, 0), (-1, 0), 14),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ])

    # 定义报告内容
    report_elements = []

    # 报告标题
    title = Paragraph(f"Monkey 测试报告({datetime.now().strftime('%Y-%m-%d')})", title_style)
    report_elements.append(title)

    # 引导语
    intro = Paragraph("", body_style)
    report_elements.append(intro)
    report_elements.append(Paragraph("", body_style))

    # 指标表格
    if isinstance(report_data, dict):
        data = [[key, str(value)] for key, value in report_data.items()]
        table_data = [[Paragraph(cell, body_style) for cell in row] for row in data]
        table = Table(table_data, style=table_style)
        report_elements.append(table)
    if isinstance(report_data, list):
        for data in report_data:
            data = [[key, str(value)] for key, value in data.items()]
            table_data = [[Paragraph(cell, body_style) for cell in row] for row in data]
            table = Table(table_data, style=table_style)
            report_elements.append(table)
            report_elements.append(Spacer(1, 20))  # 设置表格之间的间距（20像素）

    # 生成报告
    doc.build(report_elements)

# 测试数据
report_data = [{
    "Package": "com.baidu.ernie.car",
    "测试区间": "2023-06-08 22:00 - 2023-06-09 10:00",
    "测试时长": "X 小时 Y 分钟",
    "Crash数量": 0,
    "ANR数量": 0,
    "Bug单链接": "-",
    "测试结论": "PASS"
},
    {
        "Package": "com.baidu.ernie.car",
        "测试区间": "2023-06-08 22:00 - 2023-06-09 10:00",
        "测试时长": "X 小时 Y 分钟",
        "Crash数量": 0,
        "ANR数量": 0,
        "Bug单链接": "-",
        "测试结论": "PASS"
    }
]

# 生成报告
generate_monkey_test_report(report_data, "monkey_test_report.pdf")

```

