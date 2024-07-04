# 以访问csdn为例

import urllib.request
import urllib.error

url = 'https://blog.csdn.net/qq_41854911/article/details/122696986'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/113.0.0.0Safari/537.36 '
}
try:
    request = urllib.request.Request(url=url, headers=headers)

    response = urllib.request.urlopen(request)

    content = response.read().decode('utf-8')

    print(content)

except urllib.error.HTTPError:
    print('错误为HTTPError')

except urllib.error.URLError:
    print('错误为URLError')
