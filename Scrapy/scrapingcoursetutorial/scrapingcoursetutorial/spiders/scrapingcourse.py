import scrapy
from ..items import ScrapingcoursetutorialItem 

class ScrapingcourseSpider(scrapy.Spider):
    name = "scrapingcourse"
    start_urls = ["https://www.scrapingcourse.com/ecommerce/"]
    page_number=2

    def parse(self, response):
        items=ScrapingcoursetutorialItem()

        product_name=response.css(".woocommerce-loop-product__title::text").extract()
        product_price=response.css("bdi::text").extract()
        product_imagelink=response.css(".woocommerce-LoopProduct-link::attr(href)").extract()

        items['product_name']=product_name
        items['product_price']=product_price
        items['product_imagelink']=product_imagelink

        yield items
        
        next_page=response.css(".next.page-numbers::attr(href)").get() 
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)


        #next_page='https://www.scrapingcourse.com/ecommerce/page/'+str(ScrapingcourseSpider.page_number)+'/'
        #if ScrapingcourseSpider.page_number<=12:
        #    ScrapingcourseSpider.page_number+=1
        #    yield response.follow(next_page,callback=self.parse)
