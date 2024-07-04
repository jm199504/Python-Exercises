## 5.5 unix时间戳转字符串

## 问题描述

目前有很多在线Unix时间戳(timestamp)转换工具，如何用Python实现这一功能

### 输入示例

```text
1702348831
```

### 输出示例

```text
2023-12-12 10:40:31
```

### Python示例代码

```python
import time

# unix时间戳转为字符串
def timestamp_2_str(time_stamp):
    struct_time = time.localtime(time_stamp)
    str_time = time.strftime('%Y-%m-%d %H:%M:%S', struct_time)
    print(str_time)
    return str_time

timestamp_2_str(758435343)
timestamp_2_str(1702348831)

"""
1994-01-13 12:29:03
2023-12-12 10:40:31
"""
```



### 字符串转unix时间戳

```python
import time
dt = "2016-05-05 20:28:54"
#转换成时间数组
timeArray = time.strptime(dt, "%Y-%m-%d %H:%M:%S")
#转换成时间戳
timestamp = time.mktime(timeArray)
print (timestamp)
```