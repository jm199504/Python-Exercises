# 第 0008 题： 一个HTML文件，找出里面的正文。
# 第 0009 题： 一个HTML文件，找出里面的链接。
from bs4 import BeautifulSoup

html_doc = open("files\\abc.html",'r',encoding='utf-8')

htmlhandle = html_doc.read()

#使用beautifulsoup解析功能，解析器使用lxml
soup = BeautifulSoup(htmlhandle,'html.parser')
#输出标题
print('标题：',soup.title)
#输出p标签的内容
print('内容：',soup.p)
#输出a链接
print('链接：',soup.find_all('a'))
#输出body正文
print('正文：',soup.find_all('body'))
#输出整个html文件
print('整个html文件：',soup.get_text)
