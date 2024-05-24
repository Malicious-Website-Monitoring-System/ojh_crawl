# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

# https://quotes.toscrape.com/ 연습 웹사이트??
# items.py는 Spider가 작업을 완료한 후 반환하는 결과값의 Schema를 정의하는 파일
# Item은 spider가 추출한 데이터를 저장할 객체로, 프로젝트의 items.py에 정의합니다.
import scrapy


class TutorialItem(scrapy.Item):
  title= scrapy.Field()
  author= scrapy.Field()
  tag= scrapy.Field()  

class AmazonItem(scrapy.Item):
      # define the fields for your item here like:
    product_name = scrapy.Field()
    product_sale_price = scrapy.Field()
    product_category = scrapy.Field()
    product_original_price = scrapy.Field()
    product_availability = scrapy.Field()