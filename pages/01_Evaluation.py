import streamlit as st
from PIL import Image

# 웹 페이지 제목
st.title("평가기준")

# 이미지 표시
image = Image.open("평가기준.png")
st.image(image, caption='평가기준', use_column_width=True) 
