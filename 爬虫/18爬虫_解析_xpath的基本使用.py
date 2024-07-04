from lxml import etree

# xpath解析
# （1）本地文件
tree = etree.parse(r'D:\my_code\数据采集\爬虫\18爬虫_解析_xpath的基本使用.html')

# tree.xpath('xpath路径') 查找ul下面的li
li_list = tree.xpath('//body/ul/li/text()')
print(li_list)

# 查找所有有id的属性的li标签
li_list = tree.xpath('//ul/li[@id]/text()')
print(li_list)

# 查找id为1的class属性
li_list = tree.xpath('//ul/li[@id="1"]/@class')
print(li_list)

# 查询id中包含a的li标签
li_list = tree.xpath('//ul/li[contains(@id,"a")]/text()')
print(li_list)

# 查询id的值以a开头的li标签
li_list = tree.xpath('//ul/li[starts-with(@id,"a")]/text()')
print(li_list)

# 查询id为1和class为c1的标签
li_list = tree.xpath('//ul/li[@id="1" and @class="c1"]/text()')
print(li_list)

# 查询id为1或者a2的li标签
li_list = tree.xpath('//ul/li[@id="1"]/text() | //ul/li[@id="a2"]/text()')
print(li_list)

# （2）服务器响应的数据 response.read().decode('utf-8')
