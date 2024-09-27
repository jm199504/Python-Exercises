## 1.27-蛇形座位表

### 问题描述
现在有一个会场需要您进行座位排序，你希望ID临近的参会人员挨着坐，所以你想到了蛇形座位表，提供你一份ID列表，比如：[1,2,3,4,5,6,7...,87]，每一排是10位，请生成一份二维数组，并且存储到excel表。

### 输入示例

```
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87]
```

### 输出示例

```
[[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32]
[64, 63, 62, 61, 60, 59, 58, 57, 56, 55, 54, 53, 52, 51, 50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33]
[65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87]]
```

* 提醒：奇偶数排数需要考虑最后一排是靠右还是靠左排序

### 示例代码

```python
import pandas as pd

def generate_snake_seating(ids, seats_per_row=10):
    """
    生成蛇形座位表的二维数组。

    参数:
    ids: List[int] - ID列表
    seats_per_row: int - 每一排的座位数

    返回:
    List[List[int]] - 蛇形座位表的二维数组
    """
    seating = []
    for i in range(0, len(ids), seats_per_row):
        row = ids[i:i + seats_per_row]  # 获取当前排的ID
        # 根据排数是奇数还是偶数决定是否翻转行
        if (len(seating) % 2) == 1:  # 偶数排（0、2、...）时翻转
            row.reverse()
        seating.append(row)
    return seating

def save_to_excel(seating, filename):
    """
    将座位表保存到Excel文件。

    参数:
    seating: List[List[int]] - 蛇形座位表的二维数组
    filename: str - 输出的Excel文件名
    """
    # 使用 pandas 将数据转换为 DataFrame
    df = pd.DataFrame(seating)
    # 将 DataFrame 保存为 Excel 文件
    df.to_excel(filename, index=False, header=False)

# 主函数
if __name__ == "__main__":
    ids = [i for i in range(1, 88)]  # 生成 ID 列表
    seating = generate_snake_seating(ids)  # 生成蛇形座位表
    print(seating)  # 打印蛇形座位表
    save_to_excel(seating, 'snake_seating.xlsx')  # 保存为 Excel 文件

```

