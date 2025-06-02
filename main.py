import streamlit as st

st.title('나의 첫 streamlit 프로젝트!')
st.write('Hello steamlit')
import streamlit as st

# 🎨 페이지 설정
st.set_page_config(
    page_title="MBTI 직업 추천기 🎯",
    page_icon="💼",
    layout="wide"
)

# 🎆 제목
st.markdown("""
    <h1 style='text-align: center; color: #f63366;'>💖 MBTI 기반 직업 추천기 💖</h1>
    <h3 style='text-align: center; color: #4CAF50;'>당신의 성격 유형에 딱 맞는 직업은 무엇일까요? 🧠💼</h3>
""", unsafe_allow_html=True)

# 📊 MBTI 목록
mbti_types = [
    "INTJ 🧠", "INTP 🤓", "ENTJ 🧑‍💼", "ENTP 🧑‍🔬",
    "INFJ 🧘", "INFP 🎨", "ENFJ 🗣️", "ENFP 🌟",
    "ISTJ 🧾", "ISFJ 🤝", "ESTJ 🏢", "ESFJ 🌼",
    "ISTP 🛠️", "ISFP 🎸", "ESTP 🚀", "ESFP 🎤"
]

# 💡 직업 추천 DB
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

# 🎯 사용자 선택
mbti_choice = st.selectbox("당신의 MBTI를 선택하세요! 👇", mbti_types)

if mbti_choice:
    mbti_key = mbti_choice.split()[0]
    st.markdown(f"## 🌟 추천 직업 for **{mbti_choice}** 🌟")
    for job in job_recommendations[mbti_key]:
        st.markdown(f"### 🔹 {job}")

# 🌈 하단 메시지
st.markdown("""
    <br><hr>
    <p style='text-align: center; font-size: 18px;'>💡 자신의 성격에 맞는 진로를 찾는 것이 인생의 방향을 정하는 첫걸음이에요!<br>행복한 진로 탐색이 되시길 바랍니다 😊</p>
""", unsafe_allow_html=True)
