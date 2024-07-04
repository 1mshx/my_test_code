import urllib.request
import random

url = 'http://www.baidu.com/s?wd=ip'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 '
                  'Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,'
              'application/signed-exchange;v=b3;q=0.7'
}

# 请求对象的定制
request = urllib.request.Request(url=url, headers=headers)

# 设置代理池
proxies_pool = [
    {'http': '42.51.40.10:16816'},
    {'http': '183.237.194.145:16816'},
    {'http': '183.62.172.50:16816'}
]

# 使用代理
proxies = random.choice(proxies_pool)
print(proxies)

# handler build_opener open
handler = urllib.request.ProxyHandler(proxies=proxies)

opener = urllib.request.build_opener(handler)

response = opener.open(request)

content = response.read().decode('utf-8')

with open('daili1.html', 'w', encoding='utf-8') as fp:
    fp.write(content)
