# 1.3 根据文件标题和内容生成目录

### 问题描述

将一个文件夹内的md5文件中的标题和指定内容转为目录。

### 输入示例

```text
/
  - 001_生成微信头像.md
  - 002_生成随机码.md
```

`001_生成微信头像.md`文件内容

```text
# 001_生成微信头像消息

### 问题描述

请将你的 QQ 头像（或者微博头像）右上角加上红色的数字，类似于微信未读信息数量那种提示效果。

### 效果示例展示
...
```

### 输出示例

```text
### 第 001 题: 生成微信头像消息
请将你的 QQ 头像（或者微博头像）右上角加上红色的数字，类似于微信未读信息数量那种提示效果。

### 第 002 题: 生成随机码
...
```

### 解答示例代码

```python
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
```

### 代码运行截图