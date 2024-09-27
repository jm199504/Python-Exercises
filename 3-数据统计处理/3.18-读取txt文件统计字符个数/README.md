## 3.18-读取txt文件统计字符个数

### 问题描述
为了读取txt文件并统计字符个数，同时设计测试用例，你可以编写一个Python脚本，其中包含统计字符个数的函数以及相应的测试函数。这里使用unittest模块来进行测试。

### 实验示例
```
test_count_chars_in_empty_file：测试空文件的字符数是否为0。
test_count_chars_in_non_empty_file：测试非空文件的字符数是否正确。
test_count_chars_with_special_characters：测试包含特殊字符的文件的字符数是否正确。
```

### 示例代码

```python
def count_chars_in_file(filename):
    with open(filename, 'r', encoding='utf-8', errors='ignore') as file:
        content = file.read()
        return len(content)
```



