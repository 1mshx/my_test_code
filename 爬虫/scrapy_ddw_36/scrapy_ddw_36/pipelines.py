# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


# 如果想使用管道的话，就需要先在settings中开启管道
class ScrapyDdw36Pipeline:
    # item就是yield后面的book对象

    def open_spider(self, spider):
        self.file = open('book.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        # 以下这种方式不推荐，因为每传递过来一个对象就要打开一次文件，对文件的操作过于频繁

        # (1)write方法必须写一个字符串，而不能是其它对象
        # (2)w模式，每次都会打开一次然后覆盖掉之前的内容
        # with open('book.json', 'a', encoding='utf-8') as f:
        #     f.write(str(item))

        # 第二种方法，在前后创建两个方法
        self.file.write(str(item))

        return item

    def close_spider(self, spider):
        self.file.close()


# 多条管道开启
# (1)定义管道类
# (2)在settings中开启管道
import urllib.request


class DangDangPipeline:
    def process_item(self, item, spider):
        url = 'https:' + item['src']
        filename = './books/' + item['name'] + '.jpg'

        urllib.request.urlretrieve(url=url, filename=filename)

        return item
