import scrapy
from scrapy_movie_37.items import ScrapyMovie37Item


class MvSpider(scrapy.Spider):
    name = "mv"
    allowed_domains = ["www.ygdy8.net"]
    start_urls = ["https://www.ygdy8.net/html/gndy/china/index.html"]

    def parse(self, response):
        a_list = response.xpath('//div[@class="co_content8"]//tr[2]//td[2]//a[2]')
        for a in a_list:
            # 获取第一页的name和要点击的链接
            name = a.xpath('./text()').extract_first()
            href = a.xpath('./@href').extract_first()

            # 第二页的地址是
            url = 'https://www.ygdy8.net' + href

            # 对第二页的地址发起访问
            yield scrapy.Request(url, callback=self.parse_second, meta={'name': name})

    def parse_second(self, response):
        src = response.xpath('//div[@class="co_content8"]//img/@src').extract_first()
        # 接受到请求的那个meta参数的值
        name = response.meta['name']

        movie = ScrapyMovie37Item(src=src, name=name)

        # 将movie返回给管道
        yield movie
