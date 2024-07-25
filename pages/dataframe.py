import pandas as pd
import streamlit as st
import pymysql
import pymysql.cursors
import numpy as np
import pydeck as pdk
from streamlit_echarts import st_echarts
from PIL import Image 

#사이드바에 지역선택
add_selectbox = st.sidebar.selectbox(
    "지역을 선택?", (
        '합계'
        ,'서울'
        ,'부산'
        ,'대구'
        ,'인천'
        ,'광주'
        ,'대전'
        ,'울산'
        ,'세종'
        ,'경기'
        ,'강원'
        ,'충북'
        ,'충남'
        ,'전북'
        ,'전남'
        ,'경북'
        ,'경남'
        ,'제주')
)

#sql 커넥션
con= pymysql.connect(
    host='192.168.0.34',
    user='manager',
    password='1234',
    database='car_faq',
    charset='utf8'
)

conn = st.connection("mydb", type="sql", autocommit=True)
# df = conn.query("show databases", ttl=3600)

if add_selectbox=="합계" :
    st.header(f"{add_selectbox} 연도별 자동차 등록 현황 🚘 " )
    st.text(f"💚: {add_selectbox}  💙:전국 ")
    sql="""
        select 
            *
        from city
        where 1=1
        ;
    """
    df=conn.query(sql,ttl=3600)
    # st.dataframe(df)

    # st.text([  f for f in df.values[1][1:]])
    # total_data = [f for f in df.values[0][1:]]
    total_data = [1940,2012,2099,2180,2253,2320,2368,2437,2491,2550]

    option = {
        "xAxis": {
            "type": "category",
            "data": [f for f in df.columns[1:]],
        },
        "yAxis": {"type": "value"},
        "series": [
            {"data": [f for f in df.values[1][1:]], "type": "line"},
            {"data": [f for f in df.values[2][1:]], "type": "line"},
            {"data": [f for f in df.values[3][1:]], "type": "line"},
            {"data": [f for f in df.values[4][1:]], "type": "line"},
            {"data": [f for f in df.values[5][1:]], "type": "line"},
            {"data": [f for f in df.values[6][1:]], "type": "line"},
            {"data": [f for f in df.values[7][1:]], "type": "line"},
            {"data": [f for f in df.values[8][1:]], "type": "line"},
            {"data": [f for f in df.values[9][1:]], "type": "line"},
            {"data": [f for f in df.values[10][1:]], "type": "line"},
            {"data": [f for f in df.values[11][1:]], "type": "line"},
            {"data": [f for f in df.values[12][1:]], "type": "line"},
            {"data": [f for f in df.values[13][1:]], "type": "line"},
            {"data": [f for f in df.values[14][1:]], "type": "line"},
            {"data": [f for f in df.values[15][1:]], "type": "line"},
            {"data": [f for f in df.values[16][1:]], "type": "line"}


                    ],
    }
    st_echarts(options=option, height="400px",)
    st.page_link("./home.py", label="Home", icon="🏠")

if add_selectbox=="서울" :
    st.header(f"{add_selectbox} 연도별 자동차 등록 현황 🚘 " )
    st.text(f"💚: {add_selectbox}  💙:전국 ")
    sql="""
        select 
            *
        from city
        where 1=1
        and (region = '서울' or region='합계' or region='인천')
        ;
    """
    df=conn.query(sql,ttl=3600)
    # st.dataframe(df)

    # st.text([  f for f in df.values[1][1:]])
    # total_data = [f for f in df.values[0][1:]]
    total_data = [1940,2012,2099,2180,2253,2320,2368,2437,2491,2550]

    option = {
        "xAxis": {
            "type": "category",
            "data": [f for f in df.columns[1:]],
        },
        "yAxis": {"type": "value"},
        "series": [
            {"data": total_data, "type": "line"},
            {"data": [f for f in df.values[1][1:]], "type": "line"}
                    ],
    }
    st_echarts(options=option, height="400px",)
    st.page_link("./home.py", label="Home", icon="🏠")

if add_selectbox=="부산" :
    st.header(f"{add_selectbox} 연도별 자동차 등록 현황 🚘 " )
    st.text(f"💚: {add_selectbox}  💙:전국 ")
    sql="""
        select 
            *
        from city
        where 1=1
        and (region = '부산' or region='합계' )
        ;
    """
    df=conn.query(sql,ttl=3600)
    # st.dataframe(df)

    # st.text([  f for f in df.values[1][1:]])
    # total_data = [f for f in df.values[0][1:]]
    total_data = [1940,2012,2099,2180,2253,2320,2368,2437,2491,2550]

    option = {
        "xAxis": {
            "type": "category",
            "data": [f for f in df.columns[1:]],
        },
        "yAxis": {"type": "value"},
        "series": [
            {"data": total_data, "type": "line"},
            {"data": [f for f in df.values[1][1:]], "type": "line"}
                    ],
    }
    st_echarts(options=option, height="400px",)
    st.page_link("./home.py", label="Home", icon="🏠")

if add_selectbox=="대구" :
    st.header(f"{add_selectbox} 연도별 자동차 등록 현황 🚘 " )
    st.text(f"💚: {add_selectbox}  💙:전국 ")
    sql="""
        select 
            *
        from city
        where 1=1
        and (region = '부산' or region='합계' )
        ;
    """
    df=conn.query(sql,ttl=3600)
    # st.dataframe(df)

    # st.text([  f for f in df.values[1][1:]])
    # total_data = [f for f in df.values[0][1:]]
    total_data = [1940,2012,2099,2180,2253,2320,2368,2437,2491,2550]

    option = {
        "xAxis": {
            "type": "category",
            "data": [f for f in df.columns[1:]],
        },
        "yAxis": {"type": "value"},
        "series": [
            {"data": total_data, "type": "line"},
            {"data": [f for f in df.values[1][1:]], "type": "line"}
                    ],
    }
    st_echarts(options=option, height="400px",)
    st.page_link("./home.py", label="Home", icon="🏠")

if add_selectbox=="인천" :
    st.header(f"{add_selectbox} 연도별 자동차 등록 현황 🚘 " )
    st.text(f"💚: {add_selectbox}  💙:전국 ")
    sql="""
        select 
            *
        from city
        where 1=1
        and (region = '부산' or region='합계' )
        ;
    """
    df=conn.query(sql,ttl=3600)
    # st.dataframe(df)

    # st.text([  f for f in df.values[1][1:]])
    # total_data = [f for f in df.values[0][1:]]
    total_data = [1940,2012,2099,2180,2253,2320,2368,2437,2491,2550]

    option = {
        "xAxis": {
            "type": "category",
            "data": [f for f in df.columns[1:]],
        },
        "yAxis": {"type": "value"},
        "series": [
            {"data": total_data, "type": "line"},
            {"data": [f for f in df.values[1][1:]], "type": "line"}
                    ],
    }
    st_echarts(options=option, height="400px",)
    st.page_link("./home.py", label="Home", icon="🏠")

if add_selectbox=="광주" :
    st.header(f"{add_selectbox} 연도별 자동차 등록 현황 🚘 " )
    st.text(f"💚: {add_selectbox}  💙:전국 ")
    sql="""
        select 
            *
        from city
        where 1=1
        and (region = '부산' or region='합계' )
        ;
    """
    df=conn.query(sql,ttl=3600)
    # st.dataframe(df)

    # st.text([  f for f in df.values[1][1:]])
    # total_data = [f for f in df.values[0][1:]]
    total_data = [1940,2012,2099,2180,2253,2320,2368,2437,2491,2550]

    option = {
        "xAxis": {
            "type": "category",
            "data": [f for f in df.columns[1:]],
        },
        "yAxis": {"type": "value"},
        "series": [
            {"data": total_data, "type": "line"},
            {"data": [f for f in df.values[1][1:]], "type": "line"}
                    ],
    }
    st_echarts(options=option, height="400px",)
    st.page_link("./home.py", label="Home", icon="🏠")

if add_selectbox=="대전" :
    st.header(f"{add_selectbox} 연도별 자동차 등록 현황 🚘 " )
    st.text(f"💚: {add_selectbox}  💙:전국 ")
    sql="""
        select 
            *
        from city
        where 1=1
        and (region = '부산' or region='합계' )
        ;
    """
    df=conn.query(sql,ttl=3600)
    # st.dataframe(df)

    # st.text([  f for f in df.values[1][1:]])
    # total_data = [f for f in df.values[0][1:]]
    total_data = [1940,2012,2099,2180,2253,2320,2368,2437,2491,2550]

    option = {
        "xAxis": {
            "type": "category",
            "data": [f for f in df.columns[1:]],
        },
        "yAxis": {"type": "value"},
        "series": [
            {"data": total_data, "type": "line"},
            {"data": [f for f in df.values[1][1:]], "type": "line"}
                    ],
    }
    st_echarts(options=option, height="400px",)
    st.page_link("./home.py", label="Home", icon="🏠")

if add_selectbox=="울산" :
    st.header(f"{add_selectbox} 연도별 자동차 등록 현황 🚘 " )
    st.text(f"💚: {add_selectbox}  💙:전국 ")
    sql="""
        select 
            *
        from city
        where 1=1
        and (region = '부산' or region='합계' )
        ;
    """
    df=conn.query(sql,ttl=3600)
    # st.dataframe(df)

    # st.text([  f for f in df.values[1][1:]])
    # total_data = [f for f in df.values[0][1:]]
    total_data = [1940,2012,2099,2180,2253,2320,2368,2437,2491,2550]

    option = {
        "xAxis": {
            "type": "category",
            "data": [f for f in df.columns[1:]],
        },
        "yAxis": {"type": "value"},
        "series": [
            {"data": total_data, "type": "line"},
            {"data": [f for f in df.values[1][1:]], "type": "line"}
                    ],
    }
    st_echarts(options=option, height="400px",)
    st.page_link("./home.py", label="Home", icon="🏠")

if add_selectbox=="세종" :
    st.header(f"{add_selectbox} 연도별 자동차 등록 현황 🚘 " )
    st.text(f"💚: {add_selectbox}  💙:전국 ")
    sql="""
        select 
            *
        from city
        where 1=1
        and (region = '부산' or region='합계' )
        ;
    """
    df=conn.query(sql,ttl=3600)
    # st.dataframe(df)

    # st.text([  f for f in df.values[1][1:]])
    # total_data = [f for f in df.values[0][1:]]
    total_data = [1940,2012,2099,2180,2253,2320,2368,2437,2491,2550]

    option = {
        "xAxis": {
            "type": "category",
            "data": [f for f in df.columns[1:]],
        },
        "yAxis": {"type": "value"},
        "series": [
            {"data": total_data, "type": "line"},
            {"data": [f for f in df.values[1][1:]], "type": "line"}
                    ],
    }
    st_echarts(options=option, height="400px",)
    st.page_link("./home.py", label="Home", icon="🏠")

if add_selectbox=="경기" :
    st.header(f"{add_selectbox} 연도별 자동차 등록 현황 🚘 " )
    st.text(f"💚: {add_selectbox}  💙:전국 ")
    sql="""
        select 
            *
        from city
        where 1=1
        and (region = '부산' or region='합계' )
        ;
    """
    df=conn.query(sql,ttl=3600)
    # st.dataframe(df)

    # st.text([  f for f in df.values[1][1:]])
    # total_data = [f for f in df.values[0][1:]]
    total_data = [1940,2012,2099,2180,2253,2320,2368,2437,2491,2550]

    option = {
        "xAxis": {
            "type": "category",
            "data": [f for f in df.columns[1:]],
        },
        "yAxis": {"type": "value"},
        "series": [
            {"data": total_data, "type": "line"},
            {"data": [f for f in df.values[1][1:]], "type": "line"}
                    ],
    }
    st_echarts(options=option, height="400px",)
    st.page_link("./home.py", label="Home", icon="🏠")

if add_selectbox=="강원" :
    st.header(f"{add_selectbox} 연도별 자동차 등록 현황 🚘 " )
    st.text(f"💚: {add_selectbox}  💙:전국 ")
    sql="""
        select 
            *
        from city
        where 1=1
        and (region = '부산' or region='합계' )
        ;
    """
    df=conn.query(sql,ttl=3600)
    # st.dataframe(df)

    # st.text([  f for f in df.values[1][1:]])
    # total_data = [f for f in df.values[0][1:]]
    total_data = [1940,2012,2099,2180,2253,2320,2368,2437,2491,2550]

    option = {
        "xAxis": {
            "type": "category",
            "data": [f for f in df.columns[1:]],
        },
        "yAxis": {"type": "value"},
        "series": [
            {"data": total_data, "type": "line"},
            {"data": [f for f in df.values[1][1:]], "type": "line"}
                    ],
    }
    st_echarts(options=option, height="400px",)
    st.page_link("./home.py", label="Home", icon="🏠")

if add_selectbox=="충북" :
    st.header(f"{add_selectbox} 연도별 자동차 등록 현황 🚘 " )
    st.text(f"💚: {add_selectbox}  💙:전국 ")
    sql="""
        select 
            *
        from city
        where 1=1
        and (region = '부산' or region='합계' )
        ;
    """
    df=conn.query(sql,ttl=3600)
    # st.dataframe(df)

    # st.text([  f for f in df.values[1][1:]])
    # total_data = [f for f in df.values[0][1:]]
    total_data = [1940,2012,2099,2180,2253,2320,2368,2437,2491,2550]

    option = {
        "xAxis": {
            "type": "category",
            "data": [f for f in df.columns[1:]],
        },
        "yAxis": {"type": "value"},
        "series": [
            {"data": total_data, "type": "line"},
            {"data": [f for f in df.values[1][1:]], "type": "line"}
                    ],
    }
    st_echarts(options=option, height="400px",)
    st.page_link("./home.py", label="Home", icon="🏠")

if add_selectbox=="전북" :
    st.header(f"{add_selectbox} 연도별 자동차 등록 현황 🚘 " )
    st.text(f"💚: {add_selectbox}  💙:전국 ")
    sql="""
        select 
            *
        from city
        where 1=1
        and (region = '부산' or region='합계' )
        ;
    """
    df=conn.query(sql,ttl=3600)
    # st.dataframe(df)

    # st.text([  f for f in df.values[1][1:]])
    # total_data = [f for f in df.values[0][1:]]
    total_data = [1940,2012,2099,2180,2253,2320,2368,2437,2491,2550]

    option = {
        "xAxis": {
            "type": "category",
            "data": [f for f in df.columns[1:]],
        },
        "yAxis": {"type": "value"},
        "series": [
            {"data": total_data, "type": "line"},
            {"data": [f for f in df.values[1][1:]], "type": "line"}
                    ],
    }
    st_echarts(options=option, height="400px",)
    st.page_link("./home.py", label="Home", icon="🏠")

if add_selectbox=="전남" :
    st.header(f"{add_selectbox} 연도별 자동차 등록 현황 🚘 " )
    st.text(f"💚: {add_selectbox}  💙:전국 ")
    sql="""
        select 
            *
        from city
        where 1=1
        and (region = '부산' or region='합계' )
        ;
    """
    df=conn.query(sql,ttl=3600)
    # st.dataframe(df)

    # st.text([  f for f in df.values[1][1:]])
    # total_data = [f for f in df.values[0][1:]]
    total_data = [1940,2012,2099,2180,2253,2320,2368,2437,2491,2550]

    option = {
        "xAxis": {
            "type": "category",
            "data": [f for f in df.columns[1:]],
        },
        "yAxis": {"type": "value"},
        "series": [
            {"data": total_data, "type": "line"},
            {"data": [f for f in df.values[1][1:]], "type": "line"}
                    ],
    }
    st_echarts(options=option, height="400px",)
    st.page_link("./home.py", label="Home", icon="🏠")

if add_selectbox=="경북" :
    st.header(f"{add_selectbox} 연도별 자동차 등록 현황 🚘 " )
    st.text(f"💚: {add_selectbox}  💙:전국 ")
    sql="""
        select 
            *
        from city
        where 1=1
        and (region = '부산' or region='합계' )
        ;
    """
    df=conn.query(sql,ttl=3600)
    # st.dataframe(df)

    # st.text([  f for f in df.values[1][1:]])
    # total_data = [f for f in df.values[0][1:]]
    total_data = [1940,2012,2099,2180,2253,2320,2368,2437,2491,2550]

    option = {
        "xAxis": {
            "type": "category",
            "data": [f for f in df.columns[1:]],
        },
        "yAxis": {"type": "value"},
        "series": [
            {"data": total_data, "type": "line"},
            {"data": [f for f in df.values[1][1:]], "type": "line"}
                    ],
    }
    st_echarts(options=option, height="400px",)
    st.page_link("./home.py", label="Home", icon="🏠")

if add_selectbox=="경남" :
    st.header(f"{add_selectbox} 연도별 자동차 등록 현황 🚘 " )
    st.text(f"💚: {add_selectbox}  💙:전국 ")
    sql="""
        select 
            *
        from city
        where 1=1
        and (region = '부산' or region='합계' )
        ;
    """
    df=conn.query(sql,ttl=3600)
    # st.dataframe(df)

    # st.text([  f for f in df.values[1][1:]])
    # total_data = [f for f in df.values[0][1:]]
    total_data = [1940,2012,2099,2180,2253,2320,2368,2437,2491,2550]

    option = {
        "xAxis": {
            "type": "category",
            "data": [f for f in df.columns[1:]],
        },
        "yAxis": {"type": "value"},
        "series": [
            {"data": total_data, "type": "line"},
            {"data": [f for f in df.values[1][1:]], "type": "line"}
                    ],
    }
    st_echarts(options=option, height="400px",)
    st.page_link("./home.py", label="Home", icon="🏠")

if add_selectbox=="제주" :
    st.header(f"{add_selectbox} 연도별 자동차 등록 현황 🚘 " )
    st.text(f"💚: {add_selectbox}  💙:전국 ")
    sql="""
        select 
            *
        from city
        where 1=1
        and (region = '부산' or region='합계' )
        ;
    """
    df=conn.query(sql,ttl=3600)
    # st.dataframe(df)

    # st.text([  f for f in df.values[1][1:]])
    # total_data = [f for f in df.values[0][1:]]
    total_data = [1940,2012,2099,2180,2253,2320,2368,2437,2491,2550]

    option = {
        "xAxis": {
            "type": "category",
            "data": [f for f in df.columns[1:]],
        },
        "yAxis": {"type": "value"},
        "series": [
            {"data": total_data, "type": "line"},
            {"data": [f for f in df.values[1][1:]], "type": "line"}
                    ],
    }
    st_echarts(options=option, height="400px",)
    st.page_link("./home.py", label="Home", icon="🏠")






