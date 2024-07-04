import json
import urllib.request
import urllib.parse

# 网址
url = 'https://fanyi.baidu.com/sug'

# 请求对象
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 '
                  'Safari/537.36 '
}

# 对象
data = {
    'kw': 'date'
}

# post请求的参数，必须进行编码
data = urllib.parse.urlencode(data).encode('utf-8')

# 请求对象的定制
# post请求的参数，是放在请求对象定制的参数中
request = urllib.request.Request(url=url, data=data, headers=headers)

# 模仿浏览器向服务器发出请求
response = urllib.request.urlopen(request)

# 获取响应的数据
content = response.read().decode('utf-8')

# 转换为json数据
obj = json.loads(content)

# 输出返回的内容
print(content)
print(obj)





