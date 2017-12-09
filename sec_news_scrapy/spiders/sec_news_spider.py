import scrapy
from scrapy import Request, Selector

from sec_news_scrapy.items import SecNewsItem


class SecNewsSpider(scrapy.Spider):
    name = "security"
    allowed_domains = ["easyaq.com"]
    start_urls = []
    for i in range(2, 17):
        req_url = 'https://www.easyaq.com/type/%s.shtml' % i
        start_urls.append(req_url)

    def parse(self, response):
        topics = []
        for sel in response.xpath('//*[@id="infocat"]/div[@class="listnews bt"]/div[@class="listdeteal"]/h3/a'):
            topic = {'title': sel.xpath('text()').extract(), 'link': sel.xpath('@href').extract()}
            topics.append(topic)

        for topic in topics:
            yield Request(url=topic['link'][0], meta={'topic': topic}, dont_filter=False, callback=self.parse_page)

    def parse_page(self, response):
        topic = response.meta['topic']
        selector = Selector(response)

        item = SecNewsItem()
        item['title'] = selector.xpath("//div[@class='article_tittle']/div[@class='inner']/h1/text()").extract()
        item['content'] = "".join(selector.xpath('//div[@class="content-text"]/p/text()').extract())
        item['uri'] = topic['link'][0]
        print('Finish scan title:' + item['title'][0])
        yield item
