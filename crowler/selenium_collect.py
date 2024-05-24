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

