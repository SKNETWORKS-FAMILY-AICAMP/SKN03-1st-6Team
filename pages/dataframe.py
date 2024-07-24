import random
import pandas as pd
import streamlit as st
import pymysql
import pymysql.cursors
import numpy as np
import pydeck as pdk
from streamlit_echarts import st_echarts


con= pymysql.connect(
    host='192.168.0.34',
    user='manager',
    password='1234',
    database='car_faq',
    charset='utf8'
)

conn = st.connection("mydb", type="sql", autocommit=True)
# df = conn.query("show databases", ttl=3600)

sql="""
    select 
        *
    from city
    where 1=1
    and (region = '인천' or region='합계')
    ;
"""
df=conn.query(sql,ttl=3600)
st.dataframe(df)

st.text([  f for f in df.values[0][1:]])

options1 = {
    "title": {"text": "자동차 등록현황"},
    "tooltip": {"trigger": "axis"},
    "legend": {"data": ["지역", "전체", "视频广告", "直接访问", "搜索引擎"]},
    "grid": {"left": "3%", "right": "4%", "bottom": "3%", "containLabel": True},
    "toolbox": {"feature": {"saveAsImage": {}}},
    "xAxis": {
        "type": "category",
        "boundaryGap": False,
        "data": [  f for f in df.columns[1:]],
    },
    "yAxis": {"type": "value"},
    "series": [
        {
            "name": "지역",
            "type": "line",
            "stack": "总量",
            "data": [2000,2000,2000,2000,], #  f for f in df.values[1][1:]
        },
        {
            "name": "전체",
            "type": "line",
            "stack": "总量",
            "data": [ f for f in df.values[0][1:] ],
        },
    ],
}


st_echarts(options=options1, height="400px")














# st.title('Dataframe')
# st.dataframe(
#     df,
#     column_config={
#         "name": "App name",
#         "stars": st.column_config.NumberColumn(
#             "Github Stars",
#             help="Number of stars on GitHub",
#             format="%d ⭐",
#         ),
#         "url": st.column_config.LinkColumn("App URL"),
#         "views_history": st.column_config.LineChartColumn(
#             "Views (past 30 days)", y_min=0, y_max=5000
#         ),
#     },
#     hide_index=True,
# )