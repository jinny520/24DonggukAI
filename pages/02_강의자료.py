import streamlit as st
import os

st.title("💕 강의자료 👩‍🦰")

# PDF 파일 경로, 현재 스크립트 위치 기준
pdf_file_path_lecture = os.path.join(os.path.dirname(__file__), "day2.pdf")
pdf_file_path_homework = os.path.join(os.path.dirname(__file__), "day2_blank.pdf")

# 강의자료 파일 존재 여부 확인
if os.path.exists(pdf_file_path_lecture):
    # 강의자료 PDF 파일 다운로드 버튼
    with open(pdf_file_path_lecture, "rb") as file:
        btn_lecture = st.download_button(
            label="분류와 회귀 수업자료",
            data=file,
            file_name="002.pdf",
            mime="application/pdf"
        )
    st.write("버튼을 클릭하여 강의자료 PDF 파일을 다운로드하세요.")
else:
    st.error("강의자료 파일을 찾을 수 없습니다. 파일 경로와 이름을 확인해주세요.")

# 학습지 파일 존재 여부 확인
if os.path.exists(pdf_file_path_homework):
    # 학습지 PDF 파일 다운로드 버튼
    with open(pdf_file_path_homework, "rb") as file:
        btn_homework = st.download_button(
            label="240823 학습지 Download",
            data=file,
            file_name="day2_blank.pdf",
            mime="application/pdf"
        )
    st.write("버튼을 클릭하여 학습지 PDF 파일을 다운로드하세요.")
else:
    st.error("학습지 파일을 찾을 수 없습니다. 파일 경로와 이름을 확인해주세요.")
