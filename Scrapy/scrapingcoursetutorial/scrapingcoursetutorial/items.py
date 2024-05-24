# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapingcoursetutorialItem(scrapy.Item):
    product_name = scrapy.Field() # 웹사이트의 데이터 중 내가 가져오고 싶은 특정 데이터를 저장할 객체를 만드는 것/저장할 공간을 만든다고 생각
    product_price = scrapy.Field()
    product_imagelink = scrapy.Field()
