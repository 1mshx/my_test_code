# urllib_get的quote方法
import urllib.parse
import urllib.request

url = 'https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd='

# 请求对象的定制是为了解决反爬的第一种手段
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 '
                  'Safari/537.36 '
}

# 将周杰伦三个字变成unicode编码的格式
name = urllib.parse.quote('周杰伦')
print(name)

# 请求对象的定制
request = urllib.request.Request(url=url+name, headers=headers)

response = urllib.request.urlopen(request)

content = response.read().decode('utf8')

print(content)
