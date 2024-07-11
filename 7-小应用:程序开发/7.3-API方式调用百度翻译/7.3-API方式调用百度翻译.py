# 导入依赖库
import json
import hashlib
import random
import urllib.parse
import urllib.request

# 获取用户输入的要翻译的内容
content = input("请输入要翻译的内容：")

# 翻译接口的URL
url = 'http://api.fanyi.baidu.com/api/trans/vip/translate'

# 构建请求参数
data = {}
secretKey = 'T_yxtSCG_sPL06U4nxah'
data['q'] = content
data['from'] = "zh"
data['to'] = "en"
data['appid'] = '20171109000093844'
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