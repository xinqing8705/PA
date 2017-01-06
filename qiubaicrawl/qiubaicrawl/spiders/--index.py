import scrapy

from qiubaicrawl.items import QiubaicrawlItem


class QiuBaiCrawlSpider(scrapy.Spider):
    name="qiubaicrawl"
    start_urls=[
        "http://www.qiushibaike.com",
    ]
    
    def parse(self,response):
        for ele in response.xpath('//div[@class="article block untagged mb15"]'):
            authors=ele.xpath('./div[@class="author clearfix"]/a[2]/h2/text()').extract()
            contents=ele.xpath('./div[@class="content"]/text()').extract()
            yield QiubaicrawlItem(author=authors,content=contents)