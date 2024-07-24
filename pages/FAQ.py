import streamlit as st


# Using object notation
add_selectbox = st.sidebar.selectbox(
    "어떤 기업?", ("현대 자동차", "기아 자동차", "쉐보레")
)
# Using "with" notation
# with st.sidebar:
#     add_radio = st.radio(
#         "Choose a inquiry method", ("전체","차량 정비", "홈페이지","차량 구매","멤버쉽"," 기타")
#     )

# if add_selectbox:
#     # st.subheader("selectbox")
#     st.subheader(add_selectbox)

# if add_radio:
#     # st.subheader("radio")
#     st.text(add_radio)




st.title(f'🌐{add_selectbox} FAQ')

left, middle = st.columns(2, vertical_alignment="bottom")
left.text_input("ㅇㄹㅇㄹㅇ")
middle.button("검색", use_container_width=True)
# right.checkbox("Check me")



if add_selectbox=="현대 자동차":
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




# left, middle ,right= st.columns(3, vertical_alignment="bottom")
# st.button("Reset", type="primary")
# if st.left.button("홈페이지"):
#     st.write("Why 전체")
# if st.button("차량 정비"):
#     st.write("Why 차량 정비")
# if st.button("차량 구매"):
#     st.write("Why 차량 구매")
# else:
#     st.write("전체")







