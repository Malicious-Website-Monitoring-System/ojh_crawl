import scrapy
from ..items import AmazontutorialItem
class AmazonSpiderSpider(scrapy.Spider):
    name = "amazon"
    start_urls = ["https://www.amazon.com/s?bbn=283155&rh=n%3A283155%2Cp_n_publication_date%3A1250226011&dc&qid=1715614598&rnid=1250225011&ref=lp_1000_nr_p_n_publication_date_0"]
    page_number=2

    def parse(self, response):
        items=AmazontutorialItem()
        
        product_name = response.css('.a-color-base.a-text-normal::text').extract()
        product_author =  response.css('.a-color-secondary .a-size-base.s-link-style::text').extract()
        product_price =  response.css('.a-price-whole::text').extract()
        product_imagelink =  response.css('a.a-link-normal.s-no-outline::attr(href)').extract()

        items['product_name']=product_name
        items['product_author']= product_author
        items['product_price']= product_price
        items['product_imagelink']= product_imagelink

        yield items

        next_page='https://www.amazon.com/s?i=stripbooks&bbn=283155&rh=n%3A283155%2Cp_n_publication_date%3A1250226011&dc&page='+str(AmazonSpiderSpider.page_number)+'&qid=1715619245&rnid=1250225011&ref=sr_pg_3'
        if AmazonSpiderSpider.page_number<=75:
            AmazonSpiderSpider.page_number+=1
            yield response.follow(next_page,callback=self.parse)

#503에러
#settings.py에 가서 https://explore.whatismybrowser.com/useragents/explore/software_name/googlebot/ 에 있는 User agent로 고치기


#tutorial 14 - proxy
# 내 ip 주소가 아니라 다른 주소 쓰는것. 아무도 사용하지 않은 ip주소를 쓰는것이므로 신원도용이 아님
# https://github.com/rejoiceinhope/scrapy-proxy-pool
# Enable this middleware by adding the following settings to your settings.py: PROXY_POOL_ENABLED = Tru

