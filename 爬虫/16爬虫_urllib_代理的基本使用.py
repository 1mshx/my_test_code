import urllib.request

url = 'http://www.baidu.com'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 '
                  'Safari/537.36'
    # 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,'
    #           'application/signed-exchange;v=b3;q=0.7'
}

# 请求对象定制
request = urllib.request.Request(url=url, headers=headers)

# 模拟浏览器访问服务器
# response = urllib.request.urlopen(request)

proxies = {
    'http': '42.51.40.10:16816'
}

# handler build_opener open
handler = urllib.request.ProxyHandler(proxies=proxies)

opener = urllib.request.build_opener(handler)

response = opener.open(request)

# 获取响应信息
content = response.read().decode('utf-8')

# 保存在本地
with open('../爬取内容/daili.html', 'w', encoding='utf-8') as fp:
    fp.write(content)
