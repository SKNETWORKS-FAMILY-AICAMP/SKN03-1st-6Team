import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk
from streamlit_echarts import st_echarts
from PIL import Image 

# Using object notation
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

# Using "with" notation
with st.sidebar:
    add_radio = st.radio(
        "Graph Type  ", ("Line chart", "Bar graph")
    )


options1 = {
    "title": {"text": "자동차 등록현황"},
    "tooltip": {"trigger": "axis"},
    "legend": {"data": ["지역", "전체 합계", "视频广告", "直接访问", "搜索引擎"]},
    "grid": {"left": "3%", "right": "4%", "bottom": "3%", "containLabel": True},
    "toolbox": {"feature": {"saveAsImage": {}}},
    "xAxis": {
        "type": "category",
        "boundaryGap": False,
        "data": ["2015", "2016", "2017", "2018", "2019", "2020", "2021","2022","2023","2024"],
    },
    "yAxis": {"type": "value"},
    "series": [
        {
            "name": "지역",
            "type": "line",
            "stack": "总量",
            "data": [120, 132, 101, 134, 90, 230, 210,232],
        },
        {
            "name": "전체",
            "type": "line",
            "stack": "总量",
            "data": [220, 182, 191, 234, 290, 330, 310],
        },
        {
            "name": "어쩌구",
            "type": "line",
            "stack": "总量",
            "data": [150, 232, 201, 154, 190, 330, 410],
        },
        {
            "name": "기아",
            "type": "line",
            "stack": "总量",
            "data": [320, 332, 301, 334, 390, 330, 320],
        },
        {
            "name": "현대",
            "type": "line",
            "stack": "总量",
            "data": [820, 932, 901, 934, 1290, 1330, 1320],
        },
    ],
}

options2 = {
    "title": {"text": "인천광역시 자동차 등록현황"},
    "tooltip": {"trigger": "axis"},
    "legend": {"data": ["현대", "기아", "视频广告", "直接访问", "搜索引擎"]},
    "grid": {"left": "3%", "right": "4%", "bottom": "3%", "containLabel": True},
    "toolbox": {"feature": {"saveAsImage": {}}},
    "xAxis": {
        "type": "category",
        "boundaryGap": False,
        "data": ["2015", "2016", "2017", "2018", "2019", "2020", "2021","2022","2023","2024"],
    },
    "yAxis": {"type": "value"},
    "series": [
        {
            "name": "자동차",
            "type": "line",
            "stack": "总量",
            "data": [120, 132, 101, 134, 90, 230, 210,232],
        },
        {
            "name": "저쩌구",
            "type": "line",
            "stack": "总量",
            "data": [220, 182, 191, 234, 290, 330, 310],
        },
        {
            "name": "어쩌구",
            "type": "line",
            "stack": "总量",
            "data": [150, 232, 201, 154, 190, 330, 410],
        },
        {
            "name": "기아",
            "type": "line",
            "stack": "总量",
            "data": [320, 332, 301, 334, 390, 330, 320],
        },
        {
            "name": "현대",
            "type": "line",
            "stack": "总量",
            "data": [820, 932, 901, 934, 1290, 1330, 1320],
        },
    ],
}


if add_selectbox=="서울" and add_radio=="Line chart":
    st.subheader("selectbox")
    st.header(add_selectbox)
    st_echarts(options=options1, height="400px")


if add_selectbox=="인천" and add_radio=="Line chart":
    st.subheader("radio")
    st.header(add_radio)
    st_echarts(options=options2, height="400px")


# st_echarts(options=options, height="400px")

