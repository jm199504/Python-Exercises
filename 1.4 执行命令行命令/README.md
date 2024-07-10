# 1.4 执行简单命令行命令

### 问题描述

在py文件里面执行例如`touch **.txt`的命令，希望创建10个txt文件，命令分别为`1-10.txt`

### 解答示例代码

```python
import subprocess

for i in range(1, 11):
    command = f"touch {i}.txt"
    subprocess.run(command, shell=True)

```

### 生成10个txt文件

```
1.txt
2.txt
3.txt
4.txt
5.txt
6.txt
7.txt
8.txt
9.txt
10.txt
```

