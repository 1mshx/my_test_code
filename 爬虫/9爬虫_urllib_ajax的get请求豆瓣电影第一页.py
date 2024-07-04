# get请求
# 获取豆瓣电影的第一页的数据并且存储起来

import urllib.request

url = 'https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&start=0&limit=20'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 '
                  'Safari/537.36'
}

# 请求对象的定制
request = urllib.request.Request(url=url, headers=headers)

# 获取响应的数据
response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')

# 数据下载到本地
# open方法默认使用的是jbk编码，如果想保存汉字或者中文，就需要转换编码格式
fp = open('../爬取内容/豆瓣/douban.json', 'w', encoding='utf-8')
fp.write(content)
fp.close()


