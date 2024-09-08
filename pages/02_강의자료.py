import streamlit as st
import os

st.title("💕 강의자료 👩‍🦰")

# PDF 파일 경로, 현재 스크립트 위치 기준
pdf_file_path_lecture = os.path.join(os.path.dirname(__file__), "Note.pdf")

# 강의자료 파일 존재 여부 확인
if os.path.exists(pdf_file_path_lecture):
    # 강의자료 PDF 파일 다운로드 버튼
    with open(pdf_file_path_lecture, "rb") as file:
        btn_lecture = st.download_button(
            label="분류와 회귀 수업자료",
            data=file,
            file_name="Note.pdf",
            mime="application/pdf"
        )
    st.write("버튼을 클릭하여 강의자료 PDF 파일을 다운로드하세요.")
else:
    st.error("강의자료 파일을 찾을 수 없습니다. 파일 경로와 이름을 확인해주세요.")

