import streamlit as st
import os

st.title("💕 강의자료 👩‍🦰")
  

# PDF 파일 경로
pdf_file_path = "./day1.pdf"

# 파일 존재 여부 확인
if os.path.exists(pdf_file_path):
    # PDF 파일 다운로드 버튼
    with open(pdf_file_path, "rb") as file:
        btn = st.download_button(
            label="day1.pdf 다운로드",
            data=file,
            file_name="day1.pdf",
            mime="application/pdf"
        )
    st.write("아래 버튼을 클릭하여 PDF 파일을 다운로드하세요.")
else:
    st.error("파일을 찾을 수 없습니다. 파일 경로와 이름을 확인해주세요.")
