# urllib_get的urlencode方法
import urllib.parse
import urllib.request

# urlencode应用场景:多个参数的时候
# https://www.baidu.com/s?wd=周杰伦&sex=男

data = {
    'wd': '周杰伦',
    'sex': '男',
    'location': '台湾省'
}

base_url = 'https://www.baidu.com/s?'

data = urllib.parse.urlencode(data)

# 请求资源路径
url = base_url+data
print(url)
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 '
                  'Safari/537.36'
}

# 请求对象的定制
request = urllib.request.Request(url=url, headers=headers)

# 模拟浏览器向服务器发送请求
response = urllib.request.urlopen(request)

# 获取网页源码的数据
content = response.read()

# 打印数据
print(content)


