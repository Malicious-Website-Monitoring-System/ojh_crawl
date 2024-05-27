from selenium import webdriver
from selenium.webdriver.common.by import By
import queue
from urllib.parse import urlparse
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#whitelist=['www.coupang.com','www.11st.co.kr','www.gmarket.co.kr','www.auction.co.kr','www.lotteon.com',...] # 적용시키기?

def extract_links(start_url, url_queue, collected_starturl, collected_urls) : #, collected_keywords):
    try:
        # Setup Selenium WebDriver
        
        driver = webdriver.Chrome()
        driver.get(start_url)
       

        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.TAG_NAME, 'html')))
        
        html = driver.page_source
        #collected_keywords.append(keyword(html))

        # Extract links using Selenium
        links = driver.find_elements(By.TAG_NAME, 'a')
        for link in links:
            href = link.get_attribute('href')
            if href and href.startswith('http') and urlparse(href).netloc != urlparse(start_url).netloc : #and urlparse(href).netloc != whitelist:
                collected_starturl.append(start_url)
                collected_urls.append(href)
    
                url_queue.put_nowait(href)

        # Close the driver
        driver.quit()
        
        while not url_queue.empty() and not url_queue.full():
            next_url = url_queue.get()
            extract_links(next_url, url_queue, collected_starturl, collected_urls)#, collected_keywords)

    except Exception as e:
        print("Error processing URL:", start_url, "Error:", e)

    print("Processing complete for:", start_url)


# is_dynamic_content 체크:

# is_dynamic 변수를 통해 페이지가 동적인지 확인.
# 자바스크립트 태그가 많은 페이지는 동적 콘텐츠로 간주.
# BeautifulSoup과 Selenium 병행 사용:

# 페이지가 동적 콘텐츠를 포함한다고 판단되면 Selenium을 사용하여 페이지를 로드.
# 그렇지 않은 경우 BeautifulSoup을 사용하여 페이지를 로드.
# 이 방식으로, 동적 콘텐츠가 필요하지 않은 페이지는 BeautifulSoup을 사용하여 더 빠르게 처리하고
# 동적 콘텐츠가 필요한 페이지만 Selenium을 사용하여 처리함으로써 전체 크롤링 작업의 효율성을 높일 수 있습니다.