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
