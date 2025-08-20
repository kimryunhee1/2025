import streamlit as st
import random

st.title("🔬 과학 퀴즈 추천 앱")

# 샘플 데이터
quiz_data = {
    "생명과학": {
        "쉬움": [
            {"question": "생물체를 구성하는 기본 단위는?", "answer": "세포", "explanation": "모든 생물은 세포로 이루어져 있습니다."},
            {"question": "DNA의 구조는?", "answer": "이중 나선 구조", "explanation": "DNA는 이중 나선 구조로 이루어져 있습니다."},
            {"question": "체세포 분열의 핵상은?", "answer": "2n", "explanation": "체세포 분열은 한 세포에 상동염색체가 존재하므로 핵상은 2n입니다."},
            {"question": "감수 분열(생식세포 분열) ?", "answer": "세포 호흡", "explanation": "세포 호흡으로 에너지를 생성합니다."},
            {"question": "단백질 합성이 일어나는 세포소기관은?", "answer": "리보솜", "explanation": "리보솜에서 mRNA를 바탕으로 단백질이 합성됩니다."}
        ],
        "어려움": [
            {"question": "DNA 복제 시 주형 가닥과 새로 합성되는 가닥의 방향은?", "answer": "반평행", "explanation": "DNA는 5'→3' 방향으로 합성됩니다."},
            {"question": "RNA 전사 과정에서 중요한 효소는?", "answer": "RNA 중합효소", "explanation": "RNA 중합효소가 주형 가닥을 따라 RNA를 합성합니다."},
            {"question": "세포 주기에서 DNA 복제가 일어나는 시기는?", "answer": "S기", "explanation": "S기에서 DNA가 복제됩니다."},
            {"question": "체세포 분열과 감수분열의 차이는 무엇인가요?", "answer": "염색체 수와 목적", "explanation": "체세포 분열은 동일세포 생성, 감수분열은 반수체 생식세포 생성"},
            {"question": "광합성에서 빛 반응과 명반응의 장소는?", "answer": "빛 반응-틸라코이드, 명반응-스트로마", "explanation": "빛 반응은 틸라코이드, 명반응은 스트로마에서 진행됩니다."}
        ]
    },
    "화학": {
        "쉬움": [
            {"question": "물의 화학식은 무엇인가요?", "answer": "H2O", "explanation": "물은 수소 2개와 산소 1개로 이루어져 있습니다."},
            {"question": "산과 염기의 반응을 무엇이라고 하나요?", "answer": "중화 반응", "explanation": "산과 염기가 반응하여 물과 염을 생성합니다."},
            {"question": "화학 결합 중 공유 결합의 특징은?", "answer": "전자 공유", "explanation": "두 원자가 전자를 공유하여 결합합니다."},
            {"question": "산화와 환원의 정의는 무엇인가요?", "answer": "산화-전자 잃음, 환원-전자 얻음", "explanation": "산화와 환원은 전자 이동과 관련이 있습니다."},
            {"question": "분자와 이온의 차이는 무엇인가요?", "answer": "전자 결합 형태", "explanation": "분자는 공유결합, 이온은 전자 이동으로 형성됩니다."}
        ],
        "어려움": [
            {"question": "이온화 경향이 큰 금속은 무엇인가요?", "answer": "칼륨(K)", "explanation": "칼륨은 전자를 쉽게 잃습니다."},
            {"question": "반응속도를 높이는 물질을 무엇이라고 하나요?", "answer": "촉매", "explanation": "촉매는 반응속도를 높이지만 소비되지 않습니다."},
            {"question": "표준 상태에서 기체 1몰의 부피는?", "answer": "22.4L", "explanation": "표준온도와 압력에서 1몰의 기체 부피는 22.4L입니다."},
            {"question": "용액의 몰농도를 계산하는 공식은?", "answer": "몰수/부피(L)", "explanation": "용질의 몰수를 용액 부피로 나눕니다."},
            {"question": "화학 평형에서 르 샤틀리에의 원리란?", "answer": "외부 조건 변화에 따른 평형 이동", "explanation": "온도, 압력 변화 시 평형이 이동합니다."}
        ]
    },
    "지구과학": {
        "쉬움": [
            {"question": "지구의 가장 바깥층은 무엇인가요?", "answer": "지각", "explanation": "지각은 지구의 가장 바깥 층입니다."},
            {"question": "물의 순환 과정을 무엇이라고 하나요?", "answer": "물순환", "explanation": "증발, 응결, 강수, 침투 등의 과정을 포함합니다."},
            {"question": "대기권에서 날씨 현상이 주로 일어나는 층은?", "answer": "대류권", "explanation": "대류권에서 구름과 강수가 형성됩니다."},
            {"question": "지구 내부 에너지의 주된 원천은?", "answer": "방사성 붕괴", "explanation": "지구 내부 열의 대부분은 방사성 붕괴에서 옵니다."},
            {"question": "지구의 자전이 하루를 만드는 이유는?", "answer": "자전 속도", "explanation": "지구의 자전으로 낮과 밤이 생깁니다."}
        ],
        "어려움": [
            {"question": "판 구조론에서 대륙 이동의 주요 증거는?", "answer": "화석 및 지질 구조", "explanation": "유사한 화석과 지질 구조가 대륙 간에 분포합니다."},
            {"question": "지진파의 종류를 두 가지 쓰시오.", "answer": "P파와 S파", "explanation": "P파는 종파, S파는 횡파입니다."},
            {"question": "해양 지각과 대륙 지각의 차이는?", "answer": "밀도와 두께", "explanation": "해양 지각은 얇고 밀도가 높습니다."},
            {"question": "화산 활동의 종류를 두 가지 쓰시오.", "answer": "성층화산과 단층화산", "explanation": "성층화산과 단층화산은 구조와 폭발 방식이 다릅니다."},
            {"question": "지구 자기장의 원천은 무엇인가요?", "answer": "외핵의 대류", "explanation": "외핵의 액체 금속 대류로 자기장이 생성됩니다."}
        ]
    }
}

# 사용자 선택
subject = st.selectbox("한가지 과목을 선택하세요.", ["한가지 과목을 선택하세요.", "생명과학", "화학", "지구과학"])
difficulty = st.selectbox("난이도를 선택하세요", ["쉬움", "어려움"])

if subject == "한가지 과목을 선택하세요.":
    st.stop()

# 문제 랜덤 선택
if st.button("문제 추천 받기"):
    problems = quiz_data.get(subject, {}).get(difficulty, [])
    if problems:
        problem = random.choice(problems)
        st.write(f"**문제:** {problem['question']}")
        if st.button("정답 확인"):
            st.write(f"**정답:** {problem['answer']}")
            st.write(f"**해설:** {problem['explanation']}")
    else:
        st.write("해당 조건의 문제가 없습니다.")
