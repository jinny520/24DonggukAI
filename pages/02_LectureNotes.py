import streamlit as st

st.title("💕 강의자료 👩‍🦰")

st.write("📚 강의안이 곧 업로드됩니다! 🎉")
st.write("✨ 기다려주셔서 감사합니다! 🙏")
st.write("🔥 준비된 강의가 여러분을 기다리고 있어요! 🚀 ")

 
import os

# 제목
st.title("PDF 파일 다운로드 예제")

# PDF 파일 경로
pdf_file_path = "day1.pdf"

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
