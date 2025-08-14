import streamlit as st

# --- 페이지 기본 설정 ---
st.set_page_config(page_title="🌈💖 MBTI 직업 추천 🎯✨", page_icon="🌟", layout="centered")

# --- CSS로 배경/폰트 꾸미기 ---
st.markdown("""
    <style>
        body {
            background: linear-gradient(135deg, #FFDEE9 0%, #B5FFFC 100%);
            color: #333;
        }
        .title {
            text-align: center;
            font-size: 50px;
            color: #FF69B4;
            font-weight: bold;
            text-shadow: 2px 2px #FFD700;
        }
        .job-list {
            font-size: 22px;
            color: #444;
            background: #ffffffcc;
            padding: 15px;
            border-radius: 15px;
            box-shadow: 0px 4px 15px rgba(0,0,0,0.1);
        }
        .footer {
            text-align: center;
            color: gray;
            font-size: 14px;
        }
    </style>
""", unsafe_allow_html=True)

# --- 제목 ---
st.markdown("<div class='title'>🌟💖 MBTI 기반 직업 추천 💖🌟</div>", unsafe_allow_html=True)
st.write("✨ 당신의 성격에 맞는 꿈의 직업을 찾아보아요! ✨")

# --- MBTI별 추천 직업 데이터 (이모지 버전) ---
mbti_jobs = {
    "INTJ 🦉": ["🧠 전략 컨설턴트", "🔬 연구원", "📊 데이터 분석가", "📜 정책 기획자"],
    "INTP 🧩": ["🔭 과학자", "💻 프로그램 개발자", "🌀 이론 물리학자", "🔍 UX 리서처"],
    "ENTJ 🦁": ["📈 경영 컨설턴트", "💼 CEO", "🎯 마케팅 전략가", "📋 프로젝트 매니저"],
    "ENTP 🦊": ["🚀 기업가", "🎨 광고 기획자", "📺 방송 작가", "💡 혁신 기획자"],
    "INFJ 🦢": ["💬 심리상담가", "✏️ 작가", "📚 교사", "🌱 환경운동가"],
    "INFP 🐇": ["📝 작가", "🎭 아티스트", "🌍 NGO 활동가", "🤝 상담가"],
    "ENFJ 🦋": ["🎓 교육자", "📢 홍보전문가", "🧑‍💼 인사담당자", "🗳 정치가"],
    "ENFP 🐿": ["🎤 방송인", "🎬 광고 크리에이터", "✈️ 여행 작가", "🎉 이벤트 기획자"],
    "ISTJ 🐢": ["📒 회계사", "⚖️ 법률가", "🪖 군인", "🏛 공무원"],
    "ISFJ 🐕": ["🩺 간호사", "📚 교사", "🤲 사회복지사", "🖋 행정직"],
    "ESTJ 🐅": ["📊 경영자", "📋 프로젝트 매니저", "🎖 군 장교", "🏭 공장 관리자"],
    "ESFJ 🐦": ["🩺 간호사", "🎊 이벤트 플래너", "📢 홍보 담당자", "💼 영업 관리자"],
    "ISTP 🦎": ["🛠 엔지니어", "✈️ 항공 정비사", "💻 프로그래머", "🏆 스포츠 코치"],
    "ISFP 🐈": ["👗 패션 디자이너", "📷 사진작가", "🎨 예술가", "💆‍♀️ 치유사"],
    "ESTP 🐯": ["💰 세일즈 전문가", "⚽ 스포츠 선수", "🚀 창업가", "👮 경찰"],
    "ESFP 🦜": ["🎭 배우", "🎤 MC", "📸 광고 모델", "🎟 공연 기획자"]
}

# --- 사용자 입력 ---
selected_mbti = st.selectbox("💎 당신의 MBTI를 선택하세요 👇", list(mbti_jobs.keys()))

# --- 결과 출력 ---
if selected_mbti:
    st.markdown(f"<h2 style='color:#FF69B4;'>✨ {selected_mbti} 추천 직업 ✨</h2>", unsafe_allow_html=True)
    st.markdown("<div class='job-list'>", unsafe_allow_html=True)
    for job in mbti_jobs[selected_mbti]:
        st.markdown(f"- 🌟 {job}")
    st.markdown("</div>", unsafe_allow_html=True)

# --- 푸터 ---
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<p class='footer'>© 2025 🌈 MBTI Career Guide 🌟 All rights reserved.</p>", unsafe_allow_html=True)
