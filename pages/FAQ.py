import streamlit as st
url_hyudai='https://www.hyundai.com/static/images/hyu_logo_og_image.jpg'
url_kia="https://res.heraldm.com/phpwas/restmb_idxmake.php?idx=68&simg=%2Fcontent%2Fimage%2F2021%2F01%2F15%2F20210115000619_0.jpg"
# Using object notation
add_selectbox = st.sidebar.selectbox(
    "어떤 기업?", ("현대 자동차", "기아 자동차")
)

# st.title(f'🌐{add_selectbox} FAQ')

# left, middle = st.columns(2, vertical_alignment="bottom")
# left.text_input("자주하는 질문")
# middle.button("검색", use_container_width=True)
# # right.checkbox("Check me")

if add_selectbox=="현대 자동차":
    st.image(url_hyudai)
    st.title(f'🌐{add_selectbox} FAQ')

    left, middle = st.columns(2, vertical_alignment="bottom")
    left.text_input("자주하는 질문")
    middle.button("검색", use_container_width=True)
    # right.checkbox("Check me")

    tab1,tab2,tab3,tab4,tab5=st.tabs(['전체','차량 구매','홈페이지','멤버쉽','기타'])

    with tab1:
        st.header("전체")
    with tab2:
        st.header("차량구매")
    with tab3:
        st.header("홈페이지")
    with tab4:
        st.header("멤버쉽")
    with tab5:
        st.header("전체")
if add_selectbox=="기아 자동차":
    st.image(url_kia)
    st.title(f'🌐{add_selectbox} FAQ')
    left, middle = st.columns(2, vertical_alignment="bottom")
    left.text_input("자주하는 질문")
    middle.button("검색", use_container_width=True)
    # right.checkbox("Check me")

    


st.page_link("./home.py", label="Home", icon="🏠")
