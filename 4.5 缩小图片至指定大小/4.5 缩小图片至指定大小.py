import os
from PIL import Image


def reset_pic_size(file_path, new_path):
    # 打开图像并转换为RGB模式
    image = Image.open(file_path).convert('RGB')

    # 重设图像大小
    new_size = (1136, 640)
    resized_image = image.resize(new_size)

    # 保存为JPEG格式
    resized_image.save(new_path, 'JPEG')


def find_and_resize_pic_from_dir(dir_path):
    # 遍历目录中的文件
    for file_name in os.listdir(dir_path):
        if file_name.endswith(('.png', '.jpg', '.jpeg')):
            # 构建新的文件路径
            file_new_path = os.path.join('resized_images', file_name)

            # 重设图像大小并保存
            reset_pic_size(file_path=os.path.join(dir_path, file_name), new_path=file_new_path)


# 图像目录路径
input_dir = 'images'

# 创建输出目录
output_dir = 'resized_images'
os.makedirs(output_dir, exist_ok=True)

# 执行图像处理
find_and_resize_pic_from_dir(input_dir)
