from openpyxl import Workbook

# ID列表
ids = list(range(1,88))


def generate_snake_seating(_ids, people_per_row):
    rows = len(_ids) // people_per_row

    _seating = []

    for _sort, row in enumerate(range(rows + 1)):  # _sort: 座位顺序，奇数排：由左往右升序，偶数排：由左往右降序
        single_row = _ids[row * people_per_row: (row + 1) * people_per_row]
        if _sort % 2:
            _seating.append(single_row[::-1])
        else:
            _seating.append(single_row)

    # 将最后一排若为偶数靠右
    if not (rows + 1) % 2:
        for _ in range(people_per_row - len(ids) % people_per_row):
            _seating[-1].insert(0, '-')

    return _seating


# 排序
seating = generate_snake_seating(ids, people_per_row=32)

# 创建一个新的 Workbook
wb = Workbook()
sheet = wb.active

# 将数据写入到工作表中
for row_idx, row_data in enumerate(seating, start=1):
    for col_idx, cell_value in enumerate(row_data, start=1):
        sheet.cell(row=row_idx, column=col_idx, value=cell_value)

# 保存工作簿
wb.save('output.xlsx')
