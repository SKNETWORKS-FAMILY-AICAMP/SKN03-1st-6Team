import streamlit as st
from PIL import Image 
from streamlit_option_menu import option_menu
url_panda='./image/고양이.png'
st.title('🚗 🚗 ')
st.header('널부러진 코더즈', divider='rainbow')
st.subheader('전국 등록 차량 데이터와 회사별 FAQ조회 서비스')

st.page_link("./pages/FAQ.py", label="FAQ", icon="🌐")
st.page_link("./pages/register.py", label="차량 등록 현황", icon="📊")


st.image(url_panda)