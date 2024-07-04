from bs4 import BeautifulSoup

# 通过解析本地文件来加深理解
soup = BeautifulSoup(open('18爬虫_解析_xpath的基本使用.html', 'r', encoding='utf-8'), 'lxml')

# 根据标签名查找节点
# 找到的是第一个符合条件的a
print(soup.a)

# 获取标签的属性和属性值
print(soup.a.attrs)

# bs4的一些函数
# （1）find
# 返回第一个符合条件的数据
print(soup.find('a'))

# 可以通过条件找到对应的标签对象
print(soup.find('a', title="a2"))

# 根据class的值来找到对应的标签对象 注意的是class需要添加下划线
print(soup.find('a', class_="a1"))

# （2）find_all 返回的是一个列表，并且返回了所有的a标签
print(soup.find_all('a'))

# 如果想获取的是多个标签的数据，那么在里面添加的是列表的标签
print(soup.find_all(['a', 'span']))

# limit的作用是查找前几个数据
print(soup.find_all('a', limit=1))

# （3）select 返回的是一个列表，并且会返回多个数据
# 可以通过.代表class 把这种称作类选择器
print(soup.select('.a1'))

# 通过#来代表id，id选择器
print(soup.select('#a2'))

# 属性选择器 通过属性来找到对应的标签
# 查找li中有id的标签
print(soup.select('li[id]'))

# 查找li标签中id为a2的标签
print(soup.select('li[id="a2"]'))

# 层级选择器
# 后代选择器，找到的是div下的li
print(soup.select('div li'))

# 子代选择器，相当于儿子
# 注意加空格
print(soup.select('div > ul > li'))

# 找到a标签和li标签的所有内容
print(soup.select('a, li'))

# 节点信息
# 获取节点内容
obj = soup.select('body > ul > li')
# 如果标签对象中 只有内容 那么string和get_text()都可以使用
# 但是如果在标签对象中 除了内容还有标签 那么string就获取不到数据，一般使用get_text()
for i in obj:
    print(i.string)
    # print(i.get_text())

# 节点的属性
# name是标签的名字
print(soup.select('#p1')[0].name)

# attrs是将属性值作为一个字典返回
print(soup.select('#p1')[0].attrs)

# 获取节点的属性
print(soup.select('#p1')[0].attrs.get('class'))
print(soup.select('#p1')[0].get('class'))
