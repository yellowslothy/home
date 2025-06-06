import streamlit as st

st.set_page_config(
    page_title="🌈 MBTI 직업 추천기 💼",
    page_icon="🧠",
    layout="wide"
)

st.markdown("""
    <style>
    body {
        background-color: #fff8f0;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    .big-title {
        text-align: center;
        font-size: 50px;
        font-weight: bold;
        color: #d67e00;
        text-shadow: 2px 2px #ffd966;
        margin-bottom: 10px;
    }
    .subtitle {
        text-align: center;
        font-size: 24px;
        color: #b38600;
        margin-bottom: 30px;
    }
    .job-box {
        background-color: #ffec99;  /* 노란색 계열 */
        padding: 18px 20px;
        border-radius: 20px;
        margin-bottom: 10px;
        font-size: 20px;
        color: #b37400;
        font-weight: 700;
        box-shadow: 3px 3px 8px rgba(189, 158, 0, 0.4);
        transition: transform 0.2s ease-in-out;
    }
    .job-box:hover {
        transform: scale(1.03);
        box-shadow: 4px 4px 15px rgba(189, 158, 0, 0.6);
    }
    .job-desc {
        background-color: #f5f1e9; /* 베이지색 계열 */
        border-left: 6px solid #d6bc61;
        padding: 15px 25px;
        margin-bottom: 25px;
        font-size: 16px;
        color: #7a6a31;
        font-style: italic;
        border-radius: 10px;
        box-shadow: 2px 2px 10px rgba(214, 188, 97, 0.3);
    }
</style>
""", unsafe_allow_html=True)

st.markdown("<div class='big-title'>🌟 MBTI로 알아보는 나의 직업 💼</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>MBTI 유형을 선택하면, 당신에게 찰떡인 직업과 설명을 알려드려요! 💖</div>", unsafe_allow_html=True)

mbti_types = [
    "INTJ 🧠", "INTP 🤓", "ENTJ 🧑‍💼", "ENTP 🧑‍🔬",
    "INFJ 🧘", "INFP 🎨", "ENFJ 🗣️", "ENFP 🌟",
    "ISTJ 🧾", "ISFJ 🤝", "ESTJ 🏢", "ESFJ 🌼",
    "ISTP 🛠️", "ISFP 🎸", "ESTP 🚀", "ESFP 🎤"
]

job_recommendations = {
    "INTJ": {
        "전략 기획가 🧠": "기업의 장기적인 방향과 전략을 설계하고 실행하는 전문가입니다.",
        "데이터 과학자 📊": "방대한 데이터를 분석해 가치 있는 인사이트를 도출하는 전문가입니다.",
        "소프트웨어 엔지니어 👨‍💻": "효율적이고 견고한 소프트웨어를 설계하고 개발합니다.",
        "연구원 🔬": "새로운 지식과 기술을 탐구하고 연구하는 역할을 합니다."
    },
    "INTP": {
        "이론 물리학자 ⚛️": "물리 법칙을 연구하며 자연 현상의 원리를 탐구합니다.",
        "AI 연구자 🤖": "인공지능 기술 개발과 연구를 진행하는 전문가입니다.",
        "작가 ✍️": "다양한 분야의 글을 창작하고 전달합니다.",
        "UX 디자이너 🧩": "사용자 경험을 설계하고 개선하는 디자이너입니다."
    },
    "ENTJ": {
        "CEO 🧑‍💼": "회사의 경영과 운영을 총괄하는 최고 책임자입니다.",
        "마케팅 디렉터 📢": "마케팅 전략을 세우고 브랜드 가치를 높이는 역할을 합니다.",
        "경영 컨설턴트 📈": "기업의 문제를 분석하고 해결책을 제시하는 전문가입니다.",
        "정치인 🏛️": "국가와 사회를 위해 정책을 만들고 이끄는 리더입니다."
    },
    "ENTP": {
        "창업가 🚀": "새로운 사업을 시작하고 혁신을 이끄는 도전자입니다.",
        "광고 기획자 📺": "창의적인 광고 캠페인을 기획하고 실행합니다.",
        "프로듀서 🎬": "콘텐츠 제작을 총괄하며 프로젝트를 관리합니다.",
        "기술 혁신가 💡": "새로운 기술을 개발하고 적용하는 선구자입니다."
    },
    "INFJ": {
        "심리학자 🧠": "사람들의 마음을 연구하고 치료하는 전문가입니다.",
        "상담사 🗣️": "개인이나 집단의 문제 해결을 돕는 조언자입니다.",
        "작가 ✍️": "내면의 생각과 감정을 글로 표현합니다.",
        "인권 운동가 🕊️": "사회 정의와 인권을 위해 활동합니다."
    },
    "INFP": {
        "예술가 🎨": "자신만의 창의성을 작품으로 표현하는 사람입니다.",
        "시인 ✨": "감성과 상상력으로 아름다운 시를 쓰는 사람입니다.",
        "교사 👩‍🏫": "학생들의 성장과 배움을 돕는 교육자입니다.",
        "사회복지사 ❤️": "사회의 어려운 이웃을 돕는 지원자입니다."
    },
    "ENFJ": {
        "교육자 📘": "학생들의 성장을 위해 헌신하는 선생님입니다.",
        "HR 매니저 🧑‍🤝‍🧑": "사람과 조직을 연결하고 관리하는 역할을 합니다.",
        "정신과 의사 🧑‍⚕️": "정신 건강 문제를 치료하고 상담합니다.",
        "강연자 🎤": "사람들에게 영감을 주는 강연을 진행합니다."
    },
    "ENFP": {
        "광고 AE 🎨": "광고 캠페인을 기획하고 고객과 소통하는 역할입니다.",
        "기자 📰": "사회의 이슈를 취재하고 알리는 역할입니다.",
        "SNS 마케터 📱": "소셜 미디어를 활용해 브랜드를 홍보합니다.",
        "이벤트 플래너 🎉": "행사를 기획하고 운영하는 전문가입니다."
    },
    "ISTJ": {
        "회계사 📊": "재무 정보를 기록, 분석하고 보고하는 전문가입니다.",
        "경찰관 👮‍♂️": "법과 질서를 지키며 시민을 보호합니다.",
        "법무사 ⚖️": "법률 문서 작성과 법률 서비스를 제공합니다.",
        "군인 🎖️": "국가 방위와 안보 임무를 수행합니다."
    },
    "ISFJ": {
        "간호사 🩺": "환자의 건강과 회복을 도우며 돌봅니다.",
        "도서관 사서 📚": "자료 관리와 정보 제공을 담당합니다.",
        "초등학교 교사 🏫": "어린 학생들을 가르치고 지도합니다.",
        "행정직원 🏢": "조직의 행정 업무를 처리합니다."
    },
    "ESTJ": {
        "매니저 🧑‍💼": "팀과 프로젝트를 관리하고 운영합니다.",
        "은행원 🏦": "금융 서비스와 상담을 제공합니다.",
        "군 간부 🎖️": "군대를 지휘하고 전략을 세웁니다.",
        "프로젝트 매니저 📋": "프로젝트 계획과 실행을 책임집니다."
    },
    "ESFJ": {
        "간호조무사 ❤️": "환자를 직접 돌보고 간호 지원을 합니다.",
        "고객 서비스 담당자 ☎️": "고객 문의를 처리하고 지원합니다.",
        "초등 교사 🧑‍🏫": "어린 학생들의 교육과 생활을 지원합니다.",
        "플로리스트 💐": "꽃과 식물을 다루며 아름다움을 창조합니다."
    },
    "ISTP": {
        "기계공 🛠️": "기계 및 장비를 수리하고 유지합니다.",
        "엔지니어 ⚙️": "설계, 제작, 문제 해결을 담당합니다.",
        "응급 구조사 🚑": "긴급 상황에서 생명을 구하는 역할입니다.",
        "드론 조종사 🚁": "드론을 조종하고 관련 임무를 수행합니다."
    },
    "ISFP": {
        "패션 디자이너 👗": "의류와 스타일을 창조하고 디자인합니다.",
        "사진작가 📷": "사진을 통해 순간과 감정을 포착합니다.",
        "요리사 🍳": "맛있는 음식을 창조하고 요리합니다.",
        "수의사 🐾": "동물의 건강과 치료를 책임집니다."
    },
    "ESTP": {
        "세일즈맨 💼": "상품과 서비스를 판매하는 전문가입니다.",
        "스턴트맨 🤸": "위험한 장면을 연기하며 영화나 공연을 빛냅니다.",
        "파일럿 ✈️": "비행기를 조종해 사람과 화물을 안전하게 운송합니다.",
        "스포츠 트레이너 🏋️": "운동선수들의 체력과 기술을 관리합니다."
    },
    "ESFP": {
        "배우 🎭": "무대나 스크린에서 다양한 역할을 연기합니다.",
        "MC 🎤": "행사나 방송을 진행하며 분위기를 띄웁니다.",
        "이벤트 플래너 🎊": "행사를 기획하고 매끄럽게 진행합니다.",
        "유튜버 📹": "영상 콘텐츠를 제작해 대중과 소통합니다."
    }
}

mbti_choice = st.selectbox("✨ 당신의 MBTI는 무엇인가요?", mbti_types)

if mbti_choice:
    mbti_key = mbti_choice.split()[0]
    st.markdown(f"<h2 style='color:#b37400;'>💡 {mbti_choice}에게 추천하는 직업 리스트!</h2>", unsafe_allow_html=True)
    for job, desc in job_recommendations[mbti_key].items():
        st.markdown(f"<div class='job-box'>🔹 {job}</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='job-desc'>{desc}</div>", unsafe_allow_html=True)

st.markdown("""
    <hr><br>
    <div style='text-align:center; font-size:18px; color:#a67c00;'>
        🎓 진로는 인생의 나침반이에요. <br> MBTI는 그 방향을 제시해주는 하나의 힌트일 뿐! <br>
        당신의 꿈을 응원합니다 💫
    </div>
""", unsafe_allow_html=True)
