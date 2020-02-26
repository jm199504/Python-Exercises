# 第 0010 题： 使用 Python 生成类似于下图中的字母验证码图片

# 第 0010 题：使用 Python 生成类似于下图中的字母验证码图片
#
# 字母验证码
import random
import string
from PIL import Image,ImageFont,ImageDraw,ImageFilter       #pip3 install Pillow

def get_char():
    return random.choice(string.ascii_letters)

def generator_font_color():
    return (random.randint(32, 255), random.randint(32, 255), random.randint(32, 255))

def generator_bgcolor():
    return (random.randint(64, 355), random.randint(64, 355), random.randint(64, 355))

def imag_produce():
    w = 60*4
    h = 60
    img = Image.new('RGB',(w,h),(255,255,255))      # 生成一张新图片
    font = ImageFont.truetype('fonts\\simkai.ttf',60)   # 第一个参数为字体文件，第二个参数为字体大小
    draw = ImageDraw.Draw(img)   # 相当于生成一个画笔
    for i in range(w):   # 画背景，每个点的颜色随机
        for j in range(h):
            draw.point((i,j),fill=generator_bgcolor())
    chars = list()
    for i in range(4):  # 画四个字母，每个字母颜色随机
        char = get_char()
        chars.append(char)
        draw.text((i*60+10,10),char,font=font,fill=generator_font_color())
    img.save('files\\0010.jpg','jpeg')
    print(''.join(chars))

if __name__ == '__main__':
    imag_produce()
