import streamlit as st
from PIL import Image 
from streamlit_option_menu import option_menu
url_panda='https://media.discordapp.net/attachments/1264781499144867925/1265581781458096240/image.png?ex=66a20862&is=66a0b6e2&hm=be6a087f067be96fb7fb3e50de5dfb8ae8f3b23f01ae2370b0ccb0f34bef0d10&=&format=webp&quality=lossless&width=718&height=343'

st.image(url_panda)
st.title('🚗 🚗 ')
st.header('널부러진 코더즈', divider='rainbow')
st.subheader('설명 주절주절...')

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

import streamlit as st

col1, col2, col3 = st.columns(3)

with col1:
   st.header("A cat")
   st.image("https://static.streamlit.io/examples/cat.jpg")

with col2:
   st.header("A dog")
   st.image("https://static.streamlit.io/examples/dog.jpg")

with col3:
   st.header("An owl")
   st.image("https://static.streamlit.io/examples/owl.jpg")