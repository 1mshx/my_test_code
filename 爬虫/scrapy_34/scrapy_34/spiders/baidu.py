import scrapy


class BaiduSpider(scrapy.Spider):
    # 爬虫的名字 用于运行爬虫时使用的值
    name = "baidu"

    # 允许访问的域名
    allowed_domains = ["www.baidu.com"]

    # 起始的url地址
    start_urls = ["http://www.baidu.com"]

    # 是执行了start_urls之后执行的方法
    # 相当于  response = urllib.request.urlopen()
    #        response = requests.get()
    def parse(self, response):
        print('爬取成功')
