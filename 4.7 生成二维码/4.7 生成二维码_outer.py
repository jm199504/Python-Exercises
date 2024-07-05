import os
from MyQR import myqr

words = 'https://github.com/jm199504'
picture = 'files/040/bg-old.jpg'
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