# # Define your item pipelines here
# #
# # Don't forget to add your pipeline to the ITEM_PIPELINES setting
# # See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# # useful for handling different item types with a single interface
# from itemadapter import ItemAdapter

# # class DevidetutorialPipeline:
# #     def process_item(self, item, spider):
# #         return item

import sqlite3
import openai
from itemadapter import ItemAdapter
from scrapy.exceptions import NotConfigured
from .items import GetWordsItem


class SQLitePipeline:

    def open_spider(self, spider):
        self.connection = sqlite3.connect('word_counts.db')
        self.cursor = self.connection.cursor()

        # hosts 테이블에서 데이터를 가져와서 스파이더에 전달
        self.cursor.execute("SELECT host FROM hosts")
        rows = self.cursor.fetchall()
        spider.hosts = [row[0] for row in rows]
        if not spider.hosts:
            raise NotConfigured("No hosts found in the database")

    def close_spider(self, spider):
        self.connection.close()
    
    def get_top10_keywords(self, host):
        # 특정 호스트에 대해 빈도수가 가장 높은 상위 10개의 단어를 선택하여 반환
        query = """
        SELECT words FROM words_count 
        WHERE host = ? 
        ORDER BY count DESC 
        LIMIT 10
        """
        self.cursor.execute(query, (host,))
        top_10_keywords = self.cursor.fetchall()
        return top_10_keywords

    def classify_site(self, model, top_10_keywords):
        keywords_sentence = ", ".join([keyword[0] for keyword in top_10_keywords])
        question = f"웹사이트의 top 10 키워드입니다: {keywords_sentence}. 웹사이트가 정상인지 악성인지 판단해주세요. 둘 중에 답해줘. 부연설명은 필요없어."
        
        response = openai.ChatCompletion.create(
            model=model,
            messages=[
                {"role": "user", "content": question}
            ]
        )
        classification = response.choices[0].message['content'].strip()
        #print("gpt 답변 :", classification)
        
        if "정상" in classification:    
            return "정상"
        elif "악성" in classification:  
            return "악성"
        else:   
            return classification

    
    def process_item(self, item, spider):
        host = item.get('host')
        top_words = self.get_top10_keywords(host)
        if top_words:
            classification = self.classify_site("gpt-3.5-turbo", top_words)
            item['classification'] = classification

            # Update the classification in the database
            self.cursor.execute("UPDATE hosts SET classification = ? WHERE host = ?", (classification, host))
            self.connection.commit()
        else:
            spider.logger.warning(f"No top words found for host: {host}")
        return item


