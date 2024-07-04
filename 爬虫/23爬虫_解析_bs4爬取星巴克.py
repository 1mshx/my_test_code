import urllib.request
from bs4 import BeautifulSoup

url = 'https://www.starbucks.com.cn/menu/'

response = urllib.request.urlopen(url)

content = response.read().decode('utf-8')

soup = BeautifulSoup(content, 'lxml')

name_list = soup.select('ul[class="grid padded-3 product"] strong')

for i in name_list:
    print(i.get_text())
