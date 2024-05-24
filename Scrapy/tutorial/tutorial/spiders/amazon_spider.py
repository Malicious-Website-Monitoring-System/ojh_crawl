#tutorial 1
#스크래피는 웹사이트를 크롤링하고 구조화된/비구조화된 데이터를 추출하기 위한 응용 프로그램 프레임워크
#데이터를 수집하고 가공하는 일을 하는 Worker를 Spider라고 한다
#스크래핑을 시작하기 전에 새로운 스크래피 프로젝트를 설정
#scrapy startproject <projectname> 명령 실행 projectname을 tutorial로 했음

#tutorial 2
import scrapy
from ..items import AmazonItem # 그 전 디렉토리에서 items.py들어가서 AmazonItem class 불러옴

class AmazonSpider(scrapy.Spider):
    name="amazon1"
    start_urls={
        'https://www.amazon.com/s?bbn=121443933011&rh=n%3A121443933011%2Cp_n_publication_date%3A1250226011&dc&qid=1715419141&rnid=1250225011&ref=lp_121443933011_nr_p_n_publication_date_0'
    }

    def parse(self, response):
        items=AmazonItem()
        product_name = response.css('span.a-size-medium.a-color-base.a-text-normal::text').extract()
        '''
        <span class="a-size-medium a-color-base a-text-normal">
        Liberated Love: Release Codependent Patterns and Create the Love You Desire</span>

        <span class="a-size-medium a-color-base a-text-normal">Ocean's Godori: A Novel</span>

        제목에서 반복되는거 -> <span class="a-size-medium a-color-base a-text-normal">

        span.a-size-medium.a-color-base.a-text-normal::text 
        -> <span> 요소 중에서 a-size-medium, a-color-base, a-text-normal 클래스를
           모두 가진 요소를 선택하고 그 요소의 텍스트를 추출 

        '''
        
        product_sale_price=response.css('span.a-offscreen::text').extract()
        '''
        가격에서 반복되는거 

        <span class="a-offscreen">$14.99</span>
        <span class="a-offscreen">$11.49</span>

        '''
        items['product_name']=product_name
        items['product_sale_price']=product_sale_price
        yield items

#터미널 PS C:\maliciousweb\Scrapy\tutorial> scrapy crawl amazon -o items.json

#2024-05-11 19:42:02 [scrapy.core.engine] DEBUG: Crawled (503) <GET https://www.amazon.com/s?bbn=121443933011&rh=n%3A121443933 ...
#2024-05-11 19:42:02 [scrapy.spidermiddlewares.httperror] INFO: Ignoring response <503 https://www.amazon.com/s?bbn=121443933011&rh...
# 'downloader/response_status_count/503': 3,
# 'httperror/response_ignored_status_count/503': 1,
# 'retry/reason_count/503 Service Unavailable': 2, 
# 503 에러 아마존 서버에서 스크랩핑 막음 ????

#tutorial3 robot.txt
#웹 스크래핑 가능한지 안한지 robots.txt라는 파일에 기록되어 있음
#아래와 같음
#Disallow: /gp/dmusic/
#Allow: /gp/dmusic/promotions/PrimeMusic
#...
#robot.txt 규칙을 따르지 않으려면 setting.py에 가서 
#ROBOTSTXT_OBEY = True를 False로 바꾸면 됨

