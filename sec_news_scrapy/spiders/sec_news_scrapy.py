import scrapy
from scrapy import Request, Selector

from items import SecNewsItem


class SecNewsSpider(scrapy.Spider):
    name = "security"
    allowed_domains = ["easyaq.com"]
    start_urls = [
        "https://www.easyaq.com/type/1.shtml",
    ]

    def parse(self, response):
        topics = []
        for sel in response.xpath('//*[@id="infocat"]/div[@class="listnews bt"]/div[@class="listdeteal"]/h3/a'):
            topic = {'title': sel.xpath('text()').extract(), 'link': sel.xpath('@href').extract()}
            topics.append(topic)
        print(topics)

        for topic in topics:
            yield Request(url=topic['link'][0], dont_filter=True, callback=self.parse_page)

        for i in range(2, 17):
            req_url = 'https://www.easyaq.com/type/%s.shtml' % i
            yield Request(url=req_url, dont_filter=True, callback=self.parse)


    def parse_page(self, response):
        selector = Selector(response)

        item = SecNewsItem()
        item['title'] = selector.xpath("//div[@class='article_tittle']/div[@class='inner']/h1/text()").extract()
        item['content'] = "".join(selector.xpath('//div[@class="content-text"]/p/text()').extract())
        yield item
