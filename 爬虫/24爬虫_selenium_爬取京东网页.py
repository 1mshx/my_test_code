# import urllib.request
#
# url = 'https://www.jd.com'
#
# response = urllib.request.urlopen(url)
#
# content = response.read().decode('utf-8')
#
# print(content)


# from selenium.webdriver import Chrome
# from selenium.webdriver.chrome.options import Options
#
# options = Options()
# options.add_experimental_option('detach', True)
#
# web = Chrome(options=options)
# web.get("https://www.jd.com")


# (1)导入selenium
from selenium import webdriver

# (2)创建浏览器操作对象
path = 'chromedriver.exe'

browser = webdriver.Chrome()

# (3)访问网站
url = 'https://www.jd.com'

# (4)page_source获取网页源码
browser.get(url)
content = browser.page_source

print(content)



