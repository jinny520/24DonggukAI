import streamlit as st
from PIL import Image
import os

# 현재 스크립트 위치 기준으로 이미지 경로 설정
image_path = os.path.join(os.path.dirname(__file__), "001.png")

# 파일 존재 여부 확인 후 이미지 열기
try:
    image = Image.open(image_path)
    st.image(image, caption='평가기준', use_column_width=True)
except FileNotFoundError:
    st.error("이미지 파일을 찾을 수 없습니다. 경로를 확인하세요.")
