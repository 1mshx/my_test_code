import scrapy
from scrapy_ddw_36.items import ScrapyDdw36Item


class DangSpider(scrapy.Spider):
    name = "dang"
    # 如果是多页数据的下载，必须调整allowed_domains的范围，一般情况下只写域名
    allowed_domains = ["category.dangdang.com"]
    start_urls = ["https://category.dangdang.com/cp01.01.02.00.00.00.html"]

    base_url = "https://category.dangdang.com/pg"
    page = 1

    def parse(self, response):
        # pipelines  下载数据
        # items      定义数据结构

        # src = '//ul[@id="component_59"]/li//img/@src'
        # alt = '//ul[@id="component_59"]/li//img/@alt'
        # price = '//ul[@id="component_59"]/li/p[@class='price']/span[1]/text()'
        # 所有的seletor对象都可以再次调用xpath方法

        li_list = response.xpath('//ul[@id="component_59"]/li')

        for li in li_list:
            # 注意懒加载，第一张图片的标签属性和别的不一样
            src = li.xpath('.//img/@data-original').extract_first()

            if src:
                src = src
            else:
                src = li.xpath('.//img/@src').extract_first()

            name = li.xpath('.//img/@alt').extract_first()
            price = li.xpath('.//p[@class="price"]/span[1]/text()').extract_first()

            book = ScrapyDdw36Item(src=src, name=name, price=price)

            # 获取一个book就将一个book交给pipelines
            yield book

        #       每一页的爬取的业务逻辑全都是一样的，所以我们只要将执行的那个页的请求再次调用parse方法就可以了
        #       第一页 https://category.dangdang.com/cp01.01.02.00.00.00.html
        #       第二页 https://category.dangdang.com/pg2-cp01.01.02.00.00.00.html
        #       第三页 https://category.dangdang.com/pg3-cp01.01.02.00.00.00.html
        #       第四页 https://category.dangdang.com/pg4-cp01.01.02.00.00.00.html
        #       最后页 https://category.dangdang.com/pg100-cp01.01.02.00.00.00.html

        if self.page < 100:
            self.page = self.page + 1
            url = self.base_url + str(self.page) + '-cp01.01.02.00.00.00.html'

            # 怎么去调用parse方法
            # scrapy.Request就是scrapy的get请求
            # url就是请求地址
            # callback是你要执行的那个函数，注意不需要加()
            yield scrapy.Request(url, callback=self.parse)
