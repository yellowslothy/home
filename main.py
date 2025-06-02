st.set_page_config(
    page_title="🌈 MBTI 직업 추천기 💼",
    page_icon="🧠",
    layout="wide"
)
import streamlit as st

st.title('나의 첫 streamlit 프로젝트!')
st.write('Hello steamlit')

import streamlit as st

st.markdown("""
    <style>
    body {
        background-color: #fff8fc;
    }
    .big-title {
        text-align: center;
        font-size: 50px;
        font-weight: bold;
        color: #ff4b91;
        text-shadow: 2px 2px #ffe6f0;
        margin-bottom: 10px;
    }
    .subtitle {
        text-align: center;
        font-size: 24px;
        color: #f48fb1;
        margin-bottom: 30px;
    }
    .job-box {
        background-color: #ffe6f0;
        padding: 15px;
        border-radius: 15px;
        margin-bottom: 10px;
        font-size: 20px;
        color: #d81b60;
        box-shadow: 2px 2px 10px rgba(255, 182, 193, 0.2);
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<div class='big-title'>🌟 MBTI로 알아보는 나의 직업 💼</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>MBTI 유형을 선택하면, 당신에게 찰떡인 직업을 알려드려요! 💖</div>", unsafe_allow_html=True)

mbti_types = [
    "INTJ 🧠", "INTP 🤓", "ENTJ 🧑‍💼", "ENTP 🧑‍🔬",
    "INFJ 🧘", "INFP 🎨", "ENFJ 🗣️", "ENFP 🌟",
    "ISTJ 🧾", "ISFJ 🤝", "ESTJ 🏢", "ESFJ 🌼",
    "ISTP 🛠️", "ISFP 🎸", "ESTP 🚀", "ESFP 🎤"
]

job_recommendations = {
    "INTJ": ["전략 기획가 🧠", "데이터 과학자 📊", "소프트웨어 엔지니어 👨‍💻", "연구원 🔬"],
    "INTP": ["이론 물리학자 ⚛️", "AI 연구자 🤖", "작가 ✍️", "UX 디자이너 🧩"],
    "ENTJ": ["CEO 🧑‍💼", "마케팅 디렉터 📢", "경영 컨설턴트 📈", "정치인 🏛️"],
    "ENTP": ["창업가 🚀", "광고 기획자 📺", "프로듀서 🎬", "기술 혁신가 💡"],
    "INFJ": ["심리학자 🧠", "상담사 🗣️", "작가 ✍️", "인권 운동가 🕊️"],
    "INFP": ["예술가 🎨", "시인 ✨", "교사 👩‍🏫", "사회복지사 ❤️"],
    "ENFJ": ["교육자 📘", "HR 매니저 🧑‍🤝‍🧑", "정신과 의사 🧑‍⚕️", "강연자 🎤"],
    "ENFP": ["광고 AE 🎨", "기자 📰", "SNS 마케터 📱", "이벤트 플래너 🎉"],
    "ISTJ": ["회계사 📊", "경찰관 👮‍♂️", "법무사 ⚖️", "군인 🎖️"],
    "ISFJ": ["간호사 🩺", "도서관 사서 📚", "초등학교 교사 🏫", "행정직원 🏢"],
    "ESTJ": ["매니저 🧑‍💼", "은행원 🏦", "군 간부 🎖️", "프로젝트 매니저 📋"],
    "ESFJ": ["간호조무사 ❤️", "고객 서비스 담당자 ☎️", "초등 교사 🧑‍🏫", "플로리스트 💐"],
    "ISTP": ["기계공 🛠️", "엔지니어 ⚙️", "응급 구조사 🚑", "드론 조종사 🚁"],
    "ISFP": ["패션 디자이너 👗", "사진작가 📷", "요리사 🍳", "수의사 🐾"],
    "ESTP": ["세일즈맨 💼", "스턴트맨 🤸", "파일럿 ✈️", "스포츠 트레이너 🏋️"],
    "ESFP": ["배우 🎭", "MC 🎤", "이벤트 플래너 🎊", "유튜버 📹"]
}

mbti_choice = st.selectbox("✨ 당신의 MBTI는 무엇인가요?", mbti_types)

if mbti_choice:
    mbti_key = mbti_choice.split()[0]
    st.markdown(f"<h2 style='color:#d81b60;'>💡 {mbti_choice}에게 추천하는 직업 리스트!</h2>", unsafe_allow_html=True)
    for job in job_recommendations[mbti_key]:
        st.markdown(f"<div class='job-box'>🔹 {job}</div>", unsafe_allow_html=True)

st.markdown("""
    <hr><br>
    <div style='text-align:center; font-size:18px; color:#888;'>
        🎓 진로는 인생의 나침반이에요. <br> MBTI는 그 방향을 제시해주는 하나의 힌트일 뿐! <br>
        당신의 꿈을 응원합니다 💫
    </div>
""", unsafe_allow_html=True)
