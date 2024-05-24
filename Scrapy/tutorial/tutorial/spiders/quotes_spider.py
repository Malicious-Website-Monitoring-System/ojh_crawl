# tutorial 21 - 로그인창에 값 넣어서 로그인 성공하기
import scrapy
from ..items import TutorialItem

from scrapy.http import FormRequest
from scrapy.utils.response import open_in_browser

class QuoteSpider(scrapy.Spider):
    name='quotes'
    start_urls=[
        'https://quotes.toscrape.com/login'
    ]
    
    # login form data
    # csrf_token / username / assword
    

    #로그인 페이지에서 개발자도구로 보면
    #<form action="/login" method="post" accept-charset="utf-8">
    #    <input type="hidden" name="csrf_token" value="pQsIcErMdHGeNPiVSoCfDZwXOAxtnRblgkvyhKzWjUmqFBuYLJaT">
    
    def parse(self,response):
        token=response.css("form input::attr(value)").extract_first() #단일 결과를 반환한다. 일치하는 항목이 여러 개인 경우 첫번째 일치하는 내용이 반환 =get()
        print(token)
        return FormRequest.from_response(response,formdata={
            'csrf_token' : token,
            'username' : 'ddddddd',
            'password' : 'dsadsassa'
        },callback=self.start_scraping)
    # FormRequest.from_response 함수를 사용하여 로그인 요청을 생성
    # 요청에 대한 응답은 start_scraping 콜백 함수로 전달

    def start_scraping(self,response):
        open_in_browser(response)
        items=TutorialItem()

        all_div_quotes=response.css("div.quote")

        for quote in all_div_quotes:
            title=quote.css("span.text::text").extract()
            author=quote.css(".author::text").extract()
            tag=quote.css(".tag::text").extract()

            items['title']=title
            items['author']=author
            items['tag']=tag

            yield items

'''
#tutorial 19
class QuoteSpider(scrapy.Spider):
    name='quotes'
    page_number=2
    start_urls=[
        #'https://quotes.toscrape.com/'
        'https://quotes.toscrape.com/page/1/'
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

            yield items


        # <li class="next">
        #    <a href="/page/2/">Next <span aria-hidden="true">→</span></a></li>
        #next_page=response.css("li.next a::attr(href)").get() 
        #::text -> 노드의 텍스트만 추출
        #::attr(name) -> 노드 속성값 추출
        
        next_page='https://quotes.toscrape.com/page/'+str(QuoteSpider.page_number)+'/'

        if QuoteSpider.page_number < 11:
            QuoteSpider.page_number+=1
            yield response.follow(next_page, callback=self.parse)
            # 링크를 재귀적으로 따라가기
        
'''