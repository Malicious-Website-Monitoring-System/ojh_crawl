#tutorial 15
import sqlite3

conn=sqlite3.connect('myquotes.db') # DB와 연결
curr=conn.cursor() #  Connection 객체로부터 cursor() 함수를 호출하여 Cursor 객체를 호출

curr.execute("""create table quotes_db(
            title text,
            author text,
            tag text        
)""")

# Cursor 객체의 execute() 함수를 사용하여 SQL 문장을 DB 서버에 전송

curr.execute("""insert into quoes_db values ('Python is awesome!','buildwithpython','python')""")

conn.commit()
#commit 명령어는 모든 작업을 정상적으로 처리하겠다고 하는 명령어이다.
#쿼리문의 내용을 DB에 반영하기 위해, 처리된 내용을 모두 영구 저장한다.
#. 삽입, 갱신, 삭제 등의 DML(Data Manipulation Language) 문장을 실행하는 경우, INSERT/UPDATE/DELETE 후
#Connection 객체의 commit() 함수를 사용하여 data를 확정

conn.close() 
# DB 연결을 닫음
