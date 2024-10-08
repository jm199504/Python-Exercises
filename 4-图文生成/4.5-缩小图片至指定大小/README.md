# 4.5-缩小图片至指定大小

### 问题描述

你有一个照片目录，把它们的尺寸变成都不大于 iPhone5 分辨率的大小（iPhone5 分辨率：1136×640像素）

### 解答思路

- 首先定义 iPhone5 的分辨率为常量 `IPHONE5_WIDTH` 和 `IPHONE5_HEIGHT`。
- 然后定义了两个函数：`reset_pic_size` 和 `find_and_resize_pic_from_dir`。
- `reset_pic_size` 函数接收原图片路径、新图片路径、以及目标图片的宽度和高度，使用 `PIL` 库打开原图片，计算出调整尺寸之后的图片大小，并使用 `resize` 方法将原图片的大小调整为目标尺寸，最后保存为新的图片文件。
- `find_and_resize_pic_from_dir` 函数接收一个目录路径，然后遍历该目录下所有的文件，如果文件的扩展名是 `.jpg` 或 `.png`，则使用 `reset_pic_size` 函数将该文件的尺寸调整为不大于 iPhone5 分辨率的大小，并保存为新的文件，文件名前面加上 “iPhone5_” 前缀。

### 示例代码

```bash
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
```

### 原始图片



### 缩放后的图片

