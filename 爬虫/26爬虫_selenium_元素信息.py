from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

url = "https://www.baidu.com"

browser.get(url)

input_id = browser.find_element(by=By.ID, value='su')

# 获取元素属性
print(input_id.get_attribute('value'))

# 获取元素文本
print(input_id.text)

# 获取标签名
print(input_id.tag_name)
