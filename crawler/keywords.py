# -*- coding: utf-8 -*-
import re
from collections import Counter
from selenium import webdriver
from selenium.webdriver.common.by import By
from urllib.parse import urlparse
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

def extract_with_selenium(self,response):
    try:
        url = response.url      
        options = Options()
        options.add_argument("headless")
        driver = webdriver.Chrome(options=options)
        driver.get(url)
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

        # text말고도 속성값에도 유의미한 키워드들 포함한다고 생각
        # 예시 :  <meta name="description" content="무료웹툰 성인사이트 토렌트 링크모음과 무료 영화 TV 드라마 다시보기 주소모음을 소개하고 오피, 유흥, 스포츠중계 및 커뮤니티 사이트순위 정보를 제공합니다.">

        # content속성을 포함하는 모든 태그 찾기
        all_tags = driver.find_elements(By.XPATH, '//*[@content]')

        # 각 태그의 content 속성 값 가져오기
        contents = [tag.get_attribute("content") for tag in all_tags]
        contents_words=[]
        for content in contents:  
            # 각 content에서 한글만 추출하기 -> 영어까지 하면 'width' / 'index' / 'follow' / 'https', 'funbe384', 'com', 'EC', '9B', 'B9', 'ED', '88', 'B0' 등. 제외해도 될 것 같음
            content_word = re.findall(r'[\uAC00-\uD7A3]+', content)
            contents_words.extend(content_word)
        
        # body 요소 가져오기
        body_element = driver.find_element(By.TAG_NAME, 'body')

        # body 요소 안에 있는 모든 텍스트 가져오기
        body_text = body_element.text

        # 단어만 추출하기 #토토보증업체1BET1 이런거때문에 숫자도 포함
        body_words = re.findall(r'\b\w+\b', body_text)

        # 단어와 contents를 하나의 리스트로 합치기
        combined_list = body_words + contents_words
        
        return combined_list   # Counter(combined_list)     
         

    except Exception as e:
        print(f"An error occurred with {url}: {e}")
        return None
    
    finally:
        driver.quit()

#확인용
#Extract_with_selenium(url)
a=Extract_with_selenium("https://funbe385.com/%EC%9B%B9%ED%88%B0")#("https://wfwf328.com")#("https://funbe383.com")#("https://www.coupang.com")#("https://blacktoon.info")#("https://www.naver.com/")
print(a)


'''불법웹툰

1. text만 추출 _ 첫번째줄 말고는 거의 다 웹툰 제목

['웹툰', '토토보증업체1BET1', '주소알림', '고객센터', '검색어', '필수', '연재', '완결', '최신', '인기', '장르', '제목', '일', '월', '화', '수', '목', '금', '토', '열흘', '업데이트', '마섹남',
 '마술하는', '섹시한', '남자', '로맨스', '스토리', '05', '26', '0', '업데이트', '마왕의', '고백', '판타지', '스토리', '05', '26', '9', '업데이트', '망돌리부트', '드라마', '05', '26', '2', 
 '업데이트', '호랑이님의', '딸이', '되었습니다', '판타지', '로맨스', '05', '26', '4', '업데이트', '고수', '후궁으로', '깨어나다', '판타지', '로맨스', '05', '26', '8', '업데이트', '아카데미의', 
 '천재칼잡이', '판타지', '05', '26', '51', '업데이트', '내일', '드라마', '판타지', '일상', '05', '26', '17', '업데이트', '서브', '남주가', '너무', '많아', '로맨스', '05', '26', '2', '업데이트', 
 '아카데미에', '위장취업당했다', '판타지', '스토리', '05', '26', '47', '업데이트', '데빌샷', '판타지', '액션', '스토리', '05', '26', '6', '업데이트', '경자', '전성시
대', '개그', '05', '26', '2', '업데이트', '천재', '무림', '트레이너', '액션', '무협', '05', '26', '6', '업데이트', '천재', '플레이어의', '귀환', '판타지', '05', '25', '5', '업데이트', '
요기도', '괴물이', '있다', '05', '25', '1', '업데이트', '검사가', '법을', '모름', '판타지', '05', '25', '2', '업데이트', '축구재능', '다', '내꺼', '스포츠', '05', '25', '5', '업데이트', '해늘골',
 '스릴러', '공포', '05', '25', '0', '업데이트', '독의태자비', '판타지', '로맨스', '05', '25', '1', '업데이트', '더블랙LABEL', '드라마', '05', '25', '0', '업데이트', '달리는', '
여자', '로맨스', '05', '25', '0', '업데이트', '망겜탈출', '판타지', '개그', '05', '25', '0', '업데이트', '0살부터', '슈퍼스타', '드라마', '05', '25', '14', '업데이트', '반월당의', '기묘
한', '이야기', '드라마', '05', '25', '0', '업데이트', '생존', '마스터가', '되었다', '드라마', '판타지', '액션', '05', '25', '23', '업데이트', '다정한', '개새끼의', '목을', '비틀겠습니다', '드라마', '판타지', '로맨스', '순정', '05', '25', '10', '업데이트', '귀여워', 'BL', '05', '25', '1', '업데이트', '사이클링', '히트', 'BL', '05', '25', '1', '업데이트', '여제화원', '판
타지', '로맨스', '05', '25', '1', '업데이트', '림딩동', '드라마', '스포츠', '05', '25', '6', '업데이트', '구해종', 'SOS', '로맨스', '05', '25', '0', '업데이트', '칠흑의', '거버니스', '로맨스', '05', '25', '1', '업데이트', '짐승', '피해', '짐승남', '로맨스', '05', '25', '2', '업데이트', '돈나무', '판타지', '액션', '05', '25', '0', '업데이트', '무림세가', '천대받는', '손
녀', '딸이', '되었다', '판타지', '로맨스', '05', '25', '38', '업데이트', '아주', '작은', '방울', '로맨스', '05', '25', '0', '업데이트', '상태창에서', '시한부가', '빗발친다', '드라마', '05', '25', '4', '업데이트', '엉큼한', '맞선', '로맨스', '05', '25', '1', '업데이트', '악마의', '주인님이', '되어버렸다', '로맨스', '05', '25', '5', '업데이트', '이상형', '배달', '서비스', 
'드라마', '로맨스', '05', '25', '0', '업데이트', '후원에', '핀', '제비꽃', '로맨스', '05', '25', '3', '업데이트', '재혼', '부부', '로맨스', '05', '25', '1', '업데이트', '악역', '황녀님
은', '과자집에서', '살고', '싶어', '드라마', '스토리', '05', '25', '37', '업데이트', '약탈', '마드모아젤', '판타지', '로맨스', '05', '25', '20', '업데이트', '아방튀르', '왜', '하필', '역하렘이에요', '판타지', '로맨스', '05', '25', '0', '업데이트', '내가', '버린', '개에게', '물렸을', '때', '로맨스', '05', '25', '5', '업데이트', '시녀로', '살아남기', '드라마', '판타지', '로맨스',
 '순정', 'BL', '05', '25', '84', '업데이트', '언데드킹', '판타지', '액션', '05', '25', '82', '업데이트', '흑막의', '어린', '후원자', '판타지', '로맨스', '05', '25', '3', '업데이
트', '집착의', '이유', '로맨스', '05', '25', '1', '업데이트', '주문을', '말해', '로즈', '판타지', '로맨스', '05', '25', '3', '업데이트', '천재', '의사', '이무진', '드라마', '판타지', '05', '25', '62', '업데이트', '흑막', '남주의', '시한부', '유모입니다', '로맨스', '05', '25', '4', '업데이트', '회귀했더니', '공작', '판타지', '05', '25', '23', '업데이트', '남주를', '임시 보호',
 '중입니다', '판타지', '로맨스', '05', '25', '11', '업데이트', '신인인데', '천만배우', '드라마', '05', '25', '5', '업데이트', '밥만', '먹고', '레벨업', '드라마', '판타지', '액션', '05', '25', '357', '업데이트', '동화', '속', '악역의', '완벽한', '엔딩', '플랜', '판타지', '로맨스', '05', '25', '19', '업데이트', '폭군의', '위자료를', '굴려보자', '로맨스', '05', '25', '1', '업데이트',
'악녀인데요', '왜', '집착하시죠', '판타지', '로맨스', '05', '25', '5', '업데이트', '파공검제', '액션', '무협', '05', '25', '5', '업데이트', '호연가', '로맨스', '05', '25', '1', '업데이트', '천하제일', '곤륜객잔', '액션', '무협', '05', '25', '5', '업데이트', '폭군을', '길들이고', '도망쳐버렸다', '드라마', '판타지', '로맨스', '순정', '05', '25', '97', ' 업데이트', '상태창', '보는',
'아기', '황녀님', '판타지', '로맨스', '05', '25', '12', '업데이트', '황제와의', '잠자리에서', '살아남는', '법', '판타지', '로맨스', '05', '25', '11', '업데이트', '소녀', '가주가', '되었습니다', '판타지', '로맨스', '05', '25', '5', '업데이트', '이혼당했지만', '재벌입니다', '드라마', '판타지', '로맨스', '순정', '05', '25', '34', '업데이트', ' 나', '홀로', '주문', '사용자', '드라마', 
'판타지', '액션', '05', '25', '97', '업데이트', '백룡공작', '팬드래건', '판타지', '액션', '05', '25', '35', '업데이트', '점괘보는', '공녀님', '판타지', '로맨스', '05', '25', '7', '업데이트', '던전', '안의', '살림꾼', '로맨스', '05', '25', '6', '업데이트', '학교로', '간', '보스', '로맨스', '05', '25', '8', '업데이트', '두', '번째', '남편이', '절륜해서', '우울하다', '판타지', '로맨스', '05', '25', '44', '업데이트', '집착광공의', '아빠가', '꼬심', '당하는', '중', 'BL', '05', '25', '6', '업데이트', '마스터', '마인드', '드라마', '05', '25', '0', '업데이트', '전왕전기', '드라마', '판타지', '액션', '무협', '05', '25', '54', '업데이트', '멜린의', '구세', '플랜', '판타지', '로맨스', '05', '25', '2', '업데이트', '다시', '태어난', '베토벤', '드라마', '일상', '05', '25', '4', '업데이트', '무협지', '악녀인데', '내가', '제일', '쎄', '드라마', '판타지', '액션', '무협', '05', '25', '71', '업 데이트', '입양된', '며느리는', '파양을', '준비합니다', '판타지', '로맨스', '05', '25', '15', '업데이트', '사마쌍협', '액션', '무협', '05', '25', '6', '업데이트', '정령', '농사꾼', '드라 마', '판타지', '일상', '05', '25', '79', '업데이트', '역대급', '창기사의', '회귀', '판타지', '액션', '05', '25', '78', '업데이트', '악녀가', '길들인', '짐승', '판타지', '로맨스', '05', '25', '28', '업데이트', '뉴비가', '너무', '강함', '판타지', '액션', '05', '25', '53', '업데이트', '블랙기업조선', '드라마', '05', '25', '9', '업데이트', '갓', '오브', '블랙필드', '드라마', '판타지', '액션', '05', '25', '200', '업데이트', '귀환자의', '마법은', '특별해야', '합니다', '판타지', '액션', '05', '25', '839', '업데이트', '악녀는', '오늘도', '즐겁다', '드라마', ' 판타지', '로맨스', '순정', '05', '25', '61', '업데이트', '고행석', '악질의', '전설', '4탄', '액션', '무협', '05', '25', '0', '업데이트', '닳고닳은', '뉴비', '드라마', '판타지', '액션', '05', '25', '170', '업데이트', '네크로맨서', '학교의', '소환천재', '판타지', '05', '25', '20', '업데이트', '영웅', '회귀하다', '판타지', '액션', '05', '25', '62', '업데이트', '검술명가', '막내아들', '판타지', '액션', '05', '25', '119', '업데이트', '야설록', '중원일검', '컬렉션', '무협', '05', '25', '0', '업데이트', '마류', '개정판', '무협', '05', '25', '0', '업데이트', '왕의', '딸로', '태어났다고', '합니다', '판타지', '일상', '05', '25', '366', '업데이트', '쓸개', '드라마', '05', '25', '0', '업데이트', '어쩌다', '햄스터', '드라마', '05', '25', '0', '업 데이트', '아띠아띠', '드라마', '05', '25', '0', '업데이트', '황성', '일촉즉발', '컬렉션', '액션', '무협', '05', '25', '0', '업데이트', '고양이', '아가씨와', '경호원들', '드라마', '판타지', '로맨스', '일상', '05', '25', '68', '19', '업데이트', '인', '유어', '아이즈', 'BL', '05', '25', '3', '업데이트', '생존자들', '스릴러', '공포', '05', '25', '1', '19', '업데이트', '호랑이님', '잘', '먹었습니다', 'BL', '05', '25', '4', '업데이트', '야설록', '제왕군림', '컬렉션', '액션', '무협', '05', '25', '1', '업데이트', '복원가의', '집', '드라마', '판타지', '스토리', '05', '25', '6', '업데이트', '킬링', '마이', '러브', '드라마', '로맨스', '05', '25', '0', '업데이트', '대나무숲에서', '알립니다', '드라마', '05', '25', '0', '업데이트', '세자전', '드라 마', '05', '25', '0', '업데이트', '19년', '뽀삐', '드라마', '05', '25', '0', '업데이트', '황성', '강호남아', '컬렉션', '액션', '무협', '05', '25', '0', '19', '업데이트', '슬기로운', '기 사생활', '성인', '05', '25', '11', '19', '업데이트', '치트', '타자가', '다', '따먹음', '성인', '05', '25', '8', '19', '업데이트', '육체구속', '성인', '05', '25', '21', '19', '업데이트', '성지도관리', '공무원', '성인', '05', '25', '1', '19', '업데이트', '구멍가게', '구멍', '열었습니다', '성인', '05', '25', '36', '19', '업데이트', '엄마', '먼저', '드세요', '성인', '05', '25', '16', '19', '업데이트', '펌블', 'BL', '05', '25', '22', '업데이트', '첫사랑은', '헤이트', '드라마', '로맨스', '05', '25', '4', '19', '그놈은', '공이었다', 'BL', '05', '24', '17', ' 본투비갓', '판타지', '05', '24', '0', 'BJ대마도사', '판타지', '액션', '05', '23', '49', '검빨로', '레벨업', '판타지', '액션', '05', '23', '42', '19', '가족끼리', '왜', '그래', '성인', '05', '23', '2', '19', '도련님', '길들이기', 'BL', '05', '23', '1', '흙수저', '시스템에게', '선택받다', '드라마', '판타지', '액션', '05', '22', '11', '체이서', '드라마', '판타지', '액션', '05', '22', '1', '19', '야생의', '친구들과', '성인', '05', '22', '1', '19', '일진녀', '길들이기', '노벨피아', '성인', '05', '22', '13', '19', '네가', '없는', '세계', 'BL', '05', '22', '3', '황제가', '나를', '시한부라고', '생각해서', '곤란하다', '로맨스', '05', '21', '2', '정령사', '나타르', '전기', '드라마', '판타지', '액션', '05', '21', '58', '19', '하렘으로', '복수한 다', '성인', '05', '21', '1', '19', '진비서', '감금일지', 'BL', '05', '21', '12', '19', '열병', 'BL', '05', '21', '22', '그', '머리', '긴', '선배', '이름이', '뭐더라', '로맨스', '05', '20', '0', '아빠는', '버츄얼', '아이돌', '드라마', '05', '20', '1', '神장산범', '로맨스', '05', '20', '6', '포크', '나이프', '판타지', '액션', '05', '20', '2', '갑', '자기', '건물주', '드 라마', '05', '20', '2', '19', '칵테일', '라운지', 'BL', '05', '20', '0', '내게', '종말은', '게임이다', '판타지', '액션', '05', '20', '13', '아기', '다람쥐가', '다', '잘해요', '판타지', '로맨스', '05', '19', '19', '가드패스', '액션', '학원', '05', '19', '51', '19', '단비주의보', 'BL', '05', '19', '10', '19', '내', '생애', '최고의', '행운', 'BL', '05', '19', '4', '19', ' 해와', '달의', '공생관계', 'BL', '05', '19', '3', '19', '원', '샷', '원', 'BL', '05', '19', '6', '19', '오만한', '너에게', '바치는', 'BL', '05', '19', '1', '19', '미구놀이', 'BL', '05', '19', '0', '19', '새비지', '캐슬', '로맨스', '05', '19', '5', '19', '하는', '중전', '로맨스', '05', '19', '5', '19', '사랑은', '비염을', '타고', '로맨스', '05', '19', '5', '황궁의', '정 원에는', '개가', '산다', '로맨스', '05', '19', '8', '부동산이', '없는', '자에게', '치명적인', '스릴러', '05', '19', '0', '이발소', '밑', '게임가게', '드라마', '05', '19', '0', '날', '닮 은', '아이', '로맨스', '05', '19', '2', '소녀재판', '드라마', '스토리', '05', '19', '10', '이제', '와', '후회해봤자', '로맨스', '05', '19', '0', '재영과', '재영', '사이', '로맨스', '05', '19', '0', '19', '내', '인생', '떡상', '성인', '05', '19', '7', '19', '엔젤키스', 'BL', '05', '19', '0', '건객', '액션', '무협', '05', '19', '3', '19', '아내의', '여동생과', '결혼했다', '성인', '로맨스', '05', '19', '2', '19', '미증유', 'BL', '05', '19', '1', '아무래도', '결혼을', '잘못한', '것', '같다', '로맨스', '05', '19', '4', '피폐물', '남주의', '엄마가', '되었다', '로맨스', '05', '19', '5', '악녀는', '조용히', '살고싶을', '뿐인데', '로맨스', '05', '19', '5', '무진', '네이버', '드라마', '액션', '05', '19', '8', '칼끝에', '입술', '판타지', '로맨스', '스토리', '05', '19', '10', '마법스크롤', '상인', '지오', '시즌3', '판타지', '액션', '05', '19', '11', '용사보다', '너무', '강해서', '힘을', '숨김', '액션', '05', '19', '10', '망돌의', '사생', '스릴러', '05', '19', '0', '장풍전', '판타지', '액션', '05', '19', '8', '상사불상사', '로맨스', '05', '19', '4', '기기괴괴2', '스릴러', '05', '19', '2', '19', '명태새끼', '말려버려', 'BL', '05', '19', '8', '천검지존', '액션', '무협', '05', '19', '5', '다크', '판타지', '속', '성기사', '판타지', '액션', '05', '19', '2', '환생좌', '판타지', '액션', '05', '19', '18', '재벌의', '품격', '드라마', '05', '19', '3', '빛의', '후예', '드라마', '판타지', '액션', '05', '19', '29', '19', '메종', 'BL', '05', '19', '8', '19', '몽룡전', 'BL', '05', '19', '6', '19', '3학년', '5반', '성인', '로맨스', '05', '19', '25', '19', '순애가', '대체', '뭔데', '성인', '05', '19', '3', '19', '엄마의', '남자2', '성인', '05', '19', '0', '약빨이', '신선함', '판타지', '액션', '05', '19', '20', '수희0', 'tngmlek0', '드라마', '스토리', '05', '19', '5', '청춘계시록', '로맨스', '스토리', '05', '19', '2', '위닝샷', '스포츠', '05', '19', '18', '나', '혼자', '특성빨로', '무한', '성장', '판타지', '액션', '05', '19', '58', '혼자', '다', '해', '먹는', '천재', '암살자', '판타지', '05', '19', '13', '무능력자', '네이버', '액션', '05', '19', '6', '판사', '이한영', '드라마', '스토리', '05', '19', '34', '19', '릴리', '오브', '더', '밸리', 'LILY', 'OF', 'THE', 'VALLEY', '로맨스', '05', '19', '1', '19', '솔로', '포', '투', 'BL', '05', '19', '8', '19', '쌍피', 'BL', '05', '19', '2', '19', '아늑한', '집착', 'BL', '05', '19', '4', '19', '옆집', '형', 'BL', '05', '19', '0', '천화서고', '대공자', '액션', '무협', '05', '19', '39', '이웃집', '연하', '로맨스', '05', '19', '1', '별이삼샵', '드라마', '로맨스', '일상', '스토리', '05', '19', '6', '입학용병', '드라마', '액션', '스토리', '05', '19', '191', '19', '기도문', 'BL', '05', '19', '0', '요정의', '유산', '판타지', '로맨스', '05', '19', '2', 'Retry', '다시', '한번', '최강', '신선으로', '판타지', '액션', '05', '19', '278', '19', '로맨스', '낫', '로맨틱', 'BL', '05', '19', '3', '시체는', '말한다', '판타지', '로맨스', '05', '19', '1', '키스는', '자기', '전에', '로맨스', '05', '19', '0', '선', '넘지', '마세요', ' 아버님', '판타지', '로맨스', '05', '19', '3', '킬링킬러', '액션', '스토리', '05', '19', '6', '여신님의', '호랑이', '공략법', '로맨스', '스토리', '05', '19', '1', '프린키피아', '판타지', '05', '19', '0', '사랑받기', '원하지', '않는다', '판타지', '로맨스', '05', '19', '5', '한', '배를', '탄', '사이', '판타지', '로맨스', '05', '19', '9', '완벽한', '파트너', '로맨스', '스토리', '05', '19', '1', '사랑은', '없는', '것처럼', '로맨스', '05', '19', '3', '정부는', '도망친다', '판타지', '로맨스', '05', '19', '9', '매일', '밤', '집착폭군과', '잠드는', '고양이가', '되었다', '로맨스', '05', '19', '3', '손', '잡은', '사이', '로맨스', '05', '19', '0', '잉그람의', '등불', '판타지', '로맨스', '05', '19', '1', '첫눈에', '반했어요', '흑막님', '로맨스', '05', '19', '2', '첫날밤만', '세', '번째', '로맨스', '스토리', '05', '19', '5', '19', '못된', '짐승을', '길들이는', '법', '판타지', '로맨스', '05', '19', '13', '최고의', '뿔소라', '로맨스', '05', '19', '1', '신혼부부', '생활', '백서', '로맨스', '스토리', '05', '19', '2', '밤마다', '남편이', '바뀐다', '판타지', '로맨스', '05', '19', '12', '백설을', '위하여', '로맨스', '스토리', '05', '19', '4', '마녀의', '아들을', '지키는', '이유', '판타지', '로맨스', '05', '19', '5', '시월드가', '내게', '집착한다', '로맨스', '스토리', '05', '19', '39', '노래', '못', '하는', '남자', '로맨스', '05', '19', '0', '바바리안', '영애', '개그', '05', '18', '0', '19', '신부강탈', '로맨스', '05', '18', '1', '부스러기', '성녀님', '로맨스', '05', '18', '0', '왕녀는', '미친', '척을', '한다', '드라마', '판타지', '로맨스', '순정', '05', '18', '34', '설련화', '드라마', '05', '18', '0', 'Y13', '드라마', '스포츠', '05', '18', '2', '북부', '대공', '로맨 스', '05', '18', '3', '대장장이', '지그', '판타지', '액션', '05', '18', '21', '소꿉친구를', '폭군으로', '키웠습니다', '드라마', '판타지', '로맨스', '순정', '05', '18', '35', '19', '세상 에', '나쁜', '개는', '없다', 'BL', '05', '18', '4', '옥타곤의', '제왕', '드라마', '액션', '05', '16', '8', '대가는', '너희의', '모든', '것', '로맨스', '05', '14', '5', '19', '구원하는', '법', '참', '쉽습니다', 'BL', '05', '14', '27', '로봇소녀', '노이도', '드라마', '05', '12', '0', '홍끼의', '메소포타미아', '신화', '드라마', '05', '12', '0', '추락한', '곳은', '낙원', ' 로맨스', '05', '12', '1', '미친', '황제가', '나를', '안을', '때', '로맨스', '05', '12', '0', '19', '백작님', '사랑을', '주세요', 'BL', '05', '12', '4', '19', '오버클럭', 'BL', '05', '12', '4', '불완전', '신데렐라물', '로맨스', '05', '12', '1', '첫사랑넘버', 'BL', '05', '12', '0', '남고', '소년', 'BL', '05', '12', '3', '분신으로', '자동사냥', '판타지', '액션', '05', '12', '44', '망겜의', '시체줍는', '천재전사', '판타지', '05', '12', '6', '최후의', '모험가', '판타지', '액션', '05', '12', '7', '먹뀌싸', '액션', '05', '12', '3', '19', '미친', '짓인', '줄', '알면서도', '로맨스', '05', '11', '1', '톱스타', '그', '자체', '드라마', '05', '09', '17', '19', '첫사랑', '리벤지', 'BL', '05', '09', '0', '19', '개나리가', '떨어진', '길', 'BL', '05', '09', '3', '무명도', '무협', '액션', '무협', '05', '06', '2', '오', '단군', '판타지', '05', '05', '1', '허리케인', '공주님', '개그', '학원', '05', '05', '3', '19', '하렘을', '복수한다', '성인', '05', '05', '7', '과로환생전기', '액션', '무협', '05', '05', '1', '리커버리', '하프', '드라마', '판타지', '05', '05', '0', '뜻대로', '하세요', '판타지', '로맨스', '05', '04', '101', '미친', '악당의', '품으로', '떨어졌다', '판타지', '로맨스', '05', '04', '3', '19', '이력서', '성인', '판타지', '04', '29', '63', '19', '이웃집', '떡', 'BL',
 '04', '28', '11', '황금 의', '세계를', '너에게', '판타지', '04', '28', '1', '19', '서리가', '나리는', '바다', 'BL', '04', '28', '0', '하자인간', '스릴러', '공포', '04', '28', '0', '19', '꿀', '떨어지는', '알바', '성인', '04', '28', '4', '죽고', '싶습니다', '드라마', '04', '28', '0', '자존감', '없는', '소선화양', '로맨스', '학원', '04', '28', '2', '실버', '트리', '로맨스', '04', '27', '0', '골 렘', '잡고', '흙수저', '탈출', '드라마', '판타지', '액션', '04', '27', '65', '사라진', '신데렐라', '로맨스', '04', '27', '2', '시한부', '엑스트라의', '시간', '드라마', '판타지', '로맨스', '순정', '04', '27', '32', '어떤', '계모님의', '메르헨', '드라마', '판타지', '로맨스', '순정', '04', '26', '181', '날', '차버린', '소꿉친구와', '전', '여친이', '같은', '반이라', '곤란하다', '로맨스', '04', '23', '1', '사랑받는', '시집살이', '판타지', '로맨스', '04', '21', '7', '19', '마귀', 'BL', 'BL', '04', '21', '2', '19', '오메가', '애첩에', '빙의했다', '완전판', 'BL', '04', '21', '4', '19', '우리', '집에는', '쥐가', '있다', '로맨스', '04', '20', '4', '대공가의', '여우', '황녀님', '판타지', '로맨스', '04', '20', '7', '대자객교', '액션', '무협', '04', '20', '2', '19', '찐', '성인', '04', '14', '17', '19', '홈', 'HOME', 'BL', '04', '14', '4', '홍', '의관의', '은밀한', '비밀', '드라마', '로맨스', '04', '13', '2', '19', '해수면의', ' 아르페지오', 'BL', '04', '13', '11', '그', '감금물', '주인공', '내가', '하겠다', '판타지', '로맨스', '04', '13', '2', '문샤크', '상어가', '스타성을', '타고남', '로맨스', '순정', '04', '07', '0', '서브남', '아빠를', '지키는', '법', '로맨스', '04', '06', '3', '집', '잘못', '찾아오셨어요', '악역님', '판타지', '로맨스', '04', '06', '4', '언니는', '여동생을', '바르게', '키워야', '합니다', '판타지', '로맨스', '04', '06', '4', '악역의', '성좌인데', '돈이', '없어', 'BL', '03', '31', '4', '대체', '언제부터', '흑막이셨어요', '판타지', '로맨스', '03', '30', '1', '입양딸은', '세상을', '구원하고', '싶습니다', '판타지', '로맨스', '03', '30', '4', '데뷔', '못', '하면', '죽는', '병', '걸림', '드라마', '03', '30', '26', '19', '파트타임', '파트너', 'BL', '03', '27', '6', 'L', 'A', 'G', '판타지', '학원', '03', '24', '32', '빌런의', '정의', '로맨스', '03', '24', '6', '19', '가벼운', 'XX씨', 'BL', '03', '23', '2', '19', '애욕', 'BL', '03', '19', '17', '19', '전국구', '드라마', '액션', '03', '18', '8', '오빠', '베프와', '데이트하기', '로맨스', '03', '17', '3', '19', '눈', '떠보니', '침대', 'BL', '03', '10', '2', '19', ' 데블', '온', '탑', 'BL', '03', '10', '4', '19', '폭신말랑', '러브하우스', 'BL', '03', '02', '11', '제로', '데이', '어택', 'BL', '02', '25', '4', '19', '맨해튼의', '우울', 'BL', '02', '25', '3', '엑스트라가', '너무', '강함', '판타지', '액션', '02', '24', '18', '죽음을', '희망합니다', '판타지', '로맨스', '02', '17', '5', '악녀는', '아무나', '하나', '드라마', '판타지', '로맨스', '02', '17', '46', '신의', '재래', '판타지', '02', '17', '1', '조연으로', '태어났지만', '막장드라마에', '봉사하지', '않겠다', '로맨스', '02', '11', '0', '19', '나쁜남자', '탑툰', '성인', '드라마', '02', '08', '13', '19', '어린', '가정부', '성인', '02', '06', '10', '철혈의', '네크로맨서가', '귀환했다', '판타지', '02', '04', '7', '휴재', '자매전쟁', '드라마', '11', '19', '3', 'Copyright', 'FUNBE', 'All', 'rights', 'reserved']

 
 2. text추출 + 태그 속 content 값 추출 (밑에 복사해온건 1번에서 추가된 부분) _ 1번에는 없는 '무료웹툰','웹툰미리보기' 등 불법웹툰을 추측할 수 있는 키워드 포함
['width', 'device', 'width', 'initial', 'scale', '1', '7d9aa4a36c75f4880d7e6ef04ec95170', '웹툰', '펀비', 'Funbe', '펀비', 'Funbe', '펀비', 'Funbe', '펀비', 'Funbe',
 '는', '네이버웹툰', '다음웹툰', '카카오웹툰', '레진코믹스', '짬툰', '투믹스', '탑툰', '만화책', '미리보기', '및', '다시보기를', '제공합니다', '펀비', 'Funbe', '네이버웹툰',
'다음웹툰', '카카오웹툰', '레진웹툰', '웹툰미리보기', '유료만화', '무료만화', '망가', '만화미리보기', '레진코믹스', '무료웹툰', '유료 웹툰', 'index', 'follow', '웹툰', '펀비',
'Funbe', '펀비', 'Funbe', '펀비', 'Funbe', 'https', 'funbe384', 'com', 'EC', '9B', 'B9', 'ED', '88', 'B0']
'''

'''
링크모음 : 블랙툰
1. text만
['블랙넷', '현재', '페이지를', '즐겨찾기에', '추가하시면', '항상', '블랙툰', '실시간', '도메인', '주소를', '확인', '하실', '수', '있습니다', '블랙툰', 'BlackToon', '가장', '많은', '무료웹툰을', '보유하고', '있으며', '빠른', '업데이트와', '편의성으로', '네이버웹툰', '다음웹툰', '카카오웹툰', '레진코믹스', '웹툰', '서비스', '제공', '바로가기', '블랙툰', '트위터', '블랙툰', '트위터에서', '실시간', '도메인', '주소를', '확인', '하실수', '있습니다',
 '바로가기', '네이버웹툰', '매일매일', '새로운', '재미', '네이버', '웹툰', '바로가기', '카카오페이지', '오리지널', '독점', '웹툰', '웹소설', '부터', '드라마', '예능', '책', '까지', '한', '곳에서', '즐기세요', '인기', '콘텐츠가', '기다리면', '무료', '바로가기', 'Copyright', '블랙넷', 'by', 'BlackToon', 'net']

2. content 포함
['블랙넷', '현재', '페이지를', '즐겨찾기에', '추가하시면', '항상', '블랙툰', '실시간', '도메인', '주소를', '확인', '하실', '수', '있습니다', '블랙툰', 'BlackToon', '가장', '많은', '무료웹툰을', '보유하고', '있으며', '빠른', '업데이트와', '편의성으로', '네이버웹툰', '다음웹툰', '카카오웹툰', '레진코믹스', '웹툰', '서비스', '제공', '바로가기', '블랙툰', '트위터', '블랙툰', '트위터에서', '실시간', '도메인', '주소를', '확인', '하실수', '있습니
다', '바로가기', '네이버웹툰', '매일매일', '새로운', '재미', '네이버', '웹툰', '바로가기', '카카오페이지', '오리지널', '독점', '웹툰', '웹소설', '부터', '드라마', '예능', '책', '까지', '한', '곳에서', '즐기세요', '인기', '콘텐츠가', '기다리면', '무료', '바로가기', 'Copyright', '블랙넷', 'by', 'BlackToon', 'net', 
'블랙툰', '블랙넷', '블랙툰넷', '블랙툰', '주소', '웹툰', '무료웹툰', '웹툰', '미리보기', '네이버웹툰', '다음웹툰', '카카오웹툰', '레진웹툰', '블랙툰', '가장', '많은', '무료웹툰을', '보유하고', '있으며', '빠른', '업데이트와', '편의성으로', '네이버웹툰', '다음웹툰', '카카오웹툰', '레진코믹스', '웹툰', '서비스', '제공']

'''

'''
늑대툰 바로가기 링크 제공 사이트 https://wfwf328.com
1. text만 
['늑대닷컴', '주소', '안내', '늑대닷컴의', '주소가', 'https', 'wfwf329', 'com으로', '변경됐습니다', '늑대닷컴', '이동하기']

2. content도
['늑대닷컴', '주소', '안내', '늑대닷컴의', '주소가', 'https', 'wfwf329', 'com으로', '변경됐습니다', '늑대닷컴', '이동하기', '늑대닷컴', '웹툰', '주소', '늑대닷컴',
 '늑대닷컴', '늑대닷컴', '늑대닷컴의', '변경주소를', '실시간으로', '제공합니다', '늑대닷컴', '웹툰', '주소', '늑대닷컴', '늑대닷컴', '늑대닷컴의', '변경주소를', 
 '실시간으로', '제공합니다']
'''