# 你有一个目录，装了很多照片，把它们的尺寸变成都不大于 iPhone5 分辨率的大小。
# iPhone5 分辨率：1136×640像素

import os
from PIL import Image

IPHONE5_WIDTH = 1136
IPHONE5_HEIGHT = 640

# 改变图片的尺寸大小
def reset_pic_size(file_path, new_path, width=IPHONE5_WIDTH, height=IPHONE5_HEIGHT):
    image = Image.open(file_path)
    image_width, image_height = image.size

    if image_width > width:
        image_height = width * image_height // image_width
        image_width = width
    if image_height > height:
        image_width = height * image_width // image_height
        image_height = height

    # ANTIALIAS：平滑滤波。对所有可以影响输出像素的输入像素进行高质量的重采样滤波，以计算输出像素值。
    new_image = image.resize((image_width, image_height), Image.ANTIALIAS)
    new_image.save(new_path)


# 从文件夹中循环改变每一张图片
def find_and_resize_pic_from_dir(dir_path):
    for file_name in os.listdir(dir_path):
        if file_name.lower().endswith('jpg') or file_name.lower().endswith('png'):
            file_new_path = 'images\\iPhone5_' + file_name
            reset_pic_size(file_path=dir_path+'\\'+file_name, new_path=file_new_path)


find_and_resize_pic_from_dir('images')
