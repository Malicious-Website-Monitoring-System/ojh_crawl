# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
#import sqlite3
import mysql.connector

class TutorialPipeline(object):
    #tutorial 16
    def __init__(self):
        self.create_connection()
        self.create_table()
    

    def create_connection(self):
        #self.conn=sqlite3.connect("myquotes.db")
        self.conn=mysql.connector.connect( #tutorial 17
            host='localhost',
            user='root',
            passwd='1478',
            database='myquotes' # 워크벤치에서 생성한 스키마 이름
        )
        self.curr=self.conn.cursor()

    def create_table(self):
        self.curr.execute("""DROP TABLE IF EXISTS quotes_tb""")
        self.curr.execute("""CREATE TABLE quotes_tb(
                          title text,
                          author text,
                          tag text
        )""")

    def process_item(self, item, spider):
        self.store_db(item)
        return item
    
    def store_db(self,item):
        #self.curr.execute("""INSERT INTO quotes_tb values(?,?,?)""",(        #sqlite3 - ?
        self.curr.execute("""INSERT INTO quotes_tb values(%s,%s,%s)""",(      #mysql - %s
            item['title'][0],
            item['author'][0],
            item['tag'][0]
        ))
        self.conn.commit()

# 데이터를 JSON파일이나 SQL파일, SQL데이터베이스 등에 저장할 수 있도록 어딘가에 저장하려고 함.
# 이는 파이프라인을 통해 수행됨
# Scraped data -> Item Containers -> Json/csv files
# Scraped data -> Item Containers -> Pipeline -> SQL/Mongo database

'''
# tutorail 19 mongodb
import pymongo

class TutorialPipeline(object):
    def __init__(self): #초기화 함수
        self.conn=pymongo.MongoClient( # 연결 변수 생성
            'localhost',
            27017   # 원하는 포트번호
        )
        
        db=self.conn['myquotes'] #데이터베이스 생성
        self.collection = db['quotes_tb'] #테이블 생성
    
    def process_item(self, item, spider):
        self.collection.insert(dict(item))
        return item

#https://www.youtube.com/watch?v=djfnjtYB2co&list=PLhTjy8cBISEqkN-5Ku_kXG4QW33sxQo0t&index=18
    
'''