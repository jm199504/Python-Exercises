## 4.7 生成二维码

### 问题描述

希望将文本或者链接以二维码的形式保存，同时将制定图片插入二维码或者设置为背景。

### 输入示例

```text
Hello~
```

### 输出示例

### 扫码结果

![img](https://pic4.zhimg.com/80/v2-4ba06b42bbfd8db9d128d7c627d5519b_720w.webp)

### 示例代码（将自定义图片放置二维码中间）

```python
import qrcode
from PIL import Image  # 处理图像的第三方库

icon_image = 'files/040/dog.jpg'
out_image = 'files/040/inner.gif'

# 创建 QRCode 对象
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=1
)

# 设置二维码内容
qr.add_data('hello~')
qr.make(fit=True)

# 生成二维码图像
img = qr.make_image(fill_color='black', back_color='white')
img = img.convert('RGBA')

# 打开图标图片
icon = Image.open(icon_image)

# 获取二维码和图标图片的尺寸
img_w, img_h = img.size
factor = 4
size_w = int(img_w / factor)
size_h = int(img_h / factor + 10)

icon_w, icon_h = icon.size

# 调整图标图片大小
if icon_w > size_w:
    icon_w = size_w
if icon_h > size_h:
    icon_h = size_h

# 以平滑缩放的方式调整图标图片大小
icon = icon.resize((icon_w, icon_h))

# 计算图标图片在二维码上的粘贴位置
w = int((img_w - icon_w) / 2)
h = int((img_h - icon_h) / 2)

# 将图标图片粘贴到二维码图像上
img.paste(icon, (w, h))

# 保存最终生成的带有图标的二维码图像
img.save(out_image)
```

`image_qrcode_inner`参数介绍：

1.version：值为1~40的整数，控制二维码的大小（最小值是1，是个12×12的矩阵）

2.error_correction：控制二维码的错误纠正功能。可取值下列4个常量。

- ERROR_CORRECT_L：大约7%或更少的错误能被纠正。
- ERROR_CORRECT_M（默认）：大约15%或更少的错误能被纠正。
- ERROR_CORRECT_H：大约30%或更少的错误能被纠正。

3.box_size：控制二维码中每个小格子包含的像素数。

4.border：控制边框（二维码与图片边界的距离）包含的格子数（默认为4，是相关标准规定的最小值）

### 示例代码（将自定义图片作为二维码背景）

```python
import os
from MyQR import myqr

words = 'https://github.com/jm199504'
picture = 'files/040/bg.jpg'
output_name = 'files/040/outer.gif'

# 使用 MyQR 库生成带有背景图片的二维码
myqr.run(
    words,  # 二维码中的内容
    version=5,  # 二维码版本，控制二维码大小和容错率，取值范围为1到40
    level='Q',  # 二维码容错率，可选值：L, M, Q, H，依次提高容错率
    picture=picture,  # 用作背景的图片文件路径
    colorized=True,  # 是否彩色的二维码
    contrast=1.0,  # 二维码图像的对比度，取值范围为0.0到1.0，1.0表示最大对比度
    brightness=1.0,  # 二维码图像的亮度，取值范围为0.0到1.0，1.0表示最大亮度
    save_name=output_name,  # 输出的文件名
    save_dir=os.getcwd()  # 输出的文件路径，默认为当前工作目录
)
```

`image_qrcode_outer`参数介绍：

1. word：跳转URL或者自定义文字
2. version:控制边长，范围是1至40，数字越大边长越大
3. level:控制纠错水平，范围是L、M、Q、H，从左到右依次升高，即经过不同程度磨损后能否扫描到二维码完整信息程度，像小黄车的二维码经过一些磨损后还是可以扫开的原理一样
4. picture:自定义图片
5. colorized:True表示彩色，False表示黑白
6. constrast:对比度，1.0 表示原始图片，更小的值表示更低对比度，更大反之。默认为1.0
7. brightness:亮度，用法和取值与 -con 相同
8. save_name:控制文件名，即二维码名称
9. save_dir:设置输出文件路径，二维码保存目录，默认为当前工作路径。