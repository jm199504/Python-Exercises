## 4.6-制作词云

### 问题描述

将一个文本文件的重要词汇抽离生成词云。

### 输入示例

```text
我喜欢清晨的阳光，那金色的光线洒在大地上，让人感受到无尽的温暖。我喜欢夏夜的微风，轻抚着我的脸庞，给我带来片刻的凉意。我喜欢四季的变迁，春天的细雨，夏天的阳光，秋天的落叶，冬天的白雪，每一个季节都有独特的美丽。我喜欢在田野里奔跑，感受大自然的力量和活力。我喜欢探索世界的奥秘，发现未知的领域。在这个多彩多姿的世界里，我觉得自己永远都不会感到寂寞。我希望能够保护这个美丽的地球，让每一片绿叶、每一滴水、每一朵花都得到珍惜和爱护。
```

### 输出示例

![img](https://pic4.zhimg.com/80/v2-299f8995a06c3c264fc0c50bdcae51f7_720w.webp)

![img](https://pic2.zhimg.com/80/v2-000e36f6cfc36c68caa63d04a1758125_720w.webp)

### 分词工具 —— jieba

jieba 基于Python的中文分词工具

官网：[https://amueller.github.io/word_cloud](https://link.zhihu.com/?target=https%3A//amueller.github.io/word_cloud)

支持繁体分词，支持自定义词典，支持三种分词模式：

- 精确模式，试图将句子最精确地切开，适合文本分析；
- 全模式，把句子中所有的可以成词的词语都扫描出来, 速度非常快，但是不能解决歧义；
- 搜索引擎模式，在精确模式的基础上，对长词再次切分，提高召回率，适合用于搜索引擎分词。

### 示例代码

```python
import numpy
import jieba
import matplotlib.pyplot as plt
import PIL.Image as Image
from wordcloud import WordCloud, ImageColorGenerator

def chinese_jieba(text):
    wordlist_jieba = jieba.cut(text)
    text_jieba = ''.join(wordlist_jieba)
    return text_jieba

# 读取文本内容
with open('files/039.txt') as fp:
    text = fp.read()
    # 对文本进行分词
    text = chinese_jieba(text)
    # 读入遮罩图片
    mask_pic = numpy.array(Image.open('files/039.png'))
    # 定义词云对象
    wordcloud = WordCloud(font_path='files/001/simkai.ttf', background_color='white', max_font_size=120, mask=mask_pic,
                          max_words=100).generate(text)
    # 用图片颜色填充词云的颜色
    image_colors = ImageColorGenerator(mask_pic)
    wordcloud.recolor(color_func=image_colors)
    # 生成图像
    plt.imshow(wordcloud)
    plt.axis('off')
    plt.show()
```

### 利用图片自带颜色

```python
import numpy
import jieba
import matplotlib.pyplot as plt
import PIL.Image as Image
from wordcloud import WordCloud, ImageColorGenerator


def chinese_jieba(text):
    wordlist_jieba = jieba.cut(text)
    text_jieba = ''.join(wordlist_jieba)
    return text_jieba


# 读取文本内容
with open('files/039.txt') as fp:
    text = fp.read()
    # 对文本进行分词
    text = chinese_jieba(text)
    # 读入遮罩图片
    mask_pic = numpy.array(Image.open('files/039.png'))
    # 定义词云对象
    wordcloud = WordCloud(font_path='files/001/simkai.ttf', background_color='white', max_font_size=120, mask=mask_pic,
                          max_words=100).generate(text)
    # 用图片颜色填充词云的颜色
    image_colors = ImageColorGenerator(mask_pic)
    wordcloud.recolor(color_func=image_colors)
    # 生成图像
    plt.imshow(wordcloud)
    plt.axis('off')
    plt.show()
```
