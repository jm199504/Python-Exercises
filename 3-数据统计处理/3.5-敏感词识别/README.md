# 3.5-敏感词识别

### 问题描述

敏感词文本文件 filtered_words.txt，里面的内容为以下内容，当用户输入敏感词语时，则打印出 Freedom，否则打印出 Human Rights。

### 敏感词示例清单

```
北京
程序员
公务员
领导
牛比
love
sex
```

### 示例代码

```python
def check_word_in_file(file_path):
    filtered_words_list = []
    with open(file_path) as filtered_words:
        for line in filtered_words:
            line = line.strip()
            if line != '':
                filtered_words_list.append(line)

    input_word = input('请输入：')
    if input_word in filtered_words_list:
        print('Freedom')
    else:
        print('Human Rights')

# 调用函数并传入文件路径
check_word_in_file('files/filtered_words.txt')
```

### 测试预览

```python
请输入：北京
Freedom

请输入：123
Human Rights
```