import scrapy


class TcSpider(scrapy.Spider):
    name = "tc"
    allowed_domains = ["cs.58.com"]
    start_urls = ["https://cs.58.com/sou/?key=%E5%89%8D%E7%AB%AF%E5%BC%80%E5%8F%91&classpolicy=classify_C%2Cuuid_mZr2A8Hw8Hjic3a4nRdQJsiiQfnn8DTh&search_uuid=mZr2A8Hw8Hjic3a4nRdQJsiiQfnn8DTh&search_type=input"]

    def parse(self, response):
        # 字符串
        # content = response.text

        # 二进制
        # content = response.body

        # 直接采用xpath方法解析response中的内容
        response_1 = response.xpath('//div[@id="filter"]/div[@class="tabs"]/a/span')
        print("==================================================")
        print(response_1)
        print("==================================================")
        print(response_1.extract_first())
        print("==================================================")
        print(response_1.extract())
        print("==================================================")


