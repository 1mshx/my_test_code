import urllib.request

url = 'https://www.baidu.com'

# url的组成
# https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=%E5%91%A8%E6%9D%B0%E4%BC%A6
# http/https   www.baidu.com   80/443    s    ?后面的    #
#    协议           主机         端口号    路径     参数     锚点
# http      80
# https     443
# mysql     3306
# oracle    1521
# redis     6379
# mongodb   27017

headers = {
    'User_Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 '
                  'Safari/537.36 '
}

# 因为urlopen方法中不能存储字典，所以headers不能传进去
# 请求对象的定制
# 注意，因为参数顺序的问题，不能直接写参数，要使用关键字传参
request = urllib.request.Request(url=url, headers=headers)

response = urllib.request.urlopen(request)

content = response.read().decode('utf8')

print(content)
