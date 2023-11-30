import os

dir_path = 'files/notes'  # 文件目录路径

notes = os.listdir(dir_path)  # 获取目录中的文件列表

sorted_notes = sorted(notes, key=lambda x: x.lower())  # 按文件名排序

for note in sorted_notes:
    num = note.split('_')[0]  # 提取文件名中的题号
    title = note.split('_')[-1].split('.md')[0]  # 提取文件名中的题目标题

    with open(f'{dir_path}/{note}') as file:  # 打开文件
        lines = file.readlines()  # 逐行读取文件内容

        for i in range(len(lines)):
            if lines[i].startswith("### 问题描述"):  # 查找问题描述部分
                description = lines[i + 2].strip()  # 获取问题描述内容
                print(f'### 第 {num} 题: {title}\n {description}\n')  # 打印题号、题目标题和问题描述