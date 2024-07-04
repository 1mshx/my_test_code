import urllib.request

url = 'http://www.baidu.com'

# 模拟浏览器向服务器发送请求
response = urllib.request.urlopen(url)

# 一个类型和6个方法
# response是HTTPResponse的类型
print(type(response))

# 按照一个字节一个字节的去读
# content = response.read().decode('utf-8')
# print(content)

# 里面数字表示返回多少字节
# content = response.read(5)
# print(content)

# 按行读，读取一行
# content = response.readline().decode('utf-8')
# print(content)

# 按行读，读取所有
# content = response.readlines().decode('utf-8')
# print(content)

# 返回状态码，如果是200，那说明没有问题
print(response.getcode())

# 返回url地址
print(response.geturl())

# 获取状态信息
print(response.getheaders())
