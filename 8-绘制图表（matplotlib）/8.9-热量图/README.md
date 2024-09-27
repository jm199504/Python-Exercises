## 8.9-热量图

### 问题描述

（1）生成数据集

（2）绘制热量图

### 示例输出

<img src="https://github.com/jm199504/Python-Exercises/blob/master/8-%E7%BB%98%E5%88%B6%E5%9B%BE%E8%A1%A8%EF%BC%88matplotlib%EF%BC%89/8.9-%E7%83%AD%E9%87%8F%E5%9B%BE/Figure_1.jpg?raw=true" style="zoom:80%;" />

### 示例代码

```python
import matplotlib.pyplot as plt
import matplotlib.image as mpimg  # mpimg 用于读取图片

# 图片处理的matplotlib方法
# interpolation插值运算,cmap表示绘图时的样式
# interpolation：
# 'nearest'（默认值）:最近邻插值
# 'bilinear':双线性插值
# 'bicubic':双三次插值
# cmap=‘hot’热量图；gray灰度图
pic = mpimg.imread('shenzhen.jpg')
# 控制画布大小
plt.figure(num=1, figsize=(9, 5), )
# 仅显示图片第一个通道
pic = pic[:, :, 0]
plt.imshow(pic, interpolation='nearest', cmap='hot')
# 压缩90%，即控制力度图例大小
plt.colorbar(shrink=0.9)
# 关闭坐标轴刻度
plt.xticks(())
plt.yticks(())
# 显示图片
plt.show()

```