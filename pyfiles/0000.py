from PIL import Image, ImageDraw, ImageFont

def newInfoNumber(imgpath,numstr):
    im = Image.open(imgpath)  # 创建图片对象
    w,h = im.size  # 获取图片对象的宽和高

    # 创建字体对象
    if len(numstr)<=2:
        font = ImageFont.truetype('fonts\\simkai.ttf', int(h/4))
    else:
        font = ImageFont.truetype('fonts\\simkai.ttf', int(h / 5))
    # 绘制圆形(宽高为原图1/3的右上角区域)
    ImageDraw.Draw(im).pieslice([(w/3*2, 0), (w, h/3)], 0, 360, fill="red")

    # 坐标，文本绘制内容，字体对象，字体颜色
    if len(numstr)==1:
        ImageDraw.Draw(im).text((w * 0.78, h * 0.05), numstr, font=font, fill="white")
    elif len(numstr) ==2:
        ImageDraw.Draw(im).text((w * 0.71, h * 0.04), numstr, font=font, fill="white")
    else:
        numstr = '99+'
        ImageDraw.Draw(im).text((w * 0.7, h * 0.07), numstr, font=font, fill="white")
    # 可视化
    im.show()

    # 保存图片
    im.save("images\\NewInfoNumber.jpg")

newInfoNumber("images\\wechat.jpg",'1')