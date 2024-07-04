import json
import time

# 封装驱动:chrome浏览器
# def create_chrome_driver(*, headless=False):  # headless: 无头浏览器模式
# 创建Chrome浏览器对象
from selenium import webdriver


def create_chrome_driver(*, headless=False):
    options = webdriver.ChromeOptions()
    if headless:
        options.add_argument('--headless')

    # 设置debuggerAddress以连接到已打开的Chrome浏览器
    # chrome.exe --romote-debugging-port=9222
    # 浏览器复用
    # options.debugger_address = 'localhost:9222'

    # 设置其他选项，比如禁用扩展等
    options.add_argument('--disable-extensions')
    # options.add_argument('--disable-blink-features=AutomationControlled')  # 隐藏特征
    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    options.add_experimental_option('useAutomationExtension',
                                    False)  # selenium的防反爬 正常用户访问:false;selenium访问:ture 所以要改成false伪装成正常用户

    # options.add_argument('--user-data-dir=C:\\Users\\guo\\AppData\\Local\\Google\\Chrome\\User Data')  #使用本地浏览器缓存
    # options.add_argument('--profile-directory=Default')   #这行代码直接使用了，自身浏览器的缓存文件。

    # 使用代理池ip
    # resp = requests.get(url='http://localhost:8080/get').text
    # ip_list = json.loads(resp)["ip"]
    # ip = random.choice(ip_list)[0]
    # avail_ip = {"http": "http://" + ip,
    #             "https": "https://" + ip}
    # options.add_argument('--proxy-server={}'.format(avail_ip))

    browser = webdriver.Chrome(options=options)
    browser.execute_cdp_cmd(
        'Page.addScriptToEvaluateOnNewDocument',
        {'source': 'Object.defineProperty(navigator,"webdriver",{get: () => undefined})'})
    # 找到浏览器内置的navigator对象,改成undefined,
    # 平台就是通过检查这个对象的值来辨别浏览器是不是被第三方驱动的从而拦截爬虫请求，这里直接不这个对象的值改成undefined,这样目标网站就不能识别出我是爬虫
    return browser


# 写入cookie
def add_cookies(browser, cookie_file):
    # 向浏览器写入cookies信息
    try:
        with open(cookie_file, 'r') as file:
            cookies_list = json.load(file)
            for cookie_dict in cookies_list:
                if cookie_dict['secure']:
                    browser.add_cookie(cookie_dict)
                    print('cookie加入成功')
    except:
        print("cookie加入失败!")
