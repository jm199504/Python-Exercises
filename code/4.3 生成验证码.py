import random
import string
from PIL import Image, ImageFont, ImageDraw  # pip3 install Pillow


def get_char():
    return random.choice(string.ascii_letters)


def generator_font_color():
    return random.randint(32, 255), random.randint(32, 255), random.randint(32, 255)


def generator_bg_color():
    return random.randint(64, 355), random.randint(64, 355), random.randint(64, 355)


def img_produce():
    w = 60 * 4
    h = 60
    img = Image.new('RGB', (w, h), (255, 255, 255))  # 生成一张新图片
    font = ImageFont.truetype('001/simkai.ttf', 60)  # 第一个参数为字体文件，第二个参数为字体大小
    draw = ImageDraw.Draw(img)  # 相当于生成一个画笔
    for i in range(w):  # 画背景，每个点的颜色随机
        for j in range(h):
            draw.point((i, j), fill=generator_bg_color())
    chars = list()
    for i in range(4):  # 画四个字母，每个字母颜色随机
        char = get_char()
        chars.append(char)
        draw.text((i * 60 + 10, 10), char, font=font, fill=generator_font_color())
    result = ''.join(chars)
    img.save(f'{result}.jpg', 'jpeg')
    print(result)


if __name__ == '__main__':
    img_produce()
