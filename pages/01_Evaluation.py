import streamlit as st
from PIL import Image
import os

# 이미지 파일 경로 설정
image_path = "./001.png"

# 파일 존재 여부 확인
if os.path.exists(image_path):
    image = Image.open(image_path)
    st.image(image, caption='평가기준', use_column_width=True)
else:
    st.error("이미지 파일을 찾을 수 없습니다. 경로를 확인하세요.")
