height = 18  # 树的高度，单位：米
climb = 3  # 每分钟爬升的距离，单位：米
slide = 1  # 每次休息滑落的距离，单位：米

# 初始分钟数、已爬升距离和当前高度
minutes = 0
current_height = 0

while current_height < height:
    minutes += 1
    current_height += climb
    print(f'{minutes}分钟:{current_height}')
    if current_height >= height:
        break

    minutes += 1
    current_height = current_height - slide

    print(f'{minutes}分钟:{current_height}')

print("蜗牛需要在第", minutes, "分钟爬到树顶。")
