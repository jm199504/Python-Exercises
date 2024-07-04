# 4.1 生成微信头像消息

### 问题描述

请将你的 QQ 头像（或者微博头像）右上角加上红色的数字，类似于微信未读信息数量那种提示效果。

### 效果示例展示



### 解答思路

1、获取指定字体（用于标记数字）

2、绘制右上角的红色圆形区域

3、将数字填充至红色圆形区域内（最好居中显示）

4、保存填充后的图片至本地

### 解答示例代码

```python
from PIL import Image, ImageDraw, ImageFont

def new_info_number(img_path, num_str):
    im = Image.open(img_path)  # 创建图片对象
    w, h = im.size  # 获取图片对象的宽和高

    # 创建字体对象，字体大小使用图片高度的五分之一
    font = ImageFont.truetype('fonts/simkai.ttf', int(h / 5))

    """
    在右上角绘制红色圆形区域
    pieslice中的两个元组分别为矩形的左上角坐标和右下角坐标
    左上角坐标是(w / 3 * 2, 0)，右下角坐标是(w, h / 3)，这样就确定了一个矩形区域
    在这个矩形区域中花扇形（0-360度），即一个圆形
    """
    ImageDraw.Draw(im).pieslice(((w / 3 * 2 + 10, 10), (w - 10, h / 3 - 10)), 0, 360, fill="red")
    # ImageDraw.Draw(im).pieslice(((w / 3 * 2, 0), (w, h / 3)), 0, 360, fill="red")

    # 坐标，文本绘制内容，字体对象，字体颜色
    if len(num_str) == 1:  # 个位数
        ImageDraw.Draw(im).text((w * 0.78, h * 0.05), num_str, font=font, fill="white")
    elif len(num_str) == 2:  # 两位数
        ImageDraw.Draw(im).text((w * 0.71, h * 0.04), num_str, font=font, fill="white")
    else:  # 三位数（99+）
        ImageDraw.Draw(im).text((w * 0.7, h * 0.07), '99+', font=font, fill="white")

    # 可视化
    im.show()

    # 保存图片
    im.save("images/NewInfoNumber.jpg")

new_info_number("images/wechat.jpg", '3')
```

