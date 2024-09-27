## 4.9-生成手写文本

### 问题描述
将文本转为手写体的图片

### 示例代码
```python
# coding: utf-8
from PIL import Image, ImageFont

from handright import Template, handwrite

text = """
就是可以设置一些风格，让写出来的文字更像真人写的
"""

template = Template(
    background=Image.new(mode="1", size=(900, 1000), color=1),
    font=ImageFont.truetype("demo_handright/pen.ttf", size=100),
    line_spacing=150,
    fill=0,  # 字体“颜色”
    left_margin=100,
    top_margin=100,
    right_margin=100,
    bottom_margin=100,
    word_spacing=15,
    line_spacing_sigma=1,  # 行间距随机扰动
    font_size_sigma=1,  # 字体大小随机扰动
    word_spacing_sigma=3,  # 字间距随机扰动
    start_chars="“（[<",  # 特定字符提前换行，防止出现在行尾
    end_chars="，。",  # 防止特定字符因排版算法的自动换行而出现在行首
    perturb_x_sigma=1,  # 笔画横向偏移随机扰动
    perturb_y_sigma=1,  # 笔画纵向偏移随机扰动
    perturb_theta_sigma=0.05,  # 笔画旋转偏移随机扰动
)
images = handwrite(text, template)
for i, im in enumerate(images):
    assert isinstance(im, Image.Image)
    im.show()
    # im.save("path/to/my/output/{}.webp".format(i))

```

