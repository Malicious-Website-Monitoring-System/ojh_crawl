from selenium_collect import extract_links 
from keywords import collect_keywords
from compare import classify_url
import queue
import pandas as pd
import compare
from collections import Counter

# 시작 URL 설정
start_url ='https://zzang4.com/'#'https://blacktoon301.com/'#'https://www.rs9best.net/'#'https://wtwt256.com/'#'https://funbe382.com/%EC%9B%B9%ED%88%B0/%EC%97%B4%ED%9D%98'#웹툰      ;'https://baro.bet/sports/prematch?referral=7771' 'https://www.rs9best.net/' 'https://bp-114.com/'  'https://www.v210x10q.com/?btag=1642355'#도박

# 데이터 담을 리스트
collected_urls = []
collected_starturl=[]
collected_keywords=[]
classify=[]

url_queue = queue.Queue(maxsize=5)

# 시작 링크, 내부 링크 담기
extract_links(start_url, url_queue, collected_starturl, collected_urls)

# URL 리스트를 순회하며 키워드를 가져와 저장
for url in collected_urls:
    keyword_counter=collect_keywords(url)
    collected_keywords.append(keyword_counter)


# 키워드 기반 악성,정상으로 분류
malicious_keywords_webtoon = ['무료웹툰','보증토토','토토보증업체','레진','레진코믹스','네이버웹툰','다음웹툰','카카오웹툰'] 
malicious_keywords_gambling = ['베팅', '배팅','베팅하기', '카지노', '슬롯', '입금', '리그','중계중','스포츠','스포츠중계','토너먼트','고스톱','포커','섯다','맞고','룰렛']

webtoon = Counter({word: 1 for word in malicious_keywords_webtoon})
gambling = Counter({word: 1 for word in malicious_keywords_gambling})

for counter in collected_keywords:
    result=classify_url(counter,webtoon,gambling) 
    classify.append(result)


# 수집된 데이터를 데이터프레임으로 변환
df = pd.DataFrame(data=list(zip(collected_starturl, collected_urls, collected_keywords,classify)), columns=["start", "inner_url", "keywords","malicious"])

# 최종 데이터프레임 출력
print("<--------------------- End --------------------->")
print("Collected URLs DataFrame:")
print(df)

df.to_csv('C:/maliciousweb/df_ex02.csv', index=False, encoding='utf-8-sig') #utf-8도 한글깨짐..

# 출력
# Collected URLs DataFrame:
#                                  start  ... malicious
# 0                  https://zzang4.com/  ...      무료웹툰
# 1                  https://zzang4.com/  ...        정상
# 2                  https://zzang4.com/  ...        정상
# 3                  https://zzang4.com/  ...        정상
# 4                  https://zzang4.com/  ...        도박
# ..                                 ...  ...       ...
# 98   https://xn--9y2bo6lgtg81a81t.com/  ...      무료웹툰
# 99              https://t.me/linkzzang  ...        정상
# 100             https://t.me/linkzzang  ...        정상
# 101             https://t.me/linkzzang  ...        정상
# 102             https://t.me/linkzzang  ...        정상