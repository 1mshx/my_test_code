from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

path = r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
chrome_options.binary_location = path

browser = webdriver.Chrome(chrome_options=chrome_options)

url = 'https://www.baidu.com'

browser.get(url)

browser.save_screenshot('baidu.png')