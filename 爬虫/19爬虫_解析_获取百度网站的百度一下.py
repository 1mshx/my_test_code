import urllib.request
from lxml import etree

# （1) 获取网页的源码
url = 'https://baidu.com'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 '
                  'Safari/537.36'
}

# 请求对象的定制
request = urllib.request.Request(url=url, headers=headers)

# 模拟浏览器访问服务器
response = urllib.request.urlopen(request)

# 获取网页源码
content = response.read().decode('utf-8')

# （2）解析  解析服务器响应的文件
tree = etree.HTML(content)

# 获取响应的数据
bd_list = tree.xpath('//input[@id="su"]/@value')

# （3）打印
print(bd_list)
