from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

url = "https://www.baidu.com"

browser.get(url)

# 元素定位

# 通过ID查找元素
element_by_id = browser.find_element(By.ID, "su")
print(element_by_id)

# 通过Name查找元素
element_by_name = browser.find_element(By.NAME, "wd")
print(element_by_name)

# 通过XPath查找元素
element_by_xpath = browser.find_element(By.XPATH, "//input[@id='su']")
print(element_by_xpath)

# 通过CSS选择器查找元素
element_by_css_selector = browser.find_element(By.CSS_SELECTOR, "#su")
print(element_by_css_selector)

# 通过链接文本查找元素
element_by_link_text = browser.find_element(By.LINK_TEXT, "新闻")

# 通过部分链接文本查找元素
element_by_partial_link_text = browser.find_element(By.PARTIAL_LINK_TEXT, "图片")

# 通过类名查找元素
element_by_class_name = browser.find_element(By.CLASS_NAME, "s_ipt")
print(element_by_class_name)

# 通过标签名查找元素
element_by_tag_name = browser.find_element(By.TAG_NAME, "input")
print(element_by_tag_name)

# 通过表单元素属性查找元素
element_by_attribute = browser.find_element(By.CSS_SELECTOR, "input[name='wd']")
print(element_by_attribute)

# 在输入框中输入文本
element_by_id.send_keys("百度一下")
print(element_by_id)

# 提交表单
element_by_id.submit()

# 关闭浏览器窗口
browser.close()
