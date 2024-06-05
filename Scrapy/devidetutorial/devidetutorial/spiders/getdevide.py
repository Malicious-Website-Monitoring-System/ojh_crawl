import scrapy
from ..items import GetWordsItem


class DevideSpider(scrapy.Spider):
    name = "getdevide"

    def start_requests(self):
        for host in getattr(self, 'hosts', []):
            yield scrapy.Request(url=f'{host}', callback=self.parse, meta={'host': host})

    def parse(self, response):
        items = GetWordsItem()
        host = response.meta['host']
        items['host'] = host
        yield items

# scrapy crawl getdevide -o items.json