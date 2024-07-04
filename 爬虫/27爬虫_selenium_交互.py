from selenium import webdriver
import time

from selenium.webdriver.common.by import By

# 创建浏览器对象
browser = webdriver.Chrome()

url = 'https://www.baidu.com'

browser.get(url)
time.sleep(1)

# 获取文本框的对象
input_box = browser.find_element(by=By.ID, value='kw')

# 在文本框中输入周杰伦
input_box.send_keys('周杰伦')

time.sleep(1)

# 获取百度一下的按钮
button = browser.find_element(by=By.ID, value='su')

# 点击按钮
button.click()

time.sleep(2)

# 滑到底部 底下两种方法都可以，第一个比较老
# js_bottom = 'document.documentElement.scrollTop=100000'
# browser.execute_script(js_bottom)
browser.execute_script("window.scrollBy(0,10000)")
time.sleep(1)

# 点击下一页
button1 = browser.find_element(by=By.CLASS_NAME, value='n')
button1.click()
time.sleep(2)

browser.execute_script("window.scrollBy(0,10000)")
time.sleep(1)

# 回到上一页
browser.back()
time.sleep(2)

# 又回到下一页
browser.forward()
time.sleep(2)

# 关闭
browser.quit()
