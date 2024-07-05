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
