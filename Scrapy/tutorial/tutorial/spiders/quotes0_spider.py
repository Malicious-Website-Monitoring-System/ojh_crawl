#tutorial 7 - spider 만들기
import scrapy

#scrapy.Spider를 상속받음
class QuoteSpider0(scrapy.Spider):
    name='quotes0'
    #스크랩할 URL목록 제공해야함
    start_urls=[
        'https://quotes.toscrape.com/'
    ]

    #구문분석함수
    #자기참조 + 스크랩하려는 웹사이트의 소스코드(=response)
    #새 객체를 생성할 때 클래스 내에서 자체적으로 작동하기를 원할 때 - self
    def parse(self,response):

        #소스 코드 전체가 필요X 우리가 원하는 걸 가져와야함
        #웹사이트 제목만 얻어오려함
        #<title>Quotes to Scrape</title>
        title = response.css('title::text').extract()
        '''
        <span class="text" itemprop="text">“The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.”</span>
        를 가져오고 싶다면?

        title = response.css('span.text::text').extract()
        {'titletext': ['“The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.”',
        '“It is our choices, Harry, that show what we truly are, far more than our abilities.”',
        '“There are only two ways to live your life. One is as though nothing is a miracle. The other is as though everything is a miracle.”',
        '“The person, be it gentleman or lady, who has not pleasure in a good novel, must be intolerably stupid.”',
        "“Imperfection is beauty, madness is genius and it's better to be absolutely ridiculous than absolutely boring.”",
        “Try not to become a man of success. Rather become a man of value.”',
        '“It is better to be hated for what you are than to be loved for what you are not.”',
        "“I have not failed. I've just found 10,000 ways that won't work.”",
        "“A woman is like a tea bag; you never know how strong it is until it's in hot water.”",
        '“A day without sunshine is like, you know, night.”']}

        '''

        #yield엔 딕셔너리 필요 키-값쌍
        #함수 내의 return키워드라고 생각하면 됨
        #스파이더 내부의 함수에서는 return대신 yield를 써야한다
        yield {'titletext' : title}


#tutorial 8 - 만든 spider 사용해보기
#터미널 PS C:\maliciousweb\Scrapy\tutorial> scrapy crawl quotes
#위로 올리다 보면 {'titletext': ['<title>Quotes to Scrape</title>']} 가져와진것을 확인 가능
#제목만 필요한데 태그도 같이 가져와짐
#response.css('title').extract()를 response.css('title::text').extract()로 수정
#{'titletext': ['Quotes to Scrape']} 가져와짐


#tutorial 9 - shell
#터미널에 scrapy shell "https://quotes.toscrape.com/" 
#scrapy가 shell내부에서 웹페이지를 연다
#response.css("span.text::text").extract() 여기서 .으로 class 연결 class값이 text였다
#인용문 여러개를 갖고오는데 그중 2번째값을 가져오고싶다면?
#response.css("span.text::text")[1].extract()

#SelectorGadget확장프로그램으로 쉽게 class값 알기?
#작가를 클릭하니 .author이 나왔음
#response.css(".author::text").extract()
#['Albert Einstein', 'J.K. Rowling', 'Albert Einstein', 'Jane Austen', 'Marilyn Monroe', 'Albert Einstein', 'André Gide', 'Thomas A. Edison', 'Eleanor Roosevelt', 'Steve Martin'] 
#원하는 곳 클릭하고 원하지 않는곳은 또 클릭해서 빨간색으로 뜸. 제외시킨것

#원하는곳 실습해보기 - top ten tags 부분
# response.css(".tag-item .tag::text").extract()
# ['love', 'inspirational', 'life', 'humor', 'books', 'reading', 'friendship', 'friends', 'truth', 'simile']


#tutorial 10 - xpath사용해보기
#XPath는 XML 문서를 트리 구조로 표현하며 최상위 노드부터 최하위 노드까지 모든 노드들과 속성, 데이터를 추출할 수 있는 경로를 나타내줍니다.
#두개의 slash(//)를 쓴다! 그리고 ::text대신 /text()를 쓴다
#>>> response.xpath("//title/text()").extract()
#['Quotes to Scrape'] 받아와짐

#<span class="text" itemprop="text">“어쩌구저쩌구문장”</span> 을 xpath로 받아오려면
#XPath에서는 속성을 “@”로 표현
#response.xpath("//span[@class='text']/text()").extract()
# "쌍따옴표는 묶는 맨앞과 맨뒤에만! 안에도 "가 있으면 그걸 끝으로 받아들임 안에는 무조건 '로 쓰자

#css와 xpath 섞어쓰기
#<li class="next">
#<a href="/page/2/">Next <span aria-hidden="true">→</span></a></li>
#위와 같은 태그에서 href값 가져오려면?
#response.css("li.next a").xpath("@href").extract()
#['/page/2/'] 얻음

#response.css("a").xpath("@href").extract()
#a태그의 href속성 값 다 가져옴 ['/', '/login', '/author/Albert-Einstein', '/tag/change/page/1/', ...

#a태그에서 class="tag"인거만 href 가져오기 : response.css("a.tag").xpath("@href").extract()