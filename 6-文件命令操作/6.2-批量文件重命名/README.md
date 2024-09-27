## 6.2-批量文件重命名

### 问题描述

使用某笔记软件导出笔记到markdown格式，发现每一个md文件名不符合预期，存在一串不明字符，现需要批量修改。

### 输入示例

```
001_生成微信头像 23789sdhi3kh4roisdk.md
002_生成随机码 32E9SDJLKJDLJLEL.md
003_插入MySQL数据库 sdisdd9s3ni.md
```

### 输出示例

```
001_生成微信头像.md
002_生成随机码.md
003_插入MySQL数据库.md
```

### 示例代码

```python
import os

dir_path = 'files/notes'

notes = os.listdir(dir_path)  # 获取该目录下的所有文件
 
for note in notes:
    new_note = f"{note.split(' ')[0]}.md"  # 新文件名（保留空格前内容+文件扩展名）
    os.rename(f"{dir_path}/{note}", f"{dir_path}/{new_note}")  # 重命名
```