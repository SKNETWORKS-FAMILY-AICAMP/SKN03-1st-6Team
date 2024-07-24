import streamlit as st

# LOGO_URL_LARG=https://blog.may-i.io/content/images/size/w1200/2023/04/Frame-228-2.png
# st.logo(LOGO_URL_LARGE, link="https://streamlit.io/gallery", icon_image=LOGO_URL_SMALL)
st.title('🚗 🚗 ')

st.header('회사별로 faq , 등록현황 그래프', divider='rainbow')
st.header('어쩌구 저쩌구')

st.page_link("./home.py", label="Home", icon="🏠")
st.page_link("./pages/FAQ.py", label="FAQ", icon="🌐")
st.page_link("./pages/register.py", label="차량 등록 현황", icon="📊")
st.page_link("./pages/register.py", label="register", icon="📊")

# # Using object notation
# add_selectbox = st.sidebar.selectbox(
#     "How would you like to be contacted?", ("Email", "Home phone", "Mobile phone")
# )

# # Using "with" notation
# with st.sidebar:
#     add_radio = st.radio(
#         "Choose a shipping method", ("Standard (5-15 days)", "Express (2-5 days)")
#     )

# if add_selectbox:
#     st.subheader("selectbox")
#     st.text(add_selectbox)

# if add_radio:
#     st.subheader("radio")
#     st.text(add_radio)



# left, middle, right = st.columns(3, vertical_alignment="bottom")

# left.text_input("Write something")
# middle.button("검색", use_container_width=True)
# right.checkbox("Check me")


# title = st.text_input("Movie title", "Life of Brian")
# st.write("The current movie title is", title)