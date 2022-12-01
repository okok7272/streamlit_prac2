import streamlit as st
import pandas as pd
import numpy as np
import re
import datetime
import pymysql
from sqlalchemy import create_engine
# 웹 대시보드 개발 라이브러리인 스트림릿은,
# main 함수가 있어야 한다.
def db_to_df(table):
    con = pymysql.connect(host='localhost',
                        port=3306,
                        user='root',
                        password='0000',
                        db='project2',
                        charset='utf8')

    engine = create_engine('mysql+pymysql://root:0000@localhost/project2')
    conn =engine.connect()
    data = pd.read_sql_table(table,conn)
    con.commit()
    con.close()
    return data

#데이터 보는 버튼 만들고 거기에 입력 가능하게 하자


#중요 요소 고르고 project를 선택

#table 지정하고

#dataframe 형태로 데이터를 받고 해당 데이터를 정렬 가능한 표로 출력




def main() :
    st.title('안녕하세요. 웹 대시보드 프로젝트')
    st.title('Hello')
    st.table(db_to_df('context'))

if __name__ == '__main__' :
    main()
