# 1.2-蜗牛多久能爬上去

### 问题描述

有一棵光滑的葡萄树高 18 分米，一只蜗牛从底部向上攀，每分钟爬 3 分米，但每爬一分钟后都要休息一分钟，休息期间又要滑下 1 分米。请问最快在第几分钟，蜗牛可以爬到树顶端。

### 解答思路

（1）明确目标为18分米；

（2）每分钟可以爬升3米，随后一分钟会滑落1米；

（3）一旦爬升高度抵达18米，即停止计时

### 示例代码

```python
height = 18  # 树的高度，单位：米
climb = 3  # 每分钟爬升的距离，单位：米
slide = 1  # 每次休息滑落的距离，单位：米

# 初始分钟数、已爬升距离和当前高度
minutes = 0
current_height = 0

while current_height < height:
    minutes += 1  # 每增加一分钟
    current_height += climb  # 上升3分米
    print(f'{minutes}分钟:{current_height}')  # 打印看看目前爬了多高
    if current_height >= height:  # 判断一下是否已经抵达18分米
        break

    minutes += 1  # 每增加一分钟
    current_height = current_height - slide  # 滑落1分米

    print(f'{minutes}分钟:{current_height}')  # 打印看看目前爬了多高

print("蜗牛需要在第", minutes, "分钟爬到树顶。")
```

-