#tutorial 11 여러항목
#tutorial 12 컨테이너 사용하기 -> items.py

import scrapy
from ..items import TutorialItem

class QuoteSpider1(scrapy.Spider):
    name='quotes1'
    start_urls=[
        'https://quotes.toscrape.com/'
    ]

    def parse(self,response):
        items=TutorialItem()

        all_div_quotes=response.css("div.quote")

        for quote in all_div_quotes:
            title=quote.css("span.text::text").extract()
            author=quote.css(".author::text").extract()
            tag=quote.css(".tag::text").extract()

            items['title']=title
            items['author']=author
            items['tag']=tag
            '''
            yield {
                'title' : title,
                'quthor' : author,
                'tag' : tag
            }
            '''
            yield items

# C:\maliciousweb\Scrapy\tutorial> scrapy crawl quotes


# tutorial 13 json/xml/csv 파일로 저장하는 법
# -o = output 지정
# 터미널에서 scrapy crawl quotes -o items.json 혹은 .xml 혹은 .csv

#tutorial 14 pipelines
# Scraped data -> Item Containers -> Json/csv files
# Scraped data -> Item Containers -> Pipeline -> SQL/Mongo database
# db에 저장되려면 파이프라인을 거쳐야함
# settings.py에서 ITEM_PIPELINES 활성화