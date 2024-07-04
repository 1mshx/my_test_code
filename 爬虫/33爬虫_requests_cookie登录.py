import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import ddddocr

# 登录页面的url等
url = 'https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx'
user_agent = UserAgent().random
headers = {
    'User-Agent': user_agent
}

# 获取页面的源码
response = requests.get(url=url, headers=headers)
content = response.text

# 解析页面源码，获取 __VIEWSTATE  和  __VIEWSTATEGENERATOR
soup = BeautifulSoup(content, 'lxml')

# 获取__VIEWSTATE ，返回的是一个列表
VIEWSTATE = soup.select('#__VIEWSTATE')[0].attrs.get('value')

# 获取__VIEWSTATEGENERATOR
VIEWSTATEGENERATOR = soup.select('#__VIEWSTATEGENERATOR')[0].attrs.get('value')

# 获取验证码图片
code = soup.select('#imgCode')[0].attrs.get('src')
code_url = f'https://so.gushiwen.cn' + code

# 将图片下载到本地，观察后在控制台输入验证码
# 不能使用urllib.request，因为那个是两次请求，在requests中有一个方法
# session() 通过session的返回值，就可以将请求变成一个对象
session = requests.session()

# 获取验证码中的内容
response_code = session.get(code_url)

# 注意此时要使用二进制数据，因为我们要使用的是图片的下载
content = response_code.content
with open('code.jpg', 'wb') as f:
    f.write(content)

ocr = ddddocr.DdddOcr()
with open('code.jpg', 'rb') as f:
    img_bytes = f.read()

res = ocr.classification(img_bytes)
# print(res)
# 获取了验证码之后下载到本地，然后读取验证码输入
# code_name = input("请输入你的验证码:")

data = {
    '__VIEWSTATE': VIEWSTATE,
    '__VIEWSTATEGENERATOR': VIEWSTATEGENERATOR,
    'from': 'http://so.gushiwen.cn/user/collect.aspx',
    'email': '2801417588@qq.com',
    'pwd': 'gushiwenwang',
    'code': res,
    'denglu': '登录'

}

# 访问网址
post_url = 'https://so.gushiwen.cn/user/login.aspx?from=http%3a%2f%2fso.gushiwen.cn%2fuser%2fcollect.aspx'
response = session.post(url=post_url, data=data, headers=headers)

# 下载网页
content = response.text
with open('gushiwen.html', 'w', encoding='utf-8') as f:
    f.write(content)

# 难点
# （1）隐藏域
# （2）验证码
