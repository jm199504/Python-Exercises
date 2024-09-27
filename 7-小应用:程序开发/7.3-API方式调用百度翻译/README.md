## 7.3-API方式调用百度翻译

### 问题描述

用API方式调用百度翻译接口，实现在终端输入中文，返回英文结果。

### 百度翻译API入口

[百度翻译开放平台](https://link.zhihu.com/?target=https%3A//api.fanyi.baidu.com/)

### 示例输入

```text
今天天气辣么好，我们出去玩吧！
```

### 示例输出

```text
The weather is so hot today, let's go out and play!
```

### 效果截图

![img](https://pic2.zhimg.com/80/v2-2a1958933ec1185278c0cd949a78e759_720w.webp)

### Python示例代码

```python
# 导入依赖库
import json
import hashlib
import random
import urllib.parse
import urllib.request

# 获取用户输入的要翻译的内容
content = input("请输入要翻译的内容：")

# 翻译接口的URL
url = '<http://api.fanyi.baidu.com/api/trans/vip/translate>'

# 构建请求参数
data = {}
secretKey = 'T_yxtSCG_sXXXXXXX'  # 更改为你的密钥
data['q'] = content
data['from'] = "zh"
data['to'] = "en"
data['appid'] = '20171109000093844'   # 更改为你的APPID
data['salt'] = str(random.randint(32768, 65536))
tsign = str(data['appid'] + data['q'] + data['salt'] + secretKey).encode('utf-8')
m = hashlib.md5()
m.update(tsign)
data['sign'] = m.hexdigest()

# 将请求参数编码并发送请求
data = urllib.parse.urlencode(data).encode('utf-8')
req = urllib.request.Request(url, data)
response = urllib.request.urlopen(req)

# 获取返回结果并解析
html = response.read().decode("utf-8")
html = json.loads(html)
rdata = html["trans_result"][0]["dst"]

# 输出翻译结果
print(rdata)
```