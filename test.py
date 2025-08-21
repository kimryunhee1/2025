import streamlit as st

# 페이지 설정
st.set_page_config(page_title="증상별 약 & 생활 관리 가이드", page_icon="💊", layout="centered")

# 전체 배경 흰색, 카드 하늘색
page_bg = """
<style>
.stApp {
    background-color: #ffffff;
}
.card {
    background-color: #B3E5FC;
    padding: 20px;
    margin-bottom: 20px;
    border-radius: 15px;
    box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
}
.card h3 {
    margin-top: 0;
}
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

st.title("💊 증상별 약 & 생활 실천 가이드")
st.write("몸이 안 좋을 때 증상에 맞는 약과 생활 실천 방안을 안내합니다.")

# 증상별 데이터
symptom_data = {
    "두통 🧠": {
        "성분": ["아세트아미노펜", "이부프로펜"],
        "제품": ["타이레놀정 500mg", "부루펜정"],
        "생활": ["충분한 수면", "수분 섭취", "조용하고 어두운 환경에서 휴식", "카페인 과다 섭취 피하기"]
    },
    "소화불량 🤢": {
        "성분": ["제산제", "소화효소제"],
        "제품": ["겔포스", "판크레아틴정"],
        "생활": ["과식 피하기", "기름지고 자극적인 음식 줄이기", "식사 후 바로 눕지 않기", "규칙적인 식습관 유지"]
    },
    "기침 🤧": {
        "성분": ["덱스트로메토르판", "구아이페네신"],
        "제품": ["코데날시럽", "펜잘코프"],
        "생활": ["따뜻한 물 자주 마시기", "가습기 사용", "흡연 피하기", "충분한 휴식"]
    },
    "알레르기 🌸": {
        "성분": ["로라타딘", "세티리진"],
        "제품": ["지르텍정", "클라리틴정"],
        "생활": ["알레르기 원인 회피", "외출 후 세수 및 옷 갈아입기", "환기 자주 하기"]
    },
    "근육통 💪": {
        "성분": ["이부프로펜", "나프록센"],
        "제품": ["부루펜정", "나프록센정"],
        "생활": ["온찜질", "가벼운 스트레칭", "무리한 운동 피하기", "충분한 휴식"]
    },
}

# 증상 선택
selected_symptom = st.selectbox(
    "현재 느끼는 증상을 선택하세요 👇",
    ["증상을 선택하세요."] + list(symptom_data.keys())
)

# 카드형 UI 출력 (하늘색 박스)
if selected_symptom != "증상을 선택하세요.":
    data = symptom_data[selected_symptom]
    
    st.markdown(f"""
    <div class="card">
        <h3>{selected_symptom}</h3>
        <b>💊 추천 성분:</b>
        <ul>
            {''.join(f'<li>{s}</li>' for s in data['성분'])}
        </ul>
        <b>🏷️ 추천 제품:</b>
        <ul>
            {''.join(f'<li>{p}</li>' for p in data['제품'])}
        </ul>
        <b>🏡 생활 실천 방안:</b>
        <ul>
            {''.join(f'<li>{tip}</li>' for tip in data['생활'])}
        </ul>
    </div>
    """, unsafe_allow_html=True)
