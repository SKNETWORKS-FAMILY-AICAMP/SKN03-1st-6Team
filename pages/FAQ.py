import streamlit as st
import pandas as pd


# CSS를 사용하여 테이블 스타일 지정
st.markdown("""
<style>
    .dataframe td {
        white-space: normal;
        word-wrap: break-word;
        max-width: 500px;
    }
    .dataframe {
        width: 100%;
    }
</style>
""", unsafe_allow_html=True)

conn = st.connection('mydb', type="sql", autocommit=True)

# Using object notation
add_selectbox = st.sidebar.selectbox(
    "어떤 기업?", ("현대 자동차", "기아 자동차")
)


st.title(f'🌐{add_selectbox} FAQ')

left, middle = st.columns(2, vertical_alignment="bottom")
search_term = st.text_input('검색어를 입력하세요:', '')


category_tap = ''


def hyundai_faq():
    global category_tap
    
    tab_names = ['전체', '차량구매', '홈페이지', '블루멤버스', '모젠서비스', '블루링크', '빌트인캠', '현대 디지털 키', '기타']
    selected_tab = st.radio("카테고리 선택:", tab_names)
    
    if selected_tab == '전체':
        category_tap = ''
    elif selected_tab in ['차량구매', '홈페이지', '블루멤버스', '모젠서비스', '블루링크', '빌트인캠', '현대 디지털 키', '기타']:
        category_tap = selected_tab

    if category_tap == '':
        st.header("전체")
    else:
        st.header(category_tap)

    if search_term:
        if category_tap != '':
            query = f"SELECT category, question, answer FROM hyundai_faq WHERE 1 = 1 and question LIKE '%{search_term}%' and category Like '{category_tap}' "
        else:
            query = f"SELECT category, question, answer FROM hyundai_faq WHERE 1 = 1 and question LIKE '%{search_term}%'"
        
        results = conn.query(query)  \
        
        if results is not None and len(results) > 0:
            st.write("검색 결과:")
            df = pd.DataFrame(results, columns=['category', 'question', 'answer'])
            st.write(df.to_html(index=False, escape=False), unsafe_allow_html=True)
        else:
            st.warning('검색 결과가 없습니다.')
    else:
        if category_tap != '':
            query = f"SELECT category, question, answer FROM hyundai_faq WHERE 1 = 1 and question LIKE '%{search_term}%' and category Like '{category_tap}' "
        else:
            query = f"SELECT category, question, answer FROM hyundai_faq WHERE 1 = 1 and question LIKE '%{search_term}%' limit 10"
        
        results = conn.query(query)  
        

        if results is not None and len(results) > 0:
            st.write("검색 결과:")
            df = pd.DataFrame(results, columns=['category', 'question', 'answer'])
            st.write(df.to_html(index=False, escape=False), unsafe_allow_html=True)
        else:
            st.warning('검색 결과가 없습니다.')


def kia_faq():
    
    if search_term:
        query = f"SELECT question, answer FROM kia_faq WHERE 1 = 1 and question LIKE '%{search_term}%'"
        results = conn.query(query)  \
        
        if results is not None and len(results) > 0:
            st.write("검색 결과:")
            df = pd.DataFrame(results, columns=['question', 'answer'])
            st.write(df.to_html(index=False, escape=False), unsafe_allow_html=True)
        else:
            st.warning('검색 결과가 없습니다.')
    else:
        query = f"SELECT  question, answer FROM kia_faq WHERE 1 = 1 and question LIKE '%{search_term}%'"
        results = conn.query(query)  

        if results is not None and len(results) > 0:
            st.write("검색 결과:")
            df = pd.DataFrame(results, columns=['question', 'answer'])
            st.write(df.to_html(index=False, escape=False), unsafe_allow_html=True)
        else:
            st.warning('검색 결과가 없습니다.')

if add_selectbox == "현대 자동차":
    hyundai_faq()
elif add_selectbox == '기아 자동차':
    kia_faq()



