import requests
import re
from bs4 import BeautifulSoup

url = 'http://huaban.com/explore/beioufengge/'
data = requests.get(url)
soup = BeautifulSoup(data.text, 'lxml')
links = re.findall("pin_id\":(.*?),",soup.get_text())
suburl = 'http://huaban.com/pins/'
count = 1
for link in links:
    turl = suburl + link
    data = requests.get(turl)
    soup = BeautifulSoup(data.text, 'lxml')
    codes = re.findall('key":"(.*?)"',soup.get_text())
    for code in codes:
        curl = 'http://img.hb.aicdn.com/'+code
        try:
            pic = requests.get(curl, timeout=5)
            file_name = "0013/dlp_" + str(count) + ".jpg"
            count +=1
            print(file_name,'下载成功')
            fp = open(file_name, 'wb')
            fp.write(pic.content)
        except:
            print('无法下载该图片')
            continue